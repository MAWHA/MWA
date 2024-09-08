"""
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-07-18 23:52:39
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2024-09-08 15:52:35
"""
'''
Author: Night-stars-1 nujj1042633805@gmail.com
Date: 2024-07-18 23:52:39
LastEditors: Night-stars-1 nujj1042633805@gmail.com
LastEditTime: 2024-07-27 11:18:11
'''
import json
import time
from typing import Tuple

# python -m pip install maafw
from maa.define import RectType
from maa.resource import Resource
from maa.controller import AdbController
from maa.instance import Instance
from maa.toolkit import Toolkit

from maa.custom_recognizer import CustomRecognizer

import asyncio

def read_json() -> dict:
    with open("./assets/resource/data/event.json", "r", encoding="utf-8") as f:
        return json.load(f)

DATA = read_json()

async def main():
    user_path = "./"
    Toolkit.init_option(user_path)

    resource = Resource()
    await resource.load("assets/resource/base")

    device_list = await Toolkit.adb_devices()
    if not device_list:
        print("No ADB device found.")
        exit()

    # for demo, we just use the first device
    device = device_list[0]
    controller = AdbController(
        adb_path=device.adb_path,
        address=device.address,
    )
    await controller.connect()

    maa_inst = Instance()
    maa_inst.bind(resource, controller)

    if not maa_inst.inited:
        print("Failed to init MAA.")
        exit()

    maa_inst.register_recognizer("event_select", event_select)

    await maa_inst.run_task("MyCustomRecTask")


class EventSelect(CustomRecognizer):
    def analyze(
        self, context, image, task_name, custom_param
    ) -> Tuple[bool, RectType, str]:
        _, _, pos_data = context.run_recognition(
            image,
            "OCR",
            {"OCR": {"recognition": "OCR", "expected": "识别事件名称", "roi": [593, 113, 516, 46]}},
        )
        pos_data = json.loads(pos_data)
        print(pos_data)
        if len(pos_data["all"]) < 1:
            print("事件标题获取失败")
            return False, (0, 0, 100, 100), "事件标题获取失败"
        text_data = pos_data["all"][0]
        title = text_data["text"]
        score = text_data["score"]
        if (option := DATA[title]):
            print(f"识别到{title}, 相似度: {int(score * 100)}%, 选择: {option}")
            status, option_rect, _ = context.run_recognition(
                image,
                "OCR",
                {"OCR": {"recognition": "OCR", "expected": option, "roi": [598, 383, 478, 217]}},
            )
            print(f"识别结果: {status}, 坐标: {option_rect}")
            # context.click(int(option_rect[0] + option_rect[2] / 2), int(option_rect[1] + option_rect[3] / 2))
            return False, (0, 0, 100, 100), "事件选择"
        else:
            print("事件标题获取失败")
            return False, (0, 0, 100, 100), "事件标题获取失败"

event_select = EventSelect()


if __name__ == "__main__":
    asyncio.run(main())
