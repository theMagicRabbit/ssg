from textconverter import markdown_to_html_node
from mdextractor import extract_title
from os.path import basename, join, splitext
from os import makedirs

def generate_page(from_path, template_path, dest_path):
    with open(from_path, 'r', encoding='UTF-8') as source_file:
        markdown_source = source_file.read()
    with open(template_path, 'r', encoding='UTF-8') as template_file:
        template_source = template_file.read()
    html_div = markdown_to_html_node(markdown_source).to_html()
    title = extract_title(markdown_source)
    html_doc = template_source.replace("{{ Title }}", title).replace("{{ Content }}", html_div)
    file_slug = splitext(basename(from_path))
    makedirs(dest_path, exist_ok=True)
    html_file = join(dest_path, f"{file_slug}.html")
    with open(html_file, 'w', encoding='UTF-8') as out_file:
        out_file.write(html_doc)

    
    


    

