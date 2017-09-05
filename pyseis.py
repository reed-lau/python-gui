from PIL import Image as ImagePIL
from PIL import ImageTk as ImageTk
from  tkinter import *

root=0
image=1
img1=2
img=3
id=4
def can_config_event(event):
	global img
	win_width =root.winfo_width()
	win_height=root.winfo_height()
	event.widget.config(width=win_width,height=win_height)
	img1=image.resize((win_width,win_height))
	img2=img1
	for iz in range(img1.size[0]):
		for ix in range(img1.size[1]):
			img2.putpixel((iz,ix),img1.getpixel((iz,ix)))
	img=ImageTk.PhotoImage(img1)

	
	
	event.widget.itemconfig(id,image=img)
	#event.widget.config(width=)

root=Tk()
root.geometry('1000x800')

image=ImagePIL.open('img.jpg')

img=ImageTk.PhotoImage(image)

can=Canvas(root,width=800,height=600,bg='#00b300')

can.create_line(100,200,500,600,fill='red')
id=can.create_image(0,0,anchor=NW,image=img)

can.pack()



#print(img.format,img.mode,img.size)



#a=1

#print(a)

# listen the resize event
can.bind('<Configure>',can_config_event)


root.mainloop()
