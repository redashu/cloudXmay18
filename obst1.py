#!/usr/bin/python2

import  cgi
import  commands
print "Content-type:text/html"
print ""

#  taking date from apache and storing into web variable 
web=cgi.FieldStorage()

#  drive name 
drive_name=web.getvalue('dn')
#  drive size in MB 
drive_size=web.getvalue('ds')

#  checking for  name  of storage 
st_name=commands.getoutput('ls /var/www/html/storage')
#  split on behlaf of \n
check=st_name.split('\n')
if  drive_name in check:
	print  "<h1>"
	print  "Drive name already exits try new one"
	print  "</h1>"
	print   "<a href='http://192.168.10.167/index.html'>"
	print   "CLick here to Go "
	print  "</a>"


else :

#  create dynamic store 
	print  commands.getoutput('sudo  lvcreate --name  '+drive_name+' --size '+drive_size+'M  vgnew')
# now formatting  partition 
	print  commands.getoutput('sudo  mkfs.xfs   /dev/vgnew/'+drive_name)
# creating mounting point for web access
	print  commands.getoutput('sudo mkdir  /var/www/html/storage/'+drive_name)

#  mounting  
	print   commands.getoutput('sudo mount  /dev/vgnew/'+drive_name+'  /var/www/html/storage/'+drive_name)


