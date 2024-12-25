import tkinter as tk
from PIL import Image, ImageTk

app = tk.Tk()
app.title("fb log in page")
app.geometry("600x1000")

top_split = tk.Frame(app,bg="blue",height="500",width="600")
top_split.pack(side="top",fill="both")
top_split.pack_propagate(False)

like = Image.open("like.jpg")
like = like.resize((100,100))
like_rotated = like.rotate(30, expand=True
)

like_icon = ImageTk.PhotoImage(like_rotated)

like_label = tk.Label(top_split, image=like_icon, bg="blue",bd=0)
#.grid(row=7,column=0)
#like_label.pack(pady=10,)
like_label.place(x=100,y=200)

fb = Image.open("fb icon.jpg")
fb = fb.resize((150,150))
fb_icon = ImageTk.PhotoImage(fb)

fb_label = tk.Label(top_split, image=fb_icon,bg="blue",bd=0)
fb_label.place(x=280,y=200)


image = Image.open("image.jpg")
image = image.resize((100,90))
image_rotated = image.rotate(25, expand=True)
image_icon = ImageTk.PhotoImage(image_rotated)
image_label1 = tk.Label(top_split, image=image_icon, bg="blue", bd=0)
image_label1.place(x=490, y=150)

image2 = Image.open("image2.jpg")
image2 = image2.resize((100,90))
image_rotated2 = image2.rotate(10, expand=True)
image_icon2 = ImageTk.PhotoImage(image_rotated2)
image_label2 = tk.Label(top_split, image=image_icon2, bg="blue", bd=0)
image_label2.place(x=530, y=300)

bottom_split = tk.Frame(app, bg="white", width="600")
bottom_split.pack(side="bottom", fill="both", expand=True)
bottom_split.pack_propagate(False)

placeholder1 = "Phone number or email"
placeholder2 = "Password"

language_label = tk.Label(bottom_split, text="English     ودرا    More...", font=("Arial",12))
language_label.pack(pady=5,padx=10)

def remove_placeholder1(event):
    if ph_em.get() == placeholder1:
        ph_em.delete(0,tk.END)
        ph_em.config(fg="black")
        
def set_placeholder1(event):
    if ph_em.get() =="":
        ph_em.insert(0,placeholder1)
        ph_em.config(fg="gray")
        
def remove_placeholder2(event):
    if password.get() == placeholder2:
        password.delete(0,tk.END)
        password.config(fg="black")

def set_placeholder2(event):
    if password.get() == "":
        password.insert(0,placeholder2)
        password.config(fg="gray")

ph_em = tk.Entry(bottom_split, bg="white", fg="gray", bd=0,relief="flat", width=36)
ph_em.place(x=50,y=150)
ph_em.insert(0,placeholder1)

ph_em.bind("<FocusIn>",remove_placeholder1)
ph_em.bind("<FocusOut>",set_placeholder1)

password = tk.Entry(bottom_split, bg="white", fg="gray",bd=0,width=36)
password.place(x=50,y=260)
password.insert(0,placeholder2)

password.bind("<FocusIn>", remove_placeholder2)
password.bind("<FocusOut>", set_placeholder2)

log_in = tk.Button(bottom_split, text = "Log In", bg="blue", fg="white")
log_in.place(y=350, x=42, width=625)

forget_label = tk.Label(bottom_split, text="Forgotten Password?",bd=0, bg="white", fg="blue")
forget_label.place(x=200, y=470)

or_label = tk.Label(bottom_split,text="___________________OR___________________", bg="white", fg="gray")
or_label.place(x=50, y= 550)

create_button = tk.Button(bottom_split, text="Create New Facebook Account", bg="green", fg="white")
create_button.place(x=42, y=650, width=628)

tk.mainloop()