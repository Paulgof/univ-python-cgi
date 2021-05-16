import cgi
import os

import db


def handle():
    referer = os.environ['HTTP_REFERER']

    form = cgi.FieldStorage()
    name = form.getfirst('name', 'None')

    db.insert_artist(name)

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
