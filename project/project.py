#!/usr/bin/python
print("Markup Project Fall 2016 John O'Sullivan and Stefan Barac\n")

# Gets libraries from BaseHTTPServer to run script
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
#from http.server import BaseHTTPRequestHandler,HTTPServer
#import socketserver
# Dota API
import dota2api
# System Library
import sys
# Common Gateway Interface
import cgi
# Gets the time Library
import time
# Port Number to run the webserver local
PORT_NUMBER = 8080
# Our api key to use with dota2api
apikey = "EEC87D93C06D24AE7A9E243113D132BE"
# Creating an instance of the api
api = dota2api.Initialise(apikey)
# Gets the match data to build a webpage (Test)
#match = api.get_match_details(match_id=1000193456)
match = ""
matchnum = ""
#print(match)

def buildTop(data):
    #Created the title header of html
    top = ""
    top += "<h2 style=\"color:#888888\">"
    top += data['lobby_name']
    top += "</h2>"
    return top

def buildBody(data):
    #print data
    bodycontent = ""
    mode =  unicode(data['game_mode_name'])
    #Gets all the players of the match
    players = data['players']
    bodycontent += "<ul style=\"background-color: #574f48;\" class=\"nav nav-tabs\">"
    bodycontent += "<li style=\"background-color: #3e3f40;\" class=\"active\"><a data-toggle=\"tab\" href=\"#general\">General</a></li>"
    bodycontent += "<li style=\"background-color: #3e3f40;\" ><a data-toggle=\"tab\" href=\"#players\">Players</a></li>"
    bodycontent += "<li style=\"background-color: #3e3f40;\" ><a data-toggle=\"tab\" href=\"#stats\">Results</a></li>"
    bodycontent += "</ul>"
    bodycontent += "<div style=\"background-color: #574f48;\" class=\"tab-content\">"
    bodycontent += "<div id=\"general\" class=\"tab-pane fade in active\"><h4 style=\"color:#888888\">General</h4>"
    bodycontent += "<h5 style=\"color:#888888\"> Match Name: "
    #Sets the game name
    bodycontent += unicode(data['lobby_name'])
    bodycontent += "</h5>"
    bodycontent += "<h5 style=\"color:#888888\"> Match ID: "
    #Sets the match id
    bodycontent += unicode(data['match_id'])
    bodycontent += "</h5>"
    bodycontent += "<h5 style=\"color:#888888\"> Start Time: "
    timefloat = float(data['start_time'])
    #Sets the start time
    bodycontent += time.strftime("%H:%M:%S", time.gmtime(timefloat))
    bodycontent += "</h5>"
    bodycontent += "<h5 style=\"color:#888888\"> End Time: "
    #Sets the end time
    endtime = data['duration'] + timefloat
    bodycontent += time.strftime("%H:%M:%S", time.gmtime(endtime))
    bodycontent += "</h5>"
    #Gets the total number of players
    bodycontent += "<h5 style=\"color:#888888\"> Number Of Players: "
    bodycontent += unicode(len(players))
    bodycontent += "</h5 style=\"color:#888888\">"
    bodycontent += "<h5 style=\"color:#888888\"> Duration: "
    #The length of duration
    bodycontent += unicode(data['duration'] / 60)
    bodycontent += " Mins</h5>"
    bodycontent += "</div>"
    bodycontent += "<div id=\"players\" class=\"tab-pane fade in \"><h4 style=\"color:#888888\">Players</h4>"
    bodycontent += "<table class=\"table\">"
    #bodycontent += "<thead><tr><th>Account's ID</th><th>Deaths</th><th>Kills</th></tr></thead>"
    bodycontent += "<thead><tr><th>Account's</th></tr></thead>"
    bodycontent += "<tbody>"
    for player in players:
        #Gets the hero id
        herokid = unicode(player.get('hero_id'))
        #Checks the game mode
        if mode == "Captains Draft":
            team = 0
            for pick in data['picks_bans']:
                if (unicode(pick.get('hero_id')) == herokid):
                    team = pick.get('team')

            if (team == 0):
                bodycontent += "<tr style=\"background-color:#3a513e\">"

            if (team == 1):
                bodycontent += "<tr style=\"background-color:#513a3a\">"
        else:
            bodycontent += "<tr>"

        #Sets the players ba
        bodycontent += "<td>"
        bodycontent += "<div class=\"panel-group\"><div class=\"panel panel-default\"><div class=\"panel-heading\"><h4 class=\"panel-title\"><a data-toggle=\"collapse\" href=\"#collapse"
        #Sets panel id
        bodycontent += unicode(player.get('account_id'))
        bodycontent += "\">"
        #Display player name
        bodycontent += unicode(player.get('account_id'))
        bodycontent += " - "
        bodycontent += unicode(player.get('hero_name'))
        #Displays players kills
        bodycontent += " Kills: "
        bodycontent += unicode(player.get('kills'))
        #Displays the players dealths
        bodycontent += " Dealths: "
        bodycontent += unicode(player.get('deaths'))
        #Displays the players assists
        bodycontent += " Assists: "
        bodycontent += unicode(player.get('assists'))
        #Sets links to dotabuff
        bodycontent += "</a></h4></div><div id=\"collapse"
        bodycontent += unicode(player.get('account_id'))
        bodycontent += "\" class=\"panel-collapse collapse\"><ul class=\"list-group\">"
        bodycontent += "<li class=\"list-group-item\"><a href=\"https://www.dotabuff.com/players/"
        bodycontent += unicode(player.get('account_id'))
        bodycontent += "\">View Player Profile: https://www.dotabuff.com/players/"
        bodycontent += unicode(player.get('account_id'))
        #Sets the gold/min
        bodycontent += "</a></li>"
        bodycontent += "<li class=\"list-group-item\"><b>Gold/Min:</b> "
        bodycontent += unicode(player.get('gold_per_min'))
        bodycontent += "</li>"
        #Sets the xp/min
        bodycontent += "<li class=\"list-group-item\"><b>XP/Min:</b> "
        bodycontent += unicode(player.get('xp_per_min'))
        bodycontent += "</li>"
        #Sets the players denies
        bodycontent += "<li class=\"list-group-item\"><b>Denies:</b> "
        bodycontent += unicode(player.get('denies'))
        bodycontent += "</li>"
        #Sets the last hits
        bodycontent += "<li class=\"list-group-item\"><b>Last Hits:</b> "
        bodycontent += unicode(player.get('last_hits'))
        bodycontent += "</li>"
        bodycontent += " </ul></div></div></div>"
        bodycontent += "</td>"
        bodycontent += "</tr>"
        # item_0_name
    bodycontent += "</tbody>"
    bodycontent += "</table>"
    bodycontent += "</div>"
    bodycontent += "<div id=\"stats\" class=\"tab-pane fade in \"><h4 style=\"color:#888888\">Results</h4>"
    bodycontent += "<div class=\"row\">"
    bodycontent += "<div class=\"col-sm-6\">"

    #Checks for the winning team, render the radiant col-sm-6
    if (data.get('radiant_win')):
        bodycontent += "<h2 style=\"color:#88968b\">Radiant (Winner)</h2>"
    else:
        bodycontent += "<h2 style=\"color:#88968b\">Radiant</h2>"

    bodycontent += "</div>"
    bodycontent += "<div class=\"col-sm-6\">"

    #Checks for the winning team, render the dire col-sm-6
    if (data.get('radiant_win')):
        bodycontent += "<h2 style=\"color:#a89c9c\">Dire</h2>"
    else:
        bodycontent += "<h2 style=\"color:#a89c9c\">Dire (Winner)</h2>"

    bodycontent += "</div>"
    bodycontent += "</div>"

    # If Pro Match finds the total score via parsing
    if mode == "Captains Draft":
        dire = ["dire"]
        radiant = ["radiant"]
        bans = ["bans"]
        #these lists are used to store the gpm per player_id based on side(radiant/dire)
        dire_gpm = []
        radiant_gpm = []
        #variables to store total team worth
        dire_gold = 0
        radiant_gold = 0
        # loop bellow checks is the hero was piccked and if so which team they are, then adds them to the
        # corresponding list
        for hero in data['picks_bans']:
            if (bool(hero.get('is_pick')) == True and bool(hero.get('team')) == 1):
                radiant.append(unicode(hero.get('hero_id')))
            elif (bool(hero.get('is_pick')) == True and bool(hero.get('team')) == 0):
                dire.append(unicode(hero.get('hero_id')))
            else:
                bans.append(unicode(hero.get('hero_id')))
        # loop below gets each players gpm in the dire and radiant list and stores them in dire_gpm and
        # radiant gpm
        for money in data['players']:
            if ((unicode(money.get('hero_id'))) in dire):
                dire_gpm.append(money.get('gold_per_min'))

            elif ((unicode(money.get('hero_id'))) in radiant):
                radiant_gpm.append(money.get('gold_per_min'))

        # loop below goes through each gpm, multiplies it by the duration of the match and adds it to the
        # variable for dire team gold or radiant team gold
        #dire team gold
        for player_gpm_dire in dire_gpm:
            dire_gold += player_gpm_dire * (float(data['duration']) / 60)
        #radiant team gold
        for player_gpm_rad in radiant_gpm:
            radiant_gold += player_gpm_rad * (float(data['duration']) / 60)

        bodycontent += "<h4 style=\"color:#888888\">Dire Gold: "
        bodycontent += '{0:.5g}'.format(dire_gold)
        bodycontent += "</h4>"
        bodycontent += "<h4 style=\"color:#888888\">Radiant Gold: "
        bodycontent += '{0:.5g}'.format(radiant_gold)
        bodycontent += "</h4>"

    else:
        dire = ["dire"]
        radiant = ["radiant"]
        bans = ["bans"]
        #these lists are used to store the gpm per player_id based on side(radiant/dire)
        dire_gpm = []
        radiant_gpm = []
        #variables to store total team worth
        dire_gold = 0
        radiant_gold = 0
        #list of values for dire and radiant player slots
        dire_slots  = [128,129,130,131,132,133,134,135]
        radiant_slots = [0,1,2,3,4,5,6,7]

        for toon in data['players']:
            if ((int(toon.get('player_slot'))) in dire_slots):
                dire.append(unicode(toon.get('hero_id')))
            elif ((int(toon.get('player_slot'))) in radiant_slots):
                radiant.append(unicode(toon.get('hero_id')))
            else:
                bans.append(unicode(toon.get('hero_id')))

        for cash in data['players']:
            if ((unicode(cash.get('hero_id'))) in dire):
                dire_gpm.append(cash.get('gold_per_min'))

            elif ((unicode(cash.get('hero_id'))) in radiant):
                radiant_gpm.append(cash.get('gold_per_min'))
        for player_gpm_dire in dire_gpm:
            dire_gold += player_gpm_dire * (float(data['duration']) / 60)
        #radiant team gold
        for player_gpm_rad in radiant_gpm:
            radiant_gold += player_gpm_rad * (float(data['duration']) / 60)

        bodycontent += "<h4 style=\"color:#888888\">Dire Gold: "
        bodycontent += '{0:.5g}'.format(dire_gold)
        bodycontent += "</h4>"
        bodycontent += "<h4 style=\"color:#888888\">Radiant Gold: "
        bodycontent += '{0:.5g}'.format(radiant_gold)
        bodycontent += "</h4>"


    bodycontent += "</div>"
    bodycontent += "</div>"
    return bodycontent

