from flask import render_template

def configure_routes(app):
    """Configura todas las rutas de la aplicación"""
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/estudiantes')
    def estudiantes():
        return render_template('estudiantes.html')
    
    @app.route('/docentes')
    def docentes():
        return render_template('docentes.html')
    
    @app.route('/administracion')
    def administracion():
        return render_template('administracion.html')