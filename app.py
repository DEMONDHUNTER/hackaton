from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

app.route('/prueba2')
def index2():
    return render_template('index.html')

#Hola



if __name__ == '__main__':
    app.run(debug=True)