@echo off
@echo.正在签名【signapk】……

java -jar C:\apktool\signapk.jar testkey.x509.pem testkey.pk8 C:\apktool\1_Mod.apk C:\apktool\1_Mod_Signed.apk 

echo.
echo 签名【signapk】完成……
echo.
pause