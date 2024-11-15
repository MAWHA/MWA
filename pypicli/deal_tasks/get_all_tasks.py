import os
import json
from deal_tasks.get_task_entry import get_all_entry

def get_all_tasks()->list:
    """
    Get all single tasks of a project.
    :param project_name: The name of the project.
    :return: A list of single tasks.
    """
    
    with open("interface.json", 'r', encoding='utf-8') as f:
        interface = json.load(f)
    
    tasks,task_names,task_options = [],[],[]
    for task in interface.get("task"):
        tasks.append(task.get("name"))
        task_names.append(task.get("entry"))
        if task.get("option"):
            task_options.append(task.get("option"))
        else:
            task_options.append(" ")

    return tasks, task_names, task_options



if __name__ == '__main__':
    tasks, task_names, task_options = get_all_tasks()
    print(task_options)
    for i in task_options:
        if i == " ":
            continue
        for j in i:
            print(get_all_entry(j))
    # print(get_all_option_entry(""))
    