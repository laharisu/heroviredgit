from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT'])
def hello_world():
    return "Hello World"

@app.route("/Contactus", methods=['GET', 'POST', 'PUT'])
def Contactus():
    return "Hello World contact us on insta"


if __name__ =="__main__":

    app.run(debug=True)