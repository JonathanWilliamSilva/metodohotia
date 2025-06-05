# Arquivo: local_preview.py
# Execute este script localmente para visualizar o site antes do deploy

import os
from flask import Flask, render_template_string

# Cria a instância Flask com root_path explícito para evitar erro de builtins
app = Flask(__name__, root_path=os.path.dirname(os.path.abspath(__file__)))

# Carrega o código original do app.py e registra apenas a função index
with open("app.py", "r", encoding="utf-8") as f:
    exec_globals = {"__name__": "__app__"}
    exec(f.read(), exec_globals)
    index = exec_globals.get("index")
    if index:
        app.route("/")(index)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    print(f"Acesse http://localhost:{port}")
    app.run(host='127.0.0.1', port=port, debug=True)