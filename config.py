import os


class DevConfig:
    # 基础配置
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False  # 生产环境关闭SQL日志
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB_URI',
                                        'mysql+pymysql://root:root@localhost/dev_db?charset=utf8mb4')
