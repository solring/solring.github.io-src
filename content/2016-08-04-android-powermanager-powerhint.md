Title: [Android] N版PowerManager powerHint
Date: 2016-08-04 04:09
Modified: 2016-08-04 04:09
Category: Archive
Tags: [Android PowerManagement]
Authors: Solring Lin
Summary: (archive) [Android] N版PowerManager powerHint


Power hint顧名思義就是從framework層打hint下去給平台，讓下層知道說現在上面是在謥殺虫(所謂上情下達)
就可以根據情境調整power management的機制(e.g. boost performance, 降freq省電....blahblah)
先來看一下Power HAL有哪些hint:
``` c
/*
 * Power hint identifiers passed to (*powerHint)
 */

typedef enum {
    POWER_HINT_VSYNC = 0x00000001,
    POWER_HINT_INTERACTION = 0x00000002,
    /* DO NOT USE POWER_HINT_VIDEO_ENCODE/_DECODE!  They will be removed in
     * KLP.
     */
    POWER_HINT_VIDEO_ENCODE = 0x00000003,
    POWER_HINT_VIDEO_DECODE = 0x00000004,
    POWER_HINT_LOW_POWER = 0x00000005,
    POWER_HINT_SUSTAINED_PERFORMANCE = 0x00000006,
    POWER_HINT_VR_MODE = 0x00000007
} power_hint_t;
```
最早感覺是為了解決performance issue(VSYNC, INTERACTION, VIDEO)
後來在project volta增加LOW_POWER，讓平台可以安心進入low power mode ~~而不用被譙UX變差~~
最近N版又多加了SUSTAINED_PERFORMANCE & VR mode
VR就顧名思義
Sustained performance指長時間提供穩定performance，避免thermal throttling
目前是讓app可以由```Window```這個class指示進入這個mode
```
void setSustainedPerformanceMode(boolean enable)
```

# Related sources:

##HAL
hardware/libhardware/include/hardware/power.h
```
void (*powerHint)(struct power_module *module, power_hint_t hint,
                      void *data);
```

##Framework (frameworks/)
base/core/java/android/os/PowerManagerInternal.java --> 這裡面就看的到囉
base/services/core/java/com/android/server/power/PowerManagerService.java --> java端主要實做

base/services/core/jni/com_android_server_power_PowerManagerService.cpp --> JNI
native/services/powermanager/IPowerManager.cpp  --> call binder的地方

其中```PhoneWindowManager```和```WindowSurfacePlacer```都是透過```PowerManagerInternal```下power hint的

``` java base/services/core/java/com/android/server/policy/PhoneWindowManager.java
mPowerManagerInternal.powerHint(PowerManagerInternal.POWER_HINT_INTERACTION, 0);
```

``` java base/services/core/java/com/android/server/wm/WindowSurfacePlacer.java
        if (mSustainedPerformanceModeCurrent != mSustainedPerformanceModeEnabled) {
            mSustainedPerformanceModeEnabled = mSustainedPerformanceModeCurrent;
            mService.mPowerManagerInternal.powerHint(
                    mService.mPowerManagerInternal.POWER_HINT_SUSTAINED_PERFORMANCE_MODE,
                    (mSustainedPerformanceModeEnabled ? 1 : 0));
        }

```

Surface Flinger則是從native層使用
``` cpp
status_t status = mPowerManager->powerHint(POWER_HINT_VSYNC, enabled ? 1 : 0);
```