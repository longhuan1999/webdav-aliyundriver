说明：[1.1.0版本](https://github.com/zxbu/webdav-aliyundriver/releases/tag/v1.1.0)支持阿里Teambition网盘的webdav协议，后续的2.x版本仅支持阿里云盘，不再维护Teambition网盘版本
# webdav-aliyundriver
本项目实现了阿里云盘的webdav协议，只需要简单的配置一下，就可以让阿里云盘变身为webdav协议的文件服务器。
基于此，你可以把阿里云盘挂载为Windows、Linux、Mac系统的磁盘，可以通过NAS系统做文件管理或文件同步，更多玩法等你挖掘


# 如何使用
支持refreshToken登录方式，具体看参数说明
## Jar包运行
[点击下载Jar包](https://github.com/zxbu/webdav-aliyundriver/releases/latest)
> 建议自己下载源码编译，以获得最新代码
```bash
java -jar webdav.jar --aliyundrive.refresh-token="your refreshToken"
```
## 容器运行
```bash
docker run -d --name=webdav-aliyundriver --restart=always -p 8080:8080  -v /etc/localtime:/etc/localtime -v /etc/aliyun-driver/:/etc/aliyun-driver/ -e TZ="Asia/Shanghai" -e ALIYUNDRIVE_REFRESH_TOKEN="your refreshToken" -e ALIYUNDRIVE_AUTH_PASSWORD="admin" -e JAVA_OPTS="-Xmx1g" zx5253/webdav-aliyundriver

# /etc/aliyun-driver/ 挂载卷自动维护了最新的refreshToken，建议挂载
# ALIYUNDRIVE_AUTH_PASSWORD 是admin账户的密码，建议修改
# JAVA_OPTS 可修改最大内存占用，比如 -e JAVA_OPTS="-Xmx512m" 表示最大内存限制为512m
```
## Windows服务运行
[点击下载Windows服务版安装包](https://github.com/longhuan1999/webdav-aliyundriver/releases)

将 webdav-aliyundriver 安装成 Windows服务，实现开机自启、后台运行。


# 参数说明
```bash
--aliyundrive.refresh-token
    阿里云盘的refreshToken，获取方式见下文
--server.port
    非必填，服务器端口号，默认为8080
--aliyundrive.auth.enable=true
    是否开启WebDav账户验证，默认开启
--aliyundrive.auth.user-name=admin
    WebDav账户，默认admin
--aliyundrive.auth.password=admin
    WebDav密码，默认admin

```
# QQ群
> 群号（已满）：789738128

> 二群群号：979024890

# 新手教程
## 群晖
TODO

## Windows10
TODO

## Linux
TODO

## Mac
TODO

# 客户端兼容性
| 客户端 | 下载 | 上传 | 备注 |
| :-----| ----: | :----: | :----: |
| 群辉Cloud Sync | 可用 | 可用 | 使用单向同步非常稳定 | 
| Rclone | 可用 | 可用 | 推荐，支持各个系统 |
| Mac原生 | 可用 | 可用 | | 
| Windows原生 | 可用 | 有点小问题 | 不建议，适配有点问题，上传报错 |
| RaiDrive | 可用 | 可用 | Windows平台下建议用这个 |


# 浏览器获取refreshToken方式
1. 先通过浏览器（建议chrome）打开阿里云盘官网并登录：https://www.aliyundrive.com/drive/
2. 登录成功后，按F12打开开发者工具，点击Application，点击Local Storage，点击 Local Storage下的 [https://www.aliyundrive.com/](https://www.aliyundrive.com/)，点击右边的token，此时可以看到里面的数据，其中就有refresh_token，把其值复制出来即可。（格式为小写字母和数字，不要复制双引号。例子：ca6bf2175d73as2188efg81f87e55f11）
3. 第二步有点繁琐，大家结合下面的截图就看懂了
 ![image](https://user-images.githubusercontent.com/32785355/119246278-e6760880-bbb2-11eb-877c-aca16cf75d89.png)

# 功能说明
## 支持的功能
1. 查看文件夹、查看文件
2. 文件移动目录
3. 文件重命名
4. 文件下载
5. 文件删除
6. 文件上传（支持大文件自动分批上传）
7. 支持超大文件上传（官方限制30G）
8. 支持WebDav权限校验（默认账户密码：admin/admin）
9. 文件下载断点续传
10. Webdav下的流媒体播放等功能
## 暂不支持的功能
1. 移动文件到其他目录的同时，修改文件名。比如 /a.zip 移动到 /b/a1.zip，是不支持的
2. 文件上传断点续传
3. 部分客户端兼容性不好
## 已知问题
1. 没有做文件sha1校验，不保证上传文件的100%准确性（一般场景下，是没问题的）
2. 通过文件名和文件大小判断是否重复。也就是说如果一个文件即使发生了更新，但其大小没有任何改变，是不会自动上传的
3. 不支持文件名包含 `/` 字符  

## TODO
1. 支持更多登录方式（验证码、账号密码等）


# 免责声明
1. 本软件为免费开源项目，无任何形式的盈利行为。
2. 本软件服务于阿里云盘，旨在让阿里云盘功能更强大。如有侵权，请与我联系，会及时处理。
3. 本软件皆调用官方接口实现，无任何“Hack”行为，无破坏官方接口行为。
5. 本软件仅做流量转发，不拦截、存储、篡改任何用户数据。
6. 严禁使用本软件进行盈利、损坏官方、散落任何违法信息等行为。
7. 本软件不作任何稳定性的承诺，如因使用本软件导致的文件丢失、文件破坏等意外情况，均与本软件无关。
