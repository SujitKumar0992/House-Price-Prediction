from flask import Flask,jsonify,request,render_template,redirect
import numpy as np

import project_db

import houseprediction

import config

app = Flask(__name__)


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():

    return render_template('home.html')





@app.route('/register_validation',methods=['GET','POST'])
def register_validation():
    if request.method=="POST":
        data=request.form
        print(data)

        response=project_db.register_user(data)
        if not response:
            return redirect("/register")
        else:
            return redirect("/")




#############################################################################################
########################## Login Api #####################################################
#############################################################################################


@app.route('/login_validation',methods=['GET','POST'])
def login_validation():
    data=request.form
    print(data)

    response=project_db.login_user(data)

    if response:
        return redirect("/home")
    else:
        return redirect("/")



#############################################################################################
########################## Prediction Api #####################################################
#############################################################################################


@app.route('/prediction' ,methods=['POST'])
def prediction():
    data=request.form
    print(data)

    prediction_text=houseprediction.prediction_price(data)

    prediction_text=np.round(prediction_text)

    return render_template('home.html',prediction_text="Predicted Price is Rs : [{}]".format(prediction_text))



@app.route('/logout')
def logout():
    return redirect("/")





if __name__ == '__main__':
    app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=True)
