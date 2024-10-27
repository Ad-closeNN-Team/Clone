# Load Mods In Folder
# This script will load all mods in a folder into the game
# Author: GitHub @JingHai-Lingyun
# Version: 1.0.0
# License: WTFPL

import tomllib
import os

def cprint(text):
    if config["basic"]["print-log"]:
        print(text)

# Load Config from samedir
try:
    with open("lmif.toml", "rb") as f:
        config = tomllib.load(f)
except FileNotFoundError:
    with open("lmif.toml", "w") as f:
        f.write("""[basic]
remove-file-before-load = true
print-log = false

[ignore]
ignore-to-remove = []
ignore-folder-to-copy = []
ignore-file-to-copy = []""")
    with open("lmif.toml", "rb") as f:
        config = tomllib.load(f)

# Initialize
cprint(os.getcwd())
os.system("@echo off")

# Remove current mods
if config["basic"]["remove-file-before-load"]:
    for file in os.listdir("./mods"):
        if file.endswith(".jar") and file not in config["ignore"]["ignore-to-remove"]:
            os.remove(os.path.join("./mods", file))
            cprint(f"删除了模组文件 \"{os.path.join('./mods', file)}\"")

# Copy mods from folder
current_dir = os.getcwd()
mods_dir = os.path.join(current_dir, 'mods')    
folders = [name for name in os.listdir(mods_dir) if os.path.isdir(os.path.join(mods_dir, name))]
cprint(f"需要确认的文件夹有 {folders}")
for folder in folders:
    if folder not in config["ignore"]["ignore-folder-to-copy"]:
        cprint(f"文件夹 \"{folder}\"需要操作的文件有 {os.listdir(os.path.join(mods_dir, folder))}")
        for file in os.listdir(os.path.join(mods_dir, folder)):
            if file.endswith(".jar") and file not in config["ignore"]["ignore-file-to-copy"]:
                cprint(f"复制模组文件 \"{os.path.join(mods_dir, folder, file)}\" 从文件夹 \"{os.path.join(mods_dir, folder)}\"") 
                cmd = f"copy \"{os.path.join(mods_dir, folder, file)}\" \"./mods\"" 
                cprint(f"os.system 执行命令 {cmd}")
                os.system(cmd)