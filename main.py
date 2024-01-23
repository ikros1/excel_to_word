import logging
import random
import time
from flask_cors import CORS
from flask import Flask, request, jsonify, send_file, send_from_directory, render_template
import os
from task_thread import TaskManager

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='app.log',
                    filemode='w')
manager = TaskManager()
# 启动巡逻线程
manager.start_task_manager()

app = Flask(__name__)

# 指定上传文件保存的目录
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app, supports_credentials=True)
app.template_folder = './templates'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SECRET_KEY'] = 'AASDFASDF'

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'xlsx'}


def generate_unique_string():
    # 获取当前时间戳到毫秒
    timestamp_ms = int(time.time() * 1000)

    # 生成4位随机数字
    random_number = random.randint(1000, 9999)

    # 组合成随机唯一字符
    unique_string = f"{timestamp_ms}{random_number}"

    return unique_string


# 检查文件类型是否允许
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('html/home.html')


# 定义上传文件的路由
@app.route('/upload_word', methods=['POST'])
def upload_word_file():
    # 检查是否有文件被上传
    if 'file' not in request.files:
        return jsonify({'success': '0', 'message': 'No file part', 'file_name': ''})

    file = request.files['file']

    # 如果用户没有选择文件，浏览器也会发送一个空的文件名
    if file.filename == '':
        return jsonify({'success': '0', 'message': 'No selected file', 'file_name': ''})

    # 检查文件类型是否允许
    if file and allowed_file(file.filename):
        # 保存文件到本地
        filename = os.path.join(app.config['UPLOAD_FOLDER'] + 'word', generate_unique_string() + '.docx')
        file.save(filename)
        return jsonify(
            {'success': '1', 'message': 'File successfully uploaded', 'file_name': generate_unique_string() + '.docx'})

    return jsonify({'success': '0', 'message': 'File type not allowed', 'file_name': ''})


@app.route('/upload_excel', methods=['POST'])
def upload_excel_file():
    if 'file' not in request.files:
        return jsonify({'success': '0', 'message': 'No file part', 'file_name': ''}), 200

    file = request.files['file']

    # 如果用户没有选择文件，浏览器也会发送一个空的文件名
    if file.filename == '':
        return jsonify({'success': '0', 'message': 'No selected file', 'file_name': ''}), 200

    # 检查文件类型是否允许
    if file and allowed_file(file.filename):
        # 保存文件到本地
        filename = os.path.join(app.config['UPLOAD_FOLDER'] + 'excel', generate_unique_string() + '.xlsx')
        file.save(filename)
        return jsonify(
            {'success': '1', 'message': 'File successfully uploaded',
             'file_name': generate_unique_string() + '.xlsx'}), 200

    return jsonify({'success': '0', 'message': 'File type not allowed', 'file_name': ''}), 200


@app.route('/upload_task_info', methods=['POST'])
def upload_task_info():
    try:
        # 获取 JSON 数据
        data = request.get_json()

        # 提取必要的信息
        user_id = str(data.get('user_id'))
        word_file_name = data.get('word_file_name')
        excel_file_name = data.get('excel_file_name')
        passwd = data.get('passwd')
        # 进行一些简单的错误检查
        if user_id is None or word_file_name is None or excel_file_name is None:
            return jsonify({'success': '0',
                            'message': 'user_id is None or word_file_name is None or excel_file_name is None',
                            'task_id': ''}), 200

        task_id = manager.add_task(user_id, passwd)
        manager.set_excel_word_file(user_id, word_file_name, excel_file_name)

        # 返回任务 ID
        return jsonify({'success': '1', 'message': 'success', 'task_id': str(task_id)}), 200

    except Exception as e:
        return jsonify({'success': '0', 'message': str(e), 'task_id': ''}), 200


@app.route('/task_start', methods=['POST'])
def task_start():
    try:
        # 获取 JSON 数据
        data = request.get_json()

        # 提取必要的信息
        task_id = data.get('task_id')
        passwd = data.get('passwd')
        # 进行一些简单的错误检查
        if task_id is None or passwd is None:
            return jsonify({'success': '0', 'massage': 'error miss id or passwd'}), 200

        if manager.task_start(task_id, passwd):
            return jsonify({'success': '1', 'massage': 'success'}), 200
        else:
            return jsonify({'success': '0', 'massage': 'id or passwd wrong'}), 200

    except Exception as e:
        return jsonify({'success': '0', 'massage': 'error' + str(e)}), 200


@app.route('/get_task_info', methods=['POST'])
def get_task_info():
    try:
        # 获取 JSON 数据
        data = request.get_json()

        # 提取必要的信息
        task_id = data.get('task_id')
        passwd = data.get('passwd')
        print("task_id rec is : " + task_id)
        print("passwd rec is : " + passwd)
        # 进行一些简单的错误检查
        if task_id is None or passwd is None or task_id == "" or passwd == "":
            return jsonify({'success': '0', 'massage': 'error miss id or passwd', 'status': '', 'percent': '',
                            'status_info': ''}), 200

        success, task_status, task_status_info, task_over_percent = manager.get_task_info(task_id, passwd)

        if success:
            return jsonify(
                {'success': '1', 'massage': 'success', 'status': task_status, 'percent': str(task_over_percent),
                 'status_info': task_status_info}), 200
        else:
            return jsonify({'success': '0', 'massage': 'id or passwd wrong', 'status': '', 'percent': '',
                            'status_info': ''}), 200

    except Exception as e:
        return jsonify({'success': '0', 'massage': 'error' + str(e), 'status': '', 'percent': '',
                        'status_info': ''}), 200


@app.route('/get_download_info', methods=['POST'])
def get_download_info():
    try:
        # 获取 JSON 数据
        data = request.get_json()

        # 提取必要的信息
        task_id = data.get('task_id')
        passwd = data.get('passwd')
        # 进行一些简单的错误检查
        if task_id is None or passwd is None:
            return jsonify(
                {'success': '0', 'massage': 'error miss id or passwd', 'task_should_pay': '', 'preview_href': '',
                 'zip_href': ''}), 200

        success, task_should_pay, preview_href, zip_href = manager.get_download_info(task_id, passwd)

        if success:
            return jsonify(
                {'success': '1', 'massage': 'success', 'task_should_pay': task_should_pay, 'preview_href': preview_href,
                 'zip_href': zip_href}), 200
        else:
            return jsonify(
                {'success': '0', 'massage': 'id or passwd wrong', 'task_should_pay': '', 'preview_href': '',
                 'zip_href': ''}), 200

    except Exception as e:
        return jsonify(
            {'success': '0', 'massage': 'error' + str(e), 'task_should_pay': '', 'preview_href': '',
             'zip_href': ''}), 200


@app.route('/trans_file')
def trans_file():
    # 获取路径参数
    path = request.args.get('path')

    # 获取文件的绝对路径
    abs_path = os.path.abspath(os.path.join(app.static_folder, path))
    # 发送文件
    return send_file(path)


if __name__ == '__main__':
    # 运行应用
    app.run(debug=True, host='0.0.0.0')
