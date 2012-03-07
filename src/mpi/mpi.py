from Scientific import MPI
import Numeric, sys

communicator = MPI.world.duplicate()

# Send and receive

if communicator.rank == 0:

    data = 1.*Numeric.arange(10)
    communicator.send(data, 1, 0)
    print "%d sent:\n%s" % (communicator.rank, str(data))

    data, source, tag = communicator.receiveString(1, None)
    print "%d received string from %d: %s" % (communicator.rank, source, data)

elif communicator.rank == 1:

    data, source, tag, count = \
          communicator.receive(Numeric.Float, None, None)
    print "%d received from %d:\n%s" \
          % (communicator.rank, source, str(data))

    communicator.send("Hello world", 0, 42)

else:

    print "%d idle" % communicator.rank
