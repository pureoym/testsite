## 日志  
### 创建项目以及应用
```commandline
python -m django --verion
django-admin startproject cs_api
cd cs_api
python manage.py startapp api
```
### 启动系统
```commandline
python manage.py runserver 8087
```

### 配置URL

修改cs_api/api/views.py   
```python
from django.http import HttpResponse
import json


# Create your views here.
def index(request):
    return HttpResponse("Hello, ming!")


def test(request):
    d1 = {'sid': 1, 'title': 'my test title'}
    result = json.dumps(d1)
    return HttpResponse(result)

```
修改cs_api/api/urls.py  
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
]
```
修改cs_api/cs_api/urls.py
```python
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('api/',include('api.urls')),
    path('admin/', admin.site.urls),
]
```
测试接口  
http://localhost:8087/api/test

### 连接数据库
在/testsite/setting.py中，做如下修改
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'ai',
        'PASSWORD': 'ai_123',
        'HOST': '10.10.192.61',
        'PORT': '3306',
    }
}
```
在项目文件夹下的__init__.py中，做如下修改
```python
import pymysql
pymysql.install_as_MySQLdb()
```

### 创建模型
在cs_api/api/models.py中，增加  
```python
from django.db import models

class Story(models.Model):
    sid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    person = models.ForeignKey(to="Person", to_field="pid", on_delete=None)
    pub_time = models.DateTimeField()

    def __str__(self):
        return self.title


class Person(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
```
创建后执行命令  
```commandline
python manage.py makemigrations app
python manage.py sqlmigrate app 0001
python manage.py migrate
```


### 创建用户

