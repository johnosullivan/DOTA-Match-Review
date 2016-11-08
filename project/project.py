#!/usr/bin/python
print("Markup Project Fall 2016 John O'Sullivana and Stefan Barac\n")

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import dota2api
import sys

PORT_NUMBER = 8080
apikey = "EEC87D93C06D24AE7A9E243113D132BE"

class HTTPHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        html = ""
        #api = dota2api.Initialise(apikey)
        #match = api.get_match_details(match_id=sys.argv[1])
        html += "<!DOCTYPE html><html><head>"
        #Adding links
        html += "<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css' integrity='sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u' crossorigin='anonymous'>"
        html += "</head><body>"
        html += "<h1>My First Heading</h1><p>My first paragraph.</p>"
        html += "</body></html>"
        self.wfile.write(html)
        return

try:
    server = HTTPServer(('', PORT_NUMBER), HTTPHandler)
    print 'Webpage is located at localhost and port:',PORT_NUMBER
    server.serve_forever()

except KeyboardInterrupt:
    print ' Server Closed'
    server.socket.close()


