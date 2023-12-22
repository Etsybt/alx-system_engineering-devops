#installs flask from pip3

package { 'flask':
  ensure   => '2.0.3',
  provider => 'pip3',
}
