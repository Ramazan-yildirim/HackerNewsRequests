import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Hacker News")

url = "https://news.ycombinator.com"

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, "html.parser")

link_counter = 0

start_index = 2
end_index = 30

link_display = scrolledtext.ScrolledText(window, width=146, height=30)
link_display.pack(padx=10, pady=10)


for link in soup.find_all("a"):
    href = link.get("href")
    if href and href.startswith("https"):
        link_counter += 1
        if start_index <= link_counter <= end_index:
            link_display.insert(tk.END, f"{href}\n\n")
        if link_counter > end_index:
            break

window.mainloop()
