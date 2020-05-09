@echo off
@echo.正在签名【jarsigner加上时间戳】……

jarsigner -verbose -keystore C:\apktool\debug.keystore -storepass android -signedjar C:\apktool\1_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey -tsa http://sha256timestamp.ws.symantec.com/sha256/timestamp

echo.
echo 签名【jarsigner加上时间戳】完成……
echo.
pause