from textnode import TextNode, TextType
from os.path import exists, isfile, join
from os import mkdir, listdir
from shutil import rmtree, copy

def recursive_cp_dir(src, dest):
    if not exists(src):
        raise FileNotFoundError(f"{src} does not exist")
    if exists(dest):
        rmtree(dest)
    mkdir(dest)

    for f in listdir(src):
        rel_src = join(src, f)
        if not isfile(rel_src):
            rel_dest = join(dest, f)
            recursive_cp_dir(rel_src, rel_dest)
        else:
            print(f"Copy {rel_src} to {dest}")
            copy(rel_src, dest)


def main():
    recursive_cp_dir("static", "public")

if __name__ == '__main__':
    main()

