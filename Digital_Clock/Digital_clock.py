import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Smart Digital Clock")
root.geometry("480x240")
root.configure(bg="#ffffff")

# ---------------- THEMES ----------------
themes = {
    "Light": {"bg": "#ffffff", "fg": "#000000"},
    "Dark": {"bg": "#1a1a1a", "fg": "#ffffff"},
    "Neon": {"bg": "#000000", "fg": "#00ffea"},
    "Sky Blue": {"bg": "#87cefa", "fg": "#002233"}
}

current_theme = "Light"


# ---------------- LABELS ----------------
label = tk.Label(root, font=("SF Pro Display", 55, "bold"), fg="#000000", bg="#ffffff")
label.pack(pady=10)

date_label = tk.Label(root, font=("SF Pro Display", 18), fg="#707070", bg="#ffffff")
date_label.pack()


# ---------------- CLOCK FUNCTION ----------------
def time():
    label.config(text=strftime("%I:%M:%S %p"))
    date_label.config(text=strftime("%A, %d %B %Y"))
    root.after(1000, time)


# ---------------- APPLY THEME FUNCTION ----------------
def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    theme = themes[theme_name]

    root.configure(bg=theme["bg"])
    label.config(bg=theme["bg"], fg=theme["fg"])
    date_label.config(bg=theme["bg"], fg=theme["fg"])
    theme_button.config(bg=theme["bg"], fg=theme["fg"], activebackground=theme["bg"])


# ---------------- THEME DROPDOWN ----------------
theme_var = tk.StringVar()
theme_var.set("Choose Theme")

def theme_changed(event=None):
    apply_theme(theme_var.get())

theme_menu = tk.OptionMenu(root, theme_var, *themes.keys(), command=theme_changed)
theme_menu.config(font=("SF Pro Display", 12), bg="#cccccc")
theme_menu.place(x=230, y=50)


# ---------------- DARK MODE TOGGLE BUTTON ----------------
def toggle_dark_mode():
    if current_theme != "Dark":
        apply_theme("Dark")
    else:
        apply_theme("Light")

theme_button = tk.Button(root, text="🌙 Toggle Dark Mode", font=("SF Pro Display", 12), command=toggle_dark_mode)
theme_button.place(x=900, y=50)


# ---------------- START CLOCK ----------------
time()
root.mainloop()
