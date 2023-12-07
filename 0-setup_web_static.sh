#!/usr/bin/env bash
#script to install, configure nginx and create some dir

sudo apt-get -y update
sudo apt-get -y upgrade
if ! command -v nginx &> /dev/null; then
    sudo apt-get -y install nginx
fi
ufw allow 'nginx HTTP'
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
sudo ln -s -f /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
def_file=/etc/nginx/sites-enabled/default
serve_page="location /hbnb_static {\n\t alias /data/web_static/current/;\n\t}"
sudo sed -i "24i $serve_page" $def_file
service nginx restart
