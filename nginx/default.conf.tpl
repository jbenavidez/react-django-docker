server {
    listen ${LISTEN_PORT};

   
     location / {
    root /var/www/react;
  }
    location /api/{
        uwsgi_pass              backend:${APP_PORT};
        include                 /etc/nginx/uwsgi_params;
        client_max_body_size    10m;

    }
}