# Exercise 2 week9
from twisted.internet import protocol, reactor

class GuessClient(protocol.Protocol):

    def dataReceived(self, data):

        print data

        if 'Game over' in data:
            self.transport.loseConnection()
        else:
            message = raw_input('Enter quess here: \n')
            self.transport.write(message)

class GuestFactory(protocol.ClientFactory):

    def buildProtocol(self, addr):
        return GuessClient()

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed'
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print 'Y\n'
        print 'Yo\n'
        print 'You\n'
        print 'You a\n'
        print 'You ar\n'
        print 'You are\n'
        print 'You are a\n'
        print 'You are am\n'
        print 'You are ama\n'
        print 'You are amaz\n'
        print 'You are amazi\n'
        print 'You are amazin\n'
        print 'You are amazing\n'

        print 'Game Over\n'
        reactor.stop()

print 'Connecting to server'
reactor.connectTCP("192.168.26.10", 4444, GuestFactory())
reactor.run()