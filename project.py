# -*- coding: utf-8 -*-
"""
Shivam Joshi 20124015
jashit kandhari  20124045
Megha patel 20124107


File handling System
"""
import time

import os
import shutil
import json
class create:
    def __init__(self):
        print("\n==============================================\n")
        print("                 Create a file                 \n")
        print("==============================================\n")
        print("\nWhat type of FILE you would like to create?\n")
        ch="y"
        while ch=="y":
            print("1)Practical File             (heading,aim,1 paragraph for theory,conclusion)")
            print("2)A Formal Letter            (to,from,addreses,subject,2 paragraph,date,signature)")
            print("3)A Question / Answer book   (n number of que/ans)\n\n")
            opt=int(input("Enter your choice"))
            
            if opt==1:
                self.create_practical()
            elif opt==2:
                self.letter()
            elif opt==3:
                self.queans()
            ch=input("-----------Do you want to create more files? y/n?--------------\n")
    def create_practical(self):
        print("              Create a practical              \n")
        print("             --------------------             \n")
        
        heading=input("enter heading of program\n")
        aim=input("enter aim\n")
        theory=input("enter theory press enter to end\n")
        conclusion=input("enter your conclusion\n")
        name=input("Created By:")
        roll=input("Roll number?")
        
        ch='y'
        while ch=='y':
            target=input("\n\nName your file\n")
            x=os.path.isfile(target)
            
            if x!=True:
                src="/project/formates/practical.txt"
                shutil.copyfile(src, target)# copying formate of pra i target file
                fr=open(target,"r")
                stj=json.load(fr)
                stj={"HEADING": heading, "AIM":aim,"THEORY":theory,"CONCLUSION": conclusion}#adding records to a file
                fr.close()
                fw=open(target,"w")#opening target file to write in proper formate
                for k1,v1 in stj.items():
                        stj=json.dumps(stj)  #getting one value turn by turn from RAM to get dumpp into file
                        fw.write(k1)
                        fw.write("  --  ")
                        fw.write(v1)
                        fw.write("\n----------\n")
                        fw.write("       ")
                        
                        fw.write("\n\n")
                fw.write("\n\n..................\n")
                fw.write(name)
                fw.write("\n")
                fw.write(roll)
                fw.write("\n.................\n\n\n")        
                fw.close()
                print("Creating , it will take few seconds........\n")
                time.sleep(2)
                print("File Created Successfully.....")
                ch='n'
            else:
                print("file of this name already exist\n")
                ch=input("try again y/n?")
            

    def letter(self):
        print("              Create a Letter              \n")
        print("             -----------------              \n")
        to=input("enter to ,\n")
        saddr=input("senders address\n")
        raddr=input("reciever address")
        frm=input("enter from,\n")
        subject=input("enter your subject\n")
        subject="Subject:  "+subject
        para1=input("start typing letter (enter to exit)")
        para2=input("start typing letter (enter to exit)")
        para2=para2+"\nYour Faithfull"
        sign=input("your sign(your loving)\n")
        date=input("enter date")
        
        ch='y'
        while ch=='y':
            target=input("\n\nName your file\n")
            x=os.path.isfile(target)
            src="/project/formates/letter.txt"
            if x!=True:
                
                shutil.copyfile(src, target)
                fr=open(target,"r")
                stj=json.load(fr) 
                stj={"Sender Adress":saddr,"Date:":date,"To,":to,"Reciever Address":raddr,"Subject":subject,"p1":para1,"p2":para2,"sign":sign,"from":frm}
                fr.close()
                fw=open(target,"w")
                for k1,v1 in stj.items():
                        stj=json.dumps(stj) 
                        fw.write(v1)
                        fw.write("\n\n")
                fr.close()
                print("Creating , it will take few seconds........\n")
                time.sleep(2)
                print("File Created Successfully.....")
                ch='n'
            else:
                print("file of this name already exist\n")
                ch=input("try again y/n?")

    
    def queans(self):
        print("\n\n        Create a Que/Ans Bank              \n")
        print("      -------------------------              \n")
        
        l={}
        print("Start entering Que and Ans\n")
        ch="y"
        i=0
        while ch=="y":
            print(i+1,"que")
            que=input()
            ans=input("Enter its ans\n")
            l[que]=ans
            i+=1
            ch=input("\n---want to add more? y/n---\n")
            
        ch='y'
        while ch=='y':
            target=input("\n\nName your file\n")
            
            x=os.path.isfile(target)
            src="/project/formates/que_ans.txt"
            if x!=True:
                shutil.copyfile(src,target)
                fr=open(target,"r")
                stj=json.load(fr)
                stj=l
                fr.close()
                fw=open(target,"w")
                fw.write("This File has ")
                fw.write(str(i))
                fw.write(" Question and Answer\n----------------------------------------------------------\n----------------------------------------------------------\n\n\n\n")
                x=1
                for k1,v1 in stj.items():
                    
                        stj=json.dumps(stj)
                        fw.write(str(x))
                        x+=1
                        fw.write("  QUE:")
                        fw.write(k1)
                        fw.write("\n")
                        fw.write("ANS:")
                        fw.write(v1)
                        fw.write("\n\n\n\n\n")
                fw.close()       
                print("Creating , it will take few seconds........\n")
                time.sleep(2)
                print("File Created Successfully.....")
                ch='n'
            else:
                print("file of this name already exist\n")
                ch=input("try again y/n?")
        
        


