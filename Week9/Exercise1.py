# Exercise 1 week9
from twisted.internet import protocol, reactor

#Echo client class
class EchoClient(protocol.Protocol):

    def connectionMade(self):

        # Send message to server 'Hello World'
        self.transport.write("Hello World")

    def dataReceived(self, data):

        print 'server replied:', data
        self.transport.loseConnection() # Stop the client

# EchoFactory Class
class EchoFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print 'Connection Failed. \n'
        print reason
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'Connection lost'
        reactor.stop()

print "Connecting to Echo Server"
reactor.connectTCP("192.168.26.10", 7, EchoFactory())
reactor.run()
