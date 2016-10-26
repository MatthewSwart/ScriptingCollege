#First twisted application for project
from twisted.internet import protocol, reactor

class EchoClient(protocol.Protocol):
	def connectionMade(self):
		self.transport.write("Hello world!")

	def dataReceived(self, data):
		print "Server said:", data
		self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
	def buildProtocol(self, addr):
		return EchoClient()

	def clientConnectionFailed(self, connector, reason):
		print "Connection Failed !"
		reactor.stop()

reactor.connectTCP("localhost", 8002, EchoFactory())
reactor.run()

