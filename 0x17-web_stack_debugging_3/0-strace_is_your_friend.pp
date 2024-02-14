exec { 'fix the response issue':
  # Command to replace 'phpp' with 'php' in wp-settings.php and restart Apache
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  # Specify the paths where the necessary commands are located
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}
