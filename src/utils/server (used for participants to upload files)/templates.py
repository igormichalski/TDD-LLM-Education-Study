from flask import render_template_string, get_flashed_messages
from config import Config

def render_index():
    """Renderiza a página inicial"""
    return render_template_string('''
    <!doctype html>
    <html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Sistema de Upload</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 40px;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container { 
                max-width: 500px;
                background: #fff;
                padding: 40px;
                border-radius: 16px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            }
            h1 { 
                text-align: center;
                color: #333;
                margin-bottom: 30px;
            }
            .btn-container {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            .btn {
                display: block;
                padding: 15px 25px;
                text-align: center;
                text-decoration: none;
                background-color: #667eea;
                color: white;
                border-radius: 8px;
                font-size: 18px;
                transition: all 0.3s;
                border: none;
            }
            .btn:hover {
                background-color: #5568d3;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Sistema de Upload</h1>
            <div class="btn-container">
                <a href="/rodada1" class="btn">📤 Rodada 1</a>
                <a href="/rodada2" class="btn">📤 Rodada 2</a>
            </div>
        </div>
    </body>
    </html>
    ''')


def render_rodada1():
    """Renderiza a página de upload da rodada 1"""
    messages = get_flashed_messages()
    show_qr = any("enviado com sucesso" in m.lower() for m in messages)
    return render_template_string('''
    <!doctype html>
    <html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Rodada 1 - Upload</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 40px;
                min-height: 100vh;
                color: #333;
            }
            .container {
                max-width: 850px;
                margin: auto;
                background: #fff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: left;
            }
            h1, h2, h3 { color: #667eea; }
            ul { margin-left: 20px; }
            .image, .qr {
                display: flex;
                justify-content: center;
                margin: 20px 0;
            }
            img {
                max-width: 300px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            }
            .flash {
                background: #d4edda;
                color: #155724;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                border: 1px solid #c3e6cb;
                text-align: center;
                font-weight: bold;
            }
            input[type=file], input[type=submit] {
                display: block;
                margin-top: 20px;
                width: 100%;
                padding: 12px;
                border-radius: 8px;
                border: 2px dashed #667eea;
                font-size: 16px;
            }
            input[type=submit] {
                background: #667eea;
                color: white;
                font-weight: bold;
                cursor: pointer;
                border: none;
            }
            input[type=submit]:hover {
                background: #5568d3;
            }
            .back-btn {
                display: inline-block;
                margin-top: 20px;
                color: #667eea;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            {% if show_qr %}
                <h1>✅ Envio realizado com sucesso!</h1>
                <p>Agora, você deve obrigatoriamente responder à pesquisa acessando o QR Code abaixo:</p>
                <div class="qr">
                    <img src="/static/QRCodePosRodada.png" alt="QR Code da Pesquisa">
                </div>
                    <p style="text-align:center; font-weight:bold; color:#555;">
        Ou acesse diretamente pelo link: 
        <a href="https://forms.gle/jGEx3x5aX5grhYcM6" target="_blank">
            https://forms.gle/jGEx3x5aX5grhYcM6
        </a>
    </p>
                                                  <a href="/" class="back-btn">← Voltar ao Início</a>
            {% else %}
                <h1>📤 Rodada 1</h1>
                <p><strong>Prazo máximo:</strong> 60 minutos após o início da rodada.</p>

                <h2>🧩 Instruções Gerais</h2>
                <ul>
                    <li>Desenvolva os programas utilizando <strong>TDD (Test-Driven Development)</strong>.</li>
                    <li>Não utilize IA, a menos que autorizado.</li>
                    <li>Se autorizado, utilize apenas o <strong>ChatGPT deslogado</strong>.</li>
                    <li>Utilize o navegador <strong>Mozilla Firefox</strong> e instale a extensão ChatGPT Export antes de iniciar.</li>
                </ul>

                <h3>📥 Instalação da Extensão ChatGPT Export</h3>
                <ol>
                    <li>Acesse a loja de extensões do Firefox.</li>
                    <li>Pesquise por <strong>ChatGPT Export</strong>.</li>
                    <li>Confirme que o ícone é igual ao da imagem abaixo e clique em “Adicionar ao Firefox”.</li>
                </ol>
                <div class="image">
                    <img src="/static/3fcca08d-5da6-430d-b49d-386a402c2596.png" alt="Extensão ChatGPT Export">
                </div>

                <h2>🗂️ Envio do Arquivo</h2>
                <ul>
                    <li>Compacte todos os arquivos <code>.c</code> e logs da IA (se houver) em um arquivo <strong>.zip</strong>.</li>
                    <li>Envie o arquivo abaixo.</li>
                </ul>

                {% if messages %}
                    {% for message in messages %}
                      <div class="flash">{{ message }}</div>
                    {% endfor %}
                {% endif %}

                <form method=post enctype=multipart/form-data>
                  <input type=file name=file required>
                  <input type=submit value="Enviar Arquivo">
                </form>

                <a href="/" class="back-btn">← Voltar</a>
            {% endif %}
        </div>
    </body>
    </html>
    ''', messages=messages, show_qr=show_qr)


