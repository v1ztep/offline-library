# Офлайн библиотека

Офлайн библиотека, спарсенных книг с сайта [tululu.org](https://tululu.org/).

## Запуск

Для запуска библиотеки у вас уже должен быть установлен Python 3.

- Скачайте код
- Скачайте книги используя [парсер книг c сайта tululu.org](https://github.com/v1ztep/Parser-online-library), обязательный аргумент парсера `--dest_folder media`. Скопируйте итоговую папку(media) в корень "offline-library".
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите сайт командой `python render_website.py`

После этого переходите по ссылке [http://127.0.0.1:5500/pages/index1.html](http://127.0.0.1:5500/pages/index1.html).

