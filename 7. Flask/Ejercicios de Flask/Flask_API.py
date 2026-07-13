import json
from pathlib import Path
from flask import Flask, jsonify, request


app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent #path of the folder containing this .py
file_path = BASE_DIR/"tasks.json"

def load_tasks():
    try:
        with open (file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


@app.route("/tasks",methods = ["GET"])
def get_tasks():
    tasks = load_tasks() #if not found will return there
    if not tasks:
        jsonify({"message": 'file nor found or there are no tasks'}),200
    return jsonify(tasks),200


@app.route("/tasks/create",methods = ["POST"])
def create_tasks():
    try:
        request_json = request.get_json()
        if not request_json:
            return jsonify({"message": "Missing JSON body"}), 400

        required_tasks_fields = ["task_id","title","description","status"]
        status_values = ["Not Started","In Progress","Completed"]

        for field in required_tasks_fields:
            if field not in request.json:
                raise ValueError(f"The body is missing the {field} field")
            if field == "status" and request.json[field].title() not in status_values:
                raise ValueError(f"The status must be one of the following: 'Not Started', 'In Progress' or 'Completed' ")
        # create new task
        new_task = {field : request.json[field] for field in required_tasks_fields}
        
        #load tasks and append the new one
        tasks = load_tasks()
        if any (t["task_id"] == new_task["task_id"] for t in tasks):
            raise ValueError(f"The task id {new_task["task_id"]} is already created. If you want to modify it, try `/tasks/modify`")
        else:
            tasks.append(new_task)

        #write in the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

    

        return jsonify(tasks),201 #status code "created"
    

    except ValueError as ex:
        return jsonify(message=str(ex)), 400


@app.route("/tasks/modify",methods = ["PUT"])
def modify_tasks():
    try:
        request_json = request.get_json()
        if not request_json:
            return jsonify({"message": "Missing JSON body"}), 400

        required_tasks_fields = ["task_id","title","description","status"]
        status_values = ["Not Started","In Progress","Completed"]
        
        for field in required_tasks_fields:
            if field not in request.json:
                raise ValueError(f"The body is missing the {field} field")
            if field == "status" and request.json[field].title() not in status_values:
                raise ValueError(f"The status must be one of the following: 'Not Started', 'In Progress' or 'Completed' ")
        # create new task
        new_task = {field : request.json[field] for field in required_tasks_fields}
        
        #load tasks and append the new one
        tasks = load_tasks()
        
        if any (t["task_id"] == new_task["task_id"] for t in tasks):
            for t in tasks:
                if t["task_id"] == new_task["task_id"]:
                    tasks_index = tasks.index(t)
            tasks[tasks_index]=new_task
        else:
            raise ValueError(f"The task id {new_task["task_id"]} doesn't exist. If you want to create it, try `/tasks/create`")

        #write in the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

    

        return jsonify(tasks),201 #status code "modified"
    

    except ValueError as ex:
        return jsonify(message=str(ex)), 400


@app.route("/tasks/delete",methods = ["DELETE"])
def delete_tasks():

    try:
        task_to_delete = int(request.args.get("task_id"))
        tasks_loaded = load_tasks()
        
        if any (t["task_id"] == task_to_delete for t in tasks_loaded):
            tasks = [t for t in tasks_loaded if t["task_id"] != task_to_delete]
        else:
            raise ValueError(f"The task id {task_to_delete} doesn't exist. First a task with that value has to be created, try `/tasks/create`")

        #write in the file
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

    

        return jsonify(tasks),200 #status code "modified"
    

    except ValueError as ex:
        return jsonify(message=str(ex)), 400
    
    except TypeError:
        return jsonify(message="task_id must be a valid number."), 400

if __name__ == "__main__":
    app.run(host = "localhost", debug=True)


