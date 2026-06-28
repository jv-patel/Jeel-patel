from tkinter import *
from tkinter import ttk, messagebox

HOROSCOPES = {
    "Aries": "Does your house look like a cyclone hit it? Your tidy nature should drive you to clean it up.",
    "Taurus": "An exciting phone call or email could come from a friend who has some great news for you, Taurus.",
    "Gemini": "An online group could form today, Gemini.",
    "Cancer": "Communication involving romance could come unexpectedly today, Cancer.",
    "Leo": "A chance to increase your income by participating in an artistic project could come your way today.",
    "Virgo": "Have you been feeling stagnant lately, Virgo?",
    "Libra": "Inspiration could hit today, Libra.",
    "Scorpio": "You might have the chance to speak with new people in interesting fields, Scorpio.",
    "Sagittarius": "Information from surprising sources could lead to fortunate career breaks.",
    "Capricorn": "A passionate encounter with a love partner might cement the bond between you.",
    "Aquarius": "Today you may suddenly regain your strength and be raring to go.",
    "Pisces": "Love and romance are highlighted today, Pisces.",
}

ZODIAC_EMOJI = {
    "Aries": " ", "Taurus": " ", "Gemini": " ", "Cancer": " ",
    "Leo": " ", "Virgo": " ", "Libra": " ", "Scorpio": " ",
    "Sagittarius": " ", "Capricorn": "  ", "Aquarius": " ’", "Pisces": " ",
}

# ---------- Color palette ----------
BG_DARK = "#1b1035"          # deep night-sky purple
BG_PANEL = "#2a1a4d"         # slightly lighter panel
ACCENT = "#ffd166"           # golden star accent
ACCENT_HOVER = "#ffe08a"
TEXT_LIGHT = "#f4f1ff"
TEXT_MUTED = "#c9bfe8"
ENTRY_BG = "#3a2766"


def show():
    name = name_var.get().strip()
    sign = sign_var.get()
    if not name:
        messagebox.showerror("Missing Name", "Please enter your name first.")
        return

    emoji = ZODIAC_EMOJI.get(sign, " ")
    result_title.config(text=f"{emoji}  {sign}  {emoji}")
    text.config(state=NORMAL)
    text.delete("1.0", END)
    text.insert(END, f"Hello {name}! ", "greeting")
    text.insert(END, "Here's what the stars say:\n\n", "subtle")
    text.insert(END, HOROSCOPES.get(sign, ""), "body")
    text.config(state=DISABLED)


def reset():
    name_var.set("")
    sign_var.set("Aries")
    result_title.config(text="")
    text.config(state=NORMAL)
    text.delete("1.0", END)
    text.config(state=DISABLED)


# ---------- Root window (mobile phone layout) ----------
MOBILE_WIDTH = 375
MOBILE_HEIGHT = 720

root = Tk()
root.title(" Horoscope Prediction ")
root.geometry(f"{MOBILE_WIDTH}x{MOBILE_HEIGHT}")
root.minsize(MOBILE_WIDTH, MOBILE_HEIGHT)
root.maxsize(MOBILE_WIDTH, MOBILE_HEIGHT)  # lock to phone-like proportions
root.resizable(False, False)
root.configure(bg=BG_DARK)

# ---------- ttk styling ----------
style = ttk.Style()
try:
    style.theme_use("clam")
except Exception:
    pass

style.configure(
    "TCombobox",
    fieldbackground=ENTRY_BG,
    background=ENTRY_BG,
    foreground=TEXT_LIGHT,
    arrowcolor=ACCENT,
    bordercolor=ACCENT,
    padding=6,
)
style.map(
    "TCombobox",
    fieldbackground=[("readonly", ENTRY_BG)],
    foreground=[("readonly", TEXT_LIGHT)],
)

# ---------- Header ----------
header = Frame(root, bg=BG_DARK)
header.pack(fill=X, pady=(16, 4))

Label(
    header,
    text="Horoscope ",
    font=("Georgia", 26, "bold"),
    fg=ACCENT,
    bg=BG_DARK,
).pack()

