#!/usr/bin/env python3
import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time

try:
    import pyautogui
except ImportError:
    print("This script requires pyautogui. Install with:\n    pip install pyautogui")
    exit(1)

class AutoTyperApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Auto Typer")
        self.geometry("600x400")
        self.resizable(False, False)

        # Text input label
        tk.Label(self, text="Paste or type your large content below:").pack(pady=(10, 0))

        # Text area
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=70, height=15)
        self.text_area.pack(padx=10, pady=5)

        # Speed slider
        frame = tk.Frame(self)
        frame.pack(pady=10)
        tk.Label(frame, text="Delay between keystrokes (sec):").grid(row=0, column=0, padx=(0, 10))
        self.speed_slider = tk.Scale(frame, from_=0.0, to=1.0, resolution=0.01,
                                     orient=tk.HORIZONTAL, length=300)
        self.speed_slider.set(0.02)  # default ~200 chars/sec
        self.speed_slider.grid(row=0, column=1)

        # Start button
        self.start_btn = tk.Button(self, text="Start Typing ▶", command=self.on_start,
                                   bg="#4CAF50", fg="white", padx=10, pady=5)
        self.start_btn.pack(pady=(0, 15))

    def on_start(self):
        text = self.text_area.get("1.0", tk.END).rstrip("\n")
        if not text:
            messagebox.showwarning("No text", "Please paste or type some text first.")
            return

        delay = self.speed_slider.get()
        confirm = messagebox.askyesno("Ready?",
            "Click YES, then you have 5 seconds to focus the cursor where you want typing to happen.")
        if not confirm:
            return

        # Disable UI
        self.start_btn.config(state=tk.DISABLED)
        self.speed_slider.config(state=tk.DISABLED)
        self.text_area.config(state=tk.DISABLED)

        # Start background thread
        threading.Thread(target=self._do_typing, args=(text, delay), daemon=True).start()

    def _do_typing(self, text, delay):
        # Countdown
        for i in range(5, 0, -1):
            self.start_btn.config(text=f"Typing in {i}…")
            self.update()
            time.sleep(1)

        # Hide the window
        self.withdraw()
        time.sleep(1.5)  # Time to focus target app

        try:
            pyautogui.click()  # Focus where mouse is
            time.sleep(0.2)
            pyautogui.write(text, interval=delay)  # Typing text
        except Exception as e:
            print(f"Error during typing: {e}")
            messagebox.showerror("Error", str(e))
        finally:
            self.deiconify()
            self.start_btn.config(text="Start Typing ▶", state=tk.NORMAL)
            self.speed_slider.config(state=tk.NORMAL)
            self.text_area.config(state=tk.NORMAL)
            messagebox.showinfo("Done", "Finished typing!")

if __name__ == "__main__":
    app = AutoTyperApp()
    app.mainloop()
