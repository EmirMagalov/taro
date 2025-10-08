# Сборка Vue
FROM node:20 AS build
WORKDIR /app

# Копируем package.json и package-lock.json
COPY Frontend/vue-taro/package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем все исходники
COPY Frontend/vue-taro/ .

# Собираем проект
RUN npm run build

# Сервер Nginx
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80
