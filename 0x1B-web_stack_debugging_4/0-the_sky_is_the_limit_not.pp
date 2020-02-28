#fix apache bench

exec { "fix":
  command => '/bin/echo ULIMIT="-n 32768" | sudo tee /etc/default/nginx',
  command => 'service nginx restart'
}

