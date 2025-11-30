import os
from flask import Flask
from config import Config
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

# Cria as pastas necessárias na inicialização
for folder in [Config.UPLOAD_FOLDER, Config.UPLOAD_FOLDER_R1, Config.UPLOAD_FOLDER_R2]:
    os.makedirs(folder, exist_ok=True)

# Registra as rotas da aplicação
register_routes(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
