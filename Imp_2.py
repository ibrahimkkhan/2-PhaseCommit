
class Imp:
    
    def __init__(self, StoreA, StoreB):
        self.store_A = StoreA
        self.store_B = StoreB

    def put(self, key, val):
        if(ord(key[0]) < 80):
            self.store_A[key] = val
            print("put call in Database A", key)
        else:
            self.store_B[key] = val
            print("put call in Database B", key)
        
        
    def get(self,key):
        if(ord(key[0]) < 80):
            try:
                rval = self.store_A[key]
                print(key, " was found")
            except:
                rval = "ABORT"
                print(key, " was not found")
        else:
            try:
                rval = self.store_B[key]            
            except:
                rval = "ABORT"
                print(key, " was not found")
        return rval
    
    def delete(self,key):
        if(ord(key[0]) < 80):
            print("delete call for ", key)
            try:
                self.store_A.pop(key)
            except:
                print(key, " was not found")
        else:
            print("delete call for ", key)
            try:
                self.store_B.pop(key)
            except:
                print(key, " was not found")

        
        
if __name__ == '__main__':
    imp = Imp()