# =====================================================================
# IMAGEM INTENCIONALMENTE VULNERAVEL - USO EXCLUSIVO PARA TESTE DO WIZ CLI
# NAO UTILIZAR EM PRODUCAO
# =====================================================================

# Base EOL (Python 3.6 / Debian 10 "buster") -> centenas de CVEs de SO
FROM python:3.6-slim-buster

# Segredos hardcoded em variaveis de ambiente (falsos)
ENV DB_PASSWORD="SuperSecret123!" \
    AWS_ACCESS_KEY_ID="AKIA4WJPWFRTQ7ZK3XNB" \
    AWS_SECRET_ACCESS_KEY="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"

WORKDIR /app

# Bibliotecas Python antigas com CVEs conhecidas
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia codigo + arquivos com segredos (chave privada, .env, credenciais)
COPY app/ .

# Roda como root (sem USER) e expoe portas sensiveis
EXPOSE 22 5000
CMD ["python", "app.py"]
