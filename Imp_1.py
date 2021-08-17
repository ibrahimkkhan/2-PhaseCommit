from threading import Lock

class Imp:
    
    def __init__(self):
        self.store_A = dict()
        self.store_B = dict()
        self.db_lock_A = Lock()
        self.db_lock_B = Lock()

    def put(self, key, val):
        if(ord(key[0]) < 80):
            self.db_lock_A.acquire()
            self.store_A[key] = val
            print("put call in Database A", key)
            self.db_lock_A.release()
        else:
            self.db_lock_B.acquire()
            self.store_B[key] = val
            print("put call in Database B", key)
            self.db_lock_B.release()
        
        
    def get(self,key):
        if(ord(key[0]) < 80):
            self.db_lock_A.acquire()
            try:
                rval = self.store_A[key]            
            except:
                rval = "ABORT"
                print(key, " was not found")
            self.db_lock_A.release()
        else:
            self.db_lock_B.acquire()
            try:
                rval = self.store_B[key]            
            except:
                rval = "ABORT"
                print(key, " was not found")
            self.db_lock_B.release()
        return rval
    
    def delete(self,key):
        if(ord(key[0]) < 80):
            self.db_lock_A.acquire()
            print("delete call", key)
            try:
                self.store_A.pop(key)
            except:
                print(key, " was not found")
            self.db_lock_A.release()
        else:
            self.db_lock_B.acquire()
            print("delete call", key)
            try:
                self.store_B.pop(key)
            except:
                print(key, " was not found")
            self.db_lock_B.release()

        
        
if __name__ == '__main__':
    imp = Imp()