# sdn project 1
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import CPULimitedHost
from mininet.link import TCLink 

class LinearTopo(Topo):
	
	def __init__(self,k=4,**opts):
		
		super(LinearTopo,self).__init__(**opts)
		self.k=k

		hosts = [self.addHost('h%s'%i,ip='10.0.0.%s'%i) for i in irange(1,k)]
		switches = [self.addSwitch('s%s'%i) for i in irange(1,k)]
		for i in irange(0,3):
			self.addLink(hosts[i],switches[i])
		for i in irange(0,2):
			self.addLink(switches[i],switches[i+1])
		"""
		hosts = [self.addHost('h%s'%i) for i in irange(1,k) ]
		e_switches = [self.addSwitch('e%s'%i) for i in irange(1,k/2)]
		a_switches = [self.addSwitch('a%s'%i) for i in irange(1,k/4)]
		c_switch = self.addSwitch('c1')
		
		for i in irange(0,k/2-1):
			self.addLink(hosts[2*i], e_switches[i])
			self.addLink(hosts[2*i+1], e_switches[i])
 
		for i in irange(0,k/4-1):
			self.addLink(e_switches[2*i], a_switches[i])
			self.addLink(e_switches[2*i+1], a_switches[i])
			
		self.addLink(a_switches[0], c_switch)
		self.addLink(a_switches[1], c_switch)
		"""

def perfTest():
	"Create network and run simple performance test"
	topo=LinearTopo(k=8)
	net=Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
	net.start()
	print "Dumpling host connections"
	dumpNodeConnections(net.hosts)
	print "Testing network connectivity"
	net.pingAll()
	print "Testing bandwidth between h1 and h4"
	h1, h4=net.get('h1', 'h4')
	net.iperf((h1, h4))
	net.stop()

def simpleTest():
	"Create and test a simple network"
	topo=LinearTopo(k=4)
	net=Mininet(topo)
	net.start()
	print "Dumping network connectivity"
	dumpNodeConnections(net.hosts)
	print "Testing network connectivity"
	net.pingAll()
	net.stop()

topos = {'mytopo': (lambda: LinearTopo() )}
