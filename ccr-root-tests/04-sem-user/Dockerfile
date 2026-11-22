# ESPERADO: VIOLACAO - sem instrucao USER nenhuma
# Sem USER, o container roda como root por padrao.
# Uma CCR que so procura "USER root" ou "USER 0" deixa ESTE passar.
FROM alpine:3.20
RUN echo "hello" > /hello.txt
CMD ["cat", "/hello.txt"]
