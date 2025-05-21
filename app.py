from flask import Flask, render_template

app = Flask(__name__)  # ¡No necesita template_folder si usas la estructura estándar!

@app.route('/')
def index():
    return render_template('index.html')  # Flask automáticamente buscará en templates/

# Rutas para los otros templates
@app.route('/estudiantes')
def estudiantes():
    return render_template('estudiantes.html')

@app.route('/docentes')
def docentes():
    return render_template('docentes.html')

@app.route('/administracion')
def administracion():
    return render_template('administracion.html')

if __name__ == '__main__':
    app.run(debug=True)