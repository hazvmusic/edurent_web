from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def rentar():
    return render_template('rentar.html')

@app.route('/paquetes')
def paquetes():
    return render_template('paquetes.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)