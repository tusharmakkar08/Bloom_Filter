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

def timeCheckLookup(string, bloomFilter, normalList):
    '''
    Compares times between normal list and bloom filter
    INPUT 
    string : input string
    bloomFilter : Bloom Filter data structure
    normalList : Array Data structure
    '''
    print "The word which we are searching for is ", string
    start = datetime.datetime.now()
    print bloomFilter.lookup(string)
    finish = datetime.datetime.now()
    print "Using bloom filter time is",(finish-start).microseconds
    
    start = datetime.datetime.now()
    for word in normalList:
        if word == string:
            break
    finish = datetime.datetime.now()
    print "Using Normal list time is", (finish-start).microseconds


if __name__ == "__main__":
    '''
    Main function where everything is called
    '''
    bloomFilter = BloomFilter(500000, 7)
    normalList = []
    with open('harrypotter.txt','r') as f:
        for line in f: 
            for word in line.split():
                bloomFilter.add(word)
                normalList.append(word)
    timeCheckLookup("CHAPTER", bloomFilter, normalList)
    timeCheckLookup("CHAPTERRRR", bloomFilter, normalList)
    timeCheckLookup("lightning", bloomFilter, normalList)
