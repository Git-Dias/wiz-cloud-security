# ESPERADO: OK - usuario non-root com UID alto
FROM alpine:3.20
RUN adduser -D -u 10001 app && echo "hello" > /hello.txt
USER 10001
CMD ["cat", "/hello.txt"]
