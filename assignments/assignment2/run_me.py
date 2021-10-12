from flask import Flask, request, redirect
from flask.helpers import url_for
import random
import string

app = Flask(__name__)

m1 = {}  # {long, short}
m2 = {}  # # {short, long}
count_map = {} # {short, count}

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choices(letters, k=5)
        rand_letters = "".join(rand_letters)
        if not rand_letters in m2:
            return rand_letters


@app.route('/')
def home():
    return str(m1) + '\n' + str(m2) + '\n' + str(count_map) + '\n'

@app.route('/shorten', methods = ['POST'])
def shorten():
    if request.headers['Content-Type'] == 'text/plain':
        temp = shorten_url()
        data = (request.data).decode('ascii')
        if data in m1: return "URL already present: 127.0.0.1:5000/" + str(m1[data])[2:-2] + '\n'
        m1[data] = [temp]
        m2[temp] = [data]
        count_map[temp] = 0
        return "New URL created: 127.0.0.1:5000/" + temp + '\n'

@app.route('/<short_url>')
def redirection(short_url):
    if short_url not in m2: return "URL does not exist" + '\n'
    long_url = m2[short_url]
    count_map[short_url] += 1
    return redirect("".join(long_url), code=302)


@app.route('/retrieve/<x>/<url>', methods = ['GET'])
def display_long(x, url):
    if url in m2: 
        return 'Long URL for given short url: ' + str(m2[url])[2:-2] + '\n'
    else: return "URL does not exist" + '\n'

@app.route('/clicks/<x>/<short>', methods = ['GET'])
def clicks(x, short):
    if short in count_map: 
        return 'Number of clicks on this shortened link: ' + str(count_map[short]) + '\n'   
    else: return "URL does not exist" + '\n'

@app.route('/update/<x>/<short>', methods = ['PATCH'])
def update(x, short):
    if short in count_map: 
        if request.headers['Content-Type'] == 'application/json':
            data = request.json
            count_map[short] = data['clicks']
            return "Updated count for given short link to: " + str(data['clicks']) + '\n'
    else: return "URL does not exist" + '\n'

    
if __name__ == '__main__':
    app.run(port=5000, debug=True)