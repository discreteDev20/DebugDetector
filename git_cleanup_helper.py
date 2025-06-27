import os
import subprocess

def count_git_files():
    try:
        output = subprocess.check_output(['git', 'ls-files'])
        files = output.decode().split('\n')
        return len(files)
    except Exception as e:
        print("Git not initialized or error reading files.")
        return 0

def create_gitignore():
    with open(".gitignore", "w") as f:
        f.write("""__pycache__/
.vscode/
.env/
*.pyc
*.log
*.zip
""")
    print("✅ .gitignore created to ignore system files.")

file_count = count_git_files()

if file_count > 1000:
    print(f"⚠️ Git is tracking {file_count} files. This can slow down your project.")
    create_gitignore()
else:
    print(f"✅ Git is only tracking {file_count} files. You’re good!")
