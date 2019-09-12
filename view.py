from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def lenging():
    return render_template('lab_1.html')

@app.route('/1', methods=['GET'])
def example1():
    return render_template('lab_11.html')

@app.route('/2', methods=['GET'])
def example2():
    return render_template('lab_12.html')

@app.route('/3', methods=['GET'])
def example3():
    return render_template('lab_13.html')

@app.route('/4', methods=['GET'])
def example4():
    return render_template('lab_14.html')