def render_rodada2():
    """Renderiza a página de upload da rodada 2 com QR code"""
    messages = get_flashed_messages()
    show_qr = any("enviado com sucesso" in m.lower() for m in messages)
    
    return render_template_string('''
    <!doctype html>
    <html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Rodada 2 - Upload</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                margin: 0;
                padding: 40px;
                min-height: 100vh;
                color: #333;
            }
            .container {
                max-width: 850px;
                margin: auto;
                background: #fff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: left;
            }
            h1, h2, h3 { color: #f5576c; }
            ul { margin-left: 20px; }
            .image, .qr {
                display: flex;
                justify-content: center;
                margin: 20px 0;
            }
            img {
                max-width: 300px;
                border-radius: 8px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            }
            .flash {
                background: #d4edda;
                color: #155724;
                padding: 15px;
                border-radius: 8px;
                margin-bottom: 20px;
                border: 1px solid #c3e6cb;
                text-align: center;
                font-weight: bold;
            }
            input[type=file], input[type=submit] {
                display: block;
                margin-top: 20px;
                width: 100%;
                padding: 12px;
                border-radius: 8px;
                border: 2px dashed #f5576c;
                font-size: 16px;
            }
            input[type=submit] {
                background: #f5576c;
                color: white;
                font-weight: bold;
                cursor: pointer;
                border: none;
            }
            input[type=submit]:hover {
                background: #e04455;
            }
            .back-btn {
                display: inline-block;
                margin-top: 20px;
                color: #f5576c;
                text-decoration: none;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            {% if show_qr %}
                <h1>✅ Envio realizado com sucesso!</h1>
                <p>Agora, você deve obrigatoriamente responder à pesquisa acessando o QR Code abaixo:</p>
                <div class="qr">
                    <img src="/static/QRCodePosRodada.png" alt="QR Code da Pesquisa">
                </div>
                    <p style="text-align:center; font-weight:bold; color:#555;">
        Ou acesse diretamente pelo link: 
        <a href="https://forms.gle/jGEx3x5aX5grhYcM6" target="_blank">
            https://forms.gle/jGEx3x5aX5grhYcM6
        </a>
    </p>
                <a href="/" class="back-btn">← Voltar ao Início</a>
            {% else %}
                <h1>📤 Rodada 2</h1>
                <p><strong>Prazo máximo:</strong> 60 minutos após o início da rodada.</p>

                <h2>🧩 Instruções Gerais</h2>
                <ul>
                    <li>Desenvolva os programas utilizando <strong>TDD (Test-Driven Development)</strong>, conforme aprendido na última aula.</li>
                    <li>Não utilize ferramentas de Inteligência Artificial, a menos que tenha sido autorizado.</li>
                    <li>Se autorizado, utilize apenas o <strong>ChatGPT deslogado</strong>.</li>
                    <li>Você <strong>pode usar a internet</strong> normalmente para pesquisas.</li>
                    <li>Use o navegador <strong>Mozilla Firefox</strong> e instale a extensão <strong>ChatGPT Export</strong> antes de começar.</li>
                </ul>

                <h3>📥 Instalação da Extensão ChatGPT Export</h3>
                <p>Antes de começar a rodada:</p>
                <ol>
                    <li>Abra o Mozilla Firefox.</li>
                    <li>Acesse a loja de extensões.</li>
                    <li>Procure por <strong>ChatGPT Export</strong> e instale a que possui o ícone abaixo:</li>
                </ol>
                <div class="image">
                    <img src="/static/3fcca08d-5da6-430d-b49d-386a402c2596.png" alt="Extensão ChatGPT Export">
                </div>

                <h2>🗂️ Envio do Arquivo</h2>
                <ul>
                    <li>Compacte todos os códigos <code>.c</code> e os logs da IA (caso tenha) em um único arquivo <strong>.zip</strong>.</li>
                    <li>Envie o arquivo no campo abaixo.</li>
                </ul>

                <h2>🧠 Problemas da Rodada 2</h2>
                <h3>P03 – Contador de Vogais</h3>
                <p>Escreva um programa que receba uma string e conte quantas vogais (a, e, i, o, u) existem nela, desconsiderando maiúsculas e minúsculas.</p>
                <h3>P04 – Conversor Celsius ↔ Fahrenheit</h3>
                <p>Crie um programa que receba um número e uma unidade de medida (C ou F) e converta o valor para a outra unidade.</p>

                {% if messages %}
                    {% for message in messages %}
                      <div class="flash">{{ message }}</div>
                    {% endfor %}
                {% endif %}

                <form method=post enctype=multipart/form-data>
                  <input type=file name=file required>
                  <input type=submit value="Enviar Arquivo">
                </form>
                <a href="/" class="back-btn">← Voltar</a>
            {% endif %}
        </div>
    </body>
    </html>
    ''', messages=messages, show_qr=show_qr)



