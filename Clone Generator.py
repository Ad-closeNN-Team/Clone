"""Generate Clone.sh"""
input_file = 'Repos'
output_file = 'Clone.sh'

with open('Repos', 'r', encoding='utf-8') as file:
    repositories = file.read().splitlines()
sorted_repositories = sorted(repositories, key=str.lower)
with open("Repos", 'w') as Repos:
    print("仓库列表: \n")
    for repo in sorted_repositories:
        Repos.write(repo + '\n')
        print(repo)
print("仓库列表已排序")

with open(input_file, 'r', encoding="utf-8") as repos, open(output_file, 'w', encoding="utf-8") as clone_script:
    for line in repos:
        repo = line.strip()
        if repo:
            clone_script.write(f"git clone https://github.com/{repo}.git\n")

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        line_count = sum(1 for line in file)
    return line_count
print(f"已生成 Clone 脚本。脚本行数: {count_lines('Clone.sh')}")