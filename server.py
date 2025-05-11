from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return open('index.html').read()

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # 调用你的 C++ 程序处理文件
    output_path = os.path.join(RESULT_FOLDER, f"processed_{filename}")
    subprocess.run(["./your_cpp_program", filepath, output_path])

    return jsonify({"filename": f"processed_{filename}"})

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(RESULT_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    # Render 要求监听 0.0.0.0 和动态端口
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
