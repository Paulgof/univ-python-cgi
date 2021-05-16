import db


def handle():
    artists_list = db.select_all_from_table('artist')
    albums_list = db.select_all_related_album()

    artists_options = '<option value="{}">{}</option>'
    artists_select = '<select size="1" name="selected_artist">{}</select>'.format(
        ''.join([artists_options.format(*row) for row in artists_list])
    )

    album_row = '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' \
                '<td><a href="/cgi/delete.py?obj=album&id={}">✖</a></td></tr>'
    albums_rows = ''.join([album_row.format(*row, row[0]) for row in albums_list])

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
        <title>Альбомы</title>
    </head>
    <body>
        <header>
            <h1>Альбомы</h1>
            <div class="header-links-wrapper">
                <a href="/">Главная</a>
            </div>
        </header>
        <div class="form-block">
            <h3>Новый альбом</h3>
            <div class="form-wrapper">
            <form method="POST" action="/cgi/album_form.py">
                <p><label>Исполнитель: 
                    {artist_select}
                </label></p>
                <p><label>Имя альбома: <input type="text" name="name"></label></p>
                <p><label>Год выпуска: <input type="number" name="year"></label></p>
                <p><input type="submit" value="Добавить"></p>
            </form>
            </div>
        </div>
        <div class="table-wrapper">
            <table>
            <caption>Таблица альбомов</caption>
            <tr>
                <th>id</th>
                <th>Исполнитель</th>
                <th>Альбом</th>
                <th>Год выпуска</th>
                <th>Удалить</th>
            </tr>
            {albums_table}
            </table>
        </div>
    </body>
    </html>
    '''.format(artist_select=artists_select, albums_table=albums_rows)

    print(headers)
    print(html)


handle()
