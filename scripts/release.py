import re
import subprocess
from pathlib import Path

def update_version(file_path, new_version):
    content = file_path.read_text()
    new_content = re.sub(
        r'version\s*=\s*"[^"]+"',
        f'version="{new_version}"',
        content
    )
    file_path.write_text(new_content)

def main():
    setup_py = Path("setup.py")
    current_version = re.search(r'version\s*=\s*"([^"]+)"', setup_py.read_text()).group(1)
    print(f"Current version: {current_version}")
    
    new_version = input("Enter new version: ")
    
    update_version(setup_py, new_version)
    
    subprocess.run(["git", "add", "setup.py"])
    subprocess.run(["git", "commit", "-m", f"Bump version to {new_version}"])
    subprocess.run(["git", "tag", f"v{new_version}"])
    subprocess.run(["git", "push"])
    subprocess.run(["git", "push", "--tags"])
    
    print(f"Released version {new_version}")

if __name__ == "__main__":
    main()
