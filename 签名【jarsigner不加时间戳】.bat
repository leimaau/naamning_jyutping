@echo off
@echo.正在签名【jarsigner不加时间戳】……

jarsigner -verbose -keystore C:\apktool\debug.keystore -storepass android -signedjar C:\apktool\1_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey

echo.
echo 签名【jarsigner不加时间戳】完成……
echo.
pause