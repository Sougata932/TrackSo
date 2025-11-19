import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from datetime import datetime

class ExpenseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("💸 Expense Tracker")
        self.geometry("700x550")
        self.resizable(False, False)

        self.bg_color1 = "#e3f2fd"
        self.bg_color2 = "#bbdefb"
        self.font_main = ("Poppins", 12)
        self.configure(bg=self.bg_color1)

        self.create_gradient_background()
        self.create_widgets()
    def create_gradient_background(self):
        self.canvas = tk.Canvas(self, width=700, height=550, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        for i in range(0, 550):
            r = 227 - int(i * (227 - 187) / 550)
            g = 242 - int(i * (242 - 222) / 550)
            b = 253 - int(i * (253 - 251) / 550)
            color = f"#{r:02x}{g:02x}{b:02x}"
            self.canvas.create_line(0, i, 700, i, fill=color)

    def create_widgets(self):
        frame = tk.Frame(self.canvas, bg=self.bg_color1)
        frame.place(relx=0.5, rely=0.2, anchor="center")

        tk.Label(frame, text="Amount (₹):", font=self.font_main, bg=self.bg_color1).grid(row=0, column=0, padx=10, pady=5)
        self.amount_entry = tk.Entry(frame, font=self.font_main, width=15, bg="white", fg="black", relief="flat")
        self.amount_entry.grid(row=0, column=1)

        tk.Label(frame, text="Category:", font=self.font_main, bg=self.bg_color1).grid(row=0, column=2, padx=10)
        self.category_box = ttk.Combobox(frame, values=["Food", "Travel", "Shopping", "Bills", "Other"], font=self.font_main, width=13)
        self.category_box.grid(row=0, column=3)
        self.category_box.current(0)

        tk.Label(frame, text="Description:", font=self.font_main, bg=self.bg_color1).grid(row=1, column=0, padx=10)
        self.desc_entry = tk.Entry(frame, font=self.font_main, width=45, bg="white", fg="black", relief="flat")
        self.desc_entry.grid(row=1, column=1, columnspan=3, pady=5)

        self.add_btn = tk.Button(self.canvas, text="➕ Add Expense", font=("Poppins", 11, "bold"), bg="#4CAF50", fg="white", relief="flat", command=self.add_expense)
        self.add_btn.place(relx=0.35, rely=0.35, anchor="center")
        self.add_btn.bind("<Enter>", lambda e: self.on_hover(self.add_btn, "#45a049"))
        self.add_btn.bind("<Leave>", lambda e: self.on_hover(self.add_btn, "#4CAF50"))

        self.save_btn = tk.Button(self.canvas, text="💾 Save CSV", font=("Poppins", 11, "bold"), bg="#2196F3", fg="white", relief="flat", command=self.save_csv)
        self.save_btn.place(relx=0.65, rely=0.35, anchor="center")
        self.save_btn.bind("<Enter>", lambda e: self.on_hover(self.save_btn, "#1976D2"))
        self.save_btn.bind("<Leave>", lambda e: self.on_hover(self.save_btn, "#2196F3"))

        columns = ("Date", "Amount", "Category", "Description")
        self.table = ttk.Treeview(self.canvas, columns=columns, show="headings", height=10)
        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=150 if col != "Description" else 220, anchor="center")

        self.table.place(relx=0.5, rely=0.6, anchor="center")

        scrollbar = ttk.Scrollbar(self.canvas, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=0.93, rely=0.6, anchor="center", height=220)

        self.total_label = tk.Label(self.canvas, text="Total Spent: ₹0", font=("Poppins", 13, "bold"), bg=self.bg_color2, fg="#E53935")
        self.total_label.place(relx=0.5, rely=0.9, anchor="center")

        self.total = 0.0

    def on_hover(self, widget, color):
        widget["background"] = color

    def add_expense(self):
        amount = self.amount_entry.get().strip()
        category = self.category_box.get().strip()
        desc = self.desc_entry.get().strip()

        if not amount or not amount.isdigit():
            messagebox.showerror("Error", "Please enter a valid amount!")
            return

        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.table.insert("", "end", values=(date, f"₹{amount}", category, desc))

        self.total += float(amount)
        self.total_label.config(text=f"Total Spent: ₹{self.total:.2f}")

        self.amount_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def save_csv(self):
        file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file:
            return

        with open(file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount", "Category", "Description"])
            for row in self.table.get_children():
                writer.writerow(self.table.item(row)["values"])

        messagebox.showinfo("Saved", f"Expenses saved to {file}")

if __name__ == "__main__":
    app = ExpenseApp()
    app.mainloop()
