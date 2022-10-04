from flask import Flask

app = Flask(__name__)
@app.route('/')
def principal():
    return "Hola mundo! :D"

@app.route('/despedida')
def despedida():
    return"Adios mundo"
if __name__ == '__main__':
    app.run(debug=True)