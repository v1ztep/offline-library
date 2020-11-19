from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
from livereload import Server
from more_itertools import chunked
from pathlib import Path

BOOKS_PER_PAGE_NUMBER = 20


def rebuild_site():
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
    pages_paths = list(Path('pages/').glob('index*.html'))
    if not pages_paths:
        return

    paths_names = {path.name for path in pages_paths}
    expected_names = {f'index{number}.html' for number in range(1, pages_amount + 1)}
    outdated_names = expected_names.symmetric_difference(paths_names)

    if not outdated_names:
        return
    for name in outdated_names:
        Path(f'pages/{name}').unlink()


def main():
    Path('pages').mkdir(parents=True, exist_ok=True)

    rebuild_site()
    server = Server()
    server.watch('templates/template.html', rebuild_site)
    server.serve(root='.')


if __name__ == '__main__':
    main()
