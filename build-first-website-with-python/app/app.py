import random
from flask import Flask, render_template
app = Flask(__name__)

# This function will be run whenever requests to "/" are made by the browser.
# The HTML returned from here will be sent to the browser making the request.
@app.route("/")
def index():
    message = "Hello world!"
    return render_template("index.html", message=message)

# This starts our Python app
if __name__ == "__main__":
    app.run(debug=True)