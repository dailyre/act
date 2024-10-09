# 使用官方的 Ubuntu 镜像作为基础镜像
FROM python:slim

# 设置工作目录
WORKDIR /app

COPY . /app

# 生成requirements.txt文件
# pip freeze > requirements.txt
# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# # 暴露端口（如果有需要）
# EXPOSE 8080

# 运行 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]


# docker run -it --rm -p 8000:8000 -v D:\code\vs_python\act:/app python