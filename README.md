一个用于从excel到word的批量快速规则填充软件
现在功能基本能用
## 1.使用方法
运行main.py即可
遇到替换失败的标识字段，请删除次字段并且切换中文输入法将整个字段全部打出后按回车输入即可，如果还不成功，联系管理员
###接口数据结构，交换数据模式post，数据结构json
###/login
####send_json
{
str user_email,
str user_password,
bool hold_online
}
####back_json

{
bool login_success,
user_info:[str user_name,str user_image_url, int user_id]
}

###/upload_word
####接受格式docx
###/upload_excel
####接受格式xlsx

###/upload_task_info
####send_json
{
int user_id,
task_file_name:[str word_file_name,str excel_file_name]
}
####back_json
{
int task_id
}
###/task_start
####send_json
{
int user_id,
int task_id
}

###/get_task_info
####send_json
{
int task_id
}
####back_json
{
bool task_over,
int task_done_percent
}

###/get_down_info
####send_json
{
int task_id
}
####back_json
{
str download_url,
int should_pay_money
}
###/get_preview_file
####send_json
{
int task_id
}

###/download_file
####send_json
{
str download_url
}