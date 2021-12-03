FROM openresty/openresty:latest

COPY ./compose/nginx/nginx.conf /etc/openresty/nginx.conf
COPY ./compose/nginx/foxavia.conf /etc/nginx/conf.d/foxavia.conf

ENV TZ=Europe/Moscow