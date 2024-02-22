# Increases the limit for open files for the holberton user.

exec { 'increase-file-limit-for-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Reload the system configuration to apply the changes.
exec { 'reload-system-configuration':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
