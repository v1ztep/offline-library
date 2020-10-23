from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from livereload import Server


def on_reload(dict):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('templates/template.html')
    rendered_page = template.render(
        books_dict=dict,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    print("Site rebuilded")


with open("static/description.json", "r", encoding="utf8") as my_file:
    books_json = my_file.read()
books_dict = json.loads(books_json)

on_reload(books_dict)

server = Server()

server.watch('templates/template.html', on_reload(books_dict))

server.serve(root='.')

