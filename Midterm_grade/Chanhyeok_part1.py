#Chanhyeok_part1
#%%
import tkinter as tk
from tkinter import ttk
#%%
root=tk.Tk()
root.geometry("400x200")
root.title("Celsius to Fahrenheit")

def temp_convert(a):
    a= float(a)
    z= (a*9/5)+32
    return z

print(temp_convert(2))

def convert_result():
    a= celsius_entry.get()
    result = temp_convert(a)
    convert_result_label.config(text = f"{result}F")
    root.update()


celsius_label=tk.Label(root, text="Enter Celsius:")
celsius_label.grid(row=0, column=0, pady=5, padx=5)
celsius_entry = ttk.Entry(root)
celsius_entry.grid(row=0, column=1, pady=5, padx=5)
convert_button=tk.Button(root, text="Concert", command=convert_result)
convert_button.grid(row=1, column=0, columnspan=2, pady=10)
result_label=tk.Label(root, text="Result:")
result_label.grid(row=2, column=0, pady=10)
convert_result_label=tk.Label(root, text="")
convert_result_label.grid(row=2, column=1, pady=10)

root.mainloop()
# %%
