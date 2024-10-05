import re
import tkinter as tk
import subprocess
import ctypes  # To set DPI awareness (for Windows high-resolution scaling)
import platform

from tkinter import filedialog, scrolledtext
from tkinter import ttk  # Use ttk for styled widgets

class TextEditor:

    def __init__(self, root):
        # Enable DPI awareness for Windows high-resolution displays
        if platform.system() == "Windows":
            if ctypes.windll.shcore:
                ctypes.windll.shcore.SetProcessDpiAwareness(1)

        self.root = root
        root.title("CompiBuilder - CompiScript Editor")
        root.configure(bg="#1E1E2E")  # Background color for the window

        # Set an initial larger size and center the window
        self.center_window(1200, 850)  # Adjusted size to fit all widgets

        # Style Configuration
        self.font = ("Aptos", 12)  # Fuente Aptos
        self.bg_color = "#1E1E2E"  # Fondo oscuro
        self.fg_color = "#D4D4E4"  # Color de texto claro
        self.line_bg_color = "#262738"  # Fondo para líneas (similar a un gris oscuro azulado)
        self.highlight_bg = "#3B4252"  # Fondo resaltado con un tono ligeramente más claro y azulado

        # Line number area
        self.line_number_bar = tk.Text(root, width=4, padx=5, takefocus=0, border=0,
                                       background=self.line_bg_color, foreground=self.fg_color, 
                                       state='disabled', wrap='none', font=self.font)
        self.line_number_bar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Main frame to hold the text editor and terminal
        self.main_frame = tk.Frame(root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a PanedWindow for resizable areas between text editor and terminal
        self.paned_window = tk.PanedWindow(self.main_frame, orient=tk.VERTICAL, bg=self.bg_color)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        # Text area for code editing
        self.text_area = scrolledtext.ScrolledText(self.main_frame, wrap=tk.WORD, font=self.font, 
                                                   background=self.bg_color, foreground=self.fg_color,
                                                   insertbackground=self.fg_color, selectbackground=self.highlight_bg)
        self.paned_window.add(self.text_area)  # Add text area to the PanedWindow

        # Bind the Tab key to insert spaces
        self.text_area.bind("<Tab>", self.insert_spaces)

        # Syntax Highlighting
        self.text_area.bind('<KeyRelease>', self.on_key_release)
        self.setup_syntax_highlighting()

        # Terminal frame
        self.terminal_frame = tk.Frame(self.main_frame, height=70, bg=self.bg_color)
        self.paned_window.add(self.terminal_frame)  # Add terminal frame to the PanedWindow

        self.terminal_output = tk.Text(self.terminal_frame, height=10, bg=self.bg_color, fg=self.fg_color, 
                                       insertbackground=self.fg_color, selectbackground=self.highlight_bg, 
                                       font=self.font)
        self.terminal_output.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.terminal_input = tk.Entry(self.terminal_frame, bg=self.bg_color, fg=self.fg_color, 
                                       insertbackground=self.fg_color, font=self.font)
        self.terminal_input.pack(side=tk.BOTTOM, fill=tk.X)
        self.terminal_input.bind("<Return>", self.execute_command)

        # Buttons with ttk
        self.buttons_frame = ttk.Frame(root)
        self.buttons_frame.pack(fill=tk.X, side=tk.BOTTOM)

        style = ttk.Style()
        style.configure("TButton", padding=6, relief="flat", background="#ffffff", foreground="#000000")

        self.open_button = ttk.Button(self.buttons_frame, text="Open", command=self.open_file, style="TButton")
        self.open_button.pack(side=tk.LEFT, padx=2)

        self.save_button = ttk.Button(self.buttons_frame, text="Save", command=self.save_file, style="TButton")
        self.save_button.pack(side=tk.LEFT, padx=2)

        self.close_button = ttk.Button(self.buttons_frame, text="Close", command=self.close_file, style="TButton")
        self.close_button.pack(side=tk.LEFT, padx=2)

        self.clear_terminal_button = ttk.Button(self.buttons_frame, text="Clear Terminal", command=self.clear_terminal, style="TButton")
        self.clear_terminal_button.pack(side=tk.LEFT, padx=2)

        # Adding the "Generate PDF" button
        self.generate_pdf_button = ttk.Button(self.buttons_frame, text="Generate PDF", command=self.generate_pdf, style="TButton")
        self.generate_pdf_button.pack(side=tk.LEFT, padx=2)

        self.run_compiscript = ttk.Button(self.buttons_frame, text="Run", command=self.run_compiscript, style="TButton")
        self.run_compiscript.pack(side=tk.LEFT, padx=2)

        # File label as status bar
        self.file_label = ttk.Label(root, text="No file opened", anchor='w', font=("Consolas", 10))
        self.file_label.pack(fill=tk.X, side=tk.BOTTOM, padx=4, pady=2)

        # Initialize current_open_file attribute
        self.current_open_file = None

        # Update line numbers initially
        self.update_line_numbers()

    def center_window(self, width, height):
        """Centers the window on the screen."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def setup_syntax_highlighting(self):
        # Configure syntax highlighting tags
        self.text_area.tag_configure("keyword", foreground="#569cd6")
        self.text_area.tag_configure("string", foreground="#d69d85")
        self.text_area.tag_configure("comment", foreground="#6a9955")
        self.text_area.tag_configure("number", foreground="#9971CD")

        self.keywords = ["class", "fun", "var", "if", "else", "for", "while", "return", "true", "false", "nil", "print", "extends"]
        self.keyword_pattern = r"\b(" + "|".join(self.keywords) + r")\b"
        self.string_pattern = r"\".*?\""
        self.comment_pattern = r"//.*?$"
        self.number_pattern = r"\b\d+(\.\d+)?\b"

    def highlight_syntax(self, event=None):
        # Remove existing tags
        self.text_area.tag_remove("keyword", "1.0", tk.END)
        self.text_area.tag_remove("string", "1.0", tk.END)
        self.text_area.tag_remove("comment", "1.0", tk.END)
        self.text_area.tag_remove("number", "1.0", tk.END)

        content = self.text_area.get("1.0", tk.END)

        # Apply keyword highlighting
        for match in re.finditer(self.keyword_pattern, content):
            start, end = match.span()
            start_pos = f"1.0+{start}c"
            end_pos = f"1.0+{end}c"
            self.text_area.tag_add("keyword", start_pos, end_pos)

        # Apply string highlighting
        for match in re.finditer(self.string_pattern, content):
            start, end = match.span()
            start_pos = f"1.0+{start}c"
            end_pos = f"1.0+{end}c"
            self.text_area.tag_add("string", start_pos, end_pos)

        # Apply comment highlighting
        for match in re.finditer(self.comment_pattern, content, re.MULTILINE):
            start, end = match.span()
            start_pos = f"1.0+{start}c"
            end_pos = f"1.0+{end}c"
            self.text_area.tag_add("comment", start_pos, end_pos)

        # Apply number highlighting
        for match in re.finditer(self.number_pattern, content):
            start, end = match.span()
            start_pos = f"1.0+{start}c"
            end_pos = f"1.0+{end}c"
            self.text_area.tag_add("number", start_pos, end_pos)

    def on_key_release(self, event=None):
        self.update_line_numbers()
        self.highlight_syntax()

    def update_line_numbers(self):
        self.line_number_bar.config(state='normal')
        self.line_number_bar.delete(1.0, tk.END)
        
        first_line = int(self.text_area.yview()[0] * int(self.text_area.index('end-1c').split('.')[0]))
        last_line = int(self.text_area.yview()[1] * int(self.text_area.index('end-1c').split('.')[0]))
        
        line_numbers_string = "\n".join(str(i) for i in range(first_line + 1, min(last_line + 1, first_line + 1 + self.text_area.winfo_height())))
        self.line_number_bar.insert(1.0, line_numbers_string)
        self.line_number_bar.config(state='disabled')

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".cscript", filetypes=[("CompiScript Files", "*.cscript"), ("Text Files", "*.txt")])
        if file_path:
            self.text_area.delete(1.0, tk.END)
            with open(file_path, 'r') as file:
                self.text_area.insert(1.0, file.read())
            self.current_open_file = file_path
            self.update_line_numbers()
            self.update_file_label()
            self.highlight_syntax()

    def save_file(self):
        if not self.current_open_file:
            new_file_path = filedialog.asksaveasfilename(initialfile='input.cscript', defaultextension=".cscript", filetypes=[("CompiScript Files", "*.cscript"), ("Text Files", "*.txt")])
            if new_file_path:
                with open(new_file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_open_file = new_file_path
                self.update_file_label()
        else:
            with open(self.current_open_file, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

    def run_compiscript(self):
        script_path = self.current_open_file

        if script_path:
            try:
                process = subprocess.Popen(['python', 'Driver.py', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output, error = process.communicate()

                if output:
                    self.terminal_output.insert(tk.END, "Compiler Output:\n" + output + "\n")
                if error:
                    self.terminal_output.insert(tk.END, "Compiler Error:\n" + error + "\n")
            except Exception as e:
                self.terminal_output.insert(tk.END, f"Failed to run CompiScript compiler: {str(e)}\n")

            self.terminal_output.see(tk.END)

    def generate_pdf(self):
        """Generate PDF from the current file."""
        script_path = self.current_open_file

        if script_path:
            try:
                # Assuming you have a script that generates a PDF from the code
                process = subprocess.Popen(['python', 'Driver.py', script_path, '--pdf'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                output, error = process.communicate()

                if output:
                    self.terminal_output.insert(tk.END, "PDF Generated Successfully:\n" + output + "\n")
                if error:
                    self.terminal_output.insert(tk.END, "PDF Generation Error:\n" + error + "\n")
            except Exception as e:
                self.terminal_output.insert(tk.END, f"Failed to generate PDF: {str(e)}\n")

            self.terminal_output.see(tk.END)

    def close_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_open_file = ''
        self.update_file_label()

    def update_file_label(self):
        if self.current_open_file:
            self.file_label.config(text="File: " + self.current_open_file)
        else:
            self.file_label.config(text="No file opened")

    def clear_terminal(self):
        self.terminal_output.delete(1.0, tk.END)

    def execute_command(self, event=None):
        cmd = self.terminal_input.get()
        self.terminal_input.delete(0, tk.END)

        try:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            output, error = process.communicate()

            if output:
                self.terminal_output.insert(tk.END, output)
            if error:
                self.terminal_output.insert(tk.END, error)

        except Exception as e:
            self.terminal_output.insert(tk.END, f"Error: {str(e)}\n")

        self.terminal_output.see(tk.END)

    def insert_spaces(self, event=None):
        """Inserts 2 spaces instead of a tab."""
        self.text_area.insert(tk.INSERT, "   ")  # Insert 2 spaces
        return 'break'  # Prevent the default tab behavior


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
