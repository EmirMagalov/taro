FROM node:20 AS build
WORKDIR /app
COPY vue-taro/package*.json ./
RUN npm install
COPY vue-taro/ .
RUN npm run build

## Стадия сервера
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
COPY flexado /etc/nginx/conf.d/flexado.conf

EXPOSE 80
