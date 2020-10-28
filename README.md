# Офлайн библиотека

Офлайн библиотека, спарсенных книг с сайта [tululu.org](https://tululu.org/).

Пример работы сайта на [GitHub-Pages](https://v1ztep.github.io/offline-library_GitHub-Pages/pages/index1.html).

[GitHub репозиторий](https://github.com/v1ztep/offline-library_GitHub-Pages) сайта под GitHub-Pages с информацией по деплою.

## Запуск

Для запуска библиотеки у вас уже должен быть установлен [Python 3](https://www.python.org/downloads/release/python-379/).

- Скачайте код.
- Скачайте книги используя [парсер книг c сайта tululu.org](https://github.com/v1ztep/Parser-online-library), обязательный аргумент парсера `--dest_folder media`. Скопируйте итоговую папку(media) в корень "offline-library".
- Установите зависимости командой `pip install -r requirements.txt`.
- Запустите сайт командой `python render_website.py`.

После этого переходите по ссылке [http://127.0.0.1:5500/pages/index1.html](http://127.0.0.1:5500/pages/index1.html).

