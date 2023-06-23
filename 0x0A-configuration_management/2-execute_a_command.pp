# Manifest to kill a process named killmenow

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  path        => '/usr/bin:/usr/sbin:/bin:sbin',
  logoutput   => true,
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}
