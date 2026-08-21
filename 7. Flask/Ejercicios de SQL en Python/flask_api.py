import psycopg2
from psycopg_connection import PgManager
from repository_pattern import UserRepository
from repository_pattern import CarRepository
from flask import Flask, jsonify, request

app = Flask(__name__)

db_manager = PgManager(
    db_name="postgres",
    user="postgres",
    password="postgres",
    host="localhost"
    )




# @app.route("/lyfter_car_rental/<table>", methods=["POST"])
# def create_record():
#     try:
#         request_json = request.get_json()
#         if not request_json:
#             return jsonify({"message": "Missing JSON body"}), 400
#         new_task = body_validation()
#         # load tasks and append the new one
#         tasks = load_tasks()
#         if any(t["task_id"] == new_task["task_id"] for t in tasks):
#             raise ValueError(f"The task id {new_task['task_id']} is already created. If you want to modify it, try PUT method.")
#         else:
#             tasks.append(new_task)
#         # write in the file
#         save_tasks(tasks)
#         return jsonify(tasks), 201  # status code "created"
#     except ValueError as ex:
#         return jsonify(message=str(ex)), 400



# @app.route("/lyfter_car_rental", methods=["GET"])
# def get_tasks():
#     tasks = load_tasks()  # if not found will return there
#     status_filter = request.args.get("status")
#     if status_filter:
#         filtered_tasks = list(
#             filter(lambda tasks: tasks["status"].title() == status_filter.title(), tasks)
#         )
#         return jsonify(filtered_tasks), 200
#     if not tasks:
#         return jsonify({"message": 'file not found or there are no tasks.'}), 200
#     return jsonify(tasks), 200





# @app.route("/tasks", methods=["PUT"])
# def update_task():
#     try:
#         request_json = request.get_json()
#         if not request_json:
#             return jsonify({"message": "Missing JSON body"}), 400
#         # create new task
#         new_task = body_validation()
#         # load tasks and append the new one
#         tasks = load_tasks()
#         if any(t["task_id"] == new_task["task_id"] for t in tasks):
#             for t in tasks:
#                 if t["task_id"] == new_task["task_id"]:
#                     tasks_index = tasks.index(t)
#             tasks[tasks_index] = new_task
#         else:
#             raise ValueError(f"The task id {new_task['task_id']} doesn't exist. Use POST method to create it.")
#         # write in the file
#         save_tasks(tasks)
#         return jsonify(tasks), 200  # status code "modified"
#     except ValueError as ex:
#         return jsonify(message=str(ex)), 400
    
# @app.route("/tasks/<int:task_id>", methods=["DELETE"])
# def delete_task(task_id):
#     try:
#         tasks_loaded = load_tasks()
#         if any(t["task_id"] == task_id for t in tasks_loaded):
#             tasks = [t for t in tasks_loaded if t["task_id"] != task_id]
#         else:
#             raise ValueError(f"The task id {task_id} doesn't exist. Use POST to create it.")
#         save_tasks(tasks)
#         return jsonify(tasks), 200
#     except ValueError as ex:
#         return jsonify(message=str(ex)), 400


if __name__ == "__main__":
    app.run(host="localhost", debug=True)