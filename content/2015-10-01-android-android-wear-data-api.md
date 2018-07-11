Title: [Android] Android Wear Data API
Date: 2015-10-01 13:04
Modified: 2015-10-01 13:04
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) [Android] Android Wear Data API


**Android Wear Data API** 可以將app裡的data存入Google Data layer
讓data在wearable和phone之間自動sync、做batch傳輸，或是傳遞一次性資訊和命令
另外還有Channel API 專門用來做streaming，但這邊主要介紹Data API中的**Item API**

**注意**: 只有已安裝*Google Mobile Service(GMS)* (有com.google.android.gms這個service)的device才能使用DATA API

# 製作Android wear apk @ Android Studio

這邊以Android Studio 1.2.2為例

1. 重新建立
File -> New -> New Project -> 輸入project name -> 勾選 "Phone and Tablet" 和 "Wear"
這樣就會自動產生phone和wearable的module
兩邊的app完成之後各自燒到phone和watch上就可以了

2. 加入wearable module到現存的Project
Project上按右建 -> New -> Module -> Andorid Wear Module -> 輸入package name和module name
**重要** 這邊package name要和原本phone的module完全一樣
這樣在使用Data API的時候，phone和watch兩邊的才能看到彼此的data

# 使用Data Item API

## 建立GMS Client
在Activity或Service裡註冊GMC client
``` java
 //Build GMS client
 GoogleApiClient gclient = new GoogleApiClient.Builder(mContext)
     .addConnectionCallbacks(this)
     .addOnConnectionFailedListener(this)
     // Request access only to the Wearable API
     .addApi(Wearable.API)
     .build();
```

## 連接到GMS
需要實做 ```GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener``` interface
並呼叫```gclient.connect()```
要斷開連線則呼叫```gclient.disconnect()```

## 將data放到Google Data Layer

每筆data是用key, value的形式存在Data map中
而每個Data map又可以有專屬的url，url可以用來表示目錄結構
這些Data map只有同一個package下的components才看的到

``` java
//建立put request
PutDataMapRequest req = PutDataMapRequest.create("/my-heartrate");
// get data map並insert key/value
req.getDataMap().putInt(HEARTRATE_KEY, hr);
PutDataRequest putDataReq = req.asPutDataRequest();
PendingResult<DataApi.DataItemResult> pendingResult =
Wearable.DataApi.putDataItem(gclient, putDataReq);
pendingResult.setResultCallback(new ResultCallback<DataApi.DataItemResult>() {
	@Override
	public void onResult(DataApi.DataItemResult result) {
      if(result.getStatus().isSuccess()){
          Log.d(TAG, "data item set " + result.getDataItem().getUri());
      }
	}
});
```

## 拿取Data layer的Data
``` java
//建立URI
Uri.Builder builder = new Uri.Builder();
builder.scheme("wear");  					//這裡是指定要拿wearable device的資料
builder.path("/my-heartrate");   	//之前指定的uri字串
Log.d(TAG, "query url: " + builder.build().toString());

PendingResult<DataItemBuffer> pendingResult = Wearable.DataApi.getDataItems(gclient, builder.build());
pendingResult.setResultCallback(new ResultCallback<DataItemBuffer>() {
    @Override
    public void onResult(DataItemBuffer dataItems) {
        Log.d(TAG, "get Data Items");
        for(DataItem data : dataItems){
            Log.d(TAG, "data path: " + data.getUri().getPath());
            DataMap dataMap = DataMapItem.fromDataItem(data).getDataMap();
            int hr = dataMap.getInt(HEARTRATE_KEY);
            Log.d(TAG, "data value:" + hr);
            updateCount(hr);
        }  
    }
});
```

## 註冊listener
implement ```DataApi.DataListener```

``` java
    @Override
    public void onDataChanged(DataEventBuffer dataEvents) {
        Log.d(TAG, "onDataChanged");
        for (DataEvent event : dataEvents) {
            if (event.getType() == DataEvent.TYPE_CHANGED) {
                // DataItem changed
                DataItem item = event.getDataItem();
                if (item.getUri().getPath().contains(URI)) {
                    DataMap dataMap = DataMapItem.fromDataItem(item).getDataMap();
                    updateCount(dataMap.getInt(HEARTRATE_KEY));
                }
            } else if (event.getType() == DataEvent.TYPE_DELETED) {
                // DataItem deleted
            }
        }
    }
```
