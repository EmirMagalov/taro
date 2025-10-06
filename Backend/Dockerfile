# Backend/Dockerfile
FROM python:3.10.9

# Обновляем pip
RUN pip install --upgrade pip

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt и устанавливаем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY taroproject/ .

# Проверяем структуру директорий
RUN ls -la /app/

# Открываем порт
EXPOSE 8000

# Запускаем приложение
CMD ["gunicorn", "taroproject.wsgi:application", "-b", "0.0.0.0:8000"]