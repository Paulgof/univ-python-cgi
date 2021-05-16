import db


def handle():
    artists_list = db.select_all_from_table('artist')

    artist_row = '<tr><td>{}</td><td>{}</td><td><a href="/cgi/delete.py?obj=artist&id={}">✖</a></td></tr>'
    artists_rows = ''.join([artist_row.format(*row, row[0]) for row in artists_list])

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
        <title>Исполнители</title>
    </head>
    <body>
        <header>
            <h1>Исполнители</h1>
            <div class="header-links-wrapper">
                <a href="/">Главная</a>
            </div>
        </header>
        <div class="form-block">
            <h3>Новый исполнитель</h3>
            <div class="form-wrapper">
            <form method="POST" action="/cgi/artist_form.py">
                <p><label>Имя: <input type="text" name="name"></label></p>
                <p><input type="submit" value="Добавить"></p>
            </form>
            </div>
        </div>
        <div class="table-wrapper">
            <table>
            <caption>Таблица исполнителей</caption>
            <tr>
                <th>id</th>
                <th>Исполнитель</th>
                <th>Удалить</th>
            </tr>
            {}
            </table>
        </div>
    </body>
    </html>
    '''.format(artists_rows)

    print(headers)
    print(html)


handle()
