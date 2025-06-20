cd /etc/apache2/sites-available
a2dissite www.http.conf
a2ensite www.https.conf
a2enmod ssl
service apache2 restart
