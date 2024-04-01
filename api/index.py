from flask import Flask, jsonify
import pickle

app = Flask(__name__)

# model = pickle.load(open('prophet_model.pkl', 'rb'))

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"

# @app.route('/predict')
# def predict():
#     test = model.make_future_dataframe(periods=12*4, freq='M')
#     forecast = model.predict(test)  
    
#     return jsonify(forecast.to_dict())  # Kembalikan hasil prediksi dalam format JSON


@app.route("/api/posts")
def get_posts():
    # create array of object posts id, title, content
    posts = [
        {"id": 1, "title": "Post 1", "content": "This is post 1"},
        {"id": 2, "title": "Post 2", "content": "This is post 2"},
        {"id": 3, "title": "Post 3", "content": "This is post 3"}
    ]
    return jsonify({"posts":posts})