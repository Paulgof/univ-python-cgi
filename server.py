import os
from http.server import HTTPServer, CGIHTTPRequestHandler

import db

os.chdir('e://www')

db.initiate_tables()

handler = CGIHTTPRequestHandler
handler.cgi_directories = ['/cgi']

server_address = ('localhost', 8000)
http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
http_server.serve_forever()
