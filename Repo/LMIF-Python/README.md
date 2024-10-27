# LMIF-Python
让你的模组可以从自定义文件夹中加载

## 使用方式
下载 lmif.exe 放到你的版本文件夹下，PCL 启动器配置启动前执行命令为 `cd /D "{verindie}" && lmif.exe`

## 配置文件解析
```toml
[basic]
remove-file-before-load = true # 删除上一次加载的 Mod，并从所有文件夹中重新取出 Mod
print-log = false # 向控制台打印 LMIF 操作日志

[ignore]
ignore-to-remove = [] # 在删除 Mod 时不删除指定文件，需要是文件全名（包括后缀）
ignore-folder-to-copy = [] # 在复制模组时不从指定文件夹复制
ignore-file-to-copy = [] # 在复制模组时不复制指定文件，需要是文件全名（包括后缀）
```
