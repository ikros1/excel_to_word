## 接口数据结构，交换数据模式 `post`，数据结构 `json` 

### /upload_word

#### 接受格式docx 
#### `/back_json`
###{str success, str message, str file_name}

### /upload_excel 

#### 接受格式xlsx
#### `/back_json`
###{str success, str message, str file_name}

### /upload_task_info

#### send_json { str user_id, str passwd, str word_file_name, str excel_file_name} 

#### back_json { str success, str massage ,str task_id } 

### /task_start 

#### send_json { str user_id, str task_id ,str passwd}
#### back_json { str success, str massage}

### /get_task_info 

#### send_json { str task_id ,str passwd} 

#### back_json {str success,str massage,str status,str percent,str status_info}

### /get_down_info 

#### send_json { str task_id ,str passwd} 

#### back_json { str success,str massage, str task_download_url,str task_should_pay, str preview_file_url}


###公网服务器面板信息
####面板地址:
http://47.98.212.203:8888/a70c8a9d
####用户名:
ig1jejd3
####密码:
0ad55753000