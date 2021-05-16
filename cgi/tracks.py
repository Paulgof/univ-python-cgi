import db


def float_to_time(float_time):
    minutes = int(float_time)
    seconds = int((float_time - minutes) * 100)
    if seconds < 10:
        seconds = '0{}'.format(seconds)

    return '{}:{}'.format(minutes, seconds)


def handle():
    albums_list = db.select_all_from_table('album')
    tracks_list = db.select_all_related_track()

    albums_options = '<option value="{}">{}</option>'
    albums_select = '<select size="1" name="selected_album">{}</select>'.format(
        ''.join([albums_options.format(row[0], row[2]) for row in albums_list])
    )

    track_row = '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>' \
                '<td><a href="/cgi/delete.py?obj=track&id={}">✖</a></td></tr>'
    tracks_rows = ''.join([track_row.format(*row[:-1], float_to_time(row[-1]), row[0]) for row in tracks_list])

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
        <title>Треки</title>
    </head>
    <body>
        <header>
            <h1>Треки</h1>
            <div class="header-links-wrapper">
                <a href="/">Главная</a>
            </div>
        </header>
        <div class="form-block">
            <h3>Новый трек</h3>
            <div class="form-wrapper">
            <form method="POST" action="/cgi/track_form.py">
                <p><label>Альбом: 
                    {album_select}
                </label></p>
                <p><label>Имя трека: <input type="text" name="name"></label></p>
                <p><label>Продолжительность:
                    <div class="time-wrapper">
                        <input type="number" name="minutes" value="0">
                        <span>:</span>
                        <input type="number" name="seconds" value="0">
                    </div>
                </label></p>
                <p><input type="submit" value="Добавить"></p>
            </form>
            </div>
        </div>
        <div class="table-wrapper">
            <table>
            <caption>Таблица треков</caption>
            <tr>
                <th>id</th>
                <th>Исполнитель</th>
                <th>Альбом</th>
                <th>Трек</th>
                <th>Продолжительность</th>
                <th>Удалить</th>
            </tr>
            {tracks_table}
            </table>
        </div>
    </body>
    </html>
    '''.format(album_select=albums_select, tracks_table=tracks_rows)

    print(headers)
    print(html)


handle()
