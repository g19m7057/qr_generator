import qrcode
import tkinter as tk
from PIL import Image

#create window
w = tk.Tk()
w.title("qr code generator")

#entry
label1 = tk.Label(w, text = "enter object to convert") 
entry_code = tk.Entry(w)
label1.pack()
entry_code.pack()

label2 = tk.Label(w, text = "enter name for qr")
entry_name = tk.Entry(w)
label2.pack()
entry_name.pack()

#code to generate and show
def gen():
    img = qrcode.make(entry_code.get())
    img.save(entry_name.get() + ".png")
    #shows the qr as a image
    image = Image.open(entry_name.get()  + ".png")
    image.show()

    #remove the previous entries
    entry_code.delete(0, tk.END)
    entry_name.delete(0, tk.END)

sub_button = tk.Button(w, text="Submit", command = gen)
exit_button = tk.Button(w, text ="exit", command = w.destroy)

sub_button.pack()
exit_button.pack()

w.mainloop()