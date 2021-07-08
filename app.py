from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/grade')
def grade():
    return render_template('grade.html')


@app.route('/minha_grade')
def minha_grade():
    return render_template('minha_grade.html')


if __name__ == '__main__':
    app.run(debug=True)
