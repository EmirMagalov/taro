FROM node:20 AS build
WORKDIR /app
COPY vue-taro/package*.json ./
RUN npm install
COPY vue-taro/ .
RUN npm run build

## Стадия сервера
FROM nginx:alpine
COPY --from=0 /app/dist /usr/share/nginx/html
COPY nginx.conf //home/ubuntu/taro/nginx.conf

EXPOSE 80
