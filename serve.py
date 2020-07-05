import http.server
import socketserver
import socket
import os

# First, let's find out what our local IP address is, so we can advise the user to it later on.
def get_IP():
    try:
        host_name = socket.gethostname()
        my_ip = socket.gethostbyname(host_name)
    except:
        print("Couldn't get my IP address. Please check your network and do try again.")
    finally:
        return my_ip

# ip_address = get_IP()

# Setting some variables needed for http.server to run,
# Keeping the default port 8080
PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

# Changing to the directory, where the ready pictures will be.
os.chdir('pix_ready')

# Running the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at {}:8080".format(get_IP()))
    httpd.serve_forever()