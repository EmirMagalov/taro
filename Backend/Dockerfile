# Backend/Dockerfile
FROM python:3.12

WORKDIR /app

COPY Backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY Backend/taroproject /app/taroproject
COPY Backend/taroapp /app/taroapp

CMD ["gunicorn", "taroproject.wsgi:application", "--bind", "0.0.0.0:8000"]
