#!/usr/bin/python
# coding: utf-8 

import os
import re
import sys
import shutil
import subprocess
from datetime import datetime
from typing import List, Tuple

# 定义目标路径
RIME_USER_DIR = os.path.expanduser(r'~\AppData\Roaming\Rime')
ANDROID_REPO_DIR = r'E:\LocalRepository\github\naamning_jyutping_android'
ANDROID_ASSETS_DIR = r'E:\LocalRepository\github\naamning_jyutping_build\app-release-25249-o_1dm0eunhm6jq1iv3rphtqt165lq-uid-574023\assets\rime'

def get_current_version() -> str:
    """获取当前日期，格式为 YYYY.MM.DD"""
    return datetime.now().strftime("%Y.%m.%d")

def extract_version_from_file(file_path: str) -> str:
    """从 YAML 文件中提取版本号"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        match = re.search(r'version:\s*"(\d{4}\.\d{2}\.\d{2})"', content)
        if match:
            return match.group(1)
        raise ValueError(f"在文件中找不到版本号: {file_path}")

def update_version_in_file(file_path: str, old_version: str, new_version: str) -> List[str]:
    """更新文件中的版本号"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        return content.replace(f'version: "{old_version}"', f'version: "{new_version}"').splitlines(True)

def merge_files(base_content: List[str], 
                header_lines: int, 
                *additional_files: Tuple[str, str]) -> str:
    """合并基础内容和附加文件"""
    result = base_content[:header_lines]
    for file_path, _ in additional_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            result.extend(f.readlines())
    return ''.join(result)

def copy_files_to_targets(source_dir: str, yaml_files: List[str]) -> None:
    """将处理好的文件复制到目标目录"""
    print("\n开始复制文件到目标目录...")
    
    # 检查目标目录是否存在
    for target_dir in [RIME_USER_DIR, ANDROID_REPO_DIR, ANDROID_ASSETS_DIR]:
        if not os.path.exists(target_dir):
            raise ValueError(f"目标目录不存在: {target_dir}")
    
    for file_name in yaml_files:
        source_path = os.path.join(source_dir, file_name)
        if not os.path.isdir(source_path):
            try:
                # 复制到 Rime 用户目录
                shutil.copy(source_path, RIME_USER_DIR)
                print(f"已复制到 Rime 用户目录: {file_name}")
                
                # 如果是非ipa文件，复制到 Android 相关目录
                if 'ipa' not in file_name:
                    shutil.copy(source_path, ANDROID_REPO_DIR)
                    shutil.copy(source_path, ANDROID_ASSETS_DIR)
                    print(f"已复制到 Android 目录: {file_name}")
            except Exception as e:
                print(f"复制文件 {file_name} 时出错: {str(e)}")
                continue

def main():
    # 路径设置
    source_dir = r'E:\LocalRepository\github\naamning_jyutping'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bat_path = os.path.join(current_dir, 'expbat.bat')

    try:
        print("正在运行 expbat.bat ...")
        subprocess.run(bat_path, shell=True, cwd=current_dir, check=True)
    except subprocess.CalledProcessError as e:
        print("bat 执行出错，返回码：", e.returncode)
        print("错误信息：", e)
        sys.exit(1)
    
    # 获取所有 yaml 文件
    yaml_files = [f for f in os.listdir(source_dir) if f.endswith('.yaml')]
    if not yaml_files:
        raise ValueError("源目录中没有找到 YAML 文件")
    
    new_version = get_current_version()
    print(f"正在更新所有文件到版本: {new_version}")
    
    for file_name in yaml_files:
        source_path = os.path.join(source_dir, file_name)
        try:
            # 获取当前文件的版本号
            old_version = extract_version_from_file(source_path)
            print(f"正在处理 {file_name}: {old_version} -> {new_version}")
            
            # 更新文件中的版本号
            file_content = update_version_in_file(source_path, old_version, new_version)
            
            # 定义文件合并规则
            merge_rules = {
                'naamning_baakwaa.dict.yaml': (190, [
                    (os.path.join(current_dir, 'v_nb_zingjam_rime.txt'), 'r'),
                    (os.path.join(current_dir, 'tab_nbdict_all_phrase.txt'), 'r')
                ]),
                'naamning_bingwaa.dict.yaml': (180, [
                    (os.path.join(current_dir, 'v_nb_zingjam_bw_rime.txt'), 'r'),
                    (os.path.join(current_dir, 'tab_nbdict_all_bw_phrase.txt'), 'r')
                ]),
                'naamning_baakwaa.infer.dict.yaml': (28, [
                    (os.path.join(current_dir, 'temp_xxxx4_infer.txt'), 'r')
                ]),
                'naamning_bingwaa.infer.dict.yaml': (28, [
                    (os.path.join(current_dir, 'temp_xxxx4_bw_infer.txt'), 'r')
                ])
            }
            
            # 根据规则处理文件
            if file_name in merge_rules:
                header_lines, additional_files = merge_rules[file_name]
                final_content = merge_files(file_content, header_lines, *additional_files)
            else:
                final_content = ''.join(file_content)
            
            # 写入最终内容
            with open(source_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"成功更新 {file_name}")
            
        except ValueError as e:
            print(f"警告: {e}")
            continue
    
    # 复制文件到目标目录
    copy_files_to_targets(source_dir, yaml_files)

if __name__ == '__main__':
    main()
        