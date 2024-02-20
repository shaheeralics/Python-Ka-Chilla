import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class QazaNamazCounterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Qaza Namaz Counter")

        # Variables to store the counts and dates
        self.start_date_var = tk.StringVar()
        self.end_date_var = tk.StringVar()
        self.fajr_count = tk.IntVar()
        self.dhuhr_count = tk.IntVar()
        self.asr_count = tk.IntVar()
        self.maghrib_count = tk.IntVar()
        self.isha_count = tk.IntVar()

        # Create and pack widgets
        tk.Label(master, text="Qaza Namaz Counter", font=("Helvetica", 20)).grid(row=0, column=0, columnspan=2, pady=1)
        tk.Label(master, text='''By Shaheer Ali''', font=("Helvetica", 16)).grid(row=1, column=1, columnspan=3, pady=5)
        
        tk.Label(master, text='''Date Format : YYYY-MM-DD''', font=("Helvetica", 11)).grid(row=2, column=0, columnspan=3, pady=5)
        
        tk.Label(master, text="Start Date:").grid(row=3, column=0)
        tk.Entry(master, textvariable=self.start_date_var).grid(row=3, column=1)

        tk.Label(master, text="End Date:").grid(row=4, column=0)
        tk.Entry(master, textvariable=self.end_date_var).grid(row=4, column=1)

        tk.Label(master, text="Fajr:").grid(row=6, column=0)
        tk.Entry(master, textvariable=self.fajr_count).grid(row=6, column=1)

        tk.Label(master, text="Dhuhr:").grid(row=7, column=0)
        tk.Entry(master, textvariable=self.dhuhr_count).grid(row=7, column=1)

        tk.Label(master, text="Asr:").grid(row=8, column=0)
        tk.Entry(master, textvariable=self.asr_count).grid(row=8, column=1)

        tk.Label(master, text="Maghrib:").grid(row=9, column=0)
        tk.Entry(master, textvariable=self.maghrib_count).grid(row=9, column=1)

        tk.Label(master, text="Isha:").grid(row=10, column=0)
        tk.Entry(master, textvariable=self.isha_count).grid(row=10, column=1)

        tk.Button(master, text="Qaza Namaz Find Karei", command=self.calculate_counts).grid(row=12, column=0, columnspan=2, pady=10)
        tk.Label(master, text='''Power Of Python ❤️💕😁''', font=("Helvetica", 16)).grid(row=13, column=0, columnspan=3, pady=5)

    def calculate_counts(self):
        # Retrieve dates
        start_date_str = self.start_date_var.get()
        end_date_str = self.end_date_var.get()

        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
            return

        # Calculate the number of days between start and end dates
        delta = end_date - start_date
        num_days = delta.days + 1  # Including the end date

        # Set the counts based on the number of days
        self.fajr_count.set(num_days)
        self.dhuhr_count.set(num_days)
        self.asr_count.set(num_days)
        self.maghrib_count.set(num_days)
        self.isha_count.set(num_days)

def main():
    root = tk.Tk()
    app = QazaNamazCounterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()