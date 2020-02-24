# 安卓端配置文件

此處存放配置同文輸入法需要的文件，先安裝[小鶴同文主題包](http://flypy.ys168.com/)（選擇本分支下 trime.custom.yaml 對應的主題版本），後用本分支下的文件覆蓋即可。

若嫌手工配置麻煩，[**此處**](https://github.com/leimaau/naamning_jyutping/releases)已通過 apktool 重新打包，下載安裝即可。

![](https://s2.ax1x.com/2020/02/15/1xrn4H.jpg)

![](https://s2.ax1x.com/2020/02/15/1xrmUe.jpg)

## 命令簡介

```
> apktool d -f -m -s -r xxx.apk
> apktool b xxx -o app-release-mod.apk
> keytool -genkeypair -alias androiddebugkey -keyalg RSA -validity 36500 -keystore debug.keystore
> jarsigner -verbose -keystore debug.keystore -signedjar app-release-signed.apk app-release-mod.apk androiddebugkey
> zipalign -f -v 4 app-release-signed.apk app-release-20191221.apk
```

bat 處理

```
@echo off
@echo.正在反编译(解包)……

apktool d -f -m -s -r xxx.apk

echo.
echo 反编译(解包)完成……
echo.
pause
```

```
@echo off
@echo.trime重新打包……

apktool b xxx -o app-release-mod.apk && jarsigner -verbose -keystore debug.keystore -storepass android -signedjar app-release-signed.apk app-release-mod.apk androiddebugkey && zipalign -f -v 4 app-release-signed.apk app-release-20191221.apk

echo.
echo 执行trime重新打包完成……
echo.
pause
```
