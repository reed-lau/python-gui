from   Tkinter import * 
import subprocess

text=1
def bandfun():
	proc=subprocess.Popen(['ls','../','-lthr'],stdout=subprocess.PIPE)
	output=proc.stdout.read()
#	text.insert(1.0,"")
	text.delete(1.0,END)
	text.insert(END,output)
def connfun():
	print("conn test")
	
root=Tk()
root.title('GPU-Tester')
root.geometry('800x600+100+100')


btn1=Button(root,text='Band Width Test',command=bandfun)
btn2=Button(root,text='Conn Width Test',command=connfun)

text=Text(root)


btn1.grid(row=0,column=1)
btn2.grid(row=0,column=3)
text.grid(row=1,column=0,columnspan=5,sticky='nsew')
root.columnconfigure(0,weight=1)

root.rowconfigure(0,weight=0)
root.rowconfigure(1,weight=1)

root.mainloop()

