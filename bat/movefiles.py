#!/usr/bin/python
# coding: utf-8 

import os
import shutil

path = 'E:\\LocalRepository\\github\\naamning_jyutping'
files = os.listdir(path)
files = [ele for ele in files if 'yaml' in ele]

for file in files:
    if not os.path.isdir(file):
        shutil.copy(path+'\\'+file,'C:\\Users\\Administrator\\AppData\\Roaming\\Rime')
        if 'dict' in file:
            shutil.copy(path+'\\'+file,'E:\\LocalRepository\\github\\naamning_jyutping_android')
            shutil.copy(path+'\\'+file,'E:\\LocalRepository\\github\\naamning_jyutping_build\\app-release-25249-o_1dm0eunhm6jq1iv3rphtqt165lq-uid-574023\\assets\\rime')