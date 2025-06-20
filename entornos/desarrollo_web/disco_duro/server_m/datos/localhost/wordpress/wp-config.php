<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'prueba' );

/** Database username */
define( 'DB_USER', 'root' );

/** Database password */
define( 'DB_PASSWORD', 'rootpass' );

/** Database hostname */
define( 'DB_HOST', '10.33.3.200' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         '{=)Ut+RV,+_8$ALc<-p]f8a#er+f}^A$ULnbg*!+*#K*ZC#z9=ims%qk19-H%tr#' );
define( 'SECURE_AUTH_KEY',  'w_[#;Xb~KJ6R2V1Zpcq%qW9_wilee}q4:Q.H#-U,E[1BZM7cAlw<4r=7e3hu%0#.' );
define( 'LOGGED_IN_KEY',    'Ymd%Jz%bs.Ve)w50|oAVoegZ:mP(=0Hk.FG*J>sSwAj3U,n9$;*.dRQ+R[n}gh|$' );
define( 'NONCE_KEY',        '44t{V<&MUHzCrF6tfDnVhPFG2Y}o.r)DCuU#Ui xe6@`Iwf/>@s36UUZa(BiaA|a' );
define( 'AUTH_SALT',        '(q|}={@xO:DG:r,7no8MI:k@vQb9WNVX_Mrw$~ >L.kUE][!2lfB2=()X.c{`?R-' );
define( 'SECURE_AUTH_SALT', 'b!wn(*cY>]Oi`.AMn6N>o{]p4W*##YwAhU9Vmvs~;)YV_|/spZN@r,/%wb^_8>Ib' );
define( 'LOGGED_IN_SALT',   'd^95SV0XOTRN]ru[eSK&YZHGSwS-ngVCYfRrn*/+0x@|>%,$PR@+CHqW+j0stcKW' );
define( 'NONCE_SALT',       '`VQE.1S8b5PiC&E{ f~MQQ>)>6o+B@*96yGU-b#me`;,do4qbcd/kRV^NS >@@6U' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', false );

/* Add any custom values between this line and the "stop editing" line. */



/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
