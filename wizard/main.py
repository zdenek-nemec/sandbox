from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/install')
def install():
    return render_template('install.html')

@app.route('/finish')
def finish():
    return render_template('finish.html')

if __name__ == '__main__':
    app.run(debug=True)