class delete:
    def __init__(self):
        print("\n\n           Delete a file             \n")
        print("           ******************             \n")
        
        files=os.listdir('.')
        for f in files:
            print(f)
        ch="y"
        while ch==("y" or "yes"):
            target=input("which file you want to delete?\n")
            
            if os.path.exists(target):
                opt=input("do you really want to delete? y/n\n")
                if opt=="yes" or "y" or "YES":
                    try:
                       
                            os.remove(target)
                            time.sleep(1)
                            print("File Deleted Succesfully......\n")
                    except:
                        print("Sorry Some problem has occured.....!!")
                else:
                    print("NO file deleted\n")
            else:
                print("file not found in this folder!!") 
            ch=input("Do you want to delete more? y/n?")
            if ch!="y" or "y":
                break
        



class display:
    def __init__(self):
        print("\n\n            Display a File              \n")
        print("          ******************             \n")
        
        files=os.listdir('.')
        for f in files:
             print(f)
        file=input("which file you want to display?\n")
        if os.path.exists(file):
            fr=open(file,"r")
            try:
                stj=fr.read()
                print(" Printing.............\n")
                time.sleep(2)
                print(stj)
                # for k,v in stj.items():
                #     print(k,"-----",v)
            except:
                print("!!!!Enter only file with dictonary formate in it!!! ")
            
        else:
             print("No such file exixts")
        




class copy:
    def __init__(self):
        print("\n\n            Copy a file to other              \n")
        print("          ************************             \n")
        files=os.listdir('.')
        for f in files:
             print(f)
        src=input("Which File you want to copy?\n")
        target=input("Name of new file to copied into")
        if os.path.exists(src):
            
                shutil.copyfile(src, target)# copying formate of pra i target file
                print(" copying !!!will take few sec.............\n")
                time.sleep(2)
                print("file successfully codies!!!")
        else:
            print("File not found in current Directory!!!")





class rename:
    def __init__(self):
        ch="y"
        files=os.listdir('.')
        for f in files:
             print(f)
        while ch=="y":
            src=input("Which file you want to rename?\n")
            dest=input("New name of file?\n")
            if os.path.exists((src)):
               
                    os.renames(src, dest)
                    print("Renaming!!! will take few secs........\n")
                    time.sleep(2)
                    print("file successfully codies!!!")
            else:
                print("File not found in current Directory :(\n")
            ch=input("want to try more renaming? y/n")
         
            
         
####################DRIVER#############################

print("\n==============================================\n")
print("           WELCOME TO FILE MANAGEMENT           \n")
print("==============================================\n")
print("\nWhat type of operation you would like to perform?")
ch="y"
while ch=="y":
    opt=int(input("1) Create new file\n   (Practical file/letter/Que and Ans Bank)\n2)Rename a File\n3) Delete a File \n4) Display a File \n5) Create a copy of File\n "))

    if opt==1:
        c=create()
    elif opt==2:
        r=rename()
    elif opt==3:
        d=delete()
    elif opt==4:
        disp=display()
    elif opt==5:
        cpy=copy()
        
    else:
        print("invalid option ")
    print("\n\n----------Do you want to do more operation? y/n-------------")
    ch=input("           (create/rename/delete/display/copy)\n")








"""
What makes you unique?

What makes me unique is my ability to meet and exceed deadlines. 
In my previous role, my manager consistently praised me for completing my projects efficiently with a high level of quality. 
This allowed me to take on additional responsibilities and eventually led to a promotion.





D- 1801, Neptune Society,
DS Marg, Lower Parel,
Mumbai 400 008.
11th June 2018.

To,
The Editor-in-Chief,
Hindustan Times,
Main Street,
Mumbai 400 001.

Sir,

Subject: Construction work in our locality during monsoon season causing us difficulties.
Through the medium of your esteemed and respected daily, I wish to inform the municipal authorities of the difficulties the residents of my locality are facing due to the construction and repair work currently happening in our area. Monsoon season has started a few days ago and is compounding our problems.
The repair work has been ongoing for five weeks now and is falling way behind schedule. And now with the current weather conditions, we are having persistent problems of water logging and flooding in our area. Another worry is about the accidents that may occur due to the debris lying around the road. Diseases caused due to waterlogging are another one of our concerns.
Therefore I wish to draw the attention of the concerned authorities with the help of your newspaper. Hopefully, you will be able to help us in drawing their attention and resolving this matter at the earliest.
Thanking You,

Your Sincerely,

[Mr. XYZ]




Volumetric analysis

Determination of concentration/Molarity of KMnO4 solution by titrating it against a standard solution of: Oxalic acid


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur ut euismod velit, eu commodo lectus. Pellentesque viverra quis tellus ac viverra. Donec dapibus justo at dui consequat, eu lacinia est bibendum. Praesent vehicula velit at ex vulputate tempus. Cras sollicitudin quam justo, eget elementum est fringilla eu. Mauris dictum lacinia risus, a commodo nisl cursus non. Aliquam posuere eget metus eu viverra. Praesent ultricies vel ligula eget porta. Fusce semper augue non velit porta, vulputate auctor nisl interdum.

Molarity of KMnO4 solution is: 0.1m
"""