### 运行 `main.py` 即可 遇到替换失败的标识字段，请删除该字段并切换中文输入法将整个字段全部打出，然后按回车输入即可。如果仍然不成功，请联系管理员。 

## 接口数据结构，交换数据模式 `post`，数据结构 `json` 

### `/login`

 #### `send_json` ```json {    "user_email": "str",    "user_password": "str",    "hold_online": true }

### `/back_json`

### { bool login_success, user_info:[str user_name,str user_image_url, int user_id] }

### /upload_word

#### 接受格式docx 

### /upload_excel 

#### 接受格式xlsx

### /upload_task_info

#### send_json { int user_id, task_file_name:[str word_file_name,str excel_file_name] } 

#### back_json { int task_id } 

### /task_start 

#### send_json { int user_id, int task_id }

### /get_task_info 

#### send_json { int task_id } 

#### back_json { bool task_over, int task_done_percent }

### /get_down_info 

#### send_json { int task_id } 

#### back_json { str download_url, int should_pay_money } 

### /get_preview_file 

#### send_json { int task_id }

### /download_file 

#### send_json { str download_url }