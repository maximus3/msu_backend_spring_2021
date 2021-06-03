sudo cp 000-default.conf /etc/nginx/sites-available/000-default.conf
sudo rm /etc/nginx/sites-enabled/000-default.conf
sudo rm /etc/nginx/sites-enabled/default.conf
sudo ln -s /etc/nginx/sites-available/000-default.conf /etc/nginx/sites-enabled/000-default.conf
