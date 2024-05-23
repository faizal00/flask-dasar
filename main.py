from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-data', methods=['POST'])
def inputData():
    nama = request.form.get('nama')
    nim = request.form.get('nim')
    alamat = request.form.get('alamat')
    
    response = requests.post(
        'http://localhost:8081/send-data',
        json={"nama": nama, "nim": nim, "alamat": alamat}
    )
    return jsonify(response.json())

@app.route('/show-data')
def getData():
    response = requests.get('http://localhost:8081/show-data')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True, port=8080)
