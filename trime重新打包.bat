@echo off
@echo.trime重新打包……

apktool b app-release-25249-o_1dm0eunhm6jq1iv3rphtqt165lq-uid-574023 -o app-release-mod.apk && jarsigner -verbose -keystore debug.keystore -storepass android -signedjar app-release-signed.apk app-release-mod.apk androiddebugkey && zipalign -f -v 4 app-release-signed.apk naamning-20230627.apk

echo.
echo 执行trime重新打包完成……
echo.
pause