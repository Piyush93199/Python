import pandas as pd
import numpy as np
import customtkinter as ctk
from tkinter import filedialog, messagebox
import os

# Configure application-wide appearance
ctk.set_appearance_mode("Dark")  # Options: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue" (standard), "green", "dark-blue"

class ModernImputerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("Missing Value Imputer")
        self.geometry("900x600")
        self.minsize(800, 500)

        self.data = None
        self.file_path = ""

        # --- Grid Layout (1x2) ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==================== SIDEBAR ====================
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)  # Push bottom elements down

        # Title
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Data Imputer v2.0", font=ctk.CTkFont(size=22, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 30))

        # Buttons - Make it easy to load data
        self.load_btn = ctk.CTkButton(self.sidebar_frame, text="Browse CSV File", command=self.load_file, hover_color="#2E8B57", fg_color="#3CB371", font=ctk.CTkFont(weight="bold"))
        self.load_btn.grid(row=1, column=0, padx=20, pady=10)

        self.sample_btn = ctk.CTkButton(self.sidebar_frame, text="Load Sample Data", command=self.load_sample_data, fg_color="transparent", border_width=1, text_color=("gray10", "#DCE4EE"))
        self.sample_btn.grid(row=2, column=0, padx=20, pady=(0, 20))

        # Column Selection
        self.col_label = ctk.CTkLabel(self.sidebar_frame, text="Select Target Column:", font=ctk.CTkFont(size=14))
        self.col_label.grid(row=3, column=0, padx=20, pady=(10, 5), sticky="w")
        
        self.column_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["No File Loaded"], state="disabled")
        self.column_menu.grid(row=4, column=0, padx=20, pady=5, sticky="ew")

        # Analyze Trigger
        self.run_button = ctk.CTkButton(self.sidebar_frame, text="Compare Strategies", command=self.run_analysis, state="disabled", font=ctk.CTkFont(weight="bold"))
        self.run_button.grid(row=5, column=0, padx=20, pady=20)

        # Appearance Mode Option
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=ctk.set_appearance_mode)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.appearance_mode_optionemenu.set("Dark")

        # ==================== MAIN CONTENT AREA ====================
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)

        # Status Header
        self.status_label = ctk.CTkLabel(self.main_frame, text="Welcome! Please load a CSV file to begin.", font=ctk.CTkFont(size=18), text_color="gray")
        self.status_label.grid(row=0, column=0, padx=20, pady=(10, 20), sticky="w")

        # Results Display Area (Text Box)
        self.results_box = ctk.CTkTextbox(self.main_frame, font=ctk.CTkFont(family="Consolas", size=14), wrap="word", corner_radius=10)
        self.results_box.grid(row=2, column=0, padx=0, pady=0, sticky="nsew")
        self.results_box.insert("0.0", "--- Analysis Results will appear here ---")
        self.results_box.configure(state="disabled")

    def print_to_results(self, text, clear=False):
        self.results_box.configure(state="normal")
        if clear:
            self.results_box.delete("0.0", "end")
        self.results_box.insert("end", text + "\n")
        self.results_box.configure(state="disabled")

    def process_loaded_data(self):
        filename = os.path.basename(self.file_path)
        self.status_label.configure(text=f"Loaded: {filename}")
        
        # Automatically find columns with missing values (NaNs)
        nan_cols = self.data.columns[self.data.isnull().any()].tolist()
        
        if nan_cols:
            self.column_menu.configure(values=nan_cols, state="normal")
            self.column_menu.set(nan_cols[0])
            self.run_button.configure(state="normal")
            
            self.print_to_results(f"Successfully loaded '{filename}'.\nFound {len(nan_cols)} columns with missing values.", clear=True)
            self.print_to_results("\nColumns with Missing Values:", clear=False)
            for col in nan_cols:
                missing_count = self.data[col].isnull().sum()
                self.print_to_results(f" - {col}: {missing_count} missing rows", clear=False)
                
            self.print_to_results("\nPlease select a target column from the sidebar and click 'Compare Strategies'.", clear=False)
        else:
            self.column_menu.configure(values=["No Missing Data"], state="disabled")
            self.run_button.configure(state="disabled")
            self.print_to_results(f"Successfully loaded '{filename}'.", clear=True)
            self.print_to_results("\nEXCELLENT! This dataset has NO missing values. \nImputation is not required.", clear=False)
            messagebox.showinfo("Clean Data", "This file has no missing values!")

    def load_file(self):
        # Starts in the current working directory
        start_dir = os.path.join(os.getcwd(), "data") if os.path.exists(os.path.join(os.getcwd(), "data")) else os.getcwd()
        
        file_path = filedialog.askopenfilename(
            initialdir=start_dir,
            title="Select Dataset",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
        )
        
        if file_path:
            self.file_path = file_path
            try:
                self.data = pd.read_csv(self.file_path)
                self.process_loaded_data()
            except Exception as e:
                messagebox.showerror("Error", f"Could not read file:\n{e}")

    def load_sample_data(self):
        # Quick way to load the generated sample data
        sample_path = os.path.join(os.getcwd(), 'data', 'large_logistics_data.csv')
        if os.path.exists(sample_path):
            self.file_path = sample_path
            self.data = pd.read_csv(self.file_path)
            self.process_loaded_data()
        else:
            messagebox.showwarning("Not Found", "Sample data not found. \nPlease run `python src/generate_data.py` first.")

    def run_analysis(self):
        col = self.column_menu.get()
        if not col or self.data is None:
            return

        series = self.data[col]
        total = len(series)
        missing = series.isnull().sum()
        
        # Ensure it's numeric for these specific mathematical strategies
        if not pd.api.types.is_numeric_dtype(series):
            messagebox.showwarning("Type Error", f"Column '{col}' is not numeric. Imputing mean/median won't work.\nTrying frequency mode instead.")
        
        # Calculation Logic
        try:
            old_mean = series.mean()
            old_std = series.std()

            strategies = {
                "Mean": series.fillna(old_mean),
                "Median": series.fillna(series.median()),
                "Mode": series.fillna(series.mode()[0] if not series.mode().empty else 0),
                "Zero-Fill": series.fillna(0)
            }

            self.print_to_results(f"\n{'='*50}", clear=True)
            self.print_to_results(f" IMPUTATION REPORT : {col}")
            self.print_to_results(f"{'='*50}")
            self.print_to_results(f"Total Rows:     {total}")
            self.print_to_results(f"Missing Values: {missing} ({(missing/total)*100:.2f}%)")
            self.print_to_results(f"Original Mean:  {old_mean:.4f}")
            self.print_to_results(f"Original Std:   {old_std:.4f}\n")

            self.print_to_results(f"| {'Strategy':<12} | {'New Mean':<12} | {'New Std Dev':<12} |")
            self.print_to_results("-" * 45)

            for name, imp_series in strategies.items():
                new_mean = imp_series.mean()
                new_std = imp_series.std()
                self.print_to_results(f"| {name:<12} | {new_mean:<12.4f} | {new_std:<12.4f} |")
            
            self.print_to_results(f"\n{'='*50}\nDone.")
        except Exception as e:
            self.print_to_results(f"Error during calculation: {e}", clear=True)

if __name__ == "__main__":
    app = ModernImputerApp()
    app.mainloop()