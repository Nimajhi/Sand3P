import tkinter as tk
from tkinter import ttk, messagebox
from fieldGroup import FIELD_GROUPS  
from initialFormulas import SandProductionModel

class SandProductionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sand Production Prediction")
        self.root.geometry("1154x640")
        self.root.resizable(True, True)

        # Notebook for tabs
        notebook = ttk.Notebook(root)
        notebook.pack(fill="both", expand=True)

        # Create frames for each tab
        self.inputs_tab = ttk.Frame(notebook)
        self.outputs_tab = ttk.Frame(notebook)
        self.rate_chart_tab = ttk.Frame(notebook)
        self.poro_perm_chart_tab = ttk.Frame(notebook)
        self.final_results_tab = ttk.Frame(notebook)
        self.model_calibration_tab = ttk.Frame(notebook)
        self.sand_to_oil_tab = ttk.Frame(notebook)

        # Add tabs to notebook
        notebook.add(self.inputs_tab, text="Inputs")
        notebook.add(self.outputs_tab, text="Outputs")
        notebook.add(self.rate_chart_tab, text="Rate of Sand Production Chart")
        notebook.add(self.poro_perm_chart_tab, text="Porosity & Permeability Chart")
        notebook.add(self.final_results_tab, text="Final Results")
        notebook.add(self.model_calibration_tab, text="Model Calibration")
        notebook.add(self.sand_to_oil_tab, text="Sand to Oil Production")

        # Build Inputs tab
        self.build_inputs_tab()

    def build_inputs_tab(self):
        """Create all input fields on the Inputs tab with grouping and units"""
        main_frame = ttk.Frame(self.inputs_tab, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Let main_frame expand
        self.inputs_tab.rowconfigure(0, weight=1)
        self.inputs_tab.columnconfigure(0, weight=1)

        groups = FIELD_GROUPS
        
        self.entries = {}
        self.field_mapping = {}  # Maps full field names to short names

        # Place groups in 3 columns per row
        row, col = 0, 0
        for group_name, group_data in groups.items():
            lf = ttk.Labelframe(main_frame, text=group_name, padding="10")
            lf.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            # Allow entry column to expand inside group
            lf.columnconfigure(1, weight=1)

            # Get the fields dictionary from the group data
            fields = group_data.get("fields", {})
            
            for i, (field_short_name, field_data) in enumerate(fields.items()):
                full_name = field_data["full_name"]
                unit = field_data["unit"]

                ttk.Label(lf, text=full_name).grid(row=i, column=0, sticky="w", pady=2)

                if full_name == "Failure Method":
                    # Dropdown menu
                    options = ["Mohr", "Mogi-Coulomb", "Hoek-Brown"]
                    var = tk.StringVar()
                    dropdown = ttk.Combobox(
                        lf, textvariable=var, values=options, state="readonly"
                    )
                    dropdown.grid(row=i, column=1, pady=2, padx=5, sticky="ew")
                    self.entries[field_short_name] = var
                else:
                    entry = ttk.Entry(lf)
                    entry.grid(row=i, column=1, pady=2, padx=5, sticky="ew")
                    self.entries[field_short_name] = entry

                # Add unit label after entry/dropdown
                ttk.Label(lf, text=unit).grid(row=i, column=2, sticky="w", pady=2)

            # Move to next column / row (3 columns max)
            col += 1
            if col > 2:  # wrap after 3 columns
                col = 0
                row += 1

        # Add submit button at bottom
        submit_button = ttk.Button(main_frame, text="Submit", command=self.run_model)
        submit_button.grid(row=row + 1, column=0, columnspan=3, pady=20)

    def get_values(self):
        """Collect values from GUI and return dict with short names"""
        values = {}
        for short_name, widget in self.entries.items():
            val = widget.get() if not isinstance(widget, tk.StringVar) else widget.get()
            if val:  # Only add if we have a value
                try:
                    # Try to convert to float, keep as string if it fails
                    values[short_name] = float(val)
                except ValueError:
                    values[short_name] = val
        return values

    def run_model(self):
        """Run sand production model using GUI inputs"""
        input_data = self.get_values()
        
        print("Collected input data:")
        for key, value in input_data.items():
            print(f"{key}: {value}")

        try:
            # Create model instance with the collected data
            model = SandProductionModel(
                sigma_h=input_data.get("sigma_h", 0),
                sigma_H=input_data.get("sigma_H", 0),
                sigma_v=input_data.get("sigma_v", 0),
                alpha=input_data.get("alpha", 0),
                inclination=input_data.get("i", 0)  # Note: using "i" for inclination
            )
            
            # Run calculations
            results = model.compute_all()
            
            print("\nModel Results:")
            for k, v in results.items():
                print(f"{k}: {v:.6f}")
                
            # Display results in the output tabs
            self.display_results(results)
            
        except KeyError as e:
            error_msg = f"Missing required input: {e}"
            print(error_msg)
            self.show_error(error_msg)
        except Exception as e:
            error_msg = f"Calculation error: {e}"
            print(error_msg)
            self.show_error(error_msg)

    def display_results(self, results):
        """Display the calculation results in the output tabs"""
        print("Results ready for display in GUI tabs")
        
        # Simple display in outputs tab for now
        for widget in self.outputs_tab.winfo_children():
            widget.destroy()
            
        results_frame = ttk.Frame(self.outputs_tab, padding="10")
        results_frame.pack(fill="both", expand=True)
        
        ttk.Label(results_frame, text="Sand Production Model Results", 
                 font=("Arial", 14, "bold")).pack(pady=10)
        
        for i, (key, value) in enumerate(results.items()):
            row_frame = ttk.Frame(results_frame)
            row_frame.pack(fill="x", padx=20, pady=2)
            ttk.Label(row_frame, text=f"{key}:", width=15, anchor="w").pack(side="left")
            ttk.Label(row_frame, text=f"{value:.6f}").pack(side="left")

    def show_error(self, message):
        """Show error message to user"""
        messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = SandProductionGUI(root)
    root.mainloop()
