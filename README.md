# Lab Wiz: Dockerfile, vulnerabilidades e CCR de root

> Tudo aqui é **intencionalmente inseguro**. As credenciais são falsas. Não use em produção e não faça push para um repositório público.

## Estrutura

```
wiz-dockerfile-lab/
├── vuln-app/                 # app com vulnerabilidades plantadas
│   ├── Dockerfile            # base EOL + misconfigs + secrets + USER root
│   ├── requirements.txt      # libs Python com CVEs (Django 2.2.0, PyYAML 5.3...)
│   ├── package.json / package-lock.json  # libs Node com CVEs (lodash, minimist...)
│   ├── pom.xml               # log4j-core 2.14.1 (Log4Shell)
│   └── app.py                # SAST: command injection, SQLi, pickle, md5
├── ccr-root-tests/           # 11 casos para validar a sua CCR de root
└── run-scans.sh              # roteiro de scans
```

## O que cada scan deve encontrar

| Scan | Comando | Deve achar |
|---|---|---|
| Diretório | `wizcli scan dir ./vuln-app` | CVEs em requirements/package-lock/pom, secrets, SAST no app.py, misconfigs do Dockerfile |
| Imagem | `wizcli scan container-image wiz-lab/vuln-app:1.0` | CVEs de OS packages (Debian), libs Python instaladas, Python 3.7 EOL, secrets em ENV |
| Atalho | `wizcli scan container-image node:14` | Muitos CVEs sem precisar fazer build |

> Um Dockerfile **não tem CVE**. Quem tem CVE é a imagem base e os pacotes instalados. No Dockerfile, o scan de IaC acha misconfigurations. Para ver vulnerabilidades, você precisa escanear a imagem construída ou os manifests de dependências.

## Gabarito da CCR de root

| Caso | Instrução | Esperado | Armadilha |
|---|---|---|---|
| 01 | `USER root` | ❌ violação | básico |
| 02 | `USER 0` | ❌ violação | básico |
| 03 | `USER 0:0` | ❌ violação | formato uid:gid |
| 04 | sem `USER` | ❌ violação | **o padrão é root** |
| 05 | multi-stage, final `root` | ❌ violação | só o último stage importa |
| 06 | multi-stage, builder root e final `10001` | ✅ OK | falso positivo comum |
| 07 | `ARG APP_UID=0` + `USER ${APP_UID}` | ❌ violação | variável |
| 08 | `USER 10001` | ✅ OK | controle positivo |
| 09 | `USER ROOT` | ⚠️ discutível | Linux é case-sensitive |
| 10 | `USER root:app` | ❌ violação | grupo diferente |
| 11 | `USER 00` | ❌ violação | comparação como string |

Uma CCR boa acerta os casos 01–08 e 10. Os casos 07 e 11 mostram até onde vai a análise estática.

## Observações

- Rode no WSL dentro da pasta do lab, sem usar `~fdiasz/...`.
- Use `--by-policy-hits DISABLED` para ver tudo, inclusive o que nenhuma policy reprovaria.
- O `docker build` do vuln-app usa `apt-get` e `pip`. Se falhar por rede ou proxy, o `scan dir` continua achando as libs pelo requirements.txt, e o atalho com `node:14` dispensa o build.
