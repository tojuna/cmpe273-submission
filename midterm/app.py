from flask import Flask, request, redirect, Response, json
from flask.helpers import url_for
import random
import string

app = Flask(__name__)

m = {}
total_users = 0; 

@app.route('/users', methods = ['POST'])
def create_user():
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        m[total_users + 100] =  (
            {
                "id" : total_users + 100,
                "name" : data["name"],
                "email" : data["email"],
                "tweets" : [],
                "followers" : []
            }
        )
        js = json.dumps(m[total_users + 100])
        total_users += 1

        resp = Response(js, status=200, mimetype='application/json')
        return resp

@app.route('/users/{user_id}/followers/{follower_id}', methods = ['PATCH'])
def folower(user_id, follower_id):
    m[user_id]["followers"].append(follower_id)
    js = json.dumps(m[user_id])
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/users/{user_id}/tweets', methods = ['POST'])
def tweet(user_id):
    if request.headers['Content-Type'] == 'application/json':
        data = request.json
        m[user_id]["tweets"].append({ "tweet_id" : len(m[user_id]["tweets"]) + 1, "tweet": data["tweet"]})
        js = json.dumps(m[user_id]["tweets"][-1])
        resp = Response(js, status=200, mimetype='application/json')
        return resp

@app.route('/users/{user_id}', methods = ['GET'])
def us(user_id):
    js = json.dumps(m[user_id])
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route('/users/{user_id}/timeline', methods = ['GET'])
def timeline(user_id):
    templ = [user_id]
    for num in m[user_id]["followers"]:
        templ.append(num)
    data = {"timeline": []}
    for id in templ:
        for dict in m[id]["tweets"]:
            data["timeline"].append(
                { "user_id": id, "tweet_id" : dict["tweet_id"], "tweet": dict["tweet"] }
            )
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp
        

if __name__ == '__main__':
    app.run(port=5000, debug=True)