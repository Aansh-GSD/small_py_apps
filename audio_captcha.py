from tkinter import*
from tkinter import messagebox
import random
import pyttsx3


global audio_captcha
def generate_digit_captcha():
    s=''
    s1=''
    for i in range(4):
        number=str(random.randint(0,9))
        s=s+number
        s1=s1+number+" "
    #print(s1)
    global audio_captcha
    audio_captcha=s
    return s1

def generate_audio_captcha():

    digit=generate_digit_captcha()
    print(digit)
#initialising text to speech
    engine=pyttsx3.init()

    engine.setProperty('rate',170)
    engine.setProperty('volume',1.0)

    voices=engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)

    engine.say(digit)
    engine.runAndWait()
    engine.say(digit)
    engine.runAndWait()

def audio_captcha_result():
    return audio_captcha



def check_answer():
    if box.get()==audio_captcha_result():

        messagebox.showinfo("Your captcha has been verified, please proceed further")
        print("yes")

w=Tk()
w.title("audio captcha")
w.geometry("800x800")

#top=Frame(w,bg="orange",pady=1,width=100,height=50,bd=5,relief=RIDGE)
#top.place(x="0",y="0")
#top.grid(row=0, column=0)

mainframe=Frame(w,bg="powderblue",pady=5,width=500,height=500,bd=5,relief=RIDGE)
#mainframe.place(x="0",y="50")
mainframe.grid(row=1,column=0)


l1=Label(mainframe,padx=2,bg="black",font=('lato black', 33,'bold'),fg="white",text="Audio Captcha",pady=2)
#l1.place(x="20",y="10")
l1.grid(row=0,column=0)

l2=Label(mainframe,padx=2,bg="powderblue",font=('lato black', 33,'bold'),text="",pady=2)
#l1.place(x="20",y="10")
l2.grid(row=1,column=0)

button1=Button(mainframe,justify=CENTER,bg="green",font=('lato black', 13,'bold'),pady=2,padx=2,text="Click to generate audio",command=generate_audio_captcha)
#button1.place(x="20",y="80")
button1.grid(row=2,column=0)

l3=Label(mainframe,padx=2,bg="powderblue",font=('lato black', 33,'bold'),text="",pady=2)
#l1.place(x="20",y="10")
l3.grid(row=3,column=0)

box=Entry(mainframe,width=35,bg="yellow",justify=CENTER)
box.grid(row=4,column=0)
#box.place(x="20",y="120")

l4=Label(mainframe,padx=2,bg="powderblue",font=('lato black', 33,'bold'),text="",pady=2)
#l1.place(x="20",y="10")
l4.grid(row=5,column=0)

check=Button(mainframe,bg="green",text="Check",command=check_answer)
# submit.place(x="20",y="150")
check.grid(row=6,column=0)

l5=Label(mainframe,padx=2,bg="powderblue",font=('lato black', 33,'bold'),text="",pady=2)
#l1.place(x="20",y="10")
l5.grid(row=7,column=0)

regenerate=Button(mainframe,bg="green",text="Regenerate")
# regenerate.place(x="20",y="120")
regenerate.grid(row=8,column=0)
w.mainloop()
