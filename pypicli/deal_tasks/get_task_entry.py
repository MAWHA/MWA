import codecs
import json


def get_all_entry(option_name:str):
    with codecs.open("interface.json", 'r', encoding='utf-8') as f:
        interface = json.load(f)
    all_cases, all_cases_names, all_cases_pipelines,all_tasks_options,pipeline_override = {},[],[],[],[]
    try:
        for _allcases in interface.get("option").get(option_name).get("cases"):
            all_cases[_allcases.get("name")] = _allcases.get("pipeline_override")
        for _cases_name in all_cases.keys():
            all_cases_names.append(_cases_name)
        pipeline_override.append(list(list(all_cases.values())[0].keys())[0])
        for _case in all_cases.values():
            for _case_key in _case.keys():
                for _case_value in _case.get(_case_key).values():
                    all_cases_pipelines.append(_case_value)
        return pipeline_override,all_cases_names,all_cases_pipelines,all_tasks_options
    except:
        for _entry in interface.get("task"):
            if _entry.get("name") == option_name:
                all_cases_names.append(_entry.get("name"))
                all_cases_pipelines.append(_entry.get("entry"))
                try:
                    for _option in _entry.get("option"):
                        # pipeline_override,all_cases_names,all_cases_pipelines,all_tasks_options = get_all_entry(_option)
                        all_tasks_options.append(_option)
                except:
                    pass
        return pipeline_override,all_cases_names,all_cases_pipelines,all_tasks_options


    """
    {'冬谷币': {'StartTraining': {'next': 'Cash   '}},
    '教材': {'StartTraining': {'next': 'Experience'}},
    '装备': {'StartTraining': {'next': 'Weapon'}},
    '宿卫': {'StartTraining': {'next': 'Defender'}},
    '构术': {'StartTraining': {'next': 'Caster'}},
    '远击': {'StartTraining': {'next': 'Ranger'}},
    '轻锐': {'StartTraining': {'next': 'LightMelee'}},
    '战略': {'StartTraining': {'next': 'Tactical'}}}
    """
    

if __name__ == '__main__':
    # print(get_all_entry("器者征集"))
    # print(get_all_entry("领取奖励"))
    print(get_all_entry("社教模拟仪"))
    # print(get_all_entry("选择关卡-演训"))
    