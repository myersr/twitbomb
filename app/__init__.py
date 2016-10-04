from flask import Flask, render_template
app = Flask(__name__)

@app.route("/twitbomb")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=546)
