# =============================================================
# LAB WIZ - DOCKERFILE INTENCIONALMENTE INSEGURO
# NAO USAR EM PRODUCAO. Todas as credenciais sao FALSAS.
# =============================================================

# [VULN + EOL] Python 3.7 (EOL jun/2023) e imagem sem atualizacao desde 2023
#   -> CVEs de OS packages + "End of life components"
# [IaC] Tag mutavel, sem digest (@sha256:...)
FROM python:3.7-slim

# [SECRETS] Credenciais hardcoded em ENV (ficam gravadas nas camadas da imagem)
ENV AWS_ACCESS_KEY_ID=AKIAQWERTY12345678XZ
ENV AWS_SECRET_ACCESS_KEY=Zq8Lk2Vb9Nw4Rt6Yp1Xc3Mf7Hj5Gd0Sa2Ue8Wi4O
ENV DB_PASSWORD=SuperSenha@2026!

# [IaC] apt sem --no-install-recommends, sem limpar cache, instalando sudo
RUN apt-get update && apt-get install -y curl sudo

WORKDIR /app

# [IaC] ADD em vez de COPY
ADD requirements.txt /app/requirements.txt

# [VULN] Bibliotecas Python com CVEs conhecidos (ver requirements.txt)
RUN pip install -r requirements.txt

ADD . /app

# [IaC] Permissao 777
RUN chmod -R 777 /app

# [IaC] Porta SSH exposta
EXPOSE 22 5000

# [IaC / sua CCR] Rodando como root de forma explicita
USER root

# [IaC] Sem HEALTHCHECK
CMD ["python", "app.py"]
