import tkinter as tk
from tkinter import messagebox

def suggest_career():
    try:
        math = int(math_entry.get())
        programming = int(programming_entry.get())
        biology = int(biology_entry.get())
        creativity = int(creativity_entry.get())
        business = int(business_entry.get())

        scores = {
            "Software Engineer": programming + math,
            "Data Scientist": math + programming,
            "Doctor / Biotechnologist": biology,
            "Graphic Designer": creativity,
            "Business Analyst": business + math
        }

        career = max(scores, key=scores.get)

        result_label.config(text="Recommended Career: " + career)

    except:
        messagebox.showerror("Error", "Please enter numbers between 1 and 5")


app = tk.Tk()
app.title("AI Career Suggestion System")
app.geometry("400x350")

title = tk.Label(app, text="AI Career Suggestion System", font=("Arial", 16))
title.pack(pady=10)

tk.Label(app, text="Rate interest from 1 to 5").pack()

tk.Label(app, text="Mathematics").pack()
math_entry = tk.Entry(app)
math_entry.pack()

tk.Label(app, text="Programming").pack()
programming_entry = tk.Entry(app)
programming_entry.pack()

tk.Label(app, text="Biology").pack()
biology_entry = tk.Entry(app)
biology_entry.pack()

tk.Label(app, text="Creative Design").pack()
creativity_entry = tk.Entry(app)
creativity_entry.pack()

tk.Label(app, text="Business").pack()
business_entry = tk.Entry(app)
business_entry.pack()

tk.Button(app, text="Get Career Suggestion", command=suggest_career).pack(pady=15)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack()

app.mainloop()