def buildBotton():
    botton = ""
    return botton

def htmlFull(mdata):
    html = ""
    html += "<!DOCTYPE html><html>"
    # Adding links and configuring header
    html += "<head>"
    html += "<style>.graph{width:100%;height:100%;border:1pxsolid#aeaeae;background-color:#eaeaea;}.bar{width:8px;margin:1px;display:inline-block;position:relative;background-color:#121212;vertical-align:baseline;}</style>"
    html += "<title>DOTA Match Stats</title>"
    html += "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\">"
    html += "<style>"
    html += ".nav-tabs>li>a { background-color: #333333; border-color: #3e3f40; color:#fff;}/* active tab color */.nav-tabs>li.active>a, .nav-tabs>li.active>a:hover, .nav-tabs>li.active>a:focus { color: #fff; background-color: #666; border: 1px solid #888888;}/* hover tab color */.nav-tabs>li>a:hover { border-color: #FFFFFF; background-color: #111111;}"
    html += "</style>"
    html += "</head>"
    html += "<body style=\" width: 100%; height: 100%;  -webkit-background-size: cover; -moz-background-size: cover;  -o-background-size: cover; background-size: cover; background-image:url('https://hydra-media.cursecdn.com/dota2.gamepedia.com/3/30/Fall_2016_Battle_Pass_Loading_Screen_III_16x9.png');\">"
    html += "<section>"
    html += "<div class=\"container\">"
    # Buildings Markup from Match Data.
    # Build the bootstrap model
    html += "<div id=\"modal\" class=\"modal show\" style=\"position: absolute;\" tabindex=\"-1\" role=\"dialog\" aria-hidden=\"true\"><div class=\"modal-dialog\"><div style=\"background-color: #3e3f40;\" class=\"modal-content\"><div class=\"modal-body\">"
    html += "<br>"
    html += "<div class=\"row\">"
    html += "<div class=\"col-sm-12\" style=\"background-color: #3e3f40;\">"
    html += "<br><form method=\"post\"><div class=\"form-group\"><input type=\"text\" placeholder=\"Match ID\" class=\"form-control\" name=\"match\"></div><div class=\"form-group\"><button type=\"submit\" class=\"btn btn-danger\">Load</button></div></form>"
    html += "</div>"
    html += "</div>"
    # Closing the webpageno-repeat center center fixed;
    if mdata != "":
        html += "<div class=\"row\">"
        html += "<div class=\"col-sm-12\" style=\"background-color: #574f48;\">"
        #html += "<div class=\"container\"><h2>Dynamic Tabs</h2><ul class=\"nav nav-tabs\"><li class=\"active\"><a data-toggle=\"tab\" href=\"#home\">Home</a></li><li><a data-toggle=\"tab\" href=\"#menu1\">Menu 1</a></li><li><a data-toggle=\"tab\" href=\"#menu2\">Menu 2</a></li></ul><div class=\"tab-content\"><div id=\"home\" class=\"tab-pane fade in active\"><h3>HOME</h3><p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p></div><div id=\"menu1\" class=\"tab-pane fade\"><h3>Menu 1</h3><p>Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p></div><div id=\"menu2\" class=\"tab-pane fade\"><h3>Menu 2</h3><p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam.</p></div></div></div>"
        html += buildTop(mdata)
        html += buildBody(mdata)
        #html += str(mdata['players'])
        html += "</div>"
        html += "</div>"

    html += "</div>"
    html += "</div><div class=\"modal-footer\"></div></div></div></div>"
    html += "</section>"
    # Adding scripts
    html += "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js\"></script>"
    html += "<script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js\"></script>"
    html += "</body>"
    # Ends the webpage
    html += "</html>"
    return html

class HTTPHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # Gets the content type
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            # Builds the dictionary for the parameters
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        # Checks if the match parameter is even there or it is a 400 error.
        if 'match' in postvars:
             # Gets the new match id from the form-urlencoded
            new_match = postvars.get('match')[0]
            matchnum = new_match
            # print('POST: ' + new_match)
            newmatch = api.get_match_details(match_id=new_match)
            #print(newmatch)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(htmlFull(newmatch))
        else:
            self.send_response(400)


        return

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(htmlFull(match))
        return

try:
    server = HTTPServer(('', PORT_NUMBER), HTTPHandler)
    print 'Webpage is located at localhost and port:',PORT_NUMBER
    server.serve_forever()

except KeyboardInterrupt:
    print ' Server Closed'
    server.socket.close()
