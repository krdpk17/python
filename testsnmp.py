from pysnmp.entity.rfc3413.oneliner import cmdgen
from pysnmp.proto.rfc1902 import Integer, IpAddress, OctetString

def mysnmpwalk(ip,port,community,value):
	generator = cmdgen.CommandGenerator()
	comm_data = cmdgen.CommunityData('server', community, 1) # 1 means version SNMP v2c
	transport = cmdgen.UdpTransportTarget((ip, port))

	response_data = getattr(generator, 'nextCmd')
	res = (errorIndication, errorStatus, errorIndex, varBinds)\
	    = response_data(comm_data, transport, value)

	if not errorIndication is None  or errorStatus is True:
	       print "Error: %s %s %s %s" % res
	else:
	       print "%s" % varBinds
	return res

mysnmpwalk('172.17.0.4', 161, 'public', (1,3,6,1,4,1,5951,4,1,1))
