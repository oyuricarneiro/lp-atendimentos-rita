import pathlib

files_to_fix = [
    '/Users/yuricarneiro/Downloads/framework-v20/lp-atendimentos-rita/index.html',
    '/Users/yuricarneiro/Downloads/framework-v20/lp-atendimentos-rita/style.css'
]

for file_path in files_to_fix:
    path = pathlib.Path(file_path)
    if path.exists():
        content = path.read_text(encoding='utf-8')
        new_content = content.replace('/lp-atendimentos-rita/', '/')
        if new_content != content:
            path.write_text(new_content, encoding='utf-8')
            print(f"Fixed paths in {path.name}")
