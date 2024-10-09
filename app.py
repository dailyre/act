from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # 获取请求体
    data = request.json
    print("Webhook received:", data)
    
    # 返回响应
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    # 启动服务器，监听在 5000 端口
    app.run(port=5000, debug=True, host='0.0.0.0')