'''
Bloom Filter Code in python
Author: Tushar Makkar <tusharmakkar08[at]gmail.com>
'''

from bitarray import bitarray
import mmh3, datetime
 
class BloomFilter:
    
    def __init__(self, size, hash_count):
        '''
        Initializing the bloom filter
        INPUT
        size : size of bitarray
        hash_count : Number of times to run the function
        '''
        self.size = size
        self.hash_count = hash_count
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        
    def add(self, string):
        '''
        Adding string to bloom filter
        INPUT 
        string : Input string
        '''
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            self.bit_array[result] = 1
            
    def lookup(self, string):
        '''
        Checking up string from bloom filter
        INPUT 
        string : Input string
        '''
        for seed in xrange(self.hash_count):
            result = mmh3.hash(string, seed) % self.size
            if self.bit_array[result] == 0:
                return "Nope"
        return "Probably"


if __name__ == "__main__":
    '''
    Main function where everything is called
    '''
    bf = BloomFilter(500000, 7)
    huge = []
 
lines = open("harrypotter.txt").read().splitlines()
for line in lines:
    bf.add(line)
    huge.append(line)
    
start = datetime.datetime.now()
print bf.lookup("CHAPTER")
finish = datetime.datetime.now()
print (finish-start).microseconds
 
start = datetime.datetime.now()
for word in huge:
    if word == "harry":
        break
finish = datetime.datetime.now()
print (finish-start).microseconds
 
 
print bf.lookup("Max")
print bf.lookup("mice")
print bf.lookup("3")
 
 
start = datetime.datetime.now()
bf.lookup("apple")
finish = datetime.datetime.now()
print (finish-start).microseconds
 
 
start = datetime.datetime.now()
for word in huge:
    if word == "apple":
        break
finish = datetime.datetime.now()
print (finish-start).microseconds
