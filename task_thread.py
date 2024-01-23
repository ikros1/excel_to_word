import random
import threading
import time
from task import TaskInstance


def generate_unique_id():
    # 获取当前时间戳的整数部分
    timestamp = int(time.time())

    # 生成一个随机数（这里使用6位随机数，可以根据需要调整）
    random_number = random.randint(100000, 999999)

    # 将时间戳和随机数结合起来
    unique_id = f"{timestamp}{random_number}"

    return str(unique_id)


class TaskManager:
    def __init__(self):
        self.task_queue = []

    def check_over_add_task(self, from_person_id):
        # 遍历列表的切片，但修改原始列表
        for index, task in enumerate(self.task_queue[:]):
            if task.from_person_id == str(from_person_id):
                return False
        return True

    def add_task(self, from_person_id, passwd):
        index = generate_unique_id()
        task_instance = TaskInstance(str(index), str(from_person_id), str(passwd))
        self.task_queue.append(task_instance)
        return index

    def task_start(self, task_id, passwd):
        # 遍历列表检查id密码
        for task in self.task_queue:
            print(" into task_id : " + str(task_id))
            if task.index == str(task_id):
                print(" task_id : " + str(
                    task_id) + " ok ,passwd from front : " + passwd + " ,passwd from back: " + task.passwd)
                if task.passwd == str(passwd):
                    task.start()
                    return True
        return False

    def get_task_info(self, task_id, passwd):
        # 遍历列表检查id密码
        for task in self.task_queue:
            print(" into task_id : " + str(task_id))
            if task.index == str(task_id):
                print(" task_id : " + str(
                    task_id) + " ok ,passwd from front : " + passwd + " ,passwd from back: " + task.passwd)
                if task.passwd == str(passwd):
                    return True, task.get_status(), task.status_info, task.task_over_percent
        return False, None, None, None

    def get_download_info(self, task_id, passwd):
        # 遍历列表检查id密码
        for task in self.task_queue:
            if task.index == str(task_id):
                if task.passwd == str(passwd):
                    if task.task_over_percent == 1:
                        return True, str(task.pay), str(task.download_preview_file_href), str(
                            task.download_zip_file_href)
        return False, None, None, None

    def check_all_task_instance_to_delete(self):
        while True:
            time.sleep(3)
            # 遍历列表的切片，但修改原始列表
            for index, task in enumerate(self.task_queue[:]):
                if task.status == "deleted":
                    print("manager pop task id： " + task.index)
                    self.task_queue.pop(index)

    def set_excel_word_file(self, from_person_id, word_file, excel_file):
        for index, task in enumerate(self.task_queue[:]):
            if task.from_person_id == str(from_person_id):
                self.task_queue[index].set_word_file(word_file)
                self.task_queue[index].set_excel_file(excel_file)

    def start_task_manager(self):
        thread = threading.Thread(target=self.check_all_task_instance_to_delete)
        thread.start()
