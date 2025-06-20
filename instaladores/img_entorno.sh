cd "../$(dirname "$0")"
cd entornos/desarrollo_web

docker build server/ -t server

cd database

docker build mysql/ -t mysql
docker build phpmyadmin
echo "Completado"