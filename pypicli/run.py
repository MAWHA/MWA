# from runtasks.run_tasks import run_task
from deal_tasks.deal_task_list import add_task_list
from deal_tasks.get_task_entry import get_all_entry
# from deal_tasks.deal_task_list import add_task_list
from deal_tasks.get_all_tasks import get_all_tasks

if __name__ == '__main__':
    # 任务task运行
    tasks_names, tasks_entry, task_option = get_all_tasks()    # add_task_list(tasks_name,task_option)
    task_list = add_task_list(tasks_names,task_option)
    print(task_list)