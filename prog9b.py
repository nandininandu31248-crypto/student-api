
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple list to store tasks
tasks = []

# POST /tasks - Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json(silent=True)

    # Validate JSON input
    if not data:
        return jsonify({
            "error": "Invalid JSON input. Please provide valid JSON data."
        }), 400

    # Validate title
    title = data.get('title')

    if not isinstance(title, str) or not title.strip():
        return jsonify({
            "error": "Task title cannot be empty."
        }), 400

    # Validate status
    status = data.get('status')

    if not isinstance(status, str) or not status.strip():
        return jsonify({
            "error": "Task status is required."
        }), 400

    # Create task
    task = {
        "id": len(tasks) + 1,
        "title": title.strip(),
        "status": status.strip()
    }

    tasks.append(task)

    return jsonify({
        "message": "Task added successfully",
        "task": task
    }), 201


# GET /tasks - View all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({
        "message": "Tasks retrieved successfully",
        "tasks": tasks
    }), 200


if __name__ == '__main__':
    app.run(debug=True)
