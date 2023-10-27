FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf

RUN mkdir -p /staticfiles
RUN chmod 755 /staticfiles

COPY nginx.conf /etc/nginx/conf.d

EXPOSE 80
