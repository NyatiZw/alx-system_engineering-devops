# This manifest creates a file named 'school' in the '/tmp' directory
# with permissions and content


file { '/tmp/school':
  ensure  => present,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
