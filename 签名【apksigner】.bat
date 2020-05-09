@echo off
@echo.正在签名【apksigner】……

java -jar C:\apktool\apksigner.jar -keystore C:\apktool\debug.keystore -alias androiddebugkey -pswd android -aliaspswd android C:\apktool\1_Mod.apk

echo.
echo 签名【apksigner】完成……
echo.
pause