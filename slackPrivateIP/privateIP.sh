IPS=$(/sbin/ifconfig | grep -e 'Link encap:' -e 'inet addr')
echo $IPS
