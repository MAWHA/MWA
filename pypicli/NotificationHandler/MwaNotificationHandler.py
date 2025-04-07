from maa.notification_handler import NotificationHandler, NotificationType


#自定义通知处理器类
class MwaNotificationHandler(NotificationHandler):
    # 处理资源加载的通知
    def on_resource_loading(
        self,
        noti_type: NotificationType,
        detail: NotificationHandler.ResourceLoadingDetail,
    ):
        print(f"资源加载中: {noti_type}, {detail}")

    # 处理控制器动作的通知
    def on_controller_action(
        self,
        noti_type: NotificationType,
        detail: NotificationHandler.ControllerActionDetail,
    ):
        print(f"控制器动作: {noti_type}, {detail}")

    # 处理任务器任务的通知
    def on_tasker_task(
        self, noti_type: NotificationType, detail: NotificationHandler.TaskerTaskDetail
    ):
        print(f"任务器任务: {noti_type}, {detail}")

    # 处理任务的下一个列表的通知
    def on_task_next_list(
        self,
        noti_type: NotificationType,
        detail: NotificationHandler.TaskNextListDetail,
    ):
        print(f"下一个任务: {noti_type}, {detail}")

    # 处理任务识别的通知
    def on_task_recognition(
        self,
        noti_type: NotificationType,
        detail: NotificationHandler.TaskRecognitionDetail,
    ):
        print(f"任务识别: {noti_type}, {detail}")

    # 处理任务动作的通知
    def on_task_action(
        self, noti_type: NotificationType, detail: NotificationHandler.TaskActionDetail
    ):
        print(f"任务动作: {noti_type}, {detail}")