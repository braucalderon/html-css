# simulation.py

from random import random, randrange
from CheckerSim import CheckerSim
from MyQueue import Queue

class Customer:
    """ represents a customer
       arrivalTime: when the customer is ready to pay for the items (gets in line)
       itemCount: number of items in the basket
    """

    def __init__(self, arrivalTime, itemCount):
        self.arrivalTime = int(arrivalTime)
        self.itemCount = int(itemCount)

    def __repr__(self):
        return ("Customer(arrivalTime=%d, itemCount=%d)" %
                (self.arrivalTime, self.itemCount))


def genTestData(filename, totalTicks, maxItems, arrivalInterval):
    """
    generates test data
    totalTicks: length of time over which the simulation is run
                example: 2 hours -> 2*60*60 = 7200 ticks
    maxItems: maximum number of items per customer
    arrivalInterval: average number of ticks between the arrivals
                     example: 3 minutes = 3*60 = 180 ticks
    """
    outfile = open(filename, "w")
    # step through the ticks
    for t in range(1,totalTicks):            
        if random() < 1./arrivalInterval: #gives us a 1 in arrivalInterval ticks
            # chance to get a new customer.
            # A customer arrives with a random number of items
            items = randrange(1, maxItems+1)
            outfile.write("%d %d\n" % (t, items))
    outfile.close()

def createArrivalQueue(fname):
    q = Queue()
    infile = open(fname)
    for line in infile:
        time, items = line.split()
        q.enqueue(Customer(time,items))
    infile.close()
    return q

def main():
    genTestData("checkerData.txt", 2*60*60, 50, 180) # 2 hours, 50 items, 3 minutes
    q = createArrivalQueue("checkerData.txt")
    sim = CheckerSim(q, 3)
    sim.run()
    print("Average wait time is:",sim.averageWait())
    print("Maximum wait time is:",sim.maximumWait())
    print("Maximum line length is:",sim.maximumLineLength())

if __name__ == '__main__':
    main()
