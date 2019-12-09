file {'create_a_file':
content =>'I love Puppet',
path    =>'/tmp/holberton',
mode    =>'0744',
owner   =>'www-data',
group   =>'www-data'
}
