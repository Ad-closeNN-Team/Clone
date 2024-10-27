"""Generate README.md"""
input_file = 'Repos'

with open(input_file, 'r', encoding="utf-8") as repos, open('README.md', 'w', encoding="utf-8") as readme:
    readme.write("# Clone\n")
    readme.write("这是一个克隆了多个仓库的代码的仓库，由 [GitHub Actions](https://docs.github.com/zh/actions) 来完成自动化的 Clone 并上传至本仓库。\n\n")
    readme.write("> [!IMPORTANT]\n")
    important = """> 本仓库 Clone 的**所有仓库**均为删除了 `.git` 文件夹后才上传的，所以从本仓库下载仓库源代码将会失去包括\\
1.**历史提交记录**\\
2.**远程仓库地址**"""
    readme.write(important + '\n')
    readme.write("## 目前已有的仓库\n")
    for line in repos:
        repo = line.strip()  # 去除行末的换行符
        if repo:
            readme.write(f"- [{repo}](https://github.com/{repo})\n")
    with open("LastUpdate", 'r') as last_update:
        time = last_update.read()
    readme_file = f"""## 如何提交新的望 Clone 的仓库？
### 在 GitHub Web 上操作
#### 直接编辑（适用于有权限）
1. 打开文件 [Repos](https://github.com/Ad-closeNN-Team/Clone/edit/main/Repos)
2. 在文件中填写仓库名，并按照格式：**用户名(或组织名)/仓库名** (如**Hex-Dragon/PCL2**)
3. 提交更改
4. 在 [GitHub Actions](https://github.com/Ad-closeNN-Team/Clone/actions/workflows/Clone-repo.yml) 中运行工作流
#### 提交 Pull Request（适用于没有权限）
1. [Fork](https://github.com/Ad-closeNN-Team/Clone/fork) 本仓库
2. 打开文件 Repos
3. 在文件中填写仓库名，并按照格式：**用户名(或组织名)/仓库名** (如**Hex-Dragon/PCL2**)
4. 提交更改到 GitHub
5. 打开一个 Pull Request
6. 等待合并
### 在本地 Clone 后操作
#### 直接编辑（适用于有权限）
1. Clone 本仓库
2. 打开文件 Repos
3. 在文件中填写仓库名，并按照格式：**用户名(或组织名)/仓库名** (如**Hex-Dragon/PCL2**)
4. 提交更改
5. 在 [GitHub Actions](https://github.com/Ad-closeNN-Team/Clone/actions/workflows/Clone-repo.yml) 中运行工作流
#### 提交 Pull Request（适用于没有权限）
1. Clone 本仓库
2. 打开文件 Repos
3. 在文件中填写仓库名，并按照格式：**用户名(或组织名)/仓库名** (如**Hex-Dragon/PCL2**)
4. 提交更改到 GitHub
5. 打开一个 Pull Request
6. 等待合并

<p align="center"><strong>最后同步时间 <i>(UTC+8:00)</i></strong></p>
<p align="center"><strong>{time}</strong></p>"""
    readme.write(readme_file)

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file)
    return line_count
print(f"已生成 README 文档。文档行数: {count_lines('README.md')}")            
