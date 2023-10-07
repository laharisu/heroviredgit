from flask import Flask,request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT'])
def palin():
    n=int(request.args.get("num1"))
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev= (rev*10)+dig
        n=n//10
        if(temp==rev):
            return ("the number is palindrome")
        else:
            return ("the number is not  palindrome")

if __name__ =="__main__":
    app.run(debug=True)