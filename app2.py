from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        
        return f"こんにちは、{name}さん"
    return """
        <form method="POST">
            <input name="name">
            <button>送信</button>
        </form>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5001)