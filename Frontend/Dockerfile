# Стадия сборки фронтенда
FROM node:20 AS build
WORKDIR /app
COPY vue-taro/package*.json ./
RUN npm install
COPY vue-taro/ .
RUN npm run build
RUN ls -la /app/dist # Проверка содержимого dist

# Стадия сервера
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY flexado /etc/nginx/conf.d/flexado.conf
RUN ls -la /usr/share/nginx/html # Проверка содержимого html
EXPOSE 80