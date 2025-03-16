from textconverter import markdown_to_html_node
from mdextractor import extract_title
from os.path import basename, join, splitext, isfile, exists
from os import makedirs, listdir, mkdir

def generate_page(from_path, template_path, dest_path, basepath):
    with open(from_path, 'r', encoding='UTF-8') as source_file:
        markdown_source = source_file.read()
    with open(template_path, 'r', encoding='UTF-8') as template_file:
        template_source = template_file.read()
    html_div = markdown_to_html_node(markdown_source).to_html()
    title = extract_title(markdown_source)
    html_doc = (
            template_source.replace("{{ Title }}", title)
            .replace("{{ Content }}", html_div)
            .replace('href="/', f"href=\"{basepath}")
            #.replace('src="/', f"src=\"{basepath}")
    )
    file_slug,_ = splitext(basename(from_path))
    makedirs(dest_path, exist_ok=True)
    html_file = join(dest_path, f"{file_slug}.html")
    with open(html_file, 'w', encoding='UTF-8') as out_file:
        out_file.write(html_doc)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for f in listdir(dir_path_content):
        rel_src = join(dir_path_content, f)
        if not isfile(rel_src):
            rel_dest = join(dest_dir_path, f)
            if not exists(dest_dir_path):
                mkdir(dest_dir_path)
            generate_pages_recursive(rel_src, template_path, rel_dest, basepath)
        elif rel_src.endswith(".md"):
            print(f"Generating page from: {rel_src}")
            generate_page(rel_src, template_path, dest_dir_path, basepath)


