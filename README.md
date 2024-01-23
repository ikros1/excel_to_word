## 接口数据结构，交换数据模式 `post`，数据结构 `json` 
## 接口调用样式的具体方法参考文件夹中templates/html/home.html文件，已经测试通过
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

#### send_json {str task_id ,str passwd}
#### back_json { str success, str massage}

### /get_task_info 

#### send_json { str task_id ,str passwd} 

#### back_json {str success,str massage,str status,str percent,str status_info}

### /get_down_info 

#### send_json { str task_id ,str passwd} 

#### back_json { str success,str massage, str task_should_pay,str preview_href, str zip_href}

####接口调用顺序和细则
#####首先先提交必要的excel和word文件并获取接口返回的文件名，并自行拟定用户名和密码调用任务提交接口，接收任务id后便可以提交任务开始接口和任务信息查询接口，
#####当任务进度到达100%后便可以调用下载信息查询接口，下载预览文件和结果压缩文件用a标签访问
###公网服务器面板信息
####面板地址:
http://47.98.212.203:8888/a70c8a9d
####用户名:
ig1jejd3
####密码:
0ad557530