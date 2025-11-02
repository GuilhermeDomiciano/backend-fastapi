#!/usr/bin/env bash
set -euo pipefail

# Sempre rodar a partir da raiz do repo
cd "$(dirname "$0")"

# ── Escolhe o comando de Python disponível (Windows/macOS/Linux)
pick_python() {
  if command -v python >/dev/null 2>&1; then
    echo "python"
  elif command -v python3 >/dev/null 2>&1; then
    echo "python3"
  elif command -v py >/dev/null 2>&1; then
    # Em Windows com "py" instalado
    echo "py -3"
  else
    echo "Erro: Python não encontrado no PATH." >&2
    exit 1
  fi
}
PYTHON_CMD=$(pick_python)

# ── Cria venv se não existir
if [ ! -d ".venv" ]; then
  echo "▶ Criando virtualenv (.venv)…"
  eval "$PYTHON_CMD -m venv .venv"
fi

# ── Ativa venv (Windows usa Scripts/, Linux/macOS usa bin/)
if [ -f ".venv/Scripts/activate" ]; then
  # Windows (Git Bash/PowerShell)
  # shellcheck disable=SC1091
  source ".venv/Scripts/activate"
else
  # macOS/Linux/WSL
  # shellcheck disable=SC1091
  source ".venv/bin/activate"
fi

# ── Instala dependências
if [ -f "requirements.txt" ]; then
  echo "▶ Instalando dependências…"
  python -m pip install --upgrade pip
  pip install -r requirements.txt
else
  echo "⚠️  requirements.txt não encontrado; seguindo assim mesmo."
fi

# ── Porta (padrão 8000; mude com: PORT=8080 ./run.sh)
PORT="${PORT:-8000}"

# ── Sobe o backend (main:app)
echo "🚀 Subindo FastAPI em http://localhost:${PORT} (Ctrl+C para sair)"
python -m uvicorn main:app --reload --host 0.0.0.0 --port "${PORT}"
