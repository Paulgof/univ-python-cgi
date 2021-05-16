import cgi

import db


def handle():
    existing_tables = {'artist', 'album', 'track'}

    params = cgi.FieldStorage()
    table_name = params.getfirst('obj', None)
    object_id = params.getfirst('id', None)

    headers = {
        'Status': '302 Moved',
        'Location': '/'
    }

    if table_name in existing_tables:
        db.delete_object_from(table_name, object_id)
        headers['Location'] = '/cgi/{}s.py'.format(table_name)

    print('\n'.join(['{}: {}'.format(key, value) for key, value in headers.items()]))
    print('''
    <html> 
        <head> 
        <meta http-equiv="refresh" content="0;url={}" /> 
        <title>Redirecting back</title> 
        </head> 
    </html>
    '''.format(headers['Location']))


handle()
