# Puppet manifest to install a package flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec {'install flask':
  command => 'pip3 install flask',
  unless  => 'grep Version | grep -q 2.1.0',
}
