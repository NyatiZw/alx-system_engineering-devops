# Manifest to kill a process named killmenow

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/usr/bin/bash',
  logoutput   => true,
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}
