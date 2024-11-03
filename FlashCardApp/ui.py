import tkinter as tk
from tkinter import messagebox
from api import get_random_word, translate_word

class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title("I'm The Flashcard Learning ")

        # Set the size of the main window
        self.master.geometry("400x300")
        self.center_window()

        # Create a frame to center the button
        frame = tk.Frame(master)
        frame.pack(expand=True)  # Use expand to center the frame

        # Button to Get Started
        tk.Button(frame, text="Get Started", command=self.show_random_flashcard).pack(pady=20)

        # Initialize a list to store words
        self.words = []
        self.current_word_index = 0

    def center_window(self):
        # Center the window on the screen
        width = 400
        height = 300
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.master.geometry(f"{width}x{height}+{x}+{y}")

    def show_random_flashcard(self):
        self.words = []  # Clear previous words
        self.load_words()  # Load initial words

        if self.words:
            self.current_word_index = 0
            self.display_flashcard(self.words[self.current_word_index])
        else:
            messagebox.showerror("Error", "Could not retrieve words.")

    def load_words(self):
        # Load words in batches of 5
        for _ in range(5):
            word = get_random_word()  # Get word from API
            if word:
                self.words.append(word)

    def display_flashcard(self, word):
        translated_word = translate_word(word)

        # Create a new window for the flashcard
        flashcard_window = tk.Toplevel(self.master)
        flashcard_window.title("Flashcard")
        flashcard_window.geometry("400x200")
        self.center_window_on_top(flashcard_window)

        # Centering the label
        frame = tk.Frame(flashcard_window)
        frame.pack(expand=True)

        # Display word
        word_label = tk.Label(frame, text=word, justify=tk.CENTER, font=("Arial", 24))
        word_label.pack(pady=20)

        # Display translated word
        translated_label = tk.Label(frame, text=f"Translated: {translated_word}", justify=tk.CENTER, font=("Arial", 16))
        translated_label.pack(pady=10)

        # Button to go to the next word
        next_button = tk.Button(flashcard_window, text="Next Word", command=lambda: self.show_next_word(flashcard_window))
        next_button.pack(pady=10)

        # Button to load more words if we've gone through all current words
        if self.current_word_index + 1 >= len(self.words):
            load_more_button = tk.Button(flashcard_window, text="Load More", command=lambda: self.load_more_words(flashcard_window))
            load_more_button.pack(pady=10)

        # Button to close the flashcard window
        close_button = tk.Button(flashcard_window, text="Close", command=flashcard_window.destroy)
        close_button.pack(pady=10)

    def load_more_words(self, flashcard_window):
        self.load_words()  # Load additional words
        if self.words:
            self.current_word_index = len(self.words) - 5  # Set to the last 5 loaded words
            self.display_flashcard(self.words[self.current_word_index])  # Show the next word
        else:
            flashcard_window.destroy()  # Close the window if no more words are available

    def show_next_word(self, flashcard_window):
        self.current_word_index += 1
        if self.current_word_index < len(self.words):
            word = self.words[self.current_word_index]
            flashcard_window.destroy()  # Close the previous window
            self.display_flashcard(word)
        else:
            flashcard_window.destroy()  # Close the window without alert

    def center_window_on_top(self, window):
        # Center the flashcard window on top of the main window
        width = 400
        height = 200
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
