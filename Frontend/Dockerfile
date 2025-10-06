# Frontend/Dockerfile
FROM node:20

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы package.json и package-lock.json из поддиректории vue-taro/
COPY vue-taro/package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь код фронтенда из поддиректории vue-taro/
COPY vue-taro/ .

# Собираем приложение для продакшена
RUN npm run build

# Устанавливаем сервер для раздачи статики
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html

# Создаем конфигурацию Nginx прямо в образе
RUN echo 'server { \
    listen 80; \
    server_name localhost; \
    location / { \
        root /usr/share/nginx/html; \
        try_files $uri $uri/ /index.html; \
    } \
    location /api/ { \
        proxy_pass http://backend:8000; \
        proxy_set_header Host $host; \
        proxy_set_header X-Real-IP $remote_addr; \
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; \
    } \
}' > /etc/nginx/conf.d/default.conf

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]