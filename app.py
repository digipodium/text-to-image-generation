from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename  
from flask import send_from_directory
import os
from generator import generate

app = Flask(__name__)
# upload folder
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# allowed extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# secret key
app.secret_key = "secret key"

# create upload folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# check if the file is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# text input function
@app.route('/text', methods=['POST','GET'])
def text():
    if request.method == 'POST':
        text = request.form['text']
        if len(text) > 0 and len(text.split()) > 3:
            text = text.strip()
            path = generate(text)
            return render_template('output.html', text=text, path=path)
        else:
            flash('Please enter a sentence.')
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))
@app.route('/')
def index():
    path = 'static/generated'
    files = os.listdir(path)
    files = [f for f in files if f.endswith('.jpg')]
    return render_template('index.html', files=files)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
 
