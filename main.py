import requests
import tkinter as tk
from tkinter import messagebox

def get_stock_data(api_key, symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        if "Global Quote" in data:
            stock_data = data["Global Quote"]
            return stock_data
        elif "Note" in data:
            raise Exception(data["Note"])
        else:
            raise Exception("Borsa verisi alınamadı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Borsa verisi alınırken bir hata oluştu:\n{str(e)}")
        return None

def show_stock_data():
    symbol = symbol_entry.get().upper()
    stock_data = get_stock_data(api_key, symbol)

    if stock_data is not None:
        messagebox.showinfo("Borsa Verisi", f"{symbol} Borsa Verisi:\n"
                                            f"Son Fiyat: {stock_data['05. price']}\n"
                                            f"Değişim: {stock_data['09. change']}")

# Tkinter arayüzü oluşturma
app = tk.Tk()
app.title("Borsa Takip Uygulaması")
app.geometry("300x150")

label = tk.Label(app, text="Borsa simgesini girin (örn. AAPL):")
label.pack(pady=10)

symbol_entry = tk.Entry(app)
symbol_entry.pack(pady=5)

button = tk.Button(app, text="Borsa Verisini Göster", command=show_stock_data)
button.pack(pady=10)

# API anahtarını burada girin:
api_key = "BURAYA_API_ANAHTARINIZI_YAZIN"

app.mainloop()
