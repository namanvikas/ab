from tkinter import *
import speedtest
import matplot.pyplot as plt

root=Tk()
root.config(bg="yellowgreen")
root.title("Internet speed test")
root.geometry("900x600")

label=Label(root,text="Internet speed",font=("time",20,"bold"),fg="pink")
label.place(relx=0.5,rely=0.1,anchor=CENTER)

label_upload=Label(root,text="upload speed",font=("comic",18,"bold"),fg="pink")
label_upload.place(relx=0.25,rely=0.5,anchor=CENTER)

label_download=Label(root,text="download speed",font=("comic",18,"bold"),fg="pink")
label_download.place(relx=0.75,rely=0.5,anchor=CENTER)


label_upload_speed=Label(root)
label_upload_speed.place(relx=0.25,rely=0.6,anchor=CENTER)

label_download_speed=Label(root)
label_download_speed.place(relx=0.75,rely=0.6,anchor=CENTER)

def speedcheck():
    speed=speedtest.Speedtest()
    download_speed=round(speed.download()/1000000,2)
    label_download_speed['text']=str(download_speed)+"mbps"

    upload_speed=round(speed.upload()/1000000,2)
    label_upload_speed['text']=str(uplod_speed)+"mbps"
    for i in range(5):
        plt.plot(x,list_download_speed, label="DownloadSpeed")
        plt.legend()
        
        plt.plot(x,list_upload_speed, label="uploadspeed")
        plt.legend()
        
        




btn=Button(root,text="Chech speed",command=speedcheck)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

