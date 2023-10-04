from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__, 
        static_url_path='',
        static_folder='static',
        template_folder='templates')

@app.route('/')
def test_func():
    return app.send_static_file('NovoVoom.html')

@app.route('/internal')
def internal():
    return render_template('pages.html')

@app.route('/internal/it')
def info_tech():
    return render_template('info_tech.html')

@app.route('/internal/directory')
def direct_form():
    return render_template('direct_form.html')

@app.route('/internal/submit', methods = ['POST'])
def direct_submit():
    form_data = request.form
    return "Search For: " + form_data['last']

app.run(host='0.0.0.0', port=5000)
