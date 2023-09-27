ustom 404 error page
# Redirecting traffic using nginx
# update
# Install nginx
# listen to port 80
# allow nginx on firewall
# update nginx index page
# restart Nginx

sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'
echo "Hello World!" | sudo tee /var/www/html/index.html
echo "Ceci n'est pas une page" | sudo tee /var/www/html/404.html
echo "server {
   listen 80 default_server;
   listen [::]:80 default_server;

   root /var/www/html;
   index index.html;
   location /redirect_me {
      return 301 https://github.com/devbojack;
   }
   error_page 404 /404.html;
   location = /404.html{
      internal;
   }
}" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
