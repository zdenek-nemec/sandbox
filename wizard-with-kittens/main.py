from flask import Flask, render_template, send_file
import io
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/install_app')
def install_app():
    return render_template('install_app.html')

@app.route('/download')
def download():
    random_text = f"Hello, this is your random number: {random.randint(1000, 9999)}"
    file_stream = io.BytesIO(random_text.encode('utf-8'))
    return send_file(
        file_stream,
        as_attachment=True,
        download_name='hello.txt',
        mimetype='text/plain'
    )

if __name__ == '__main__':
    app.run(debug=True)
