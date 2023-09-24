#Install flask from pip3 using puppet

exec { 'install_flask':
  ensure      => 'installed',
  command     => '/usr/bin/pip3 install flask==2.1.0',
  require     => Package['python3-pip'],
  refreshonly => true,
}
