from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/greeting')
def greeting():
        return jsonify({"message": "Welcome to my portfolio",
                        "name": "swetha",
                        "role": "webdeveloper"})
if __name__ == '__main__':
    app.run(debug=True)