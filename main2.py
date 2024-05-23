from flask import Flask, request, jsonify

app = Flask(__name__)

data_mahasiswa = []

@app.route('/send-data', methods=['POST'])
def inputData():
    data = request.json
    data_mahasiswa.append(data)
    return jsonify({"status": True, "message": "Data berhasil ditambahkan"})

@app.route('/show-data')
def getData():
    return jsonify(data_mahasiswa)

if __name__ == '__main__':
    app.run(debug=True, port=8081)
