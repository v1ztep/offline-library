from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from livereload import Server
from more_itertools import chunked
from pathlib import Path

BOOKS_PER_PAGE_NUMBER = 20


def on_reload():
    with open("media/description.json", "r", encoding="utf8") as my_file:
        books_json = my_file.read()
    books = json.loads(books_json)

    grouped_books = list(chunked(books, BOOKS_PER_PAGE_NUMBER))
    pages_amount = len(grouped_books)
    remove_outdated_pages(pages_amount)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('templates/template.html')

    for page_current_number, per_page_books in enumerate(grouped_books, start=1):
        grouped_by_two_books = list(chunked(per_page_books, 2))

        rendered_page = template.render(
            grouped_by_two_books=grouped_by_two_books,
            pages_amount=pages_amount,
            page_current_number=page_current_number,
        )

        with open(f'pages/index{page_current_number}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)
    print("Site rebuilded")


def remove_outdated_pages(pages_amount):
    paths_to_pages = list(Path('pages/').glob('index*.html'))
    if len(paths_to_pages) == 0:
        return

    names_pages = {path.name for path in paths_to_pages}
    expected_names_pages = {f'index{number}.html' for number in range(1, pages_amount + 1)}
    outdated_names = expected_names_pages.symmetric_difference(names_pages)
    print(outdated_names)

    while True:
        if not outdated_names:
            return
        Path(f'pages/{outdated_names.pop()}').unlink()


def main():
    Path('pages').mkdir(parents=True, exist_ok=True)

    on_reload()
    server = Server()
    server.watch('templates/template.html', on_reload)
    server.serve(root='.')


if __name__ == '__main__':
    main()
