import tkinter as tk
from tkinter import messagebox


class VotingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Voting Management System")
        self.master.configure(bg="lightblue")  # Background color for the main window

        # Data structure for candidates and votes
        self.candidates = {}
        self.voters = set()

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        self.input_frame = tk.Frame(self.master, bg="lightblue")  # Set the background color of the frame
        self.input_frame.pack(pady=10)

        self.subject_label = tk.Label(self.input_frame, text="Voting Subject:", fg="orange", bg="lightblue")
        self.subject_label.grid(row=0, column=0, padx=5)

        self.subject_entry = tk.Entry(self.input_frame)
        self.subject_entry.grid(row=0, column=1)

        # Buttons
        self.add_candidate_button = tk.Button(self.master, text="Add Candidate", command=self.open_add_candidate_window)
        self.add_candidate_button.pack(pady=5)

        self.register_voter_button = tk.Button(self.master, text="Register Voter", command=self.open_register_voter_window)
        self.register_voter_button.pack(pady=5)

        self.vote_button = tk.Button(self.master, text="Vote", command=self.open_vote_window)
        self.vote_button.pack(pady=5)

        self.results_button = tk.Button(self.master, text="Show Results", command=self.open_show_results_window)
        self.results_button.pack(pady=5)

        # Text box for displaying results
        self.results_text = tk.Text(self.master, height=10, width=50, bg="lightyellow")
        self.results_text.pack(pady=10)

    def open_add_candidate_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Add Candidate")
        new_window.configure(bg="lightgreen")  # Set background color for the new window

        # Voting Subject Entry
        tk.Label(new_window, text="Voting Subject:", fg="orange", bg="lightgreen").grid(row=0, column=0, padx=5, pady=5)
        subject_entry = tk.Entry(new_window)
        subject_entry.grid(row=0, column=1, padx=5, pady=5)

        # Candidate Name Entry
        tk.Label(new_window, text="Candidate Name:", fg="white", bg="lightgreen").grid(row=1, column=0, padx=5, pady=5)
        candidate_entry = tk.Entry(new_window)
        candidate_entry.grid(row=1, column=1, padx=5, pady=5)

        # Add Candidate Button
        tk.Button(new_window, text="Add Candidate", command=lambda: self.add_candidate(new_window, subject_entry, candidate_entry)).grid(row=2, column=0, columnspan=2, pady=10)

    def add_candidate(self, window, subject_entry, candidate_entry):
        subject = subject_entry.get().strip()
        candidate_name = candidate_entry.get().strip()

        if not subject:
            messagebox.showwarning("Input Error", "Please enter a voting subject.")
            return

        if not candidate_name:
            messagebox.showwarning("Input Error", "Please enter a candidate name.")
            return

        if subject not in self.candidates:
            self.candidates[subject] = {}

        if candidate_name in self.candidates[subject]:
            messagebox.showwarning("Input Error", "Candidate already exists.")
        else:
            self.candidates[subject][candidate_name] = 0
            messagebox.showinfo("Success", f"Candidate '{candidate_name}' added for '{subject}' voting.")

        window.destroy()

    def open_register_voter_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Register Voter")
        new_window.configure(bg="lightcoral")  # Set background color for the new window

        tk.Label(new_window, text="Voter ID:", fg="green", bg="lightcoral").grid(row=0, column=0, padx=5, pady=5)
        voter_entry = tk.Entry(new_window)
        voter_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(new_window, text="Register Voter", command=lambda: self.register_voter(new_window, voter_entry)).grid(row=1, column=0, columnspan=2, pady=10)

    def register_voter(self, window, voter_entry):
        voter_id = voter_entry.get().strip()

        if not voter_id:
            messagebox.showwarning("Input Error", "Please enter a voter ID.")
            return

        if voter_id in self.voters:
            messagebox.showwarning("Input Error", "Voter ID already registered.")
        else:
            self.voters.add(voter_id)
            messagebox.showinfo("Success", f"Voter '{voter_id}' registered.")

        window.destroy()

    def open_vote_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Vote")
        new_window.configure(bg="lightyellow")  # Set background color for the new window

        tk.Label(new_window, text="Voter ID:", fg="green", bg="lightyellow").grid(row=0, column=0, padx=5, pady=5)
        voter_entry = tk.Entry(new_window)
        voter_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(new_window, text="Candidate Name:", fg="white", bg="lightyellow").grid(row=1, column=0, padx=5, pady=5)
        candidate_entry = tk.Entry(new_window)
        candidate_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(new_window, text="Voting Subject:", fg="orange", bg="lightyellow").grid(row=2, column=0, padx=5, pady=5)
        subject_entry = tk.Entry(new_window)
        subject_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(new_window, text="Vote", command=lambda: self.vote(new_window, voter_entry, candidate_entry, subject_entry)).grid(row=3, column=0, columnspan=2, pady=10)

    def vote(self, window, voter_entry, candidate_entry, subject_entry):
        voter_id = voter_entry.get().strip()
        subject = subject_entry.get().strip()
        candidate_name = candidate_entry.get().strip()

        if not voter_id:
            messagebox.showwarning("Input Error", "Please enter a voter ID.")
            return

        if voter_id not in self.voters:
            messagebox.showwarning("Input Error", "Voter ID not registered.")
            return

        if subject not in self.candidates:
            messagebox.showwarning("Input Error", "No candidates available for this subject.")
            return

        if candidate_name not in self.candidates[subject]:
            messagebox.showwarning("Input Error", "Candidate does not exist.")
            return

        self.candidates[subject][candidate_name] += 1
        messagebox.showinfo("Success", f"Thank you for voting for '{candidate_name}'.")
        self.voters.remove(voter_id)  # Ensure the voter cannot vote again

        window.destroy()

    def open_show_results_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Show Results")
        new_window.configure(bg="lightblue")  # Set background color for the new window

        tk.Label(new_window, text="Voting Subject:", fg="orange", bg="lightblue").grid(row=0, column=0, padx=5, pady=5)
        subject_entry = tk.Entry(new_window)
        subject_entry.grid(row=0, column=1, padx=5, pady=5)

        results_text = tk.Text(new_window, height=10, width=50, bg="lightyellow")
        results_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        tk.Button(new_window, text="Show Results", command=lambda: self.show_results(new_window, subject_entry, results_text)).grid(row=2, column=0, columnspan=2, pady=10)

    def show_results(self, window, subject_entry, results_text):
        subject = subject_entry.get().strip()

        if subject not in self.candidates:
            messagebox.showwarning("Input Error", "No voting results available for this subject.")
            return

        results = f"Results for '{subject}':\n"
        for candidate, votes in self.candidates[subject].items():
            results += f"{candidate}: {votes} vote(s)\n"

        results_text.delete(1.0, tk.END)  # Clear previous results
        results_text.insert(tk.END, results)

        window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="lightblue")  # Set background color for the main window
    app = VotingSystem(root)
    root.mainloop()
