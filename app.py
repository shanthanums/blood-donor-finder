from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/search")
def search_donors():
    blood_group = request.args.get("blood_group", "")
    return render_template("index.html", blood_group=blood_group)

if __name__ == "__main__":
    app.run(debug=True)