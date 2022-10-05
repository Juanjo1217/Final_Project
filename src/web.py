from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def principal():
    return render_template('inicio.html')

@app.route('/Login')
def Login():
    return render_template('login.html')
if __name__ == '__main__':
    app.run(debug=True)