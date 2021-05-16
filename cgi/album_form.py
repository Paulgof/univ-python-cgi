import cgi
import os

import db


def handle():
    referer = os.environ['HTTP_REFERER']

    form = cgi.FieldStorage()
    selected_artist = form.getfirst('selected_artist', 'None')
    name = form.getfirst('name', 'None')
    year = form.getfirst('year', 'None')

    db.insert_album(selected_artist, name, year)

    headers = '\n'.join([
        'Status: 302 Moved',
        'Location: {}'.format(referer)
    ])
    html = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta http-equiv="refresh" content="0;url={}" /> 
        <title>redirecting</title>
    </head>
    </html>
    '''.format(referer)

    print(headers)
    print(html)


handle()
