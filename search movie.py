from tkinter import *
from imdb import *

def search_movie(): 
    imdb_object=IMDb()
    movie_name=e1.get()
    result=imdb_object.search_movie(movie_name)
    for i in result:
        textbox.insert(0, i)
        
root=Tk()
root.title("Movie database")
root.minsize(width=400,height=400)
root.geometry("500x500")

lbl=Label(root,text="Enter movie to search: ").pack()
e1=Entry(root, text="")
e1.pack()

search_button=Button(root, text="Search movie",command=search_movie).pack()

textbox=Entry(root,width=500)
textbox.pack(padx=10, pady=10)

root.mainloop()

