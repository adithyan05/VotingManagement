# login.py
import tkinter as tk
from tkinter import messagebox
import Voting_Management  # Import the Voting Management System file

class LoginSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Login System")
        self.master.configure(bg="lightblue")

        # Predefined login credentials
        self.username = "Adithyan"
        self.password = "12318383"

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Username
        tk.Label(self.master, text="Username:", fg="black", bg="lightblue").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password
        tk.Label(self.master, text="Password:", fg="black", bg="lightblue").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # Login Button
        tk.Button(self.master, text="Login", command=self.authenticate).grid(row=2, column=0, columnspan=2, pady=10)

    def authenticate(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if username == self.username and password == self.password:
            messagebox.showinfo("Login Success", "Welcome to the Voting Management System!")
            self.master.destroy()  # Close the login window
            self.open_voting_system()  # Open the main voting application
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def open_voting_system(self):
        root = tk.Tk()
        root.configure(bg="lightblue")
        app = Voting_Management.VotingSystem(root)  # Initialize the voting system
        root.mainloop()


if __name__ == "__main__":
    login_root = tk.Tk()
    app = LoginSystem(login_root)
    login_root.mainloop()
