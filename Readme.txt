apktool 使用说明


1、将apktool程序zip压缩包直接解压至磁盘分区 C:\ 根目录下 ，然后把待编译程序如C4009-C7P07.apk重命名为1.apk，复制到 C:\apktool 目录中
    
2、需要jdk支持,官方下载地址: https://www.oracle.com/technetwork/java/javase/downloads/

3、环境变量JAVA_HOME，要指向jdk目录，若电脑上环境变量没有JAVA_HOME路径，可在电脑上设置本机环境变量JAVA_HOME路径

       Windows 64位系统安装*****-windows-x64为64位的jdk或jre以及Windows 32位系统安装*****-windows-i586为32位的jdk或jre的Java路径为 C:\Program Files\Java\ 如：

       C:\Program Files\Java\jdk1.7.0_80             64位系统安装 jdk-7u80-windows-x64   32位系统安装 jdk-7u80-windows-i586
       C:\Program Files\Java\jre7                    64位系统安装 jdk-7u80-windows-x64  
 
       C:\Program Files\Java\jdk1.8.0_192            64位系统安装 jdk-8u192-windows-x64  32位系统安装 jdk-8u192-windows-i586
       C:\Program Files\Java\jre1.8.0_192            64位系统安装 jdk-8u192-windows-x64  

       C:\Program Files\Java\jre1.7.0_80             64位系统安装 jre-7u80-windows-x64   32位系统安装 jre-7u80-windows-i586   
       C:\Program Files\Java\jre1.8.0_161            64位系统安装 jre-8u161-windows-x64  32位系统安装 jre-8u161-windows-i586  

       Windows 64 位系统安装*****-windows-i586为32位的jdk或jre的Java路径为 C:\Program Files (x86)\Java\ 如：

       C:\Program Files (x86)\Java\jdk1.7.0_80       64位系统安装 jdk-7u80-windows-i586
       C:\Program Files (x86)\Java\jdk1.8.0_192      64位系统安装 jdk-8u192-windows-i586
       C:\Program Files (x86)\Java\jre1.7.0_80       64位系统安装 jre-7u80-windows-i586
       C:\Program Files (x86)\Java\jre1.8.0_161      64位系统安装 jre-8u161-windows-i586

    在电脑上可按以下方法设置环境变量：JAVA_HOME、PATH、CLASSPATH ,若只设置JAVA_HOME 、PATH就能正常编译或签名apk，就无需设置CLASSPATH 

       JAVA_HOME：我的电脑(计算机)->属性->高级（高级系统设置）->单击“环境变量”按钮
                  ->单击“系统变量”区域的“新建”按钮->在“变量名”文本框中输入JAVA_HOME
                  在“变量值”文本框中输入JDK的安装路径（如：C:\Program Files\Java\jdk1.7.0_80）,单击确定

       PATH ：    在系统变量中查看PATH变量，如果存在PATH，则在最末尾多添加一个%JAVA_HOME%\bin;（直接添加，连;也加上，无需加空格之类的，以下相同）
                  如果不存在，则新建变量PATH，设定变量值为：%JAVA_HOME%\bin;

       CLASSPATH：在系统变量中查看CLASSPATH变量，如果存在CLASSPATH，则在最末尾添加(前面有个.):  .%JAVA_HOME%lib\dt.jar;%JAVA_HOME%\lib\tools.jar;
                  如果不存在，则新建一个，设定变量值为(前面有个.):    .;%%JAVA_HOME%%\lib\dt.jar;%%JAVA_HOME%%\lib\tools.jar; 

       完成以上步骤后，开始验证是否安装成功
       运行CMD（开始，运行，输入cmd，回车），Win7以上系统，右键点击“以管理员身份运行”“命令提示符”，然后输入javac，回车，假如出现了一堆如何使用java的帮助，那就是已经安装成功了
       如果没有显示java的帮助那么就重新设置环境变量，把AVA_HOME、PATH、CLASSPATH都删除掉，按上述步骤重新建立即可

4、反编译(解包)

   把待编译程序如C4009-C7P07.apk重命名为1.apk，复制到 C:\apktool 目录中，然后进行反编译(解包)
   用代码反编译(解包)，先 Windows + R 输入cmd，打开dos窗口，或在附件中运行“命令提示符”，打开dos界面
   在dos窗口输入： java -jar C:\apktool\apktool.jar d C:\apktool\1.apk -o C:\apktool\1

