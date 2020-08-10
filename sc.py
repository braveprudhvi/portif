from flask import Flask, render_template, request
import csv
app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    return render_template(name)


def writer(data):
    with open('database.csv', 'a', newline='') as wr:
        li = list(data)
        csvw = csv.DictWriter(wr, fieldnames=li)
        csvw.writerow(data)


@app.route('/submit', methods=['POST', 'GET'])
def hello1():
    if request.method == 'POST':
        data = dict(request.form)
        writer(data)
        return 'form submitted'
    else:
        return 'something wrng'


app.run(debug=True)
