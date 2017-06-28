def FNVHash(key):
    fnv_prime = 0x811C9DC5
    hash = 0
    for i in range(len(key)):
      hash *= fnv_prime
      hash ^= ord(key[i])
    return hash

def APHash(key):
    hash = 0xAAAAAAAA
    for i in range(len(key)):
      if ((i & 1) == 0):
        hash ^= ((hash <<  7) ^ ord(key[i]) * (hash >> 3))
      else:
        hash ^= (~((hash << 11) + ord(key[i]) ^ (hash >> 5)))
    return hash


class BloomFilter(object):
    def __init__(self, connection, bitvector_key, n, k):


        self.connection = connection
        self.bitvector_key = bitvector_key
        self.n = n
        self.k = k


    def __contains__(self, key):
        pipeline = self.connection.pipeline()
        for hashed_offset in self.calculate_offsets(key):
            pipeline.getbit(self.bitvector_key, hashed_offset)
        results = pipeline.execute()
        #print "zjk"
        #print all(results)
        return all(results)

    def add(self, key, set_value=1, transaction=False, timeout=None):

        pipeline = self.connection.pipeline(transaction=transaction)
        for hashed_offset in self.calculate_offsets(key):
            pipeline.setbit(self.bitvector_key, hashed_offset, set_value)
        # print "xhn"
        # print pipeline.getbit(self.bitvector_key, hashed_offset)
        # if timeout is not None:
        #     pipeline.expire(self.bitvector_key, timeout)

        pipeline.execute()

    def delete(self, key):

        self.add(key, set_value=0, transaction=True)

    def calculate_offsets(self, key):

        hash_1 = FNVHash(key)
        hash_2 = APHash(key)

        for i in range(self.k):
            yield (hash_1 + i * hash_2) % self.n
