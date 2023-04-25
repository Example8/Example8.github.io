import tkinter
import customtkinter
from pytube import YouTube
import threading

def startDownload():
    def download():
        try:
            ytlink = link.get()
            ytObject = YouTube(ytlink)
            video = ytObject.streams.get_highest_resolution()

            title.configure(text=ytObject.title, text_color="white")
            finishLabel.config(text="")

            video.download()
            finishLabel.config(text="Downloaded!")
        except:
            finishLabel.config(text="Download Error", text_color="red")
        
    thread = threading.Thread(target=download)
    thread.start()

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#our app Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding Ui Elements
title = customtkinter.CTkLabel(app, text= "Insert a Youtube link")
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width= 350, height = 40, textvariable=url_var)
link.pack()

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#run app
app.mainloop()
