import os, hashlib, random, time
from datetime import datetime

# hashlib.sha256('Nobody inspects the spam'.encode('utf-8')).hexdigest()

class Block:

    def __init__(self, record):
        self.timestamp = datetime.now()
        self.record = record
        self.prev_blk_id = ''
        self.blk_id = ''

    def view(self):
        print ('Timestamp: '+str(self.timestamp)+'\n'+
        'Record:    '+self.record +'\n'+
        'Prev Hash: '+self.prev_blk_id +'\n'+
        'This Hash: '+self.blk_id)
        
class Chain:

    def __init__(self):
        self.currBlk_id = 'genesisBlk'
        #for query only
        self.query = []    
        
    def addBlock(self, record):
        blk = Block(record)
        blk.blk_id = hashlib.sha256((str(record)+
                                     str(blk.timestamp))
                                    .encode('utf-8')).hexdigest()
        blk.prev_blk_id = self.currBlk_id

        self.currBlk_id = blk.blk_id
        self.query.append(blk)

    def view(self):
        for i in range(len(self.query)):
            self.query[i].view()
            print('\n')

    def shuffle(self):
        size = len(self.query)
        output = []
        for i in range(size):
            randIndex = random.randint(0,len(self.query)-1)
            output.append(self.query[randIndex])
            self.query.remove(self.query[randIndex])
        self.query = output

    

    
#####################################################################################################


class Member:
    
    def __init__(self):
        pass

    def contrib(self, record, chain):
        chain.addBlock(record)
        

    def mine(self):
        while solved == False:
	h = hashlib.sha256((str(random.randint(1,1000))+'fingers crossed').encode('utf-8')).hexdigest()
	print(h)
	if(h[0:2]=='00'):
		solved = True
	else:
		pass


class Network:
    
    def __init__(self, #members?
                 ):
        print('under construction')
    

#####################################################################################################


chain1 = Chain()
chain1.addBlock('this is first block')
time.sleep(random.randint(1,3))
chain1.addBlock('this is second block')
time.sleep(random.randint(1,3))
chain1.addBlock('this is third block')

burgerChain = Chain()

patrick = Member()
gary = Member()
bob = Member()

patrick.contrib('Patrick ate one burger.',burgerChain)
time.sleep(random.randint(1,5))
gary.contrib('Gary ate three burgers.',burgerChain)
time.sleep(random.randint(1,5))
bob.contrib("Bob doesn't eat burgers. He ate none.",burgerChain)
time.sleep(random.randint(1,5))
patrick.contrib('Patrick ate one more burger.',burgerChain)

burgerChain.view()