4、回编译（打包）
   用代码回编译（打包），先 Windows + R 输入cmd，打开dos窗口，或在附件中运行“命令提示符”，打开dos界面  
   在dos窗口输入： java -jar C:\apktool\apktool.jar b C:\apktool\1 -o C:\apktool\1_Mod.apk

5、Windows + R 输入cmd，打开dos窗口，或在附件中以管理员权限运行“命令提示符”，打开dos界面，根据电脑上安装的jdk位数

   Windows 64位系统安装*****-windows-x64为64位的jdk以及Windows 32位系统安装*****-windows-i586为32位的jdk 输入以下代码
   cd C:\Program Files\Java\jdk*\bin         
   Windows 64 位系统安装*****-windows-i586为32位的jdk 输入以下代码
   cd C:\Program Files (x86)\Java\jdk*\bin
   切换到jdk的bin目录：C:\Program Files\Java\jdk*\bin 或 C:\Program Files (x86)\Java\jdk*\bin

6、生成密钥文件

  在dos窗口输入：keytool -genkey -alias androiddebugkey -keyalg RSA -validity 36500 -keysize 2048 -keystore C:\apktool\debug.keystore -keypass android -storepass android
   
   出现问题并填写
   您的名字与姓氏是什么?
       [Unknown]: localhost
   您的组织单位名称是什么?
       [Unknown]: btbut
   您的组织名称是什么?
       [Unknown]: btbu
   您所在的城市或区域名称是什么?
       [Unknown]: haidian
   您所在的省/市/自治区名称是什么?
       [Unknown]: beijing
   该单位的双字母国家/地区代码是什么?
       [Unknown]: cn
   CN=localhost, OU=btbut, O=btbu, L=haidian, ST=beijing, C=cn 是否正确?
       [否]:  y

   填写相关信息后会在apktoolBox或apktoolAid目录下生成密钥文件 debug.keystore    
   就是我们需要的安卓Android签名密钥文件，（-validity 36500 表示证书的有效天数为36500天）

   其中：
        KeystoreFile密钥文件名为                            debug.keystore 
        -alias androiddebugkey 表示密钥别名KeystoreAlias为  androiddebugkey  
        -storepass android 表示密钥密码KeystorePassword为   android 
        -keypass android 表示密钥密码keypassPassword为      android 
        密钥文件名debug.keystore、密钥别名 androiddebugkey、 密钥storepass和keypassPassword密码 android 都可根据自己的需要设定 
  
  在dos窗口输入：输入keytool -list -v -keystore C:\apktool\debug.keystore 

   使用 -v 参数能看到详细的签名信息，包括md5和SHA1证书等其他功能，输入keytool命令，可查看详细命令

   若已有密钥，可跳过此步，直接用已有的密钥文件对回编译的apk进行签名

安卓开发工具自带用于调试程序的KeystoreFile密钥文件名为：debug.keystore ；KeystoreAlias 密钥别名是 androiddebugkey ；KeystorePassword 密码是 android


7、签名

   在dos窗口输入：

   不加时间戳验证参数 -tsa ： jarsigner -verbose -keystore C:\apktool\debug.keystore -storepass android -signedjar C:\apktool\1_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey
   加时间戳验证参数   -tsa ： jarsigner -verbose -keystore C:\apktool\debug.keystore -storepass android -signedjar C:\apktool\1_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey -tsa http://sha256timestamp.ws.symantec.com/sha256/timestamp

   注意：

   在签名命令参数
   jarsigner -verbose -keystore C:\apktool\debug.keystore -storepass android -signedjar C:\apktool\C4009_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey

   末尾加上 -tsa 时间戳验证参数，如赛门铁克提供的时间戳验证参数 -tsa http://sha256timestamp.ws.symantec.com/sha256/timestamp 后
   jarsigner -verbose -keystore C:\apktool\debug.keystore -storepass android -signedjar C:\apktool\C4009_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey -tsa http://sha256timestamp.ws.symantec.com/sha256/timestamp

   会解决签名时出现的 “未提供 -tsa 或 -tsacert, 此 jar 没有时间戳。如果没有时间戳, 则在签名者证书的到期日期 (2042-06-20) 或以后的任何撤销日期之后, 用户可能无法验证此 jar”的 警告。 注意：(2042-06-20)中的日期与所采用的签名证书有关，不同的证书有有所不同
   不过签名命令参数末尾不加 -tsa 时间戳参数，并不影响签名后的apk的安装和使用

   常用三种签名方式：signapk 签名、apksigner 签名、jarsigner
   签名【signapk】:             java -jar C:\apktool\signapk.jar testkey.x509.pem testkey.pk8 C:\apktool\1_Mod.apk C:\apktool\1_Mod_Signed.apk 
   签名【apksigner】:           java -jar C:\apktool\apksigner.jar -keystore C:\apktool\debug.keystore -alias androiddebugkey -pswd android -aliaspswd android C:\apktool\1_Mod.apk
   签名【jarsigner不加时间戳】: jarsigner -verbose -keystore C:\apktool\debug.keystore -storepass android -signedjar C:\apktool\1_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey
   签名【jarsigner加上时间戳】: jarsigner -verbose -keystore C:\apktool\debug.keystore -storepass android -signedjar C:\apktool\1_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey -tsa http://sha256timestamp.ws.symantec.com/sha256/timestamp

   zip对齐后apk压缩包里的文件都是整整齐齐的，解压运行速度就会得到提升
   程序用的是apktool里apksigner.jar签名或jdk里jarsigner.exe签名，都是v1签名
   用jdk里的apksigner.exe签名，是v2签名
   如果是v1签名，zip对齐既可以在签名之前做，也可以在签名之后做
   如果是v2签名，zip对齐只能在签名之前做
   
