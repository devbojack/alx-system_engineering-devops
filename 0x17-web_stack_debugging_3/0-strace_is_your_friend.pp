
service { 'apache2':
  ensure => 'running',
}

file { '/etc/apache2/sites-available/your-site.conf':
  ensure  => present,
  content => template('your-site-config.erb'),
  notify  => Service['apache2'],
}

file { '/etc/apache2/sites-available/your-site-config.erb':
  ensure  => present,
  content => template('your-site-config.erb'),
  notify  => Service['apache2'],
}
