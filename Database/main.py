import oss2
import pyodbc

# 阿里云OSS配置
access_key_id = 'yourAccessKeyId'
access_key_secret = 'yourAccessKeySecret'
bucket_name = 'yourBucketName'
endpoint = 'http://oss-cn-hangzhou.aliyuncs.com'

# 初始化OSS客户端
auth = oss2.Auth(access_key_id, access_key_secret)
bucket = oss2.Bucket(auth, endpoint, bucket_name)

# SQL Server配置
server = 'your_sql_server'
database = 'your_database'
username = 'your_username'
password = 'your_password'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# 连接数据库
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

def upload_file(user_id, local_file_path):
    try:
        # 生成OSS文件路径
        file_name = local_file_path.split('/')[-1]
        oss_file_path = f'photos/{user_id}/{file_name}'
        
        # 上传文件到OSS
        with open(local_file_path, 'rb') as fileobj:
            bucket.put_object(oss_file_path, fileobj)
        
        # 插入文件元数据到数据库
        cursor.execute("""
            INSERT INTO PhotoAlbums (UserId, FileName, FilePath)
            VALUES (?, ?, ?)
        """, user_id, file_name, oss_file_path)
        conn.commit()
        
        print(f'File uploaded to OSS and metadata saved in SQL Server: {oss_file_path}')
    except Exception as e:
        print(f'Error occurred: {e}')

def get_file_url(file_id):
    try:
        # 从数据库获取文件路径
        cursor.execute("SELECT FilePath FROM PhotoAlbums WHERE Id = ?", file_id)
        row = cursor.fetchone()
        
        if row:
            oss_file_path = row[0]
            # 生成文件访问链接
            url = bucket.sign_url('GET', oss_file_path, 60*60)  # 生成一个1小时有效的访问链接
            return url
        else:
            print('File not found')
            return None
    except Exception as e:
        print(f'Error occurred: {e}')
        return None

# 示例使用
user_id = 1
local_file_path = 'path/to/your/file.jpg'
upload_file(user_id, local_file_path)

file_id = 1
file_url = get_file_url(file_id)
if file_url:
    print(f'Access URL: {file_url}')
else:
    print('Failed to get access URL')
