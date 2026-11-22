# ESPERADO: VIOLACAO - USER 0:0 (UID:GID)
# Sua regex/logica precisa tratar o formato user:group
FROM alpine:3.20
RUN echo "hello" > /hello.txt
USER 0:0
CMD ["cat", "/hello.txt"]
