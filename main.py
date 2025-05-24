from flask import Flask
from src.urls import configure_routes

app = Flask(__name__)

# Configurar todas las rutas
configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)