from flask import Flask,render_template
from flask import request,jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")
mydb = client["personsDatabase"]
mycol = mydb["personsData"]
app = Flask("InfoHub")


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods = ["GET"])
def upload():
    name = request.args.get('Name')
    email = request.args.get('Email')
    dob = request.args.get('date')
    insertDict = {
        "Name": name, "Email": email , "Date of birth" : dob
    }
    try:
        insertOp = mycol.insert_one(insertDict)
        return "Your id is " + str(insertOp.inserted_id)
    except:
        return "Insertion failed"

@app.route('/showData')
def showData():
    showDataList = []
    for i in mycol.find({},{"_id":0}):
        showDataList.append(i)
    return jsonify(showDataList)
    
app.run(debug=True,host="0.0.0.0",port=8080)