def render_rodada_bloqueada(rodada, cor_principal, cor_hover):
    """Renderiza a página de rodada bloqueada"""
    return render_template_string('''
    <!doctype html>
    <html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Rodada {{ rodada }} - Bloqueada</title>
        <style>
            body { 
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, {{ cor_principal }} 0%, {{ cor_hover }} 100%);
                margin: 0;
                padding: 40px;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .container { 
                max-width: 500px;
                background: #fff;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
            }
            h1 { color: {{ cor_principal }}; margin-bottom: 20px; }
            p { color: #666; font-size: 18px; line-height: 1.6; }
            .lock-icon { font-size: 80px; margin-bottom: 20px; }
            .back-btn {
                display: inline-block;
                margin-top: 30px;
                padding: 12px 30px;
                background-color: {{ cor_principal }};
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-weight: bold;
                transition: all 0.3s;
            }
            .back-btn:hover {
                background-color: {{ cor_hover }};
                transform: translateY(-2px);
            }
        </style>
        <script>
            // Verifica se a rodada foi liberada
            setInterval(() => {
                fetch('/api/rodada{{ rodada }}/status')
                    .then(r => r.json())
                    .then(data => {
                        if (data.liberada) {
                            location.reload();
                        }
                    })
                    .catch(err => console.error('Erro ao verificar status:', err));
            }, 3000);
            
            // Heartbeat
            setInterval(() => {
                fetch('/heartbeat?page=rodada{{ rodada }}');
            }, {{ heartbeat_interval }});
        </script>
    </head>
    <body>
        <div class="container">
            <div class="lock-icon">🔒</div>
            <h1>Rodada {{ rodada }} Bloqueada</h1>
            <p>A Rodada {{ rodada }} ainda não foi liberada pelo administrador.</p>
            <p>Aguarde a liberação para fazer o upload.</p>
            <a href="/" class="back-btn">← Voltar ao Início</a>
        </div>
    </body>
    </html>
    ''', rodada=rodada, cor_principal=cor_principal, cor_hover=cor_hover, 
        heartbeat_interval=Config.HEARTBEAT_INTERVAL)


