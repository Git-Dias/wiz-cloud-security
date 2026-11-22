# ESPERADO: VIOLACAO - multi-stage, o stage FINAL roda como root
# O builder usa non-root, mas o que vai para producao e o ultimo stage.
FROM alpine:3.20 AS builder
RUN adduser -D -u 10001 builder
USER 10001
RUN echo "build" > /tmp/artifact.txt

FROM alpine:3.20
COPY --from=builder /tmp/artifact.txt /artifact.txt
USER root
CMD ["cat", "/artifact.txt"]
