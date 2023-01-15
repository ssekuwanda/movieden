# SOCKET
sudo nano /etc/systemd/system/gunicorn.socket
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target


# SERVICE
sudo nano /etc/systemd/system/gunicorn.service

[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=doug
Group=www-data
WorkingDirectory=/home/doug/Documents/moviestore/movieden
ExecStart=//home/doug/Documents/moviestore/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          MoviesBack.wsgi:application

[Install]
WantedBy=multi-user.target

# RUN GUNICORN
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket

# Sites Available
sudo nano /etc/nginx/sites-available/moviestore
server {
    listen 80;
    server_name 192.168.0.2;

    location = /favicon.ico { access_log off; log_not_found off; }

    location /static/ {
        root /home/doug/Documents/moviestore/movieden;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

sudo ln -s /etc/nginx/sites-available/moviestore /etc/nginx/sites-enabled

sudo systemctl daemon-reload
sudo systemctl restart gunicorn

# GET ALL THE ERROR LOGS
sudo tail -F /var/log/nginx/error.log


# MAX SIZE NGINX
server {
    client_max_body_size 10000000M;
}