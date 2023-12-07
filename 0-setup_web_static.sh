#!/usr/bin/env bash
#script to install, configure nginx and create some dir

if ! command -v nginx &> /dev/null; then
    apt-get -y update
    apt-get -y install nginx
    apt ufw allow 'nginx HTTP'
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/current
echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>" >  /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default
service nginx restart
