from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# 假设的城市列表
cities = ["北京", "上海", "广州", "深圳", "成都", "杭州"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_city', methods=['POST'])
def get_random_city():
    selected_city = random.choice(cities)
    return jsonify({'city': selected_city})

if __name__ == '__main__':
    app.run(debug=True)
