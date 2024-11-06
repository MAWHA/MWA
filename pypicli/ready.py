from runtasks.run_tasks import run_task
from deal_tasks.deal_task_list import add_task_list
from deal_tasks.get_task_entry import get_all_entry
from deal_tasks.get_all_tasks import get_all_tasks
import ast

def ready_run_task():
    # 任务task运行
    tasks_names, tasks_entry, task_option = get_all_tasks()    # add_task_list(tasks_name,task_option)
    task_list = add_task_list(tasks_names,task_option)
    print(f"任务列表：{task_list}")
    entry_list = []
    for _entry_type in task_list:
        if type(_entry_type) == str:
            pipeline_override,task_name, task_entry, task_option = get_all_entry(_entry_type)
            print(f"添加了{task_name[0]}任务：", task_entry[0])
            entry_list.append(task_entry[0])
        elif type(_entry_type) == dict:
            pipeline_override,task_name, task_entry, task_option = get_all_entry(list(_entry_type)[0])

            print(f"添加了{task_name[0]}任务：", task_entry[0])
            entry_list.append(task_entry[0])
            print("_entry_type",_entry_type)
            for option_name in _entry_type.keys():
                pipeline_overrides,task_name, task_entry, task_options = get_all_entry(option_name)
                all_entry = ast.literal_eval(list(list(_entry_type.values()))[0])

                for i in range(len(all_entry)):
                    entry = all_entry[i]
                    entry_name = task_option[i]
                    pipeline_overrides,task_name, task_entry, task_options = get_all_entry(entry_name)
                    # print("pipeline_overrides:",pipeline_overrides,"\n",)
                    # print("task_name:",task_name,"\n",)
                    # print("task_entry:",task_entry,"\n",)
                    # print("task_options:",task_options,"\n",)
                    
                    entry_id = task_name.index(entry)
                    entry_list.append(task_entry[entry_id])
            
                    # print(f"添加了{task_name[entry_id]}任务：", pipeline_override[entry_id])
                    # entry_list.append(pipeline_override[0])

                    # index = task_name.index(task_name[entry_id])
                    # # print("index",index)
                    # print(f"添加了{task_name[entry_id]}的子任务：{task_name[entry.index(entry[index])]}", task_entry[entry.index(entry[index])])
                    # entry_list.append(task_entry[entry.index(entry[index])])
                
                    
                    # print("pipeline_override:",pipeline_override,"\n",
                    #     "task_name:",task_name,"\n",
                    #     "entry_names:",task_entry,"\n",
                    #     "task_options:",task_option)




            #     print(option_name)
            #     pipeline_override,all_cases_names,all_cases_pipelines,all_tasks_options = get_all_entry(option_name)#征集几个
            #     print("pipeline_override:",pipeline_override,"\n",
            #             "all_cases_names:",all_cases_names,"\n",
            #         "entry_names:",all_cases_pipelines,"\n",
            #             "options:",all_tasks_options)
            #     entry_list.append(pipeline_override)
                # for 
    print("entry_list:",entry_list)
    # print(task_list)
    return entry_list

def run():
    entry_list = ready_run_task()
    num = 0
    for entry in entry_list:
        if type(entry) == str:
            run_task(entry)
            num += 1
        elif type(entry) == list:
            for task in entry_list[num]:
                run_task(task)
            num += 1

if __name__ == '__main__':
    ready_run_task()