from configparser import *
import os

# 读取ini文件
def read_cf():
    if os.path.isfile("config.ini") is False:
        print("\n配置文件config.ini不存在，请根据config.ini.example创建！")
        input("回车以退出")
        exit(1)
    cf = RawConfigParser()
    cf.read("config.ini", encoding="utf8")
    return cf


# 获取参数配置
def get_parameters():
    cf = read_cf()
    return_D = {}
    try:
        aliyundrive_refresh_token = cf.get("main", "aliyundrive_refresh_token").strip('"')
        return_D["aliyundrive_refresh_token"] = aliyundrive_refresh_token
    except NoSectionError:
        print("\n[main]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\naliyundrive_refresh_token不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    try: 
        server_port = cf.get("main", "server_port").strip('"')
        return_D["server_port"] = server_port
    except NoOptionError:
        pass
    try: 
        aliyundrive_auth_enable = cf.get("main", "aliyundrive_auth_enable").strip('"')
        return_D["aliyundrive_auth_enable"] = aliyundrive_auth_enable
    except NoOptionError:
        pass
    try: 
        aliyundrive_auth_user_name = cf.get("main", "aliyundrive_auth_user_name").strip('"')
        return_D["aliyundrive_auth_user_name"] = aliyundrive_auth_user_name
    except NoOptionError:
        pass
    try: 
        aliyundrive_auth_password = cf.get("main", "aliyundrive_auth_password").strip('"')
        return_D["aliyundrive_auth_password"] = aliyundrive_auth_password
    except NoOptionError:
        pass
    return return_D


    # 获取java配置
def get_java():
    cf = read_cf()
    return_D = {}
    try:
        use_system = cf.get("java", "use_system").strip('"')
        return_D["use_system"] = use_system
    except NoSectionError:
        print("\n[java]不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    except NoOptionError:
        print("\nuse_system不存在，请检查config.ini文件")
        input("回车以退出")
        exit(1)
    try: 
        jre_path = cf.get("java", "jre_path").strip('"')
        return_D["jre_path"] = jre_path
    except NoOptionError:
        if use_system == "false":
            print("\njre_path不存在，请检查config.ini文件")
            input("回车以退出")
            exit(1)
    return return_D