#Puppet manifest to ammend server
file { '/var/www/html/index.html':
  ensure => file,
  mode   => '0644',
  owner  => 'www-data',
  group  => 'www-data',
}

file { '/var/www/html/Holberton':
  ensure  => file,
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
  content => '<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &rdqou; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &rdqou; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
<div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div> </div>
<h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
<p>Yet another bug by a HOlberton student</p>',
}
