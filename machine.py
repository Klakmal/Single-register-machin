#Implementation of Stack using python list
class Stack:
  def __init__(self):
    self.list=[]
  def isEmpty(self):
    return self.list==[]
  def push(self,item):
    self.list.append(item)
  def pop(self):
    return self.list.pop()
  def peek(self):
    return self.list[len(self.list)-1]
  def size(self):
    return len(self.list)

#create stack
s=Stack()

from Tkinter import *

class machine:

  def __init__(self):
    
    window=Tk()
    window.title("machine")
    window.geometry("500x600")
    window.configure(background="#a1dbcd")

    Label1=Label(window,text="Type postfix expression:", fg ="#383a39" , bg = "#a1dbcd")
    Label1.pack()
 
    #TextBox to enter the postfix expression
    self.e=Entry(window,bd=4,width=60)
    self.e.pack()

    #Add Buttons
    button1=Button(window,text="print",command=self.print,width=15)
    button1.pack(side="top")

    #TextArea to display the answer
    self.Text = Text(window, height=25, width=40)
    self.Text.pack()

  def print(self):
    x=self.e.get()#Input from the TextBox
    n=0    
    f=""   
    # Evaluate one character at a time
    for i in range (0,len(x)):

    #See whether the character is an operator or not
      if(x[i]=="+"):
         a=s.pop()
         b=s.pop()
         n=n+1
         p="TEMP"+str(n)
         f=f+"LD  "+b+"\n"+"AD  "+a+"\n"+"ST  "+p+"\n"
         s.push(p)
                  
      elif(x[i]=="-"):
         a=s.pop()
         b=s.pop()
         n=n+1
         p="TEMP"+str(n)
         f=f+"LD  "+b+"\n"+"SB  "+a+"\n"+"ST  "+p+"\n"
         s.push(p)
         
      elif(x[i]=="*"):
         a=s.pop()
         b=s.pop()
         n=n+1
         p="TEMP"+str(n)
         f=f+"LD  "+b+"\n"+"ML  "+a+"\n"+"ST  "+p+"\n"
         s.push(p)
         
      elif(x[i]=="/"):
         a=s.pop()
         b=s.pop()
         n=n+1
         p="TEMP"+str(n)
         f=f+"LD  "+b+"\n"+"DV  "+a+"\n"+"ST  "+p+"\n"
         s.push(p)

      else:
         s.push(x[i])
    #Instructions are inserted in to the TextArea
    self.Text.insert(INSERT,f)

ma=machine()

