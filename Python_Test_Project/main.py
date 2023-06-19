from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("2000x900+0+0")
        self.root.title("Face Recognition System")

## uploding top wlala purple image

        img=Image.open("/home/sakib/Desktop/Python_Test_Project/Image_GUI/Whitewall.jpg")
        img=img.resize((2000,130),Image.LANCZOS)
        
        self.photoimg=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=2000,height=130) 
      

##background image    
        
        img2=Image.open("/home/sakib/Desktop/Python_Test_Project/Image_GUI/bg.jpg")
        img2=img2.resize((2000,900),Image.LANCZOS)
        
        self.photoimg2=ImageTk.PhotoImage(img2)
        bg_img=Label(self.root,image=self.photoimg2)
        bg_img.place(x=0,y=130,width=2000,height=900)
        
        title_lbl = Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWEARE",font=("times new  roman",35,"bold"),bg="White",fg="black")
        title_lbl.place(x=0,y=0,width=2000,height=100)

# student button image
        img3=Image.open("/home/sakib/Desktop/Python_Test_Project/Image_GUI/student.jpg")
        img3=img3.resize((220,130),Image.LANCZOS)
        
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        b1=Button(bg_img,image=self.photoimg3)
        b1.place(x=400,y=200,width=220,height=220)
        
        b1=Button(bg_img,text="Student Detail",cursor="hand2",font=("times new  roman",15,"bold"),bg="pink",fg="black")
        b1.place(x=400,y=200,width=220,height=40)
        
 # Detectpace button image
        img4=Image.open("/home/sakib/Desktop/Python_Test_Project/Image_GUI/student.jpg")
        img4=img4.resize((220,130),Image.LANCZOS)
        
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b2=Button(bg_img,image=self.photoimg4)
        b2.place(x=800,y=200,width=220,height=220)
        
        b2=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new  roman",15,"bold"),bg="pink",fg="black")
        b2.place(x=800,y=200,width=220,height=40)
        
# Attendance button image
        img5=Image.open("/home/sakib/Desktop/Python_Test_Project/Image_GUI/student.jpg")
        img5=img5.resize((220,130),Image.LANCZOS)
        
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b3=Button(bg_img,image=self.photoimg5)
        b3.place(x=1200,y=200,width=220,height=220)
        
        b3=Button(bg_img,text="Attendance",cursor="hand2",font=("times new  roman",15,"bold"),bg="pink",fg="black")
        b3.place(x=1200,y=200,width=220,height=40)

# Train button image
        img6=Image.open("/home/sakib/Desktop/Python_Test_Project/Image_GUI/student.jpg")
        img6=img6.resize((220,130),Image.LANCZOS)
        
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b4=Button(bg_img,image=self.photoimg6)
        b4.place(x=400,y=550,width=220,height=220)
        
        b4=Button(bg_img,text="Train",cursor="hand2",font=("times new  roman",15,"bold"),bg="pink",fg="black")
        b4.place(x=400,y=550,width=220,height=40)
 
 # photos image
        img7=Image.open("/home/sakib/Desktop/Python_Test_Project/Image_GUI/student.jpg")
        img7=img7.resize((220,130),Image.LANCZOS)
        
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b5=Button(bg_img,image=self.photoimg7)
        b5.place(x=800,y=550,width=220,height=220)
        
        b5=Button(bg_img,text="Photos",cursor="hand2",font=("times new  roman",15,"bold"),bg="pink",fg="black")
        b5.place(x=800,y=550,width=220,height=40)

# Exit image
        img8=Image.open("/home/sakib/Desktop/Python_Test_Project/Image_GUI/student.jpg")
        img8=img8.resize((220,130),Image.LANCZOS)
        
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b5=Button(bg_img,image=self.photoimg8)
        b5.place(x=1200,y=550,width=220,height=220)
        
        b5=Button(bg_img,text="Exit",cursor="hand2",font=("times new  roman",15,"bold"),bg="pink",fg="black")
        b5.place(x=1200,y=550,width=220,height=40)
             

  
  

  

      


if __name__ =="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()