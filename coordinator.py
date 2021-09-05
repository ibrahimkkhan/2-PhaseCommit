from Imp_2 import Imp as Imp_2
from multiprocessing import Process, Manager

class Coordinator:
    def __init__(self, users):
        self.users = users
         

            
            
    def manage_tasks(self):
        with Manager() as manager:
            storeA = manager.dict()
            storeB = manager.dict()            
            
            self.imp = Imp_2(storeA, storeB)
            
            while(self.users):
                user1 = self.users.pop(0)
                user1.imp = self.imp
                
                try:
                    user2 = self.users.pop(0)
                except:
                    user2 = None
                    print("No more users")
                    
                p1 = Process(target=user1.perform_ops)
                p1.start()
                
                if(user2 != None):
                    user2.imp = self.imp
                    p2 = Process(target=user2.perform_ops)
                    p2.start()
                    p2.join() 
                    
                    
                p1.join()
                    
                    
                    
            print(self.imp.store_B)
                
                
                
                  
