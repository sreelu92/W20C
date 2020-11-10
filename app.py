from flask import Flask,request,Response
import mariadb
import json
import random

animals=["monkey","lion","tiger","bear","rabbit"]

app= Flask(__name__)

@app.route('/animals', methods=['GET','POST','DELETE','PATCH'])
def animalspage():
    if request.method=="GET":
        random_number=random.randrange(len(animals))
        choice=animals[random_number]
        animal={"animal":choice}
        return Response(json.dumps(animal,default=str),mimetype="application/json",status=200)
    if request.method=="POST":
        return Response("giraffe added successfully to the list",mimetype="text/html",status=200)
    if request.method=="PATCH":
        return Response("rabbit turning into a snowy rabbit",mimetype="text/html",status=200)
    if request.method=="DELETE":
        return Response("tiger successfully removed from the list",mimetype="text/html",status=200)
    



