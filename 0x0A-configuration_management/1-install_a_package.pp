# Puppet manifest to install a package flask from pip3

package { 'python3-pip':
  ensure   => '2.1.0',
  provider => 'flask',
}

exec {'install_flask':
  command => 'pip3 install flask',
}
