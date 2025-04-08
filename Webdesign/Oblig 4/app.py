from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page='index')

@app.route('/aboutflask')
def aboutflask():
    return render_template('aboutflask.html', active_page='aboutflask')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', active_page='aboutme')

if __name__ == '__main__':
    app.run(debug=True)