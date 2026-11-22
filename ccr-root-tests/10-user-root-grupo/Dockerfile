# ESPERADO: VIOLACAO - root com grupo diferente (root:app)
FROM alpine:3.20
RUN addgroup -S app && echo "hello" > /hello.txt
USER root:app
CMD ["cat", "/hello.txt"]
