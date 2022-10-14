from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return 'Hello flask'

#############################################################
###############                    ##########################
############################################################

@app.route('/test')
def test():
    print('test api')
    return jsonify({'message':'Test Successfully'})


@app.route('/name/<name>')
def Name(name):
    print('name is :',name)
    return jsonify({'message':'Test Successfully'})




@app.route('/marks/<int:marks>')
def Marks(marks):
    print('Marks is :',marks)
    return jsonify({'message':f'students marks are :{marks}'})



if __name__ == '__main__':
    app.run(debug=True)