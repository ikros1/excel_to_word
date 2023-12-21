from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 指定上传文件保存的目录
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 允许上传的文件类型
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx', 'xlsx'}

# 检查文件类型是否允许
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 定义上传文件的路由
@app.route('/upload_word', methods=['POST'])
def upload_word_file():
    # 检查是否有文件被上传
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # 如果用户没有选择文件，浏览器也会发送一个空的文件名
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # 检查文件类型是否允许
    if file and allowed_file(file.filename):
        # 保存文件到本地
        filename = os.path.join(app.config['UPLOAD_FOLDER']+'word', file.filename)
        file.save(filename)
        return jsonify({'message': 'File successfully uploaded'})

    return jsonify({'error': 'File type not allowed'})

@app.route('/upload_excel', methods=['POST'])
def upload_excel_file():
    # 检查是否有文件被上传
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    # 如果用户没有选择文件，浏览器也会发送一个空的文件名
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # 检查文件类型是否允许
    if file and allowed_file(file.filename):
        # 保存文件到本地
        filename = os.path.join(app.config['UPLOAD_FOLDER']+'excel', file.filename)
        file.save(filename)
        return jsonify({'message': 'File successfully uploaded'})

    return jsonify({'error': 'File type not allowed'})

if __name__ == '__main__':
    # 运行应用在本地服务器
    app.run(debug=True)
