#!/usr/bin/python2

import  cgi,commands,os
print "Content-type:text/html"
print ""
#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()

#  drive name 
drive_name=web.getvalue('dn')
#  drive size in MB 
drive_size=web.getvalue('ds')

#  creating  thin LVM  partition 
#lvcreate  --name  part1  -V3000M  --thin  cld/pooL1 

commands.getoutput('lvcreate  --name  '+drive_name+'  -V'+drive_size+'M   --thin  cld/pooL1')

#  now formating the Partion 
commands.getoutput('mkfs.xfs    /dev/cld/'+drive_name )

#  mount storage  on server side first  
commands.getouput('mkdir   /var/www/html/'+drive_name)
# now mounting 
commands.getoutput('mount  /dev/cld/'+drive_name+'       /var/www/html/'+drive_name)











