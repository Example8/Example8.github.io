import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        video.download()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.config(text="Download Error", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    #Update progress bar
    progressbar.set(float(percentage_of_completion) / 100)

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

#Progress Percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressbar = customtkinter.CTkProgressBar(app, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)


# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#run app
app.mainloop()