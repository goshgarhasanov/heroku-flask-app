from flask import Flask,jsonify
import requests
app=Flask(__name__)
posts=requests.get("https://jsonplaceholder.typicode.com/posts").json()
@app.get("/posts")
def getUsers():
    return jsonify(posts)

if __name__=="__main__":
    app.run(debug=0)

    