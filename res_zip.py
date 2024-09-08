"""
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-09-07 22:31:32
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2024-09-08 16:16:33
"""
import os
import subprocess
import zipfile

# 压缩包名称
zip_filename = 'res.zip'

def add_folder_to_zip(zipf: zipfile.ZipFile, folder_path: str):
    """
    将指定文件夹添加到 ZIP 文件中，同时保持目录结构
    :param zipf: zipfile.ZipFile 对象
    :param folder_path: 要添加到 ZIP 文件中的文件夹路径
    """
    for foldername, subfolders, filenames in os.walk(folder_path):
        print(filenames)
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            # 在 ZIP 文件中创建相对路径
            relative_path = file_path.replace(r"/assets/resource_picli/base", "")
            zipf.write(file_path, relative_path)

def get_git_commit_count():
    """
    获取仓库的提交总数
    :param repo_path: 仓库路径，默认为当前路径
    :return: 提交总数，如果获取失败则返回空字符串
    """
    try:
        # 执行 Git 命令获取提交总数
        result = subprocess.run(
            ['git', 'rev-list', '--count', 'HEAD'],
            text=True,
            capture_output=True,
            check=True
        )
        # 返回提交总数
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"获取提交数失败: {e}")
        return ''

# 创建压缩包并添加文件
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    add_folder_to_zip(zipf, './assets/resource_picli/base/pipeline')
    add_folder_to_zip(zipf, './assets/resource_picli/base/image')
    add_folder_to_zip(zipf, './assets/resource_picli/data')
    zipf.write('./assets/interface.json', 'interface.json')

with open('version.txt', 'w', encoding='utf-8') as f:
    f.write(get_git_commit_count())
