import http.server
import socketserver
import socket
import os

# First, let's find out what our local IP address is, so we can advise the user to it later on.
def get_IP():
    try:
        host_name = socke.gethostname()
        my_ip = socket.gethostbyname(host_name)
    except:
        print("Couldn't get my IP address. Please check your network and do try again.")
    finally:
        return my_ip

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

os.chdir('pix_ready')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at {}:8080".format(my_ip))
    httpd.serve_forever()