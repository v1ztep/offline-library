from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from livereload import Server
from more_itertools import chunked


def on_reload():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('templates/template.html')
    rendered_page = template.render(
        group_books_list=group_books_list,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    print("Site rebuilded")


with open("static/description.json", "r", encoding="utf8") as my_file:
    books_json = my_file.read()
books_list = json.loads(books_json)
group_books_list = list(chunked(books_list, 2))

on_reload()

server = Server()

server.watch('templates/template.html', on_reload)

server.serve(root='.')