Label(
    header,
    text="What do the stars say today?",
    font=("Helvetica", 9, "italic"),
    fg=TEXT_MUTED,
    bg=BG_DARK,
    wraplength=MOBILE_WIDTH - 40,
    justify="center",
).pack(pady=(2, 0))

# ---------- Input card ----------
card = Frame(root, bg=BG_PANEL, padx=16, pady=14)
card.pack(padx=14, pady=10, fill=X)

name_var = StringVar()
sign_var = StringVar(value="Aries")

Label(card, text="Your Name", font=("Helvetica", 11, "bold"), fg=TEXT_LIGHT, bg=BG_PANEL).grid(
    row=0, column=0, sticky="w", pady=(0, 4)
)
name_entry = Entry(
    card,
    textvariable=name_var,
    font=("Helvetica", 12),
    bg=ENTRY_BG,
    fg=TEXT_LIGHT,
    insertbackground=TEXT_LIGHT,
    relief=FLAT,
    highlightthickness=1,
    highlightbackground=ACCENT,
    highlightcolor=ACCENT,
)
name_entry.grid(row=1, column=0, sticky="ew", pady=(0, 16), ipady=6)

Label(card, text="Zodiac Sign", font=("Helvetica", 11, "bold"), fg=TEXT_LIGHT, bg=BG_PANEL).grid(
    row=2, column=0, sticky="w", pady=(0, 4)
)
sign_box = ttk.Combobox(
    card,
    textvariable=sign_var,
    values=list(HOROSCOPES.keys()),
    state="readonly",
    font=("Helvetica", 12),
)
sign_box.grid(row=3, column=0, sticky="ew", ipady=4)

card.columnconfigure(0, weight=1)

# ---------- Buttons (stacked, full width for mobile) ----------
btn_frame = Frame(root, bg=BG_DARK)
btn_frame.pack(pady=(2, 8), padx=14, fill=X)


def _make_button(parent, label, command, bg, fg, hover_bg):
    b = Button(
        parent,
        text=label,
        command=command,
        font=("Helvetica", 11, "bold"),
        bg=bg,
        fg=fg,
        activebackground=hover_bg,
        activeforeground=fg,
        relief=FLAT,
        bd=0,
        padx=18,
        pady=10,
        cursor="hand2",
    )
    b.bind("<Enter>", lambda e: b.config(bg=hover_bg))
    b.bind("<Leave>", lambda e: b.config(bg=bg))
    return b


show_btn = _make_button(btn_frame, " Show Horoscope", show, ACCENT, BG_DARK, ACCENT_HOVER)
show_btn.pack(fill=X, pady=(0, 6))

reset_btn = _make_button(btn_frame, "Reset", reset, BG_PANEL, TEXT_LIGHT, ENTRY_BG)
reset_btn.pack(fill=X)

# ---------- Result panel ----------
result_card = Frame(root, bg=BG_PANEL, padx=14, pady=12)
result_card.pack(padx=14, pady=(4, 16), fill=BOTH, expand=True)

result_title = Label(
    result_card,
    text="",
    font=("Georgia", 14, "bold"),
    fg=ACCENT,
    bg=BG_PANEL,
    wraplength=MOBILE_WIDTH - 60,
)
result_title.pack(anchor="w", pady=(0, 6))

text = Text(
    result_card,
    wrap=WORD,
    font=("Helvetica", 12),
    bg=BG_PANEL,
    fg=TEXT_LIGHT,
    relief=FLAT,
    state=DISABLED,
    highlightthickness=0,
    padx=2,
    pady=2,
)
text.tag_configure("greeting", font=("Helvetica", 12, "bold"), foreground=ACCENT)
text.tag_configure("subtle", font=("Helvetica", 10, "italic"), foreground=TEXT_MUTED)
text.tag_configure("body", font=("Helvetica", 12), foreground=TEXT_LIGHT, spacing1=6, spacing3=2)
text.pack(fill=BOTH, expand=True)

# Allow Enter key in name field to trigger show()
name_entry.bind("<Return>", lambda e: show())

root.mainloop()