from tkinter import *
import subprocess
import threading


def download():
    track_url = url.get()
    text_box.insert(END, f"Downloading: Please wait...\n")
    text_box.see(END)

    thread = threading.Thread(target=run_spotdl, args=(track_url,))
    thread.start()


def run_spotdl(track_url):
    command = f"spotdl {track_url}"

    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        shell=True
    )

    for line in process.stdout:
        update_progress(line)

    process.wait()
    update_progress("\n✔ Download Completed!\n")


def update_progress(message):
 
    text_box.after(0, lambda: (text_box.insert(END, message), text_box.see(END)))


root = Tk()
root.title("Spotify Downloader")
root.geometry("520x800")
root.configure(bg="#232224")
root.resizable(False, False)

Label(root, text="Spotify Downloader", font=("Helvetica", 24), bg="#232224", fg="white").pack(pady=20)
Label(root, text="Paste Spotify Track / Album / Playlist Link", font=("Helvetica", 14), bg="#232224", fg="white").pack(pady=10)

url = Entry(root, font=("Helvetica", 14), width=40, bg="#3E3E3E", fg="white", bd=0, insertbackground="white")
url.pack(pady=10)

Button(root, text="Download", font=("Helvetica", 14), bg="#1DB954", fg="white",
       bd=0, padx=20, pady=10, command=download).pack(pady=20)

text_box = Text(root, height=20, width=60, bg="#1e1e1e", fg="white", font=("Consolas", 12))
text_box.pack(pady=10)

root.mainloop()
