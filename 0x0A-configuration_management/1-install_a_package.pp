#Install flask from pip3 using puppet

exec { 'install_flask':
  command     => '/usr/bin/pip3 install -y flask==2.1.0',
  path        => ['/usr/bin'],
  refreshonly => true,
  require     => Package['python3-pip'],
}

package { 'flask':
  ensure => 'installed',
  before => Exec['install-flask']
}
