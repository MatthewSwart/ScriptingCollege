#Question 4 week 10 exercise
from twisted.internet import protocol, reactor

#Echo class
class AuctionServer(protocol.Protocol):
    def __init__(self,factory):
        self.factory = factory

    def connectionMade(self):
        '''
        Connection made. Prompt the client to add bid.
        :return:
        '''
        if self.factory.highest_bid > 0:
            self.transport.write('Highest bid so far: '+
                                  str(self.factory.highest_bid) + '\nEnter your bid please: ')
        else:
            self.transport.write(' No bids have been entered yet. \n enter your bid now: ')

    def dataReceived(self, data):
        '''
        Check if the bid made is the new highest other wise prompt the client to
        make new bid
        :param data: Data received from the client.
        :return:
        '''
        bid = int(data) #Data received from the clients
        print 'Clients bid received: ', bid
        if bid > self.factory.highest_bid: #checking for new highest bid
            self.factory.highest_bid = bid #If it is new highest bid then write that to bid
            self.factory.write('You are the new highest bidder.')
        else:
            self.factory.write('Too low try again sucker.')

class AuctionFactory(protocol.Factory):
    def __init__(self):
        self.highest_bid = 0

    def buildProtocol(self, addr):
        return AuctionServer(self)

if __name__ == '__main__':
    print 'Auction server is up and running'
    reactor.listenTCP(8888, AuctionFactory())
    reactor.run()

