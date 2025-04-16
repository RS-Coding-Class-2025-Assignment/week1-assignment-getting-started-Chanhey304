#%%
import tkinter as tk
from tkinter import ttk
import time
import threading

#%%
root = tk.Tk()
root.title("Chanhyeok part 2")
root.geometry("300x300")

stop_thread=False
def start_function():
    global stop_thread
    stop_tread=False
    t=threading.Thread(target=process)
    t.start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

def stop_function():
    global stop_thread
    stop_tread=True
    progressbar_a["value"]=0
    progress_label.config(text="0%")
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)


def process():
    for i in range(0, 101):
        global stop_thread
        if stop_thread:
            break
        progressbar_a["value"] = i
        progress_label.config(text=f"{i}%")
        root.update()
        time.sleep(1.2)


progressbar_a= ttk.Progressbar(root, orient='horizontal', mode='determinate', length=100)
progress_label=tk.Label(root, text="0%")
progress_label.pack(pady=10)
progressbar_a.pack(pady=10)
start_button=ttk.Button(root, text="Start", command=start_function)
start_button.pack(pady=10)
stop_button=ttk.Button(root, text="Stop", command=stop_function)
stop_button.config(state=tk.DISABLED)
stop_button.pack(pady=10)

root.mainloop()
# %%
