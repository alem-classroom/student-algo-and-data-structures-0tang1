class HashMap():
    def __init__(self):
        self.bucket_number = 10
        self.list = [None] * self.bucket_number
        # initialiize bucket_number equal to 1000
        # initialize list of bucket number size. Fill it with None

    def insert(self, key, value):
        # insert element to the hashmap, using system function hash
        hashed_data = hash(key) % self.bucket_number
        dict1 = [key, value]

        if self.list[hashed_data] is None:
            self.list[hashed_data] = list([hashed_data])
        else:
            self.list(hashed_data).append(dict1)

    def get_elem(self, key):
        # return element in the list with 'key' as key
        hashed_data = hash(key) % self.bucket_number
        return self.list[hashed_data]

    
    def get_list(self):
        # return list where you store elements
        return self.list


h = HashMap()
h.insert("1", 1)
h.insert("2", 2)
h.insert("3", 3)
print(h.get_list())
print(h.get_elem("1"))