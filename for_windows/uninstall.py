import os
import time
instsrv_q = os.popen('sc query aliyun_webdav')
instsrv_qs = ""
for i in instsrv_q.readlines():
    instsrv_qs += i
if "RUNNING" in instsrv_qs:
    os.system('sc stop aliyun_webdav')
    time.sleep(3)
    os.system('sc delete aliyun_webdav')
    instsrv_q = os.popen('sc query aliyun_webdav')
    instsrv_qs = ""
    for i in instsrv_q.readlines():
        instsrv_qs += i
    if "1060" in instsrv_qs:
        print("aliyun_webdav服务删除成功")
elif "1060" in instsrv_qs:
    print("aliyun_webdav服务未安装")

input("回车以退出")