# 使用官方的 Python 镜像作为基础镜像
FROM python:3.12.5-alpine

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 运行 Django 管理命令以收集静态文件
RUN python manage.py collectstatic --noinput

# 暴露端口
EXPOSE 8000

# 运行 Django 应用
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "hqcmdb.wsgi:application"]
