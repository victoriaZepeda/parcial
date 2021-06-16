from flask import Flask, render_template
from requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("http://localhost:23512/store")
    print (response)
    results={}
    if response.status_code == 200:
        dataJson = response.json()
        results = dataJson
    return render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
