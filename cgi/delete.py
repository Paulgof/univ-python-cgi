import cgi
import os

import db


def handle():
    existing_tables = {'artist', 'album', 'track'}

    params = cgi.FieldStorage()
    table_name = params.getfirst('obj', None)
    object_id = params.getfirst('id', None)

    referer = os.environ['HTTP_REFERER']

    headers = '\n'.join([
        'Status: 302 Moved',
        'Location: {}'.format(referer)
    ])
    if table_name in existing_tables:
        db.delete_object_from(table_name, object_id)

    print(headers)
    print('''
    <html> 
        <head> 
        <meta http-equiv="refresh" content="0;url={}" /> 
        <title>Redirecting back</title> 
        </head> 
    </html>
    '''.format(referer))


handle()
