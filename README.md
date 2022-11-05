# django_demo
简单的diango 网站demo，

引用了一些网络上的前端模版
## 环境
python3.9,django 3.2  
ps:python3.7.0 实测无效  
## 快速运行：
### win： 
- 激活虚拟环境  
virtualvenv venv   
．/venv/script/acivate  
- 安装依赖  
pip install -r requirements.txt  
- 首次运行，需要移植表和数据库  
python manage.py makemigrations  
python manage.py migrate [app name]  
- 运行服务器  
python manage.py runserver 0.0.0.0:8000  
- 打开浏览器，  
输入http://127.0.0.1:8000/ 就可以访问网站

## 测试信息：
- 管理员：admin ， admin  
 


