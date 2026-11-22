# ESPERADO: VIOLACAO (caso dificil) - "00" tambem e UID 0
# Comparacao de string == "0" deixa passar. Precisa comparar como numero.
FROM alpine:3.20
RUN echo "hello" > /hello.txt
USER 00
CMD ["cat", "/hello.txt"]
