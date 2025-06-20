# Usa Debian como base
FROM debian:latest

# Actualiza el sistema y agrega algunas herramientas básicas
RUN apt-get update && \
    apt-get install -y vim nano && \
    apt-get install -y bind9 bind9utils bind9-doc && \
    apt-get install -y apache2 apache2-utils \
    php php-cli php-mysql php-mbstring php-xml php-bcmath php-gd php-curl php-zip  && \
    apt-get install -y php-sqlite3 && \
    apt install -y default-mysql-client && \	
    apt-get install -y supervisor && \
    apt-get install -y curl php-cli php-mbstring unzip git && \

    apt-get clean

# Instalar composer globalmente
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php && \
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \
    rm composer-setup.php

# Crear la carpetas del sitio web y permisos
RUN mkdir /home/web
RUN mkdir /home/web/public_html
RUN chmod 777 /home/web
RUN chmod 777 /home/web/public_html

#Para habilitar http y https
COPY a_http.sh a_http.sh
COPY a_https.sh a_https.sh
RUN chmod o+x a_http.sh
RUN chmod o+x a_https.sh

# Copiar los archivos de configuración del certificado para https
COPY codec.key /etc/ssl/private/codec.key
COPY codec.crt /etc/ssl/certs/codec.crt
# Copia tu configuración de supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Crea el punto de montaje del volumen (opcional, para referencia dentro del contenedor)
VOLUME /datos

# Puertos DNS
EXPOSE 53/tcp 53/udp

# Arranca supervisord (que gestionará BIND9)
CMD ["/usr/bin/supervisord", "-n"]
