Title: [Android] [PokemonGO] 我也來inverse engineering一下
Date: 2016-08-25 02:22
Modified: 2016-08-25 02:22
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Android] [PokemonGO] 我也來inverse engineering一下


其實大部分的分析就靠這篇[神文](http://www.inside.com.tw/2016/08/24/source-code-of-pokemon-go)就可以了XD
但其中對於Sensor/Location資訊是如何利用的著墨較少，所以只好自己來一下
亂猜的部分很多，還請不吝指教<(_    _)>

# Use dex2jar & JD-GUI to decompile .dex files
*(Update: 原文有附整理過的[source code](https://github.com/applidium/PokemonGo_Android_RE)了--雖然是剛出的時候的版本，不想自己做的可以跳過這段:P)*
因為我的目標不是創一個可build的專案，只要看懂裡面在幹麻就好
所以就使用原文第一階段的方法，先用dex2jar把.dex轉成.jar file，然後用JD-GUI去讀

## Compile dex2jar
RRRR　因為現在找不到prebuilt版的，只好從[source](https://github.com/pxb1988/dex2jar)開始
目前已經是用gradle build，還有gradle wrapper
所以只要解壓縮，點兩下`gradlew.bat`就可以惹
會在src外面產生`dex-tools-2.1-SNAPSHOT.zip`這個壓縮檔，裡面就是dex2jar全部的工具了
(如果沒有在外面找到，也可以在dex-tools/build/distributions/找到)

### Refs:
https://sourceforge.net/p/dex2jar/wiki/BuildFromSource/

## Pull out Pokemon GO apk
找一支有root過的手機，從play上下載最新的程式 (本文使用2016/8/25的版本)
再用adb pull下來
(adb安裝方法可參考[這篇](http://wangwangtc.blogspot.tw/2015/03/adbandroid.html))
通常production buildl的load都不能直接pull `/data/app`底下的東西
所以我都會先copy到sdcard裡
``` sh
cp -r /data/app/com.nianticlabs.pokemongo-2 /sdcard/pkgo
//結尾不一定是2 看你更新了幾次 : P
```
``` bat
adb pull /sdcard/pkgo
```
拉下來之後，可以看到這裡面有一個`base.apk`
和其他prebuilt的native lib
(都只有arm的，x86的phone繼續哭哭XD)
![pkgo-lib.png](http://user-image.logdown.io/user/13673/blog/12890/post/804838/PvB7A5aRjq17IzZmVHfD_pkgo-lib.png)

因為我們只需要看Android Location/Sensor API的部分
所以就只要把`base.apk`用7zip之類的解壓縮之後
拿裡面的`classes.dex`

## Turn .dex to .jar file
`dex-tools-2.1-SNAPSHOT.zip`解壓縮之後
用裡面的`d2j-dex2jar.bat`把base.apk轉成.classes檔
``` bat
\> dex-tools-2.1-SNAPSHOT\d2j-dex2jar.bat classes.dex
dex2jar classes.dex -> .\classes-dex2jar.jar
```
## Download JD-GUI
官網有各種平台的prebuilt程式，直接下載來用就對了~
http://jd.benow.ca/
打開剛剛gen出來的.jar檔就可以看到裡面的class啦~
![pkgo-classes.png](http://user-image.logdown.io/user/13673/blog/12890/post/804838/Oc050z0JQKTajC5Ub9jQ_pkgo-classes.png)

# Location/Sensor related analysis
核心功能部分幾乎都放在com.nianticlabs.nia這個package底下

幾個簡單的conclusion:
- 好險還是沒有用Proguard XD
- 使用了Android的三種location來源: GPS, Network, Google的Fused location
- Location update的min period都滿短的: GPS 1 sec, Network 5 sec (很噴電不意外 : /
- 直接call Sensor API的部分主要是拿來偵測手機旋轉or取得玩家面向的方位
- 有使用到Google的ActivityRecognition

## Location part
#### package: com.nianticlabs.nia.location
在`NianticLocationManager.java`裡面可以看到有三個Location provider
``` java NianticLocationManager.java
addProvider("fused", new FusedLocationProvider(this.context, this.gpsUpdateTimeMs, this.gpsUpdateDistanceM));
addProvider("gps", new LocationManagerProvider(this.context, "gps", this.gpsUpdateTimeMs, this.gpsUpdateDistanceM));
addProvider("network", new LocationManagerProvider(this.context, "network", this.netUpdateTimeMs, this.netUpdateDistanceM));
```
其中`LocationManagerProvider.java`就是個wrapper
三個provider裡面分別用Android `LocationManager`這個system service去拿GPS和Network location
和使用Google Mobile Service(GMS)的Fused location
"gps" 這個應該是`LocationManager.GPS_PROVIDER`, "network" 是`LocationManager.NETWORK_PROVIDER`
``` java LocationMangerProvider.java
this.locationManager = ((LocationManager)this.context.getSystemService("location"));
```
實際拿location的方法是呼叫[requestLocationUpdates(String, long, float, LocationListener)](https://developer.android.com/reference/android/location/LocationManager.html#requestLocationUpdates(java.lang.String,%20long,%20float,%20android.location.LocationListener))註冊更新location時的listener
其中*最小更新時間&距離*的參數就是上面constructor帶入的
``` java NianticLocationManager.java
  private float gpsUpdateDistanceM = 0.0F;
  private int gpsUpdateTimeMs = 1000;
  private float netUpdateDistanceM = 0.0F;
  private int netUpdateTimeMs = 5000;
```
更新時的listener則是統一使用`NianticLocationManager.java`裡建立的listener
這個listener最後會call到native lib，未看先猜應該是接到unity遊戲引擎

## Sensor
主要都在`NianticSensorManager.java`
接了一堆sensor service，但感覺最終目標都是要偵測手機旋轉和方位
最後接回native lib給遊戲引擎使用，未看先猜用來進省電模式和update地圖畫面使用
尤其是角色在地圖上的方向旋轉部分
``` java
  public NianticSensorManager(Context paramContext, long paramLong)
  {
    super(paramContext, paramLong);
    this.display = ((WindowManager)paramContext.getSystemService("window")).getDefaultDisplay();
    this.sensorManager = ((SensorManager)paramContext.getSystemService("sensor"));
    this.gravity = this.sensorManager.getDefaultSensor(9);
    this.gyroscope = this.sensorManager.getDefaultSensor(4);
    this.accelerometer = this.sensorManager.getDefaultSensor(1);
    this.magnetic = this.sensorManager.getDefaultSensor(2);
    this.rotation = this.sensorManager.getDefaultSensor(11);
    this.linearAcceleration = this.sensorManager.getDefaultSensor(10);
  }
```

## Activity Recognition
最後，他居然有用Google 的[Acitivity Recognition API](https://developers.google.com/android/reference/com/google/android/gms/location/ActivityRecognitionApi)!
看起來一樣也是接到Activity之後直接call native function。


瞄一下[目前Google AR可以detect到的activity](https://developers.google.com/android/reference/com/google/android/gms/location/DetectedActivity)
可以偵測到的Activity有以下幾項:
```
int 	IN_VEHICLE 	The device is in a vehicle, such as a car.
int 	ON_BICYCLE 	The device is on a bicycle.
int 	ON_FOOT 	The device is on a user who is walking or running.
int 	RUNNING 	The device is on a user who is running.
int 	STILL 	The device is still (not moving).
int 	TILTING 	The device angle relative to gravity changed significantly.
int 	UNKNOWN 	Unable to detect the current activity.
int 	WALKING 	The device is on a user who is walking.
```
可能是拿來偵測玩家是否在跑動和是否在開車
(雖然專家指出，因為他目前實做似乎只有拿三軸資料，IN_VEHICLE ON_BICYCLE都很不準...)

# Conclusion
只是decompile .dex看code能知道的還是有限
有試著用ELF tools decompile .so檔，但是大部分的symbol都mangled過不好分析

目前看不出來有做其他的省電機制(e.g. 玩家靜止就降低或停止location query)
想想這款遊戲核心技術部分本來就不在終端裝置，還沒有做多少優化也是滿合理的 : P

至於剩下有關網路的部分還是看原本的神文就好XD
API實作方法應該不會改動太大

以上~