def render_dashboard(stats):
    """Renderiza o dashboard administrativo"""
    return render_template_string('''
    <!doctype html>
    <html lang="pt-br">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Dashboard - Admin</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                padding: 30px;
                min-height: 100vh;
            }
            .header {
                text-align: center;
                color: white;
                margin-bottom: 40px;
            }
            .header h1 {
                font-size: 36px;
                margin-bottom: 10px;
            }
            .header p {
                font-size: 18px;
                opacity: 0.9;
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 25px;
                max-width: 1200px;
                margin: 0 auto 40px;
            }
            .stat-card {
                background: white;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                text-align: center;
                transition: transform 0.3s;
            }
            .stat-card:hover {
                transform: translateY(-5px);
            }
            .stat-number {
                font-size: 48px;
                font-weight: bold;
                margin: 15px 0;
            }
            .stat-label {
                color: #666;
                font-size: 16px;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .stat-icon {
                font-size: 50px;
            }
            .charts-container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
                gap: 30px;
                max-width: 1200px;
                margin: 0 auto 40px;
            }
            .chart-card {
                background: white;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            .chart-title {
                text-align: center;
                font-size: 22px;
                color: #333;
                margin-bottom: 20px;
                font-weight: bold;
            }
            .chart-wrapper {
                position: relative;
                width: 250px;
                height: 250px;
                margin: 0 auto 20px;
            }
            .progress-ring {
                transform: rotate(-90deg);
            }
            .progress-ring-circle {
                transition: stroke-dashoffset 0.5s;
            }
            .percentage-text {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                font-size: 36px;
                font-weight: bold;
                color: #333;
            }
            .chart-info {
                text-align: center;
                color: #666;
                font-size: 16px;
            }
            .control-panel {
                max-width: 800px;
                margin: 0 auto;
                background: white;
                padding: 30px;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            }
            .control-title {
                font-size: 24px;
                color: #333;
                margin-bottom: 20px;
                text-align: center;
            }
            .rodada-control {
                margin-bottom: 30px;
                padding: 20px;
                border-radius: 8px;
                background: #f9fafb;
            }
            .rodada-control:last-child {
                margin-bottom: 0;
            }
            .rodada-header {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 15px;
                color: #333;
            }
            .control-buttons {
                display: flex;
                gap: 10px;
            }
            .control-btn {
                flex: 1;
                padding: 12px;
                font-size: 16px;
                font-weight: bold;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: all 0.3s;
            }
            .btn-liberar {
                background-color: #10b981;
                color: white;
            }
            .btn-liberar:hover:not(:disabled) {
                background-color: #059669;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(16, 185, 129, 0.4);
            }
            .btn-bloquear {
                background-color: #ef4444;
                color: white;
            }
            .btn-bloquear:hover:not(:disabled) {
                background-color: #dc2626;
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(239, 68, 68, 0.4);
            }
            .control-btn:disabled {
                opacity: 0.5;
                cursor: not-allowed;
            }
            .status-badge {
                display: inline-block;
                padding: 8px 20px;
                border-radius: 20px;
                font-size: 14px;
                font-weight: bold;
                margin: 10px 0;
            }
            .status-liberada {
                background-color: #d1fae5;
                color: #065f46;
            }
            .status-bloqueada {
                background-color: #fee2e2;
                color: #991b1b;
            }
            .back-link {
                display: block;
                text-align: center;
                margin-top: 30px;
                color: white;
                text-decoration: none;
                font-size: 16px;
            }
            .back-link:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>

        <div class="control-panel">
            <div class="control-title">Controle das Rodadas</div>
            
            <div class="rodada-control">
                <div class="rodada-header">🔵 Rodada 1</div>
                <div style="text-align: center; margin-bottom: 15px;">
                    <span class="status-badge" id="status-badge-r1">
                        Status: <span id="status-text-r1">Carregando...</span>
                    </span>
                </div>
                <div class="control-buttons">
                    <button class="control-btn btn-liberar" id="btn-liberar-r1" onclick="toggleRodada(1, true)">
                        🔓 Liberar
                    </button>
                    <button class="control-btn btn-bloquear" id="btn-bloquear-r1" onclick="toggleRodada(1, false)">
                        🔒 Bloquear
                    </button>
                </div>
            </div>

            <div class="rodada-control">
                <div class="rodada-header">🔴 Rodada 2</div>
                <div style="text-align: center; margin-bottom: 15px;">
                    <span class="status-badge" id="status-badge-r2">
                        Status: <span id="status-text-r2">Carregando...</span>
                    </span>
                </div>
                <div class="control-buttons">
                    <button class="control-btn btn-liberar" id="btn-liberar-r2" onclick="toggleRodada(2, true)">
                        🔓 Liberar
                    </button>
                    <button class="control-btn btn-bloquear" id="btn-bloquear-r2" onclick="toggleRodada(2, false)">
                        🔒 Bloquear
                    </button>
                </div>
            </div>
        </div>

        <a href="/" class="back-link">← Voltar ao Início</a>

        <script>
            const circumference = 2 * Math.PI * 100;
            
            function updateChart(circleId, percentId, countId, totalId, count, total) {
                const percentage = total > 0 ? Math.round((count / total) * 100) : 0;
                const offset = circumference - (percentage / 100) * circumference;
                
                const circle = document.getElementById(circleId);
                const percentEl = document.getElementById(percentId);
                const countEl = document.getElementById(countId);
                const totalEl = document.getElementById(totalId);
                
                if (circle) circle.style.strokeDashoffset = offset;
                if (percentEl) percentEl.textContent = percentage + '%';
                if (countEl) countEl.textContent = count;
                if (totalEl) totalEl.textContent = total;
            }
            
            function updateStats() {
                fetch('/api/stats')
                    .then(response => response.json())
                    .then(data => {
                        const totalEl = document.getElementById('total-users');
                        const r1El = document.getElementById('rodada1-users');
                        const r2El = document.getElementById('rodada2-users');
                        
                        if (totalEl) totalEl.textContent = data.total;
                        if (r1El) r1El.textContent = data.rodada1;
                        if (r2El) r2El.textContent = data.rodada2;
                        
                        updateChart('circle-r1', 'percent-r1', 'count-r1', 'total-r1', data.rodada1, data.total);
                        updateChart('circle-r2', 'percent-r2', 'count-r2', 'total-r2', data.rodada2, data.total);
                    })
                    .catch(err => console.error('Erro ao buscar stats:', err));
            }
            
            function updateRodadaStatus(rodada) {
                fetch(`/api/rodada${rodada}/status`)
                    .then(response => response.json())
                    .then(data => {
                        const badge = document.getElementById(`status-badge-r${rodada}`);
                        const statusText = document.getElementById(`status-text-r${rodada}`);
                        const btnLiberar = document.getElementById(`btn-liberar-r${rodada}`);
                        const btnBloquear = document.getElementById(`btn-bloquear-r${rodada}`);
                        
                        if (!badge || !statusText || !btnLiberar || !btnBloquear) return;
                        
                        if (data.liberada) {
                            badge.className = 'status-badge status-liberada';
                            statusText.textContent = 'Liberada';
                            btnLiberar.disabled = true;
                            btnBloquear.disabled = false;
                        } else {
                            badge.className = 'status-badge status-bloqueada';
                            statusText.textContent = 'Bloqueada';
                            btnLiberar.disabled = false;
                            btnBloquear.disabled = true;
                        }
                    })
                    .catch(err => console.error(`Erro ao buscar status rodada ${rodada}:`, err));
            }
            
            function toggleRodada(rodada, liberar) {
                const btnLiberar = document.getElementById(`btn-liberar-r${rodada}`);
                const btnBloquear = document.getElementById(`btn-bloquear-r${rodada}`);
                
                // Desabilita ambos os botões temporariamente
                if (btnLiberar) btnLiberar.disabled = true;
                if (btnBloquear) btnBloquear.disabled = true;
                
                fetch(`/api/rodada${rodada}/toggle`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ liberar: liberar })
                })
                .then(response => response.json())
                .then(data => {
                    // Aguarda 500ms antes de atualizar o status
                    setTimeout(() => {
                        updateRodadaStatus(rodada);
                    }, 500);
                })
                .catch(err => {
                    console.error(`Erro ao alterar rodada ${rodada}:`, err);
                    // Re-habilita os botões em caso de erro
                    updateRodadaStatus(rodada);
                });
            }
            
            // Atualiza stats a cada 3 segundos
            setInterval(updateStats, {{ dashboard_interval }});
            
            // Atualiza status das rodadas a cada 5 segundos (menos frequente para evitar loop)
            setInterval(() => {
                updateRodadaStatus(1);
                updateRodadaStatus(2);
            }, 5000);
            
            // Heartbeat
            setInterval(() => {
                fetch('/heartbeat?page=dashboard');
            }, {{ heartbeat_interval }});
            
            // Inicialização
            updateStats();
            updateRodadaStatus(1);
            updateRodadaStatus(2);
        </script>
    </body>
    </html>
    ''', stats=stats, dashboard_interval=Config.DASHBOARD_UPDATE_INTERVAL, 
        heartbeat_interval=Config.HEARTBEAT_INTERVAL)