from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from metadata_scrapper import get_metadata

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metadata', methods=['POST'])
def data():
    ins_id = request.form.get('ins-id')
    response = []
    response = get_metadata(ins_id)
    print(response)
    if type(response) != list:
        return render_template('error.html', data=response) 
    else:
        return render_template('metadata.html', data=response)

if __name__ == '__main__':
    app.run()
