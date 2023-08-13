#Puppet manifest to ammend server
file { '/var/www/html/index.html':
  ensure => file,
  mode => '0644',
  owner => 'www-data',
  group => 'www-data',
}
