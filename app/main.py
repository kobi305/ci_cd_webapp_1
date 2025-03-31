from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", title="Deployed via CI/CD!")


@app.route("/api/status")
def status():
    return jsonify({"status": "OK", "version": "1.0.3"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
