# from runtasks.run_tasks import run_task
from deal_tasks.deal_task_list import add_task_list
from deal_tasks.get_task_entry import get_all_entry
from deal_tasks.get_all_tasks import get_all_tasks

def run_task():
    # 任务task运行
    tasks_names, tasks_entry, task_option = get_all_tasks()    # add_task_list(tasks_name,task_option)
    task_list = add_task_list(tasks_names,task_option)
    print(f"任务列表：{task_list}")
    entry_list = []
    for _entry_type in task_list:
        if type(_entry_type) == str:
            task_name, task_entry, task_option = get_all_entry(_entry_type)
            entry_list.append(task_entry[0])
        elif type(_entry_type) == dict:
            for _entry, _entry_option in _entry_type.items():
                print(f"case: {get_all_entry(_entry)}")
                for i in _entry_type.keys():
                    print(i)
                    all_cases_names,all_cases_pipelines,all_tasks_options = get_all_entry(i)
                    print("entry_names:",all_cases_pipelines,"\n",
                          "options:",all_tasks_options)
                # for 
    print("entry_list:",entry_list)
    # print(task_list)

if __name__ == '__main__':
    run_task()