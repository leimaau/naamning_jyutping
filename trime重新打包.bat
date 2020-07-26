@echo off
@echo.trime重新打包……

apktool b com.osfans.trime_20181226 -o app-release-mod.apk && jarsigner -verbose -keystore debug.keystore -storepass android -signedjar app-release-signed.apk app-release-mod.apk androiddebugkey && zipalign -f -v 4 app-release-signed.apk naamning-20200726.apk

echo.
echo 执行trime重新打包完成……
echo.
pause