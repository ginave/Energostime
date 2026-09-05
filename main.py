import time
import tkinter as tk
from tkinter import messagebox

class EnergyTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ENERGY TRACKER")
        self.root.geometry("380x650")
        self.root.configure(bg="#100914")

        # 24 часа кулдауна в секундах
        self.COOLDOWN_DURATION = 24 * 3600
        self.end_time = 0
        self.timer_running = False

        # Заголовок
        title_label = tk.Label(
            root, 
            text="⚡ ENERGY TRACKER", 
            font=("Helvetica", 18, "bold"), 
            bg="#100914", 
            fg="#A855F7"
        )
        title_label.pack(pady=(20, 15))

        # Карточка таймера
        timer_card = tk.Frame(root, bg="#1A0F24", highlightbackground="#3B1459", highlightthickness=1, bd=0)
        timer_card.pack(fill="x", padx=20, pady=5)

        self.status_label = tk.Label(
            timer_card, 
            text="✔ Готов к зарядке!", 
            font=("Helvetica", 14, "bold"), 
            bg="#1A0F24", 
            fg="#A855F7"
        )
        self.status_label.pack(pady=(15, 5))

        self.timer_label = tk.Label(
            timer_card, 
            text="24:00:00", 
            font=("Helvetica", 28, "bold"), 
            bg="#1A0F24", 
            fg="#FFFFFF"
        )
        self.timer_label.pack(pady=5)

        self.drink_btn = tk.Button(
            timer_card, 
            text="⚡ ВЫПИЛ ЭНЕРГОС", 
            font=("Helvetica", 12, "bold"), 
            bg="#8B0000", 
            fg="#FFFFFF", 
            activebackground="#550000", 
            activeforeground="#FFFFFF",
            bd=0, 
            padx=15, 
            pady=10, 
            command=self.drink_energy
        )
        self.drink_btn.pack(pady=(10, 15))

        # Заголовок коллекции
        coll_header = tk.Frame(root, bg="#100914")
        coll_header.pack(fill="x", padx=20, pady=(20, 10))

        coll_title = tk.Label(
            coll_header, 
            text="Моя коллекция", 
            font=("Helvetica", 14, "bold"), 
            bg="#100914", 
            fg="#FFFFFF"
        )
        coll_title.pack(side="left")

        coll_count = tk.Label(
            coll_header, 
            text="3 банки", 
            font=("Helvetica", 11), 
            bg="#100914", 
            fg="#B388FF"
        )
        coll_count.pack(side="right")

        # Список банок
        collection_items = [
            {"name": "BURN Сочная Энергия", "info": "0.449 л • 135 мг кофеина"},
            {"name": "Adrenaline Rush", "info": "0.449 л • 135 мг кофеина"},
            {"name": "Monster Energy", "info": "0.5 л • 160 мг кофеина"},
        ]

        for item in collection_items:
            card = tk.Frame(root, bg="#160C21", highlightbackground="#2C1242", highlightthickness=1, bd=0)
            card.pack(fill="x", padx=20, pady=5)

            info_frame = tk.Frame(card, bg="#160C21")
            info_frame.pack(side="left", padx=12, pady=10)

            item_name = tk.Label(
                info_frame, 
                text=item["name"], 
                font=("Helvetica", 12, "bold"), 
                bg="#160C21", 
                fg="#FFFFFF", 
                anchor="w"
            )
            item_name.pack(fill="x")

            item_desc = tk.Label(
                info_frame, 
                text=item["info"], 
                font=("Helvetica", 10), 
                bg="#160C21", 
                fg="#B388FF", 
                anchor="w"
            )
            item_desc.pack(fill="x")

            add_btn = tk.Button(
                card, 
                text="+", 
                font=("Helvetica", 14, "bold"), 
                bg="#2C1242", 
                fg="#A855F7", 
                activebackground="#3B1459", 
                activeforeground="#FFFFFF",
                bd=0, 
                width=3, 
                command=self.drink_energy
            )
            add_btn.pack(side="right", padx=10, pady=10)

    def drink_energy(self):
        if self.timer_running:
            messagebox.showwarning("Кулдаун", "Кулдаун ещё не закончился!")
            return

        self.end_time = time.time() + self.COOLDOWN_DURATION
        self.timer_running = True
        self.status_label.config(text="⏳ Кулдаун активен", fg="#FF2E93")
        self.drink_btn.config(state="disabled", bg="#2A1A2A", text="ЗАРЯД ПОЛУЧЕН ⚡")
        self.update_timer()

    def update_timer(self):
        if not self.timer_running:
            return

        remaining = int(self.end_time - time.time())
        if remaining <= 0:
            self.timer_running = False
            self.timer_label.config(text="24:00:00")
            self.status_label.config(text="✔ Готов к зарядке!", fg="#A855F7")
            self.drink_btn.config(state="normal", bg="#8B0000", text="⚡ ВЫПИЛ ЭНЕРГОС")
            messagebox.showinfo("Готово", "Кулдаун сброшен!")
            return

        hours = remaining // 3600
        minutes = (remaining % 3600) // 60
        seconds = remaining % 60
        self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        self.root.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = EnergyTrackerApp(root)
    root.mainloop()
