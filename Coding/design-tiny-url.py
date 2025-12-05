# no correct approach here, however a hashmap to store is required
# in this algorithm, random url map is created from a pool
# pool = abcdefghijklmnopqrstuvwxyz1234567890

class Codec:
    def __init__(self):
        #Explaination 
        self.url_map = {}                                               # dictionary 
        self.pool = string.ascii_lowercase + string.digits              # pool = abcdefghijklmnopqrstuvwxyz1234567890
        self.random_chars = random.choices(self.pool, k = 5)            # random.choices will chose length(k) = 5 string which will be different every time and return in array
        self.random_string = ''.join(self.random_chars)                 # random_string is the len 5 string that we can store to url_map
    
    def encode(self, longUrl: str) -> str:
        
        shortUrl = self.random_string                                   
        self.url_map[shortUrl] = longUrl                                # Insert in shorturl as key and value = longURL 
        return "http://tinyurl.com/" + shortUrl                         
    

    def decode(self, shortUrl: str) -> str:

        shortUrl = shortUrl.split('/')[-1]                              # spliting at 1st occurance of '/' from right to left
        return self.url_map[shortUrl]
        