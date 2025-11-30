class Config:
    """Configurações da aplicação"""
    UPLOAD_FOLDER = 'uploads'
    UPLOAD_FOLDER_R1 = 'uploads/rodada1'
    UPLOAD_FOLDER_R2 = 'uploads/rodada2'
    ALLOWED_EXTENSIONS = set()
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB
    SECRET_KEY = 'supersecretkey1234'
    
    # Configurações de controle de rodadas
    RODADA1_LIBERADA = True
    RODADA2_LIBERADA = False
    
    # Configurações de timeout
    TIMEOUT_SECONDS = 15
    CLEANUP_INTERVAL = 5
    HEARTBEAT_INTERVAL = 10000  # em milissegundos (JavaScript)
    DASHBOARD_UPDATE_INTERVAL = 3000  # em milissegundos (JavaScript)