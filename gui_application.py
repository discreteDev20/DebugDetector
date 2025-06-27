import tkinter as tk  
from tkinter import scrolledtext  
from main import check_code  

def run_check():  
    code = code_input.get("1.0", tk.END)  
    errors = check_code(code)  
    result_text.delete("1.0", tk.END)  
    for error in errors:  # ✅ Loop  
        result_text.insert(tk.END, error + "\n")  

# ✅ GUI setup  
root = tk.Tk()  
root.title("Debug Detector")  

# Code input  
tk.Label(root, text="Paste code:").pack()  
code_input = scrolledtext.ScrolledText(root, height=10)  
code_input.pack()  

# Check button  
tk.Button(root, text="Check for Errors", command=run_check).pack()  

# Results  
tk.Label(root, text="Results:").pack()  
result_text = scrolledtext.ScrolledText(root, height=10)  
result_text.pack()  

root.mainloop()  