import os
from deal_tasks.get_all_tasks import get_all_tasks
from deal_tasks.get_task_entry import get_all_entry

# 添加任务列表的函数
def add_task_list(all_task_list,task_option):
    task_list = []
    
    while True:
        os.system("cls")
        # 显示所有任务
        print("添加任务")
        add_task_num = 1
        if all_task_list:
            for i in all_task_list:
                print(add_task_num,".",i,end="\n")
                add_task_num += 1
        # 显示已添加的任务
        print("已添加任务：")
        added_task_num = 1
        for i in task_list:
            try:
                i = dict(i)
                if type(i) == dict:
                    for key,value in i.items():
                        print(added_task_num,".",key,":",value,end="\n")
                added_task_num += 1
            except:
                print(added_task_num,".",i,end="\n")
                added_task_num += 1
        print("\n")
        # 输入任务编号
        task_id = input("请输入任务编号,输入0退出：")
        # 将输入的任务编号转换为整数
        try:
            task_id = int(task_id)
        except:
            os.system("cls")
            continue
        # 判断输入的任务编号是否有效
        if task_id > len(all_task_list) or task_id < 0:
            print("输入错误，请重新输入！")
            os.system("cls")
        elif task_id == 0:
            os.system("cls")
            break
        else:
            if task_option[task_id-1] != " ":
                print(task_option[task_id-1])
                option_name = get_option_task(task_option[task_id-1])
                if get_all_entry(option_name) == ([],[],[],[]):
                    task_list.append({f'{all_task_list[task_id-1]}':f'{option_name}'})
            else:
                task_list.append(all_task_list[task_id-1])
                os.system("cls")
        """
        [' ', 
        ['征集几个'], 
        ['领取资源、好感、售卖机', '社教模拟仪', '制造物品', '是否喝茶', '是否领取活力值'], 
        ' ', 
        ['和合版本'], 
        ' ', 
        ' ', 
        ' ', 
        ' ', 
        ['选择关卡-演训', '打哪个-演训', '打几次'], 
        ['选择关卡-资源', '打哪个-资源', '打几次'], 
        ' ',
        ' ',
        ['选择研学主题', '选择地图(仅老研学)', '是否自行选择角色和buff'], 
        ['分解的装备的最大品质'], 
        ' ', 
        ' ']
        """
    return task_list

# 删除任务列表的函数
def delete_task_list(task_list):
    os.system("cls")
    while True:
        num = 1
        print("删除任务")

        print("已添加任务：")
        
        for i in task_list:
            print(num,".",i,end=",")
            num += 1
        print("\n")

        task_id = int(input("请输入任务编号,输入0退出："))

        if task_id > len(task_list) or task_id < 0:
            print("输入错误，请重新输入！")
            os.system("cls")
        elif task_id == 0:
            break
        else:
            task_list.pop(task_id-1)
            os.system("cls")
        
    return task_list

# 获取任务选项的函数
def get_option_task(task_option):
    
    # task_option = [
    #             "领取资源、好感、售卖机",
    #             "社教模拟仪",
    #             "制造物品",
    #             "是否喝茶",
    #             "是否领取活力值"
    #         ]
     # ['领取奖励', '不领取']  
     # ['entry_dispath_one', ['entry_back', 'entry_convened']]
    task_list = []
    for task_name in task_option:
        pipeline_override,all_cases_names,all_cases_pipelines,all_tasks_options = get_all_entry(task_name)
        os.system("cls")
        num = 1
        print(f"{task_name}")
        for i in all_cases_names:
            print(num,".",i,end="\n")
            num += 1
        # 输入任务编号
        task_id = input("请输入任务编号,输入0退出：")
        # 将输入的任务编号转换为整数
        try:
            task_id = int(task_id)
            task_list.append(all_cases_names[task_id-1])
            os.system("cls")
        except:
            os.system("cls")
            continue
    return task_list

# 主程序入口
if __name__ == '__main__':
    tasks_names, tasks_entry, task_option = get_all_tasks()
    
    task_list = add_task_list(tasks_names,task_option)
    print(task_list)
    # get_option_task()