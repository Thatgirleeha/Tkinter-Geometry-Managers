import customtkinter as ctk
from PIL import Image
screen = ctk.CTk()
screen.geometry("800x550")
images = ["baddie.jpg", "cuttie.gg.jpg", "fantasy girl.jpg", "nice girl.jpg"]
index = 0
def slideshow():
    global index
    photo = ctk.CTkImage(Image.open(images[index]), size=(800, 550))
    bg.configure(image=photo)
    bg.image = photo
    index = (index + 1) % len(images)
    screen.after(2000, slideshow) 
def login():
    if user.get() == "admin" and password.get() == "1234":
        message.configure(
            text="login successful!")
    else:
        message.configure(
            text="login failed!")
bg = ctk.CTkLabel(screen, text="")
bg.place(x=0, y=0, relwidth=1, relheight=1)
frame = ctk.CTkFrame(screen)
frame.place(relx=0.5, rely=0.5, anchor="center")
user = ctk.CTkEntry(frame, placeholder_text="Username")
user.pack(pady=10)
password = ctk.CTkEntry(frame, placeholder_text="Password", show="*")
password.pack(pady=10)
ctk.CTkButton(frame, text="Login", command=login).pack(pady=10)
message = ctk.CTkLabel(frame, text="")
message.pack(pady=10)
slideshow()
screen.mainloop()