import os
import shutil

# 定义 Repo 文件夹的路径
repo_path = 'Repo'  # 替换为你的 Repo 文件夹的实际路径

# 遍历 Repo 文件夹下的所有子文件夹
for root, dirs, files in os.walk(repo_path):
    # 检查是否存在 .git 文件夹
    if '.git' in dirs:
        git_folder_path = os.path.join(root, '.git')
        try:
            # 删除 .git 文件夹
            shutil.rmtree(git_folder_path)
            print(f"已删除: {git_folder_path}")
        except Exception as e:
            print(f"遇到未知错误，无法删除文件夹 {git_folder_path}: {e}")