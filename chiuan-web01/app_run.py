from flask import *
from datetime import datetime
from dbModel import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html', **locals())
    
@app.route('/test.html')
def test():

    return render_template('test.html', **locals())





if __name__ == '__main__':
    app.run(debug=True)
