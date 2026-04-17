import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk
from annotator.core.runner import run_pipeline

class AnnotatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Annotator WasteParrot")
        self.root.geometry("600x600")
        self.root.resizable(True, False)
        
        # Variables to hold the UI state
        self.input_folder_var = tk.StringVar()
        self.output_folder_var = tk.StringVar()
        self.format_var = tk.StringVar(value="json")
        
        self.setup_ui()

    def setup_ui(self):
        """Sets up the layout of the GUI with improved consistency and log panel."""
        # Use ttk Style for consistent appearance
        style = ttk.Style()
        style.configure("Header.TLabel", font=("Arial", 10, "bold"))
        style.configure("Run.TButton", font=("Arial", 11, "bold"))

        # Main container with uniform padding
        main_container = ttk.Frame(self.root, padding=20)
        main_container.pack(fill="both", expand=True)

        # Content frame using grid for precise alignment
        content_frame = ttk.Frame(main_container)
        content_frame.pack(fill="x")
        content_frame.columnconfigure(0, weight=1)

        # --- Input Folder Section ---
        ttk.Label(content_frame, text="Input Folder:", style="Header.TLabel").grid(row=0, column=0, columnspan=2, sticky="w")
        
        self.input_entry = ttk.Entry(content_frame, textvariable=self.input_folder_var)
        self.input_entry.grid(row=1, column=0, sticky="ew", pady=(5, 15), padx=(0, 10))
        
        input_button = ttk.Button(content_frame, text="Browse", command=self.browse_input, width=12)
        input_button.grid(row=1, column=1, pady=(5, 15))

        # --- Output Folder Section ---
        ttk.Label(content_frame, text="Output Folder:", style="Header.TLabel").grid(row=2, column=0, columnspan=2, sticky="w")
        
        self.output_entry = ttk.Entry(content_frame, textvariable=self.output_folder_var)
        self.output_entry.grid(row=3, column=0, sticky="ew", pady=(5, 15), padx=(0, 10))
        
        output_button = ttk.Button(content_frame, text="Browse", command=self.browse_output, width=12)
        output_button.grid(row=3, column=1, pady=(5, 15))

        # --- Format Selection Section ---
        ttk.Label(content_frame, text="Output Format:", style="Header.TLabel").grid(row=4, column=0, columnspan=2, sticky="w")
        
        self.format_dropdown = ttk.Combobox(
            content_frame, 
            textvariable=self.format_var, 
            values=["json", "yolo", "both"],
            state="readonly"
        )
        self.format_dropdown.grid(row=5, column=0, sticky="ew", pady=(5, 15), padx=(0, 10))

        # --- Log Panel Section ---
        ttk.Label(content_frame, text="Progress Log:", style="Header.TLabel").grid(row=6, column=0, columnspan=2, sticky="w")
        
        self.log_area = scrolledtext.ScrolledText(
            content_frame, 
            height=12, 
            state='disabled', 
            font=("Consolas", 9),
            bg="#f5f5f5"
        )
        self.log_area.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(5, 15))

        # --- Run Button Section ---
        run_button = ttk.Button(
            main_container, 
            text="Run Annotation", 
            command=self.run_annotation,
            style="Run.TButton"
        )
        run_button.pack(fill="x", side="bottom", ipady=5)

    def update_log(self, message):
        """Appends a message to the log area and ensures it scrolls to the end."""
        self.log_area.configure(state='normal')
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.configure(state='disabled')
        self.log_area.see(tk.END)
        self.root.update_idletasks() # Force UI refresh

    def browse_input(self):
        """Opens a dialog to select the input folder."""
        directory = filedialog.askdirectory(title="Select Input Folder")
        if directory:
            self.input_folder_var.set(directory)

    def browse_output(self):
        """Opens a dialog to select the output folder."""
        directory = filedialog.askdirectory(title="Select Output Folder")
        if directory:
            self.output_folder_var.set(directory)

    def run_annotation(self):
        """Validates inputs and runs the annotation pipeline with progress callback."""
        input_path = self.input_folder_var.get().strip()
        output_path = self.output_folder_var.get().strip()
        selected_format = self.format_var.get()

        if not input_path:
            messagebox.showerror("Error", "Input folder path cannot be empty.")
            return

        if not output_path:
            messagebox.showerror("Error", "Output folder path cannot be empty.")
            return

        # Clear log for a new run
        self.log_area.configure(state='normal')
        self.log_area.delete(1.0, tk.END)
        self.log_area.configure(state='disabled')

        self.update_log(f"Starting annotation process...")
        self.update_log(f"Input: {input_path}")
        self.update_log(f"Output: {output_path}")
        self.update_log(f"Format: {selected_format}")
        self.update_log("-" * 30)

        # Progress callback function
        def progress_callback(index, total, filename, result):
            self.update_log(f"[{index}/{total}] {filename} → done")

        try:
            # Execute pipeline with the callback
            run_pipeline(
                path=input_path, 
                output_folder=output_path, 
                output_format=selected_format, 
                callback=progress_callback
            )
            
            self.update_log("-" * 30)
            self.update_log("Success: Annotation pipeline completed.")
            messagebox.showinfo("Success", "Annotation pipeline completed successfully!")
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            self.update_log(f"ERROR: {error_msg}")
            messagebox.showerror("Error", error_msg)

def main():
    root = tk.Tk()
    app = AnnotatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
