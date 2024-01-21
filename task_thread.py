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
        self.lock = threading.Lock()

    def check_over_add_task(self, from_person_id):
        # 遍历列表的切片，但修改原始列表
        for index, task in enumerate(self.task_queue[:]):
            if task.from_person_id == str(from_person_id):
                return False
        return True

    def add_task(self, from_person_id, passwd):
        with self.lock:
            index = generate_unique_id()
            task_instance = TaskInstance(index, str(from_person_id), passwd)
            self.task_queue.append(task_instance)
            return index

    def task_start(self, task_id, passwd):
        # 遍历列表检查id密码
        for task in self.task_queue:
            if task.index == str(task_id):
                if task.passwd == str(passwd):
                    task.start()
                    return True
        return False

    def get_task_info(self, task_id, passwd):
        # 遍历列表检查id密码
        for task in self.task_queue:
            if task.index == str(task_id):
                if task.passwd == str(passwd):
                    return True, task.get_status(), task.status_info, task.task_over_percent
        return False, None, None, None

    def get_down_info(self, task_id, passwd):
        # 遍历列表检查id密码
        for task in self.task_queue:
            if task.index == str(task_id):
                if task.passwd == str(passwd):
                    return True, task.send_zip_file_path_name, str(task.pay), str(task.last_one_preview_file_path_name)
        return False, None, None, None

    def check_all_task_instance_to_delete(self):
        while True:
            # 遍历列表的切片，但修改原始列表
            for index, task in enumerate(self.task_queue[:]):
                if task.status == "deleted":
                    self.task_queue.pop(index)

    def set_excel_word_file(self, from_person_id, word_file, excel_file):
        while True:
            # 遍历列表的切片，但修改原始列表
            for index, task in enumerate(self.task_queue[:]):
                if task.from_person_id == str(from_person_id):
                    self.task_queue[index].set_word_file(word_file)
                    self.task_queue[index].set_excel_file(excel_file)

    def start_task_manager(self):
        thread = threading.Thread(target=self.check_all_task_instance_to_delete)
        thread.start()
