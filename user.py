import threading
import sys,argparse
from Imp_1 import Imp

class User():

    def __init__(self, argv):
        print('starting 2PC.user')
        
        ## To run use python 2PC.user.ipynb [-h] <num_threads> <op_names>
        ## <op_names> are name of all the operations. for eg: put(k1),put(k2),delete(k1)
        p = argparse.ArgumentParser(
          usage='python 2PC/user.py -num_threads -op_names',
          description='create a user to drive the given 2PC implementation')
        
        p.add_argument("-num_threads", type=int, help='number of user threads', default = 1)
        
        p.add_argument("-op_names", type=str)

        
        args = p.parse_args(argv[1:])

        print("2PC args:", args)
        self.num_threads = args.num_threads
        self.op_names = args.op_names
        
        self.op_names = self.op_names.split(" ")
        
        self.user_threads = []
        self.imp = Imp()
        
      
        for j in range(self.num_threads):
          t = threading.Thread(target=self.perform_ops)
          self.user_threads.append(t)
          t.start()
        
        
       

    def perform_ops(self):
        tid = threading.current_thread().name
        print('starting user thread', tid)
        
        while(self.op_names):
            i = self.op_names.pop(0)
            print("Operation being performed is ", i, "by ", tid)
            s = i.split("(")
            
            func = s[0]
            key = "key"
            value = "value"
            
            
            if(func == "put"):
                param = s[1].split(",")
                
                key = param[0]
                value = param[1].replace(")", "")
                
                self.imp.put(key, value)
                
            elif(func == "get"):
                key = s[1].replace(")", "")
                self.imp.get(key)

            elif(func == "delete"):
                key = s[1].replace(")", "")
                self.imp.delete(key)

            else:
                print("Invalid Arguments")
                

        print(tid, " is Committing...")
        print("Database A after commit by", tid, self.imp.store_A) 
        print("Database B after commit by", tid, self.imp.store_B) 
                   
        

if __name__ == '__main__':
  user = User(sys.argv)
  # if user.imp has __end__ (ie, is service_imp), end service process
  if hasattr(user.imp, '__end__'):
    for t in user.user_threads:
      t.join()
    user.imp.__end__()
    