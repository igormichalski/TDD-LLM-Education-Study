# Configuração do Gunicorn
# Use: gunicorn -c gunicorn_config.py server:app

import multiprocessing

# Endereço e porta
bind = "0.0.0.0:5000"

# Número de workers - IMPORTANTE: Use apenas 1 worker para evitar problemas de sincronização
# Com múltiplos workers, cada um tem sua própria instância do UserManager
workers = 1

# Tipo de worker - gevent é melhor para I/O bound
worker_class = "gevent"

# Número de conexões simultâneas por worker
worker_connections = 1000

# Timeout
timeout = 120
keepalive = 5

# Logs
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Preload app para economizar memória
preload_app = True

# Restart workers após N requisições (previne memory leaks)
max_requests = 1000
max_requests_jitter = 50