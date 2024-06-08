# 后端设计文档：用户相册管理系统

---

## 1. 简介

用户相册管理系统的后端负责处理用户上传图片的存储和管理。

该系统使用阿里云OSS进行图片存储，并使用SQL Server管理图片的元数据。

## 2. 技术栈

* **编程语言** : Python
* **云存储** : 阿里云OSS (Object Storage Service)
* **数据库** : SQL Server
* **库和框架** :
  * oss2 (与阿里云OSS交互)
  * pyodbc (与SQL Server交互)

## 3. 系统架构

### 3.1. 模块划分

* **文件上传模块** : 负责接收用户上传的图片，并将图片上传到阿里云OSS，同时将图片的元数据存储在SQL Server中。
* **文件管理模块** : 负责生成图片的访问链接，并提供图片的删除和更新功能。
* **数据库管理模块** : 负责与SQL Server进行交互，管理图片的元数据。

### 3.2. 数据库设计

数据库中包含两个主要表：

1. **Users** : 存储用户信息

   * Id: INT, PRIMARY KEY, AUTO_INCREMENT
   * UserName: NVARCHAR(255)
   * Password: NVARCHAR(255)
2. **PhotoAlbums** : 存储图片元数据

   * Id: INT, PRIMARY KEY, AUTO_INCREMENT
   * UserId: INT, FOREIGN KEY REFERENCES Users(Id)
   * FileName: NVARCHAR(255)
   * FilePath: NVARCHAR(255)
   * UploadTime: DATETIME, DEFAULT GETDATE()

## 4. 部署

1. **环境准备** :

   * 配置好阿里云OSS。
   * 配置好SQL Server并创建相应的数据库和表。
   * 配置Python运行环境并安装所需库。
2. **部署代码** :

   * 将后端代码部署到服务器上。
   * 确保服务器可以访问阿里云OSS和SQL Server。

## 5. 函数说明

函数：`upload_file`

将用户上传的本地文件上传到阿里云OSS，并将文件的元数据保存到SQL Server数据库中。

* `user_id` (int): 用户的唯一标识符。
* `local_file_path` (str): 本地文件路径。

示例：

```python
user_id = 1
local_file_path = 'path/to/your/file.jpg'
upload_file(user_id, local_file_path)
```

函数：`get_file_url`

从SQL Server数据库中获取指定文件的路径，并生成一个临时访问链接。

* `file_id` (int): 文件的唯一标识符。

返回值

* `url` (str): 生成的访问链接，如果文件不存在则返回None。

示例：

```python
file_id = 1
file_url = get_file_url(file_id)
if file_url:
    print(f'Access URL: {file_url}')
else:
    print('Failed to get access URL')
```
