# MarkUp Fall Project 2016

##### John O'Sullivan and Stefan Barac

Libraries Used:
- BaseHTTPServer (Basic HTTP Server)
  - BaseHTTPRequestHandler
  - HTTPServer
- dota2api (DOTA API)
- sys (System Python)
- cgi (Common Gateway Interface)
- time (Time Library)

### Do It Works:

The project designed is super simple. Once the python the script is ran, it will launch a basic HTTP server on the localhost. As soon as the user going to the url printed in the console a DOTA page will appear. To use the service enter a valid DOTA session match ID. Once enter and submitted via the client interface the python script begins processing. The HTTP handle catch the POST request and parses the payload. The payload is converted in a match_id. This match_id return a large JSON data object. This JSON object is passed into the html builder function. The html builder builds an unique html page from the object and returns it the client for display.  
