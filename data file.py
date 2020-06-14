app = Flask(__name__)

@app.route('/name')
def name():
    return 'neetu'

@app.route('/age')
def age():
    return 'age'

@app.route('/Gender')
def gender():
    return 'gender'

@app.route('/address')
def address():
    return 'gender'


if __name__ == '__main__':
    app.run()
