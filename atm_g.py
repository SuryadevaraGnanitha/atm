import time

class Atm:
    def __init__(self,ac_balance):
        self.ac_balance=ac_balance
    
    def withdraw(self):
        amt=int(input("enter amount (multiple of 100) to be withdraw:\n"))
        time.sleep(2)
        if amt%100==0:
            if amt<=self.ac_balance and amt>=100:                
                self.ac_balance-=amt
                print("\t\t........JUST A SECOND........")
                print("---------------------------------------")
                print("withdraw successfull")
                print("---------------------------------------")
                print("current balance is ",self.ac_balance)
                print("---------------------------------------")
                print("THANK YOU")
            else:
                print("---------------------------------------")
                print("insufficient amount\n")
                print("---------------------------------------")
        else:
            print("---------------------------------------")
            print("ERROR")
            print("---------------------------------------")
            #continue
            
    def deposit(self):
        print("---------------------------------------")
        ac_no=input("enter your account number:\n")
        print("---------------------------------------")
        if len(ac_no)!=14:
            print("---------------------------------------")
            print("Invalid account number\n")
            print("---------------------------------------")
        else:
            print("---------------------------------------")
            ac_no2=input("Re enter your account number:\n")
            print("---------------------------------------")
            if ac_no==ac_no2:
                amt=int(input("enter amount to be deposit\n"))
                print("\t\t........JUST A SECOND........")
                self.ac_balance+=amt
                print("deposit successful")
                time.sleep(2)
                print("current balance ",self.ac_balance)
                print("---------------------------------------")
                print("\t\t...THANK YOU...!")
                print("---------------------------------------")
        
    def transfer(self):
        print("---------------------------------------")
        ac_no=input("enter account number to transfer:\n")
        print("---------------------------------------")
        time.sleep(2)
        if len(ac_no)!=14:
            print("---------------------------------------")
            print("Invalid account number\n")
            print("---------------------------------------")
        else:
            print("---------------------------------------")
            ac_no2=input("Re enter account number to transfer:\n")
            print("---------------------------------------")
            print("\t\t........JUST A SECOND........")
            time.sleep(2)
            if ac_no==ac_no2:
                amt=int(input("enter amount to transfer:\n"))
                if amt<=self.ac_balance:
                    self.ac_balance-=amt
                    print("---------------------------------------")
                    print("transfer successful")
                    print("---------------------------------------")
                    time.sleep(2)
                    print("current balance ",self.ac_balance)
                    print("---------------------------------------")
                    print("THANK YOU...!")
                    print("---------------------------------------")
                    
                else:
                    time.sleep(2)
                    print("Insufficient balance")
                    
    def check_balance(self):
        time.sleep(2)
        print("current balance is ",str(self.ac_balance))
        
    def transaction(self):
        print("---------------------------------------")
        opt=int(input("SELECT\n1.WITHDRAW\n2.DEPOSIT\n3.TRANSFER\n4.CHECK_BALANCE\n5.QUIT\n"))
        print("---------------------------------------")
        time.sleep(2)
        if opt==1:
            obj.withdraw()
        elif opt==2:
            obj.deposit()
        elif opt==3:
            obj.transfer()
        elif opt==4:
            obj.check_balance()
        elif opt==5:
            exit()
        else:
            print("enter correct option\n")

        
print("\t\tWELCOME TO ATM\n")
time.sleep(2)
obj=Atm(5000)
def passwordCheck(): 
    pass_word=1234
    n=1
    while(n<4):
        pin=input("enter pin")
        time.sleep(2)
        if int(pin)==pass_word:
            print("login successful\n")     
            break
        else:
            print("Invalid pin\n")      
        n+=1
    else:
        print("YOUR ACCOUNT IS BLOCKED FOR 24 HOURS")
        exit()
passwordCheck()
obj.transaction()
i=3
while i>0:
    opt2=input("do you want to continue <Y/N>:")
    time.sleep(2)
    if opt2 == "Y" or opt2 == "y":
        passwordCheck()
        obj.transaction()
    else:
        print("THANKS FOR VISITING")
        break
    i-=1
    
