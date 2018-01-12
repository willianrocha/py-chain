from core.transaction import Transaction
from flask import Flask, request
import os
import json

app = Flask(__name__)

@app.route("/txn/", methods=['POST'])
def incoming_transaction():
    t = Transaction()
    tx = request.get_json()
    if t.isValidTx(tx):
        return json.dumps(t.pushToMiner(tx)).encode('utf-8')
    else:
        return json.dumps({'status':'error', 'msg': 'invalid transaction'}).encode('utf-8')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port, debug=True)
    app.run(host='0.0.0.0', port=port)