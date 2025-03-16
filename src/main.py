from textnode import TextNode, TextType
from os.path import exists, isfile, join
from os import mkdir, listdir
from shutil import rmtree, copy
from htmlgenerator import generate_pages_recursive

def delete_public(public_path):
    if exists(public_path):
        rmtree(public_path)
    mkdir(public_path)

def recursive_cp_dir(src, dest):
    if not exists(src):
        raise FileNotFoundError(f"{src} does not exist")
    for f in listdir(src):
        rel_src = join(src, f)
        if not isfile(rel_src):
            rel_dest = join(dest, f)
            mkdir(rel_dest)
            recursive_cp_dir(rel_src, rel_dest)
        else:
            print(f"Copy {rel_src} to {dest}")
            copy(rel_src, dest)


def main():
    delete_public("public")
    recursive_cp_dir("static", "public")
    #generate_page("content/index.md", "template.html", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == '__main__':
    main()

