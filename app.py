from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This app was built using S2I (Source-to-Image). Build stream!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
