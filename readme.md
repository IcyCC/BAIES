# Api

## Prefix

### /user

用户登陆有关

### /qualitative

定性数据

### /quantify

定量数据

## Model

* log.py 日志系统的表
* information.py 定性系统的表
* agriculture_products.py 定量系统农产品的表
* socioeconomic.py 定量系统社会经济的表
* user/\_\_init__.py 用户系统的表 以及权限

### 权限

```python


    QUANTIFY_R = 0x01 # 定量信息读
    QUANTIFY_W = 0x02 # 定量信息写

    QUALITATIVE_R = 0x04 # 定性信息读
    QUALITATIVE_W = 0x08 # 定性信息写

    USER_R = 0x10 # 用户信息读
    USER_W = 0x20 # 用户信息写

    SYSTEM_R = 0x40 # 系统信息读
    SYSTEM_W = 0X80 # 系统信息写


``` 

## CURD API 范式

### /{Prefix}/{表名}
eg: /user/Role

> 根据条件获得资源

* method: GET
* args: 
  * 任意数目表字段 进行AND查询 为空时,获取全部
  * page 查询第几页
* return: {
    status: "success" or "fail",
    reason: 成功时为空,失败见原因参考表,
    data:[] 请求的数据,永远为一个list,
    page: {'current':当前页数,
            'per_page':每页条数,
            'total':总计页数}
}

> 根据条件新增资源

* method: GET
* args: 
    *　数据表的字段ｋ-v　content-type: "application/x-www-form-urlencoded"
* return: {
    status: "success" or "fail",
    reason: 成功时为空,失败见原因参考表,
    data:[] 新增的对象
}

### /{Prefix}/{表名}/{id}
eg: /user/Role/２


> 获得id资源

* method: GET
* args: 
* return: {
    status: "success" or "fail",
    reason: 成功时为空,失败见原因参考表,
    data:[] 请求的数据,永远为一个list,
   
}

> 修改id资源

* method: PUT
* args: 数据表字段k-v
* return: {
    status: "success" or "fail",
    reason: 成功时为空,失败见原因参考表,
    data:[] 修改后的数据,永远为一个list,
}

> 删除id资源

* method: DELETE
* args: 数据表字段ｋ-ｖ
* return: {
    status: "success" or "fail",
    reason: 成功时为空,失败见原因参考表,
    data:[] 删除的数据,永远为一个list,
}

## 业务ａｐｉ

### 用户

#### /user/login

> 登陆一个用户

* method: POST
* args: username,password
* return: {
    status: "success" or "fail",
    reason: 成功时为空,失败见原因参考表,
    data:[] 删除的数据,永远为一个list,
}

#### /user/logout

> 登出一个用户

* method: GET
* args: 
* return: {
    status: "success" or "fail",
    reason: 成功时为空,失败见原因参考表,
    data:[] null
}


## reason list

### CURD

* "error args": GET方法时 数据表无此字段
* "error form args": POST方法时，数据表无此字段
* "no this id thing": 带id查询时无此id的数据条目
* ....　数据库写入失败会给出详细的异常

### User

* "no this user or password error": 没有此用户名或者密码错误
* "no permission": 权限不足


## Example

### 新增一个定量数据的性别分布

#### request

```

POST /quantify/SexDistributionProfiles HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache
Postman-Token: 0d8ec008-bbbc-8f55-8290-37e7b4e2ac52

men=23&women=23&country=zsh

```

#### response

```json

{
    "data": [
        {
            "country": null,
            "id": 1,
            "men": 123,
            "time": null,
            "women": 143
        }
    ],
    "reason": "",
    "status": "success"
}

```

### 查询国别为ｚｓｈ的性别分布数据

#### request

```
GET /quantify/SexDistributionProfiles?contry=zsh HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache
Postman-Token: cb68b664-1315-90f5-9f30-3dc0f2acc7e5

```

#### response

```json

{
    "data": [
        {
            "country": "zsh",
            "id": 2,
            "men": 123,
            "time": null,
            "women": 143
        }
    ],
    "page": {
        "current": 1,
        "per_page": 20,
        "total": 1
    },
    "reason": "",
    "status": "success"
}

```




### 修改此ｉｄ性别分布数据情况

```

PUT /quantify/SexDistributionProfiles/2 HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache
Postman-Token: 316fe0a6-8943-dc16-a218-2cb43fbbf59c

men=23&women=23&country=zsh

```

### 删除该ｉｄ的性别分布数据

```

DELETE /quantify/SexDistributionProfiles/2 HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/x-www-form-urlencoded
Cache-Control: no-cache
Postman-Token: 9e1431a6-a261-c5fd-b745-f69d09e34ff0

men=23&women=23&country=zsh

```

### 运维相关

> 管理员账号  密码账号　admin

#### 启动(开发环境)

```commandline

python BAIES.py runserver -h 0.0.0.0 -p 5000 

```
程序运行在5000 端口

#### 数据库表结构修改迁移

```commandline

python BAIES.py db migrate -m　"日志" 
python BAIES.py Upgrade

```

