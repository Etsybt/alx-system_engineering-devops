# Install Python 3.8.10
package { 'python3.8':
  ensure => '3.8.10',
}

# Install pip for Python 3.8
package { 'python3-pip':
  ensure => installed,
  require => Package['python3.8'],
}

# Install Flask 2.1.0 using pip
exec { 'install_flask':
  command => '/usr/bin/python3.8 -m pip install --force-reinstall Flask==2.1.0',
  require => Package['python3-pip'],
}

# Install Werkzeug 2.1.1 using pip
exec { 'install_werkzeug':
  command => '/usr/bin/python3.8 -m pip install --force-reinstall Werkzeug==2.1.1',
  require => Package['python3-pip'],
}

