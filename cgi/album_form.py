import cgi

import db


def handle():
    form = cgi.FieldStorage()
    selected_artist = form.getfirst('selected_artist', 'None')
    name = form.getfirst('name', 'None')
    year = form.getfirst('year', 'None')

    db.insert_album(selected_artist, name, year)

    headers = '\n'.join([
        'Content-Type: text/html',
        'Content-Language: ru-RU'
    ])
    html = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../styles.css">
        <title>Новый Альбом</title>
    </head>
    <body>
        <header>
            <h1>Новый Альбом</h1>
            <div class="header-links-wrapper">
                <a href="/">Главная</a>
                <a href="/cgi/albums.py">Альбомы</a>
            </div>
        </header>
        <div class="new-object-info">
            <p>Имя: {}</p>
        </div>
    </body>
    </html>
    '''.format(name)

    print(headers)
    print(html)


handle()
