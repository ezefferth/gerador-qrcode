import qrcode
from qrcode.constants import ERROR_CORRECT_M
import tkinter as tk
from tkinter import messagebox


def gerar_qrcode():
    link = entrada_link.get().strip()

    if not link:
        messagebox.showerror("Erro", "Informe um link válido.")
        return

    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")

    messagebox.showinfo(
        "Sucesso",
        "QR Code gerado com sucesso!\nArquivo: qrcode.png"
    )


# ---------------- INTERFACE ----------------

janela = tk.Tk()
janela.title("Gerador de QR Code")
janela.geometry("420x180")
janela.resizable(False, False)

tk.Label(
    janela,
    text="Cole o link abaixo:",
    font=("Segoe UI", 10)
).pack(pady=(15, 5))

entrada_link = tk.Entry(
    janela,
    width=55
)
entrada_link.pack(pady=5)
entrada_link.focus()

tk.Button(
    janela,
    text="Gerar QR Code",
    command=gerar_qrcode,
    width=20,
    height=2
).pack(pady=15)

tk.Label(
    janela,
    text="Desenvolvido por Ezéfferth C. A. Fernandes",
    font=("Segoe UI", 8),
    fg="gray"
).pack(side="bottom", pady=5)

janela.mainloop()