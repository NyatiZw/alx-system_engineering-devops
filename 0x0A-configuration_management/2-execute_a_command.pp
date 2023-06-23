# Manifest to kill a process named killmenow

exec { 'killmenow_process':
  command  => 'pkill killmenow',
  onlyif   => 'pgrep killmenow',
}
