from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/api/posts")
def get_posts():
    # create array of object posts id, title, content
    posts = [
        {"id": 1, "title": "Post 1", "content": "This is post 1"},
        {"id": 2, "title": "Post 2", "content": "This is post 2"},
        {"id": 3, "title": "Post 3", "content": "This is post 3"}
    ]
    return jsonify({"posts":posts})