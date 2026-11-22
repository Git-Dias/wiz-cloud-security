# ESPERADO: OK (falso positivo se a CCR acusar)
# O builder roda como root (normal para compilar), mas o stage FINAL e non-root.
FROM alpine:3.20 AS builder
USER root
RUN echo "build" > /tmp/artifact.txt

FROM alpine:3.20
RUN adduser -D -u 10001 app
COPY --from=builder /tmp/artifact.txt /artifact.txt
USER 10001
CMD ["cat", "/artifact.txt"]
