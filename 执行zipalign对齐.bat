@echo off
@echo.正在执行zipalign对齐……

zipalign -f -v 4 C:\apktool\1_Mod_Signed.apk 1_Mod_Signed_zipalign.apk 

echo.
echo 执行zipalign对齐完成……
echo.
pause