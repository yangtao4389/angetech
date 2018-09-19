### 正式使用说明
#### 1.conf_docker文件夹里的内容应该与manage.py 同级 
> `mv -f conf_docker/* . `
#### 2.创建docker image
> 如果已经创建过，记得删除： `rm -rf uwsgi_docker.sock`
> `docker build -t angetech:1.0 . `
#### 3.修改uwsgi.ini
> 写上相对路径：module= angetech.wsgi:application
> 测试需要将  py-autoreload=1 注释
#### 4.修改supervisor-app.conf
> 写上该模块名： command= celery -A angetech worker --loglevel=INFO 
#### 5.创建docker container
* 端口映射  -p 8001:80  
* 容器名称 --name dev_reports  
* 项目文件目录 -v  path_to_your_project_code:/home/code/app  
* 容器nginx日志：/var/log/nginx/  
* session,cache 数据
* rabbitmq数据
> `docker run -d -p 8601:80  --name dev_angetech --restart=always -v /home/code/dev/angetech:/home/code/app -v /home/logs/dev/angetech/docker:/home/logs -v /home/session/dev/angetech/docker:/home/session -v /home/cache/dev/angetech/docker:/home/cache -v /home/logs/dev/angetech/docker/rabbitmq:/data/rabbitmq/mnesia angetech:1.0  `开发
> `docker run -d -p 8600:80 --name online_angetech --restart=always -v /home/code/online/angetech:/home/code/app -v /home/logs/online/angetech/docker:/home/logs -v /home/session/online/angetech/docker:/home/session -v /home/cache/online/angetech/docker:/home/cache  -v /home/logs/dev/angetech/docker/rabbitmq:/data/rabbitmq/mnesia angetech:1.0  `正式
    

### 容器操作 
以下的6c33d849a971为容器id
* 进入终端页面  
>`docker exec -it 969fb21c364e /bin/bash`
* 查看supervisorctl 状态
> `docker exec -it 969fb21c364e supervisorctl status`
* 重启supervisor
> `docker exec -it 969fb21c364e supervisorctl reload`
* 重启uwsgi
> `docker exec -it 969fb21c364e supervisorctl restart app-uwsgi`
* 重启nginx
> `docker exec -it 969fb21c364e supervisorctl restart nginx-app`
* 当有些启动不起来，比方rabbitmq，可以先ps 关闭进程，然后再用supervisorctl 重启

### 参考链接
* https://github.com/yangtao4389/django-uwsgi-nginx



 




