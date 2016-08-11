import os
import glob
import re
from flask import Flask,jsonify, json, render_template, send_file

# app = Flask(__name__)
#
app = Flask(__name__, static_url_path='', static_folder='web')


@app.route("/config/userdata.js")
def userdata():
    gmap_api_key = os.getenv('GMAP_API', '')
    users = []
    for file in glob.glob('web_data/location-*.json'):
        
        m = re.search('location-(.*)\.json', file)
        if m:
            users.append(m.group(1))
    return render_template('userdata.js', 
        gmap_api_key=gmap_api_key, 
        users=users)

@app.route("/location-<username>.json")
def location_user(username):
    filename = 'location-' + username + '.json'
    if (os.path.exists('web_data/' + filename)):
        return send_file('web_data/' + filename)
    return "", 404

@app.route("/catchable-<username>.json")
def catchable_user(username):
    filename = 'catchable-' + username + '.json'
    if (os.path.exists('web_data/' + filename)):
        return send_file('web_data/' + filename)
    return "", 404

@app.route("/inventory-<username>.json")
def inventory_user(username):
    filename = 'inventory-' + username + '.json'
    if (os.path.exists('web_data/' + filename)):
        return send_file('web_data/' + filename)
    return "", 404

@app.route("/")
def index():
    filename = 'index.html'
    if (os.path.exists('web/' + filename)):
        return send_file('web/' + filename)
    return "", 404

@app.route("/socket.io/", methods=["GET", "POST"])
def socket_io():
    return "" 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)