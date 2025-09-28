#!/bin/bash

echo "!!!!!!!!!!!!!!!!!!!!Updating system!!!!!!!!!!!!!!!!!!!!"
sudo apt-get update -y

echo "####################Installing apache2####################"
sudo apt-get install apache2 -y

echo "Removing default Apache page..."
sudo rm -rf /var/www/html/index.html

echo "Checking Apache status..."
sudo service apache2 status

echo "Restarting Apache service..."
sudo service apache2 restart

echo "Apache installation and configuration complete."

echo "!!!!!!!!!!!!!!!!!!!!Installing PHP!!!!!!!!!!!!!!!!!!!!"
sudo apt-get install php libapache2-mod-php php-mysql -y

echo "Checking Apache status..."
sudo service apache2 status

echo "Restarting Apache service to enable PHP module..."
sudo service apache2 restart

echo "PHP installation complete."
