import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

def calculate_denominations():
    try:
        amount = int(entry_amount.get())
        denominations = [100, 50, 20, 10, 5, 1]
        result_text = ""
        
        for denom in denominations:
            count = amount // denom
            amount %= denom
            if count > 0:
                result_text += f"{denom}: {count}\n"
        
        label_result.config(text=result_text if result_text else "No denominations needed")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Create the main window
root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("300x300")


# Create widgets
label_amount = tk.Label(root, text="Enter Amount:")
label_amount.pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

btn_calculate = tk.Button(root, text="Calculate", command=calculate_denominations)
btn_calculate.pack()

label_result = tk.Label(root, text="Denominations:")
label_result.pack()

# Run the Tkinter event loop
root.mainloop()
