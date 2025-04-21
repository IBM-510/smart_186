from datetime import datetime
from flask import jsonify  # 用于生成JSON响应
from flask import request  # 用于获取请求参数
from template_render import render_template  # 用于渲染Word模板
from flask import send_from_directory


def register_blueprints(app, download_dir):
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': '请求参数错误'}), 400

    @app.route('/api/download/<filename>', methods=['GET'])
    def download_file(filename):
        return send_from_directory(
            directory=download_dir,
            path=filename,
            as_attachment=True  # 强制浏览器弹出下载框[4,5](@ref)
        )

    @app.route('/api/chat', methods=['POST'])
    def chat():
        # 验证请求头格式
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        # 获取请求体
        data = request.get_json()
        message = data.get('message')
        context = {
            "部门名称": message
        }
        render_template("./template_doc/1、嘉善公司信息设备入网申请单.docx", context, "./output/1.docx")
        return jsonify({"status": "ok",
                        "timestamp": datetime.now().isoformat(),
                        "content": "hello world",
                        "filename": "1.docx"})
