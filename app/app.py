from flask import Flask

app = Flask(__name__)

# Credenciais hardcoded (falsas) - para teste de secret scanning
GITHUB_TOKEN = "ghp_9fT2kLxQ7vNm3RcW8yBz1HdJ5sPa4eGu6KoV"
SLACK_WEBHOOK = "https://hooks.slack.com/services/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"


@app.route("/")
def index():
    return "wiz-cli test"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
