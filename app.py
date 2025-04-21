from flask import Flask
from flask_cors import CORS

from config import DevConfig
from request import register_blueprints
import os


def create_app(config_name='dev'):
    app = Flask(__name__)
    DOWNLOAD_DIR = os.path.join(app.root_path, 'output')  # 存储下载文件的目录
    CORS(app)  # 默认允许所有来源（*）
    register_blueprints(app, DOWNLOAD_DIR)  # 注册蓝图和下载目录
    app.config.from_object(DevConfig)  # 加载配置

    return app


app = create_app()
