import threading
import sys,argparse
from Imp_1 import Imp as Imp_1
from Imp_0 import Imp as Imp_0
from coordinator import Coordinator
import multiprocessing
import time


class User():

    def __init__(self, num_threads, op_names, imp_name):
        self.num_threads = num_threads
        self.op_names = op_names
        self.user_threads = []
         
        if(imp_name == "Imp_0"):
            self.imp_name = imp
            self.imp = Imp_0()
            for j in range(self.num_threads):
                t = threading.Thread(target=self.perform_ops)
                self.user_threads.append(t)
                t.start()
                
            print("Database after ", self.imp.store) 
        elif(imp_name == "Imp_1"):
            self.imp_name = imp
            self.imp = Imp_1()
            for j in range(self.num_threads):
                t = threading.Thread(target=self.perform_ops)
                self.user_threads.append(t)
                t.start()
                
            
            print("Database A after ", self.imp.store_A) 
            print("Database B after ", self.imp.store_B) 
        elif(imp_name == "Imp_2"):
            self.imp_name = imp_name
            
        else:
            print("Not a valid implementation")
             

    def perform_ops(self):
        if(self.imp_name == "Imp_2"):
            pid = multiprocessing.current_process().name
            print('Current process', pid)     
        else:
            tid = multiprocessing.current_thread().name
            print('Starting user thread', tid)

        while(self.op_names):
            i = self.op_names.pop(0)
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

if __name__ == '__main__':
    
#     print('starting 2PC.user')
        
    ## To run use python 2PC.user.ipynb [-h] <num_threads> <op_names>
    ## <op_names> are name of all the operations. for eg: put(k1),put(k2),delete(k1)
    p = argparse.ArgumentParser(
      usage='python 2PC/user.py -num_threads -op_names -imp -num_users',
      description='create a user to drive the given implementation')

    p.add_argument("-imp", type=str, help='implementation running')
    p.add_argument("-num_users", type=int, help='number of users', default = 1)
    p.add_argument("-num_threads", type=int, help='number of user threads', default = 1)
    
    args = p.parse_args(sys.argv[1:])
    print("Implementation args:", args)
    
    num_threads = args.num_threads
    imp_name = args.imp
    op_names = []
    num_users = args.num_users
    
    print("Starting ", imp_name)

    if(imp_name == "Imp_2"):
        users = []
        for j in range(num_users):
            print("Enter op_names for User ", j + 1 , ": ")
            op_name = input()
            user = User(1, op_name.split(" "), imp_name)
            users.append(user)  

        coordinator = Coordinator(users)
        coordinator.manage_tasks()         

    else:
        p.add_argument("-op_names", type=str, help='name of the operations')
        op_names = args.op_names
        op_names = self.op_names.split(" ") #list of all operations
        user = User(num_threads, op_names, imp)
        
        if hasattr(user.imp, '__end__'):
            for t in user.user_threads:
              t.join()
            user.imp.__end__()


    

   

 
    