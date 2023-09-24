#Install flask from pip3 using puppet

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}

package { 'python3_pip':
  ensure => 'installed',
}

package { 'flask':
  ensure => 'installed',
  before => Exec['install-flask']
}
