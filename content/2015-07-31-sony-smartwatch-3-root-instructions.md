Title: Sony Smartwatch 3 Root Instructions
Date: 2015-07-31 10:58
Modified: 2015-07-31 10:58
Category: Archive
Tags: 
Authors: Solring Lin
Summary: (archive) Sony Smartwatch 3 Root Instructions


1. **安裝driver**
	用Sony的PC Companion裡的driver
	如果有問題的話也可以改用Google的USB driver
	但是要手動加smartwatch 3 SWR50進支援清單
	到Google USB driver的目錄下修改 *androidwinusb.inf*
```
; Sony Smartwatch 3 SWR50 ADB interface
%SonyFastbootInterface%    = USB_Install, USB\VID_0FCE&PID_0DDE
%SonyFastbootInterface%    = USB_Install, USB\VID_0FCE&PID_0DDE&REV_0001
%SonySmartwatch3ADBInterface%  = USB_Install, USB\VID_0FCE&PID_A1BD
%SonySmartwatch3ADBInterface%  = USB_Install, USB\VID_0FCE&PID_A1BD&REV_0100
```
	後面的ID用裝置管理員查device hardware ID就查的到了

2. **連接裝置到電腦**
	用usb連到電腦上之後
	手錶還要往下滑一下找"Allow debugging?"的認證確認卡片
	Open on phone之後，手機上會出現一般的adb authorization畫面
	確認後才能連的上去

3. **unlock device**
	手錶關機之後，長壓電源按鈕，會出現insert USB的畫面
	在按兩下會進入工程畫面，可以進fastboot, recovery之類的
	按一下按鈕switch, 按兩下確認
	進fastboot之後unlock:
```
fastboot oem unlock
```

4. **下載Wear-Supersu,zip 丟進sdcard裡面待用**

5. **刷TWRP recovery**
	下載修改過的TWRP recovery for smartwatch 3, 用fastboot刷進去
http://forum.xda-developers.com/smartwatch-3/development/recovery-twrp-2-8-3-0-sony-smartwatch-3-t2986907
```
fastboot flash recovery 
```
	刷進去之後
	想辦法先關機，之後進fastboot再轉recovery mode
	如果用fastboot continue會reboot的話，就要再重刷一次recovery
	因為他boot進系統之後會回復recovery, TWRP會不見 : P

	成功在剛刷完TWRP就進recovery之後
	就可以將先放到sdcard裡面的.zip檔刷進去啦~
