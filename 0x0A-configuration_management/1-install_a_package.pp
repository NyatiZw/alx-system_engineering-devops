# Puppet manifest to install a package flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec {'install_flask':
  command => 'pip3 install flask',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => 'pip3 show flask | grep Version | grep -q 2.1.0',
}
