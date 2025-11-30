import os
from flask import request, redirect, url_for, flash, jsonify
from werkzeug.utils import secure_filename
from config import Config
from templates import (
    render_index, render_rodada1, render_rodada2, 
    render_rodada_bloqueada, render_dashboard
)

def register_routes(app):
    """Registra todas as rotas da aplicação"""
    
    # Estado global das rodadas
    state = {
        "rodada1": Config.RODADA1_LIBERADA,
        "rodada2": Config.RODADA2_LIBERADA
    }

    @app.route('/')
    def index():
        return render_index()
    
    @app.route('/rodada1', methods=['GET', 'POST'])
    def rodada1():
        if not state["rodada1"]:
            return render_rodada_bloqueada(
                rodada=1,
                cor_principal='#667eea',
                cor_hover='#5568d3'
            )
        
        if request.method == 'POST':
            file = request.files.get('file')
            if not file or file.filename == '':
                flash('Nenhum arquivo selecionado')
                return redirect(request.url)
            
            os.makedirs(Config.UPLOAD_FOLDER_R1, exist_ok=True)
            filename = secure_filename(file.filename)
            base, ext = os.path.splitext(filename)
            counter, path = 1, os.path.join(Config.UPLOAD_FOLDER_R1, filename)
            while os.path.exists(path):
                path = os.path.join(Config.UPLOAD_FOLDER_R1, f"{base}({counter}){ext}")
                counter += 1
            file.save(path)
            flash(f'Arquivo "{os.path.basename(path)}" enviado com sucesso!')
            return redirect(url_for('rodada1'))
        
        return render_rodada1()
    
    @app.route('/rodada2', methods=['GET', 'POST'])
    def rodada2():
        if not state["rodada2"]:
            return render_rodada_bloqueada(
                rodada=2,
                cor_principal='#f5576c',
                cor_hover='#e04455'
            )
        
        if request.method == 'POST':
            file = request.files.get('file')
            if not file or file.filename == '':
                flash('Nenhum arquivo selecionado')
                return redirect(request.url)
            
            os.makedirs(Config.UPLOAD_FOLDER_R2, exist_ok=True)
            filename = secure_filename(file.filename)
            base, ext = os.path.splitext(filename)
            counter, path = 1, os.path.join(Config.UPLOAD_FOLDER_R2, filename)
            while os.path.exists(path):
                path = os.path.join(Config.UPLOAD_FOLDER_R2, f"{base}({counter}){ext}")
                counter += 1
            file.save(path)
            flash(f'Arquivo "{os.path.basename(path)}" enviado com sucesso!')
            return redirect(url_for('rodada2'))
        
        return render_rodada2()
    
    @app.route('/dashboard')
    def dashboard():
        stats = {"total": 0, "rodada1": 0, "rodada2": 0}
        return render_dashboard(stats)
    
    # --- APIs de controle das rodadas ---
    @app.route('/api/rodada1/status')
    def api_r1_status():
        return jsonify({"liberada": state["rodada1"]})
    
    @app.route('/api/rodada2/status')
    def api_r2_status():
        return jsonify({"liberada": state["rodada2"]})
    
    @app.route('/api/rodada1/toggle', methods=['POST'])
    def api_r1_toggle():
        data = request.get_json(force=True)
        state["rodada1"] = bool(data.get("liberar", False))
        return jsonify({"success": True, "liberada": state["rodada1"]})
    
    @app.route('/api/rodada2/toggle', methods=['POST'])
    def api_r2_toggle():
        data = request.get_json(force=True)
        state["rodada2"] = bool(data.get("liberar", False))
        return jsonify({"success": True, "liberada": state["rodada2"]})
