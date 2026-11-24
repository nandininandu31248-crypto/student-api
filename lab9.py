from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    title = data.get("title", "").strip()
    status = data.get("status", "").strip()

    if not title:
        return jsonify({
            "error": "Task title cannot be empty"
        }), 400

    if not status:
        return jsonify({
            "error": "Task status is required"
        }), 400

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "status": status
    }

    tasks.append(task)

    return jsonify(task), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

if __name__ == "__main__":
    app.run(debug=True)
