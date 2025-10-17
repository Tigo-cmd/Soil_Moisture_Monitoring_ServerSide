# app.py
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import threading, json, time

app = Flask(__name__)
CORS(app)

latest = {}
cond = threading.Condition()

@app.route('/ingest', methods=['POST'])
def ingest():
    global latest
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"status": "bad request"}), 400
    # Save latest reading
    with cond:
        latest = {
            "raw": data.get("raw"),
            "percent": data.get("percent"),
            "state": data.get("state"),
            "ts": int(time.time())
        }
        # notify SSE listeners
        cond.notify_all()
    return jsonify({"status":"ok"}), 200

@app.route('/latest', methods=['GET'])
def get_latest():
    return jsonify(latest)
    
@app.route('/', methods=['GET'])
def home():
    return jsonify({"status":"ok"}), 200

@app.route('/stream')
def stream():
    def event_stream():
        last_ts = None
        while True:
            with cond:
                cond.wait()  # wait until new data is available
                data = json.dumps(latest)
            # SSE event
            yield f"data: {data}\n\n"
    return Response(event_stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8080))
    # Run: python app.py  (or use flask run -h 0.0.0.0 -p 5000)
    app.run(host='0.0.0.0', port=port, threaded=True)
