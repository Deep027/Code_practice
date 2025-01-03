# Initializing a Dictionary 

stock_prices = {"march 6": 310.0, "march 7": 340.0, "march 8": 380.0, "march 9": 302.0, 
                "march 10": 297.0, "march 11": 323.0}
#print(stock_prices)

## Hashtable basic definition of seperate chaining : linked_list
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)] # list comprehension

    def get_hash(self, key):
        h=0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def add(self, key, val):
        h = self.get_hash(key)
        print(f'value of h is {h}')
        found = False
        for indx, element in enumerate(self.arr[h]):
            print("element in arr[h]: "+element[0])
            if (len(element) == 2) and (element[0] == key):
                self.arr[h][indx] = (key,val)
                found = True
                break 
        if (found == False):
            self.arr[h].append((key, val))
            print(f"successfully added {key} {val} at {h}")

    def get(self, key):
        h = self.get_hash(key)
        found = False
        for element in self.arr[h]:
            print("element in arr[h]: "+element[0])
            if (element[0] == key):
                found = True
                return element[1]
        if (found == False):
            return "element does not exist"

t = HashTable()
t.add('march 6', 310)
t.add('march 7', 240)
t.add('march 8', 231)
t.add('march 9', 212)
t.add('march 10', 342)
t.add('march 11', 530)
t.add('march 12', 654)
t.add('march 13', 632)
t.add('march 14', 753)
t.add('march 15', 124)
t.add('march 16', 153)
t.add('march 17', 753)
print(t.arr)
print(t.get('march 6'))
