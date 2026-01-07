# 🧾 Gerador de QR Code (Link → PNG)

Aplicação simples para **gerar QR Codes a partir de links**, com **interface gráfica no Windows**.  
O QR Code é salvo automaticamente em formato **PNG** no mesmo local onde o programa é executado.

---

## ✨ Funcionalidades

- Interface gráfica (Windows)
- Geração de QR Code a partir de qualquer link
- Salvamento automático em **PNG**
- Não exige conhecimento técnico do usuário final
- Pode ser distribuído como **executável (.exe)**

---

## 📁 Estrutura do projeto

main.py
├── README.md
└── dist/

## 🚀 Como executar (modo Python)

### Pré-requisitos
- Python 3.10+
- Bibliotecas:
  - `qrcode`
  - `pillow`
  - `tkinter` (já incluso no Python)

### Instalação das dependências
```bash
pip install qrcode[pil]