#!/usr/bin/python2
import  cgi
import  cgitb
cgitb.enable()
import  commands
print  "Content-type:text/html"
print   ""

web_data=cgi.FieldStorage()
#  extracting  os name from html file 
os_name=web_data.getvalue('os')
os_ram=web_data.getvalue('or')
os_cpu=web_data.getvalue('oc')
os_hdd=web_data.getvalue('oh')

#  print all data
os_launch="sudo  virt-install   --cdrom  /kali.iso  --ram  "+os_ram+"   --vcpu  "+os_cpu+"    --nodisk   --name  "+os_name 

print  commands.getoutput(os_launch)










