from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flask')
def flask():
    return render_template('flask.html')

@app.route('/me')
def me():
    return render_template('me.html')

if __name__ == '__main__':
    app.run(debug=True)