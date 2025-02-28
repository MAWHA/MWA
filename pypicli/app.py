import json
from maa.toolkit import Toolkit
from maa.resource import Resource
from maa.controller import AdbController
from maa.tasker import Tasker

from NotificationHandler.MwaNotificationHandler import MwaNotificationHandler


def tasker_init():
    user_path = "./"
    Toolkit.init_option(user_path)
    
    resource = Resource()
    resource.set_cpu()

    res_job = resource.post_path("./resource_picli/base")
    res_job.wait()
    
    adb_devices = Toolkit.find_adb_devices()
    if not adb_devices:
        print("No ADB device found.")
        exit()

    # for demo, we just use the first device
    device = adb_devices[0]
    controller = AdbController(
        adb_path=device.adb_path,
        address=device.address,
        screencap_methods=device.screencap_methods,
        input_methods=device.input_methods,
        config=device.config
    )
    controller.post_connection().wait()

    # tasker = Tasker()
    tasker = Tasker(notification_handler=MwaNotificationHandler())
    tasker.bind(resource, controller)

    if not tasker.inited:
        print("Failed to init MAA.")
        exit()
    return tasker 


if __name__ == "__main__":
    # main()
    pass