from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal FLASK (diferente a GitHub Pages)
@app.route('/app')
def home():
    return render_template('index.html')  # Carga el index.html completo desde templates/

# Rutas secundarias (ajustadas para coexistir con GitHub Pages)
@app.route('/app/estudiantes')
def estudiantes():
    return render_template('estudiantes.html')

@app.route('/app/catedraticos')  # Corregido para coincidir con tu HTML
def catedraticos():
    return render_template('catedraticos.html')  # Asegúrate de renombrar docentes.html -> catedraticos.html

@app.route('/app/planes')
def planes():
    return render_template('planes.html')

if __name__ == '__main__':
    app.run(debug=True)