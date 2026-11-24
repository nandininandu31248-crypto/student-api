from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or "title" not in data or "status" not in data:
        return jsonify({"error": "title and status are required"}), 400

    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "status": data["status"]
    }

    tasks.append(task)

    return jsonify(task), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200

if __name__ == "__main__":
    app.run(debug=True)