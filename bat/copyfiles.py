#!/usr/bin/python
# coding: utf-8 

import os

path = 'E:\\LocalRepository\\github\\naamning_jyutping'
files = os.listdir(path)
files = [ele for ele in files if 'yaml' in ele]

old_str = '2022.12.03'
new_str = '2023.03.28'

for file in files:
    if not os.path.isdir(file):
        file_data = []
        f = open(path+'\\'+file,'r',encoding='utf-8')
        iter_f = iter(f)
        for line in iter_f:
            if old_str in line:
                line = line.replace(old_str,new_str)
            file_data.append(line)
        f.close()
        f2 = open(path+'\\'+file,'w',encoding='utf-8')
        file_data2 = ''
        if file == 'naamning_baakwaa.dict.yaml':
            f3 = open('v_nb_zingjam_rime.txt','r',encoding='utf-8')
            f4 = open('tab_nbdict_2020_phrase.txt','r',encoding='utf-8')
            file_data2 = ''.join(file_data[0:188] + f3.readlines() + f4.readlines())
            f4.close()
            f3.close()
        elif file == 'naamning_bingwaa.dict.yaml':
            f3 = open('v_nb_zingjam_bw_rime.txt','r',encoding='utf-8')
            f4 = open('tab_nbdict_2020_bw_phrase.txt','r',encoding='utf-8')
            file_data2 = ''.join(file_data[0:179] + f3.readlines() + f4.readlines())
            f4.close()
            f3.close() 
        elif file == 'naamning_baakwaa.infer.dict.yaml':
            f3 = open('temp_xxxx4_infer.txt','r',encoding='utf-8')
            file_data2 = ''.join(file_data[0:27] + f3.readlines())
            f3.close() 
        elif file == 'naamning_bingwaa.infer.dict.yaml':
            f3 = open('temp_xxxx4_bw_infer.txt','r',encoding='utf-8')
            file_data2 = ''.join(file_data[0:27] + f3.readlines())
            f3.close() 
        else:
            file_data2 = ''.join(file_data)
        f2.write(file_data2)
        f2.close()
        