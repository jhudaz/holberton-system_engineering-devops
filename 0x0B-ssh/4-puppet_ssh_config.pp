#config ssh using puppet
include stdlib
file_line { 'private keyphers':
ensure => present,
path   => '/etc/ssh/sshd_config',
line   => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'refuse authenticate using a password':
ensure => present,
path   => '/etc/ssh/sshd_config',
line   => 'PasswordAuthentication no',
}
