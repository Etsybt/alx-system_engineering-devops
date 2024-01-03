# Ensure Nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Define Nginx service to ensure it's running
service { 'nginx':
  ensure => running,
  enable => true,
}

# Configure Nginx to listen on port 80 and return "Hello World!" at the root
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      root /var/www/html;
      index index.html;

      location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
      }

      location / {
        try_files \$uri \$uri/ =404;
      }
    }
  ",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
