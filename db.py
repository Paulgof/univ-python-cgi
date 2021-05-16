import sqlite3

_DB_NAME = 'music.db'

SQL_CREATE_TABLES = [
    '''CREATE TABLE artist (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT);''',
    '''CREATE TABLE album (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        artist_id INTEGER, 
        name TEXT, 
        year INTEGER, 
        FOREIGN KEY (artist_id) REFERENCES artist(id)
    );''',
    '''CREATE TABLE track (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        album_id INTEGER, 
        name TEXT, 
        play_time REAL, 
        FOREIGN KEY (album_id) REFERENCES album(id)
    );'''
]

SQL_CHECK_TABLES = '''SELECT name FROM sqlite_master WHERE type = "table" AND name NOT LIKE "sqlite_%"'''


def _get_connection_and_cursor():
    connection = sqlite3.connect(_DB_NAME)
    return connection, connection.cursor()


def _close_cursor_and_connection(cursor, connection):
    cursor.close()
    connection.close()


def initiate_tables():
    connection, cursor = _get_connection_and_cursor()
    cursor.execute(SQL_CHECK_TABLES)
    db_tables = cursor.fetchall()
    if db_tables:
        _close_cursor_and_connection(cursor, connection)
        return

    for sql_create in SQL_CREATE_TABLES:
        cursor.execute(sql_create)

    connection.commit()
    _close_cursor_and_connection(cursor, connection)


def select_all_from_table(table_name):
    connection, cursor = _get_connection_and_cursor()
    cursor.execute('''SELECT * FROM {};'''.format(table_name))
    result = cursor.fetchall()
    _close_cursor_and_connection(cursor, connection)
    return result


def select_all_related_album():
    connection, cursor = _get_connection_and_cursor()
    cursor.execute(
        '''SELECT album.id, artist.name, album.name, album.year 
        FROM album JOIN artist ON album.artist_id = artist.id;'''
    )
    result = cursor.fetchall()
    _close_cursor_and_connection(cursor, connection)
    return result


def select_all_related_track():
    connection, cursor = _get_connection_and_cursor()
    cursor.execute(
        '''SELECT track.id, artist.name, album.name, track.name, track.play_time
        FROM track JOIN (album JOIN artist on album.artist_id = artist.id) ON track.album_id = album.id;'''
    )
    result = cursor.fetchall()
    _close_cursor_and_connection(cursor, connection)
    return result


def insert_artist(name):
    connection, cursor = _get_connection_and_cursor()
    cursor.execute(
        '''INSERT INTO artist(name) VALUES ("{}");'''.format(name)
    )
    connection.commit()
    _close_cursor_and_connection(cursor, connection)


def insert_album(artist_id, name, year):
    connection, cursor = _get_connection_and_cursor()
    cursor.execute(
        '''INSERT INTO album(artist_id, name, year) VALUES ({}, "{}", {});'''.format(
            artist_id,
            name,
            year
        )
    )
    connection.commit()
    _close_cursor_and_connection(cursor, connection)


def insert_track(album_id, name, play_time):
    connection, cursor = _get_connection_and_cursor()
    cursor.execute(
        '''INSERT INTO track(album_id, name, play_time) VALUES ({}, "{}", {});'''.format(
            album_id,
            name,
            play_time
        )
    )
    connection.commit()
    _close_cursor_and_connection(cursor, connection)


def delete_object_from(table_name, object_id):
    connection, cursor = _get_connection_and_cursor()
    cursor.execute(
        '''DELETE FROM {} WHERE id = {};'''.format(
            table_name,
            object_id
        )
    )
    connection.commit()
    _close_cursor_and_connection(cursor, connection)