9、其中tool文件夹中的apktool.jar文件可替换成最新版的apktool.jar ，apktool官方网站：https://ibotpeaches.github.io/apktool/


简要过程

1. 新建文本文件，将下面的脚本复制到文本并保存，然后重命名为apktool.bat

@echo off
if "%PATH_BASE%" == "" set PATH_BASE=%PATH%
set PATH=%CD%;%PATH_BASE%;
java -jar -Duser.language=en "%~dp0\apktool.jar" %1 %2 %3 %4 %5 %6 %7 %8 %9


将下载的apktool_2.*.*.jar文件重命名为apktool.jar

将上述两个文件apktool.bat和apktool.jar文件放到同一文件夹下（任意路径），

2. 打开命令窗口（win+R-->cmd-->enter）, cmd 在dos 窗口进入到apktool目录下输入以下命令

(1)反编译（解包）
    apktool d 1.apk -f
	
	apktool d -f -m -s -r com.osfans.trime_20181226.apk
	

(2)回编译（打包）
   apktool b 1 -o 1_Mod.apk
   
   apktool b com.osfans.trime_20181226 -o app-release-mod.apk
   

(3)生成keystore 密钥
  keytool -genkeypair -alias androiddebugkey -keyalg RSA -validity 36500 -keystore debug.keystore
  输入密码: android
  一路回车 
  到最后时输入y

(4)给apk签名 
   jarsigner -verbose -keystore C:\apktool\debug.keystore -signedjar C:\apktool\1_Mod_Signed.apk C:\apktool\1_Mod.apk androiddebugkey
   
   jarsigner -verbose -keystore debug.keystore -signedjar app-release-signed.apk app-release-mod.apk androiddebugkey
   

命令行的解释
jarsigner -verbose -keystore [您的私钥存放路径] -signedjar [签名后文件存放路径] [未签名的文件路径] [您的证书的别名]
使用 jarsigner 签名的时候，特别注意最后一个参数：[您的证书的别名]，不是我们的 keystore 的文件名
命令行 jarsigner 签字和解决找不到证书链错误: https://blog.csdn.net/qq_18948359/article/details/79703658

(5)zipalign 对齐
   zipalign -f -v 4 C:\apktool\1_Mod_Signed.apk 1_Mod_Signed_zipalign.apk
或 C:\apktool\zipalign -f -v 4 1_Mod_Signed.apk 1_Mod_Signed_zipalign.apk 

   zipalign -f -v 4 app-release-signed.apk app-release-20191221.apk
   
   
使用命令行对其的方法：
1、在Android SDK的tools文件夹下，找到zipalign.exe文件。
2、把你要优化的apk复制到你解压出来的tools文件夹下。
开始->运行->CMD调出命令行窗口
命令行下输入 你解压的文件夹路径\zipalign -v 4 你要优化的apk名字.apk 优化后的apk名字.apk
例如C:\Windows\android-sdk-windows\tools\zipalign -v 4 Example.apk Example.1.apk
其中这里-v代表详细输出，4代表对齐为4个字节。

bat批量自动签名apk: https://blog.csdn.net/mqy1023/article/details/51472920
Android-APK签名工具-jarsigner和apksigner: https://blog.csdn.net/qq_32115439/article/details/55520012