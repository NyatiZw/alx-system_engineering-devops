# Manifest to kill a process named killmenow

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}
