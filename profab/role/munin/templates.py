"""Functions for generating Munin configuration files
"""
from cStringIO import StringIO


APACHE_CONFIG = """
<VirtualHost *:80>
    DocumentRoot /var/cache/munin/www
</VirtualHost>
"""

MUNIN_CONFIG = """includedir /etc/munin/munin-conf.d
"""

MUNIN_NODE_CONFIG = """log_level 4
log_file /var/log/munin/munin-node.log
pid_file /var/run/munin/munin-node.pid

background 1
setsid 1

user root
group root

host_name localhost.localdomain
allow ^127\.0\.0\.1$
host *
port 4949
"""

MUNIN_SERVER_CONFIG = """[ec2-server.example.com]
127.0.0.1
"""
