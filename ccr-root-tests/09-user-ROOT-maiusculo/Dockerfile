# ESPERADO: DISCUTIVEL - "ROOT" maiusculo
# No Linux, nome de usuario e case-sensitive: "ROOT" NAO e o usuario root.
# (Este container nem sobe, porque o usuario "ROOT" nao existe.)
# Se sua CCR compara sem case-sensitivity, ela acusa aqui. Isso e o que voce quer?
FROM alpine:3.20
RUN echo "hello" > /hello.txt
USER ROOT
CMD ["cat", "/hello.txt"]
