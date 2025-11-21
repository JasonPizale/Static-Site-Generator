import os
import shutil
import sys
from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

print(sys.argv)
if len(sys.argv) == 1:
    basepath = "/"
else:
    basepath = sys.argv[1]

DIR_STATIC = "static"
DIR_PUBLIC = "docs"
DIR_CONTENT = "content"
TEMPLATE_PATH = "template.html"

def main():
    copy_files_recursive(DIR_STATIC, DIR_PUBLIC)
    generate_pages_recursive(DIR_CONTENT, TEMPLATE_PATH, DIR_PUBLIC, basepath)
    
if __name__ == "__main__":
    main()