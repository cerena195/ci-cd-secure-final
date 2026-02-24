from flask import Flask, jsonify # <-- import flask and jsonify maintenant 
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "DevSecure API running 🚀"})

@app.route('/health')
def health():
    return jsonify({"status": "OK"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)


 
