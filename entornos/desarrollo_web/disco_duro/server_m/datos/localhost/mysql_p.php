<?php
$host = '10.33.3.200';         // El nombre del servicio MySQL en docker-compose
$user = 'root';          // Usuario MySQL
$password = 'rootpass';      // Contraseña MySQL
$database = 'prueba';      // Nombre de la base de datos (ajusta según tu config)

$conn = new mysqli($host, $user, $password, $database);

// Verificar conexión
if ($conn->connect_error) {
    die("Conexión fallida: " . $conn->connect_error);
}
echo "✅ Conexión exitosa a la base de datos.";

$conn->close();


?>

