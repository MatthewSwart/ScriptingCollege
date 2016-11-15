# Exercise 1 b week9
from twisted.internet import protocol, reactor

#Echo client class
class EchoClient(protocol.Protocol):

    def connectionMade(self):

        # Send message to server that we type out
        message = raw_input('Type message here: \n')
        self.transport.write(message)

    def dataReceived(self, data):

        print 'server replied:', data

        message = raw_input('Type message here: \n')

        if message.lower() == 'quit':
            self.transport.loseConnection()  # Stop the client
        else:
            self.transport.write(message)

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
