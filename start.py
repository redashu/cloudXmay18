#!/usr/bin/python2
import time
print  " :  Welcome to AdHoc Networks Cloud : "
print  "######################################"
print  "###                                 ##"
print  "###                                 ##"
print  "##                                  ##"
print  "######################################"
time.sleep(0.9)
c_user=raw_input("enter cloud credentials :  ")
c_password=raw_input("enter cloud Password :  ")

if  c_user ==  'root' and  c_password == '123' :

	print "PLZ wait CLoud Service is about to start "
	execfile('menu.py')

else :
	print  "Plz check your details !!!"




