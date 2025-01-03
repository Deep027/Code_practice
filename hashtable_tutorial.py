# Initializing a Dictionary 

stock_prices = {"march 6": 310.0, "march 7": 340.0, "march 8": 380.0, "march 9": 302.0, 
                "march 10": 297.0, "march 11": 323.0}
#print(stock_prices)

## Hashtable basic definition
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] # list comprehension

    def get_hash(self, key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __setitem__(self, key, val):  #index operator built in function to enable [] access to dictionaries
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):  #index operator built in function to enable [] access to dictionaries
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

obj_1_of_Hashtable_class = HashTable()
obj_2_of_Hashtable_class = HashTable()
# obj_3_of_Hashtable_class = HashTable()

print(obj_1_of_Hashtable_class.get_hash('march 16'))

obj_1_of_Hashtable_class.add('march 12', 450.0)
print(obj_1_of_Hashtable_class.arr)
obj_1_of_Hashtable_class.add('march 13', 150.0)
print(obj_1_of_Hashtable_class.arr)
obj_1_of_Hashtable_class.add('march 14', 350.0)
print(obj_1_of_Hashtable_class.arr)

del obj_1_of_Hashtable_class['march 14']
print(obj_1_of_Hashtable_class.arr)

# after enabling get items and set items 
obj_2_of_Hashtable_class['march 12'] = 230
obj_2_of_Hashtable_class['march 14'] = 220 
print(obj_2_of_Hashtable_class.arr)

print(obj_2_of_Hashtable_class['march 12'])

print(obj_1_of_Hashtable_class.get('march 13'))
