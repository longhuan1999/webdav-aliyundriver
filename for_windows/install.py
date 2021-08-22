import os
import winreg
import time
from config import get_parameters, get_java

JavaPath = get_java()
if JavaPath["use_system"] == "true":
    systemJava = os.popen('java -version')
    systemJavaString = ""
    for i in systemJava.readlines():
        systemJavaString += i
    if "不是" in systemJavaString or "not" in systemJavaString:
        print("\njava未安装或未设置环境变量！")
        input("回车以退出")
        exit(1)
    else:
        Application = "java"
elif JavaPath["use_system"] == "false":
    if ":" not in JavaPath["jre_path"]:
        Application = os.getcwd() + "\\" + JavaPath["jre_path"] + "\\bin\java.exe"
    elif ":" in  JavaPath["jre_path"]:
        Application = JavaPath["jre_path"] + "\\bin\java.exe"

AppDirectory = os.getcwd()
webdav = os.getcwd() + "\webdav.jar"
AppParameters_D = get_parameters()
#print(AppParameters_D)
if AppParameters_D["aliyundrive_refresh_token"] == "你的refreshToken":
    print("\n请根据config.ini注释获取refreshToken")
    input("回车以退出")
    exit(1)
AppParameters = '-jar %s --aliyundrive.refresh-token="%s"'%(webdav,AppParameters_D["aliyundrive_refresh_token"])
if "server_port" in AppParameters_D.keys():
    AppParameters += ' --server.port='+AppParameters_D["server_port"]
if "aliyundrive_auth_enable" in AppParameters_D.keys():
    AppParameters += ' --aliyundrive.auth.enable='+AppParameters_D["aliyundrive_auth_enable"]
if "aliyundrive_auth_user_name" in AppParameters_D.keys():
    AppParameters += ' --aliyundrive.auth.user-name='+AppParameters_D["aliyundrive_auth_user_name"]
if "aliyundrive_auth_password" in AppParameters_D.keys():
    AppParameters += ' --aliyundrive.auth.password='+AppParameters_D["aliyundrive_auth_password"]


if os.path.isfile("C:\\Windows\\System32\\srvany.exe") is False:
    os.system('copy "instsrv+srvany\\srvany.exe" C:\\Windows\\System32\\')
if os.path.isfile("C:\\Windows\\System32\\instsrv.exe") is False:
    os.system('copy "instsrv+srvany\\instsrv.exe" C:\\Windows\\System32\\')
instsrv_q = os.popen('sc query aliyun_webdav')
instsrv_qs = ""
for i in instsrv_q.readlines():
    instsrv_qs += i
if "RUNNING" in instsrv_qs:
    os.system('sc stop aliyun_webdav')
    time.sleep(3)
#print(instsrv_qs)
if "1060" in instsrv_qs:
    os.system('instsrv aliyun_webdav C:\\Windows\\System32\\srvany.exe')

key = winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\\ControlSet001\Services\\aliyun_webdav",0,winreg.KEY_ALL_ACCESS)
newkey = winreg.CreateKey(key,r'Parameters')
key1 = winreg.OpenKeyEx(key,r"Parameters",0,winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(key1,"AppDirectory",0,winreg.REG_SZ,AppDirectory)
winreg.SetValueEx(key1,"Application",0,winreg.REG_SZ,Application)
winreg.SetValueEx(key1,"AppParameters",0,winreg.REG_SZ,AppParameters)

winreg.CloseKey(key1)
winreg.CloseKey(key)

os.system('sc description aliyun_webdav "阿里云盘的webdav协议服务，可在 %s\\config.ini 中修改配置，然后再次安装即可"'%(os.getcwd()))
os.system('sc start aliyun_webdav')
time.sleep(3)
instsrv_q = os.popen('sc query aliyun_webdav')
instsrv_qs = ""
for i in instsrv_q.readlines():
    instsrv_qs += i
if "RUNNING" in instsrv_qs:
    print("aliyun_webdav服务启动成功，详情请查看日志")
else:
    print("aliyun_webdav服务启动失败，详情请查看日志")

input("回车以退出")