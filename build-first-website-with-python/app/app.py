from flask import Flask, render_template
app = Flask(__name__)

# We will add our custom app functions here to support our website

# This starts our Python app
if __name__ == "__main__":
    app.run(debug=True)