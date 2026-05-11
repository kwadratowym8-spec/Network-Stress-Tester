import tkinter as tk
from tkinter import ttk
import threading
import time
import random

class FiveDosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FIVE DOS - Professional Infrastructure Tester")
        self.root.geometry("600x800")
        self.root.configure(bg="#050505")

        # --- TWÓJ NAPIS ASCII ---
        self.ascii_banner = """
___________._______   _______________             ________   ________   _________
\_   _____/|   \   \ /   /\_   _____/             \______ \  \_____  \  /   _____/
 |    __)  |   |\   Y   /  |    __)_                |    |  \  /   |   \ \_____  \ 
 |     \   |   | \     /   |        \               |    `   \/    |    \/        \ 
 \___  /   |___|  \___/   /_______  /              /_______  /\_______  /_______  /
     \/                           \/                       \/         \/        \/ 
        """
        
        self.banner_label = tk.Label(root, text=self.ascii_banner, font=("Consolas", 7, "bold"), 
                                     fg="#ff0000", bg="#050505", justify="left")
        self.banner_label.pack(pady=10)

        # --- KONTENER PANELU ---
        self.container = tk.Frame(root, bg="#050505")
        self.container.pack(pady=5, padx=50, fill='x')

        self.create_input("TARGET IP / DOMAIN:", "127.0.0.1", "target")
        self.create_input("TARGET PORT:", "80", "port")
        self.create_input("DURATION (SEC):", "200", "time")

        # Metoda
        tk.Label(self.container, text="METHOD:", fg="#666", bg="#050505", font=("Arial", 8, "bold")).pack(anchor='w')
        self.method_var = tk.StringVar()
        self.method_select = ttk.Combobox(self.container, textvariable=self.method_var, 
                                          values=["UDP-FLOOD", "TCP-STORM", "HTTPS-TLS", "API-VIP (50Gbps)"])
        self.method_select.current(3)
        self.method_select.pack(pady=5, fill='x')

        # Suwak Speed
        tk.Label(self.container, text="FLOOD INTENSITY:", fg="#666", bg="#050505", font=("Arial", 8, "bold")).pack(anchor='w')
        self.speed_slider = tk.Scale(self.container, from_=1, to=100, orient='horizontal', bg="#050505", fg="red", highlightthickness=0)
        self.speed_slider.set(75)
        self.speed_slider.pack(pady=5, fill='x')

        # Pasek postępu
        self.progress = ttk.Progressbar(self.container, orient='horizontal', mode='determinate')
        self.progress.pack(pady=15, fill='x')

        # PRZYCISK ATTACK
        self.attack_btn = tk.Button(root, text="ATTACK", bg="#ff0000", fg="white", font=("Impact", 24), 
                                    activebackground="#550000", relief="flat", command=self.start_thread)
        self.attack_btn.pack(pady=10, padx=50, fill='x')

        # STOPKA INFRASTRUKTURY
        self.footer = tk.Label(root, text="NODES: ONLINE | API: READY | SYSTEM: PROTECTED", 
                               font=("Courier", 8), fg="#00ff00", bg="#050505")
        self.footer.pack(side="bottom", pady=10)

        # LOGI
        self.log_box = tk.Text(root, height=12, bg="#000", fg="#ff0000", font=("Consolas", 9), borderwidth=0)
        self.log_box.pack(pady=5, padx=20, fill='both')

    def create_input(self, label, default, attr):
        tk.Label(self.container, text=label, fg="#666", bg="#050505", font=("Arial", 8, "bold")).pack(anchor='w')
        ent = tk.Entry(self.container, bg="#111", fg="white", insertbackground="red", borderwidth=1, relief="flat", justify="center")
        ent.insert(0, default)
        ent.pack(pady=5, fill='x', ipady=5)
        setattr(self, f"{attr}_entry", ent)

    def log(self, msg):
        self.log_box.insert(tk.END, f"[#] {msg}\n")
        self.log_box.see(tk.END)

    def start_thread(self):
        threading.Thread(target=self.execute_attack, daemon=True).start()

    def execute_attack(self):
        target = self.target_entry.get()
        self.log(f"SCANNING TARGET: {target}...")
        time.sleep(1)
        self.log(f"LOCATING NODES... [WARSAW, PL] [MOLDOVA, CH] [FRANKFURT, DE]")
        time.sleep(1)
        self.log("INJECTING PACKETS VIA API CLUSTER...")
        
        self.progress['value'] = 0
        duration = int(self.time_entry.get())
        
        for i in range(duration):
            self.progress['value'] = (i / duration) * 100
            if i % 10 == 0:
                self.log(f"ATTACKING... POWER: {random.uniform(48.5, 50.8):.2f} Gbps")
            time.sleep(1)
        
        self.log("ATTACK SEQUENCE COMPLETED.")
        self.progress['value'] = 100

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TProgressbar", thickness=10, background="red", troughcolor="#111")
    app = FiveDosApp(root)
    root.mainloop()
