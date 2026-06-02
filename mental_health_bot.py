import tkinter as tk
from tkinter import messagebox, scrolledtext
import random

class CarnellaBot:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Carnella 2.0")
        self.root.geometry("600x700")
        
        # Show welcome
        messagebox.showinfo("Welcome", "✨ Carnella 2.0\n\nKwa crisis: 0722 178 177")
        
        # Create chat display
        self.chat = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", font=("Arial", 11))
        self.chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Input frame
        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.entry = tk.Entry(input_frame, font=("Arial", 12))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.entry.bind("<Return>", lambda e: self.send())
        
        send_btn = tk.Button(input_frame, text="TUMA", command=self.send, font=("Arial", 11, "bold"), bg="#228B22", fg="white")
        send_btn.pack(side=tk.RIGHT)
        
        # Load responses
        self.responses = {
            "hi": ["Vipi msee! 👋 Niko hapa. Unahisi vipi?", "Poa! Carnella 2.0 iko ready. Niseme!"],
            "sad": ["Aiiish msee... 😔 Nikusikie. Unataka uzungumze?", "Pole sana. Hii pia itapita. 💜"],
            "stress": ["Stress ni nyingi eh? 😅 Pumzia kidogo. Unaweza!", "Msee relax! Take a break."],
            "crisis": ["🚨 PIGA 0722 178 177 SASA! Usikae peke yako!"]
        }
        self.crisis_words = ["suicide", "kill myself", "hurt myself", "die"]
        
    def get_reply(self, text):
        text = text.lower()
        for word in self.crisis_words:
            if word in text:
                return self.responses["crisis"][0]
        if any(w in text for w in ["hi", "hello", "vipi"]):
            return random.choice(self.responses["hi"])
        if any(w in text for w in ["sad", "down", "depressed"]):
            return random.choice(self.responses["sad"])
        if any(w in text for w in ["stress", "tired"]):
            return random.choice(self.responses["stress"])
        return "Nikusikie msee. Carnella 2.0 iko listening. 💜"
    
    def send(self):
        msg = self.entry.get().strip()
        if not msg:
            return
        
        self.entry.delete(0, tk.END)
        
        # Show user message
        self.chat.config(state="normal")
        self.chat.insert(tk.END, f"Wewe: {msg}\n\n")
        
        # Show bot reply
        reply = self.get_reply(msg)
        self.chat.insert(tk.END, f"Carnella 2.0: {reply}\n\n")
        
        self.chat.see(tk.END)
        self.chat.config(state="disabled")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CarnellaBot(root)
    app.run()