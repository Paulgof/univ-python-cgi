import cgi

import db


def raise_bad_time_error():
    print('Content-Type: text/html')
    print('''
    <html>
    <head>
        <title>ERROR</title>
    </head>
    <body>
    <h1>ERROR: BAD TIME</h1><p><a href="/cgi/tracks.py"><-- Back</a></p>
    </body>
    </html>
    ''')


def handle():
    form = cgi.FieldStorage()
    selected_album = form.getfirst('selected_album', 'None')
    name = form.getfirst('name', 'None')
    play_time_minutes = form.getfirst('minutes', '-1')
    play_time_seconds = form.getfirst('seconds', '-1')

    if not (play_time_minutes.isdigit() and play_time_seconds.isdigit()):
        raise_bad_time_error()
        return

    play_time_minutes, play_time_seconds = int(play_time_minutes), int(play_time_seconds)

    if any([
        play_time_minutes < 0,
        play_time_seconds < 0,
        play_time_seconds > 59,
        play_time_minutes == play_time_seconds == 0
    ]):
        raise_bad_time_error()
        return

    play_time = play_time_minutes + play_time_seconds / 100
    db.insert_track(selected_album, name, play_time)

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
        <title>Новый Трек</title>
    </head>
    <body>
        <header>
            <h1>Новый Трек</h1>
            <div class="header-links-wrapper">
                <a href="/">Главная</a>
                <a href="/cgi/tracks.py">Треки</a>
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
