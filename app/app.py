from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecretkey")
tasks = []

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    if not task_content or len(task_content.strip()) == 0:
        return jsonify({"error": "Content cannot be empty!"}), 400
    tasks.append(task_content)
    return jsonify({"message": "Task added successfully!"}), 200

@app.route('/delete', methods=['POST'])
def delete_task():
    try:
        task_index = int(request.form.get('index'))
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            return jsonify({"message": "Task deleted successfully!"}), 200
        return jsonify({"error": "Invalid task index!"}), 400
    except ValueError:
        return jsonify({"error": "Invalid input format!"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Update to bind to 0.0.0.0