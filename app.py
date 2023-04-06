from flask import Flask,render_template,request

import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url_api = "https://api.codetabs.com/v1/alexa?web="+request.form["url"]

        response = requests.request("GET", url_api,)
        result = json.loads(response.text)
        if len(result)==2:
            data=0
        else:
            data=1
        if data == 0:    
            value = "Legitimate"
            return render_template("home.html",error=value)
        else:
            value = "Phishing"
            return render_template("home.html",error=value)
if __name__ == "__main__":
    app.run(debug=True)