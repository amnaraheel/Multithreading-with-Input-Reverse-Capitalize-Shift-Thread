import threading

def input_string():
    global string
    string = str(input("Enter a string: "))
    return string 
    
def reverse_string(string):
    reversed_string=string[::-1]
    print("Reversed String is: ",reversed_string)
    
def capitalize_string(string):
    print("Capitalized String is: ",string.upper())
    
def shift_string(string):
    shifted_string = ""
    for i in string:
      shifted_string += chr(ord(i) + 2)
    print("Shifted string is:", shifted_string)

if __name__=="__main__":
    t1=threading.Thread(target=input_string)
    t1.start()
    t1.join()
    
    t2=threading.Thread(target=reverse_string,args=(string,))
    t3=threading.Thread(target=capitalize_string,args=(string,))
    t4=threading.Thread(target=shift_string,args=(string,))
    
    t2.start()
    t3.start()
    t4.start()
    
    t2.join()
    t3.join()
    t4.join()
    
    