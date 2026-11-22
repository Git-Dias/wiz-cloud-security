# ESPERADO: VIOLACAO (caso dificil) - root escondido em ARG
# Analise estatica precisa resolver o valor default do ARG.
FROM alpine:3.20
ARG APP_UID=0
RUN echo "hello" > /hello.txt
USER ${APP_UID}
CMD ["cat", "/hello.txt"]
