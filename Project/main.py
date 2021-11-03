import flask
from flask import Flask, render_template, Response,redirect,request, jsonify
from numpy import dtype
from camera import VideoCamera
from flask_pymongo import PyMongo
import os
from beautify.Moisturizer import *
from beautify.Facewash import *
from beautify.Sunscreen import *
import bson
from bson.objectid import ObjectId
app = Flask(__name__)

CART=[]
# 
app.config["MONGO_URI"] = "mongodb+srv://admindb:admindatabase@cluster0-vlwic.mongodb.net/myntra"
mongo = PyMongo(app)
db_operations = mongo.db.products

@app.route('/tryon/<file_path>',methods = ['POST', 'GET'])
def tryon(file_path):
	file_path = file_path.replace(',','/')
	os.system('python tryOn.py ' + file_path)
	return redirect('http://127.0.0.1:5000/',code=302, Response=None)

@app.route('/tryall',methods = ['POST', 'GET'])
def tryall():
        CART = request.form['mydata'].replace(',', '/')
        os.system('python test.py ' + CART)
        render_template('checkout.html', message='')


@app.route('/')
def indexx():
    return render_template('home.html')

@app.route('/read')
def read():
    users = db_operations.find()
    output = [{'Label' : user['Label'] } for user in users]
    return jsonify(output)

@app.route('/form', methods =["GET", "POST"])
def formData():
    if request.method == "POST":
        filter = {}
        filter['Label'] = request.form.get("label")
        skin = request.form.getlist("skin")
        for x in skin:
            if x == "Combination":
                filter['Combination'] = 1
            if x == "Dry":
                filter['Dry'] = 1
            if x == "Normal":
                filter['Normal'] = 1
            if x == "Oily":
                filter['Oily'] = 1
            if x == "Sensitive":
                filter['Sensitive'] = 1
        price_min = int(request.form['price-min'])
        price_max = int(request.form['price-max'])
        filter['price'] = { "$lte" : price_max, "$gte" : price_min}
        products = db_operations.find(filter)
        output = [
            {'Label' : product['Label'] ,
            'Img' : product['img'],
            'Brand' : product['brand'] ,
            'Name':product['name'],
            'Price':product['price'],
            'Rating':product['rating'],
            'Combination':product['Combination'],
            'Dry':product['Dry'],
            'Normal':product['Normal'],
            'Oily':product['Oily'],
            'Sensitive':product['Sensitive'],
            'Ingredients':product['ingredients'],
            '_id' : product['_id']
            }
            for product in products]
        return render_template("formoutput.html",output = output)
    return render_template('form.html')

@app.route("/details/<dbid>")
def insert_one(dbid):
    product=db_operations.find_one({'_id':bson.ObjectId(oid=str(dbid))})
    output = [
            {'Label' : product['Label'] ,
            'Img' : product['img'],
            'Brand' : product['brand'] ,
            'Name':product['name'],
            'Price':product['price'],
            'MRP':product['mrp'],
            'Rating':product['rating'],
            'Combination':product['Combination'],
            'Dry':product['Dry'],
            'Normal':product['Normal'],
            'Oily':product['Oily'],
            '_id':product['_id'],
            'Sensitive':product['Sensitive'],
            'Ingredients':product['ingredients']}]
    return render_template("details.html",output = output)

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/details/Face Moisturizer')
def applyMoisturizer_fun():
    applyMoisturizer()
    return redirect("http://127.0.0.1:5000/form")

@app.route('/details/Sunscreen')
def applySunscreen_fun():
    applySunscreen()
    return redirect("http://127.0.0.1:5000/form")

@app.route('/details/Face Wash And Cleanser')
def applyFacewash_fun():
    applyFacewash()
    return redirect("http://127.0.0.1:5000/form")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route("/cart/<file_path>",methods = ['POST', 'GET'])
def cart(file_path):
    global CART
    file_path = file_path.replace(',','/')
    print("ADDED", file_path)
    CART.append(file_path)
    return render_template("checkout.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run()