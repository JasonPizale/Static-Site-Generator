import os
import shutil
def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for name in os.listdir(source_dir_path):
        source_path = os.path.join(source_dir_path, name)
        dest_path = os.path.join(dest_dir_path, name)

        if os.path.isdir(source_path):
            copy_files_recursive(source_path, dest_path)
        else:
            shutil.copy2(source_path, dest_path)