import hashlib
import pickle
import sqlite3
import subprocess

import yaml
from flask import Flask, request

app = Flask(__name__)

# [SECRETS] senha hardcoded (falsa)
DB_PASSWORD = "SuperSenha@2026!"


@app.route("/ping")
def ping():
    host = request.args.get("host")
    # [SAST] Command injection
    return subprocess.check_output(f"ping -c 1 {host}", shell=True)


@app.route("/user")
def user():
    uid = request.args.get("id")
    conn = sqlite3.connect("app.db")
    # [SAST] SQL injection
    return str(conn.execute(f"SELECT * FROM users WHERE id = {uid}").fetchall())


@app.route("/load", methods=["POST"])
def load():
    # [SAST] Desserializacao insegura
    return str(pickle.loads(request.data))


@app.route("/config", methods=["POST"])
def config():
    # [SAST] yaml.load sem SafeLoader
    return str(yaml.load(request.data))


def hash_password(p):
    # [SAST] Hash fraco
    return hashlib.md5(p.encode()).hexdigest()


if __name__ == "__main__":
    # [SAST] debug=True e bind em 0.0.0.0
    app.run(host="0.0.0.0", debug=True)
