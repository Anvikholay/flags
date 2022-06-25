from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root=Tk()
root.title("Country Flags")
root.geometry("600x400")

india_map = ImageTk.PhotoImage(Image.open ("Flag_of_India.svg"))
uk_map = ImageTk.PhotoImage(Image.open ("Flag_of_the_United_Kingdom.svg"))
maps_dictionary={"India":india_map,
                 "UK":uk_map}

def showMaps():
    try:
        map_name = get_input.get()
        print(map_name)
        show_label['image'] = maps_dictionary[map_name]
    except:
        messagebox.showinfo("Error", "Sorry! This country flag is not present in our system")

btn = Button(root , text="Show Map", bg="green", command=showMaps)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()