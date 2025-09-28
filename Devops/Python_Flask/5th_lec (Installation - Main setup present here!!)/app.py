from flask import Flask
app = Flask(__name__)
myhome="HOME PAGE"
mycontact= "CONTACT US PAGE"
@app.get("/")
def get_home():
	return myhome

@app.get("/contact")
def get_data():
	return mycontact

