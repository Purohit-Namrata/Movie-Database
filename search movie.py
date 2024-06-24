import tkinter as tk
import imdb as im

def search_movie():
    imdb_object = im.IMDb()
    movie_name = e1.get()
    result = imdb_object.search_movie(movie_name)
    textbox.delete(1.0, tk.END)  # Clear the text box
    if result:
        for movie in result:
            title = movie.get('title', 'Unknown Title')
            year = movie.get('year', 'Unknown Year')
            textbox.insert(tk.INSERT, f"{title} ({year})\n")
    else:
        textbox.insert(tk.INSERT, "No results found.\n")

root = tk.Tk()
root.title("Movie Database")
root.minsize(width=400, height=400)
root.geometry("500x500")

lbl = tk.Label(root, text="Enter movie to search: ").pack()
e1 = tk.Entry(root, text="")
e1.pack()

search_button = tk.Button(root, text="Search Movie", command=search_movie)
search_button.pack()

textbox = tk.Text(root)
textbox.pack(padx=10, pady=10)

root.mainloop()
