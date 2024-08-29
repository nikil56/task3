import tkinter as tk
from tkinter import messagebox
import lyricsgenius


genius = lyricsgenius.Genius("DtgSBbf50ywsKBgnjIlHq-gn7MMRH0vBcY_zpYkud5O7mWIb3KOZBoVKogmYn6vK_KUM3p7kRru9STqtiPuxTw")

def get_lyrics():
    song_title = entry_song.get()
    artist_name = entry_artist.get()

    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            text_lyrics.delete(1.0, tk.END)
            text_lyrics.insert(tk.END, song.lyrics)
        else:
            messagebox.showerror("Error", "Lyrics not found!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = tk.Tk()
root.title("Lyrics Extractor")


label_song = tk.Label(root, text="Song Title:")
label_song.grid(row=0, column=0, padx=10, pady=10)

entry_song = tk.Entry(root, width=40)
entry_song.grid(row=0, column=1, padx=10, pady=10)

label_artist = tk.Label(root, text="Artist Name:")
label_artist.grid(row=1, column=0, padx=10, pady=10)

entry_artist = tk.Entry(root, width=40)
entry_artist.grid(row=1, column=1, padx=10, pady=10)

button_get_lyrics = tk.Button(root, text="Get Lyrics", command=get_lyrics)
button_get_lyrics.grid(row=2, column=0, columnspan=2, pady=10)

text_lyrics = tk.Text(root, wrap='word', height=20, width=60)
text_lyrics.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
