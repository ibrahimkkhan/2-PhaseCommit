from threading import Lock

class Imp:
    
    def __init__(self):
        self.store = dict()
        self.db_lock = Lock()

    def put(self, key, val):
        self.db_lock.acquire()
        self.store[key] = val
        print("put call", key)
        self.db_lock.release()
        
    def get(self,key):
        self.db_lock.acquire()
        try:
            rval = self.store[key]            
        except:
            rval = "ABORT"
            print(key, " was not found")
        self.db_lock.release()
        return rval
    
    def delete(self,key):
        self.db_lock.acquire()
        print("delete call", key)
        try:
            self.store.pop(key)
        except:
            print(key, " was not found")
        self.db_lock.release()

        
        
if __name__ == '__main__':
    imp = Imp()