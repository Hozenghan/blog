import os
import re

# 获取当前文件夹下的所有md文件
def get_md_files():
    return [f for f in os.listdir() if f.endswith('.md')]

# 处理并替换md文件中的img标签
def replace_img_tags(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 使用正则表达式替换img标签中的src路径
    updated_content = re.sub(
        r'<img src="./([^"]+)" alt="([^"]+)" style="([^"]+)" />',
        lambda match: f'<img src="https://raw.githubusercontent.com/Hozenghan/blogsResources/master/images/{os.path.basename(match.group(1))}" alt="{match.group(2)}" style="{match.group(3)}" />',
        content
    )

    # 如果需要将更新后的内容写回文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

# 批量处理所有md文件
def process_md_files():
    md_files = get_md_files()
    for md_file in md_files:
        replace_img_tags(md_file)
        print(f"Processed {md_file}")

# 执行批量替换操作
process_md_files()
