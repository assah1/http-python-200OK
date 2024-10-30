from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/healthz', methods=['GET', 'POST'])
def healthz():
    if request.method == "POST":
        data = request.get_json(silent=True)
        if data is not None:
            print("Received JSON data:", data)
        else:
            print("No JSON data received")
        return "200 OK", 200

    return jsonify({'message': 'Success'}), 200

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
