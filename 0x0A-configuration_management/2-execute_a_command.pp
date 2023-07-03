# Manifest to kill a process named killmenow

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/usr/bin',
  onlyif      => 'pgrep killmenow',
  provider    => 'shell',
  logoutput   => true,
  refreshonly => true,
}
