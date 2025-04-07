from app import tasker_init

tasker = tasker_init()

def run_task(task_name):
    tasker.post_pipeline(task_name).wait()