import os
import shutil

USER = os.getlogin()
BACKUP_PATH = "/home/" + USER + "/backup"
PATHS = ("/home/" + USER + "/.config", "/home/" + USER + "/Documents", "/home/" + USER + "/Downloads", "/home/" + USER + "/Pictures", "/home/" + USER + "/Music", "/home/" + USER + "/Videos")


def main():
    print(f"[\033[95m*\033[0m] Creating backup folder in '{BACKUP_PATH}'..")
    if not os.path.exists(BACKUP_PATH):
        os.makedirs(BACKUP_PATH)
        print("[\033[95m*\033[0m] Done")
    for path in PATHS:
        root_dir = path.rsplit("/", 1)[-1] + "/"
        new_path = BACKUP_PATH + "/" + root_dir
        print(f"[\033[95m*\033[0m] Copying '{path}' to '{BACKUP_PATH}'")
        if not os.path.exists(new_path):
            shutil.copytree(path, new_path)
        print("[\033[95m*\033[0m] Done")
        
if __name__ == "__main__":
    main()
