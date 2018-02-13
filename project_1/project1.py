import PIL.Image
from tkColorChooser import askcolor
import PIL.ImageTk
from PIL import *
from Tkinter import *
import tkFileDialog

from tkColorChooser import askcolor    
choosenColor=(0,0,0)
drawingImage = None

def main():
	global root 
	root = Tk ()
	

	root.title("Painting Project")
	root.geometry("600x400")

		
	menu_bar = Menu(root)# Create main menu bar
	file_menu = Menu(menu_bar, tearoff=0)# Create the submenu (tearoff is if menu can pop out)	
	file_menu.add_command(label="Add Image!", command=openFile)# Add commands to submenu
	file_menu.add_command(label="Save Image!", command=saveImage)
	file_menu.add_command(label="End!", command=root.destroy)
	menu_bar.add_cascade(label="File", menu=file_menu)# Add the "File" drop down sub-menu in the main menu bar
	root.config(menu=menu_bar)

	pickColor= Button (root,text='Pick Color' , command=getColor)
	pickColor.grid(row=0,column=0)	

	

	root.mainloop()

#***********************
def getColor():
    color = askcolor() 
    color = str(color)
    start = color.index("((")
    stop = color.index("),")
    color = color[(start):stop]
    color = color [2:len(color)]
    r,g,b=color.split(",")
    global choosenColor
    choosenColor= int(r),int(g),int(b)
    print ("choosenColor is :",choosenColor)

def saveImage():
	pass	
def openFile():
	file_path_string = tkFileDialog.askopenfilename()
	#drawingImage=Image.open(file_path_string)
	fp = open(file_path_string,"rb")
	global drawingImage
	drawingImage = PIL.Image.open(fp)
	
	global pix 
	pix= drawingImage.load()
	xSize,ySize =  drawingImage.size #Get the width and hight of the image for iterating over
	for i in range (xSize):
			for j in range (ySize):						
				pix[i,j]=convertToBinaryRGB( pix[i,j] )		
	addToScreen(drawingImage)
	
def addToScreen( Img ):
	render = ImageTk.PhotoImage(Img)
	img = Label (root,image=render)
	img.image=render
	img.place(x=150,y=50)
	img.bind("<Button-1>",printcoords)

def printcoords(event):   
	#outputting x and y coords to console
    print (event.x,event.y)
    paintReagion(event.x,event.y)

def paintReagion(x,y):
	global choosenColor
	pix[x,y]=choosenColor
	drawingImage.putpixel((x,y), choosenColor)
	render = ImageTk.PhotoImage(drawingImage)
	img = Label (root,image=render)
	img.image=render
	img.place(x=150,y=50)
	img.bind("<Button-1>",printcoords)

def convertToBinaryRGB(  rgbValue ):
	r,g,b=rgbValue
	average=(r+g+b)/3
	if average>200:
		return 255,255,255
	return 0,0,0
	

if __name__=='__main__':
    main()