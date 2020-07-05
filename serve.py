import http.server
import socketserver

import os

# Setting some variables needed for http.server to run,
# Keeping the default port 8080
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

# Changing to the directory, where the ready pictures will be.
os.chdir('pix_ready')

# Running the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port 8080.")
    httpd.serve_forever()