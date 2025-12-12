import pandas as pd
from sklearn.linear_model import LinearRegression
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox
from tkinter import filedialog, Listbox, MULTIPLE, Canvas


df = None


def choose_file():
    global df
    filepath = filedialog.askopenfilename(
        title=" Pilih file CSV ",
        filetypes=[("CSV Files", "*.csv")]
    )
    if not filepath:
        return

    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()

    columns = list(df.columns)

    # Update dropdown Y
    y_combo.configure(values=columns)
    y_combo.set("")

    # Update listbox X
    x_listbox.delete(0, "end")
    for col in columns:
        x_listbox.insert("end", col)

    Messagebox.show_info(" Dataset berhasil dimuat! ", " Sukses! ")


def run_regression():
    global df
    if df is None:
        Messagebox.show_error(" Upload CSV terlebih dahulu! ", "Error")
        return

    y_var = y_combo.get()
    x_indices = x_listbox.curselection()

    if not y_var:
        Messagebox.show_error(" Pilih variabel Y! ", "Error")
        return
    if len(x_indices) == 0:
        Messagebox.show_error(" Pilih minimal satu variabel X! ", "Error")
        return

    X_vars = [x_listbox.get(i) for i in x_indices]

    try:
        data = df[[y_var] + X_vars].dropna()

        X = data[X_vars]
        y = data[y_var]

        model = LinearRegression()
        model.fit(X, y)

        coef_text = "\n".join([f"- {col}: {coef:.4f}" for col, coef in zip(X_vars, model.coef_)])

        Messagebox.show_info(
            f"""
Hasil Regresi Linier Berganda

Y: {y_var}
X: {", ".join(X_vars)}

Intercept: {model.intercept_:.4f}

Koefisien:
{coef_text}

R-Squared (R²): {model.score(X, y):.4f}
""",
            " Hasil Regresi "
        )

    except Exception as e:
        Messagebox.show_error(f"Terjadi kesalahan:\n{e}", "Error")


# UI

app = tb.Window(themename="superhero")
app.title("Analisis Regresi Linear Berganda")
app.geometry("950x900")
app.resizable(False, False)

# === TITLE ===
tb.Label(app,
         text="Analisis Regresi Linier Berganda",
         font=("Segoe UI", 30, "bold"),
         bootstyle="light").pack(pady=25)

# === CANVAS UTAMA ===
canvas_frame = tb.Frame(app)
canvas_frame.pack()

canvas = Canvas(
    canvas_frame,
    width=880,
    height=760,
    bg=app.cget("background"),
    highlightthickness=0
)
canvas.pack()

def round_rect(x1, y1, x2, y2, r, color):
    canvas.create_arc(x1, y1, x1+2*r, y1+2*r, start=90, extent=90,
                      fill=color, outline=color)
    canvas.create_arc(x2-2*r, y1, x2, y1+2*r, start=0, extent=90,
                      fill=color, outline=color)
    canvas.create_arc(x1, y2-2*r, x1+2*r, y2, start=180, extent=90,
                      fill=color, outline=color)
    canvas.create_arc(x2-2*r, y2-2*r, x2, y2, start=270, extent=90,
                      fill=color, outline=color)
    canvas.create_rectangle(x1+r, y1, x2-r, y2, fill=color, outline=color)
    canvas.create_rectangle(x1, y1+r, x2, y2-r, fill=color, outline=color)

# === BACKGROUND HITAM (besar) ===
round_rect(10, 10, 860, 740, r=50, color="#2C2F33")


# === CONTENT
# === STYLE FRAME HITAM ===
style = tb.Style()
style.configure("Black.TFrame", background="#2C2F33")

# === CONTENT FRAME (warna hitam) ===
content = tb.Frame(canvas_frame, style="Black.TFrame")
content.place(relx=0.5, y=380, anchor="center")

# === Upload CSV ===
btn_upload = tb.Button(content, text="  Upload CSV  ", width=20,
                       bootstyle="info", command=choose_file)
btn_upload.grid(row=0, column=0, pady=(10, 25))

# === PILIH VARIABEL Y ===
tb.Label(content, text="  Pilih Variabel Y:  ",
         font=("Segoe UI", 12, "bold"),
         bootstyle="light").grid(row=1, column=0, sticky="w")

y_combo = tb.Combobox(content, width=70)
y_combo.grid(row=2, column=0, pady=7)

# === PILIH VARIABEL X ===
tb.Label(content, text="  Pilih Variabel X (bisa lebih dari satu):  ",
         font=("Segoe UI", 12, "bold"),
         bootstyle="light").grid(row=3, column=0, sticky="w", pady=(20, 7))

x_listbox = Listbox(content, width=70, height=12, selectmode=MULTIPLE)
x_listbox.grid(row=4, column=0, pady=5)

# === BUTTON RUN ===
btn_run = tb.Button(
    content, text=" Jalankan Regresi ",
    width=30, bootstyle="success",
    command=run_regression
)
btn_run.grid(row=5, column=0, pady=25)

app.mainloop()