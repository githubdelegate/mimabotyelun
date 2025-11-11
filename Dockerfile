# 使用一个轻量级的Python基础镜像，就跟选个小巧的煎饼模具似的
FROM python:3.10-slim

# 设置工作目录，相当于在厨房里划个专区
WORKDIR /app

# 先复制依赖文件，安装包，就跟先备好调料避免乱锅
COPY requirements.txt .

# 安装依赖，带点加速，就跟快速炒菜不糊锅
RUN pip install --no-cache-dir -r requirements.txt

# 复制所有代码进去，项目就齐活了
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]