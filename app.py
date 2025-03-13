from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
    return f"""
        <form method="post">
            Enter something: <input type="text" name="user_input">
            <input type="submit">
        </form>
        <p>You entered: {user_input}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
