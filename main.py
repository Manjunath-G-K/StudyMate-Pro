import customtkinter as ctk
from tkinter import messagebox

class StudyMate(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("StudyMate Pro")
        self.geometry("400x600")
        self.resizable(False, False)

        # Appearance
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Variables
        self.tasks = []
        self.task_vars = []
        self.timer_active = False
        self.time_left = 25 * 60  # default 25 minutes timer

        self.create_widgets()

    def create_widgets(self):
        primary_color = "#6C63FF"
        accent_color = "#4FC3F7"

        # Header
        header = ctk.CTkLabel(self, text="📝 StudyMate Pro", font=("Arial", 24, "bold"), text_color=primary_color)
        header.pack(pady=(20, 10))

        # Task input box 
        task_frame = ctk.CTkFrame(self)
        task_frame.pack(pady=10, padx=20, fill="x")

        self.task_entry = ctk.CTkEntry(task_frame, placeholder_text="Add your task here...")
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0,10))

        add_task_btn = ctk.CTkButton(task_frame, text="+ Add", width=70, fg_color=accent_color, command=self.add_task)
        add_task_btn.pack(side="left")

        # Task lists 
        task_label = ctk.CTkLabel(self, text="Your Tasks:", font=("Arial", 14))
        task_label.pack(pady=(15,5), anchor="w", padx=25)

        # Scrollable task list
        self.task_list = ctk.CTkScrollableFrame(self, height=160)
        self.task_list.pack(padx=25, fill="both", expand=False)

        # Timer input
        timer_input_frame = ctk.CTkFrame(self)
        timer_input_frame.pack(pady=20, padx=25, fill="x")

        timer_label = ctk.CTkLabel(timer_input_frame, text="Set Timer (minutes):", font=("Arial", 14))
        timer_label.pack(side="left")

        self.timer_entry = ctk.CTkEntry(timer_input_frame, width=60)
        self.timer_entry.pack(side="left", padx=10)

        set_timer_btn = ctk.CTkButton(timer_input_frame, text="Set", width=50, command=self.set_custom_timer)
        set_timer_btn.pack(side="left")

        # Timer display
        self.time_display = ctk.CTkLabel(self, text="25:00", font=("Arial", 48, "bold"))
        self.time_display.pack(pady=(10, 20))

        # Timer control buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)

        start_btn = ctk.CTkButton(btn_frame, text="Start Focus", fg_color=primary_color, width=100, command=self.start_timer)
        start_btn.pack(side="left", padx=10)

        break_btn = ctk.CTkButton(btn_frame, text="Take Break", fg_color=accent_color, width=100, command=self.take_break)
        break_btn.pack(side="left", padx=10)

        reset_btn = ctk.CTkButton(btn_frame, text="Reset", fg_color="#FF6B6B", width=100, command=self.reset_timer)
        reset_btn.pack(side="left", padx=10)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Please enter a task first!")
            return

        task_number = len(self.tasks) + 1
        task_text = f"{task_number}. {task}"

        var = ctk.BooleanVar()
        checkbox = ctk.CTkCheckBox(self.task_list, text=task_text, variable=var, width=300)
        checkbox.pack(anchor="w", pady=2)

        self.tasks.append(task_text)
        self.task_vars.append(var)
        self.task_entry.delete(0, "end")

    def set_custom_timer(self):
        val = self.timer_entry.get().strip()
        if val.isdigit():
            minutes = int(val)
            if minutes <= 0:
                messagebox.showerror("Invalid Input", "Please enter a positive number.")
                return
            self.time_left = minutes * 60
            self.time_display.configure(text=f"{minutes:02}:00")
            messagebox.showinfo("Timer Set", f"Timer set to {minutes} minutes")
            self.timer_entry.delete(0, "end")
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def start_timer(self):
        if not self.timer_active:
            self.timer_active = True
            self.update_timer()

    def take_break(self):
        self.timer_active = False
        self.time_left = 5 * 60
        messagebox.showinfo("Break Time!", "Good work! Taking a 5 minute break.")
        self.timer_active = True
        self.update_timer()

    def reset_timer(self):
        self.timer_active = False
        self.time_left = 25 * 60
        self.time_display.configure(text="25:00")

    def update_timer(self):
        if self.timer_active and self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.time_display.configure(text=f"{mins:02}:{secs:02}")
            self.time_left -= 1
            self.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.timer_active = False
            messagebox.showinfo("Time's Up!", "Focus session completed!")

if __name__ == "__main__":
    app = StudyMate()
    app.mainloop()
