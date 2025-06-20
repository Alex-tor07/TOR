cd /etc/apache2/sites-available
a2dissite www.https.conf
a2ensite www.http.conf
service apache2 restart
