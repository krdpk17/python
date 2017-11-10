#!/usr/bin/env python
import pexpect


def connect_ssh(ip,login,passwd):
	# ssh command line
	p=pexpect.spawn('ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ' + login + '@' + ip)
	print p
	i = p.expect ([pexpect.TIMEOUT, pexpect.EOF, 'yes/no', 'assword:', '>'])
	print i
	if i==0:
	    print "Timeout"
	    return None
	if i==1:
	    print "Error"
	    return None
	elif i==2:
	    print "Need password"
	    p.sendline('yes')
	    p.sendline(passwd)
	    p.expect('#')
	elif i==3:
	    print "I give password",
	    p.sendline(passwd)
	    p.expect('#')
	print p.before # print out the result
	return p

#test here
connect_ssh('10.102.53.248', 'root', 'linux')
