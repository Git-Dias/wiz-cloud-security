# ESPERADO: VIOLACAO - USER 0 (UID numerico)
FROM alpine:3.20
RUN echo "hello" > /hello.txt
USER 0
CMD ["cat", "/hello.txt"]
