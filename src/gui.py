import tkinter as tk
from tkinter import ttk
from fieldGroup import FIELD_GROUPS  


class SandProductionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sand Production Prediction")
        self.root.geometry("1154x640")   # initial window size
        self.root.resizable(True, True)  # allow resize

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

        # -----------------------------
        # Build Inputs tab
        # -----------------------------
        self.build_inputs_tab()

    def build_inputs_tab(self):
        """Create all input fields on the Inputs tab with grouping and units"""
        main_frame = ttk.Frame(self.inputs_tab, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Let main_frame expand
        self.inputs_tab.rowconfigure(0, weight=1)
        self.inputs_tab.columnconfigure(0, weight=1)

        #import Fields
        groups = FIELD_GROUPS
        
        self.entries = {}

        # Place groups in 3 columns per row
        row, col = 0, 0
        for group_name, fields in groups.items():
            lf = ttk.Labelframe(main_frame, text=group_name, padding="10")
            lf.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            # Allow entry column to expand inside group
            lf.columnconfigure(1, weight=1)

            for i, (field, unit) in enumerate(fields.items()):
                ttk.Label(lf, text=field).grid(row=i, column=0, sticky="w", pady=2)

                if field == "Failure Method":
                    # Dropdown menu
                    options = ["Mohr", "Mogi-Coulomb", "Hoek-Brown"]
                    var = tk.StringVar()
                    dropdown = ttk.Combobox(
                        lf, textvariable=var, values=options, state="readonly"
                    )
                    dropdown.grid(row=i, column=1, pady=2, padx=5, sticky="ew")
                    self.entries[field] = var
                else:
                    entry = ttk.Entry(lf)
                    entry.grid(row=i, column=1, pady=2, padx=5, sticky="ew")
                    self.entries[field] = entry

                # Add unit label after entry/dropdown
                ttk.Label(lf, text=unit).grid(row=i, column=2, sticky="w", pady=2)

            # Move to next column / row (3 columns max)
            col += 1
            if col > 2:  # wrap after 3 columns
                col = 0
                row += 1

        # Add submit button at bottom
        submit_button = ttk.Button(main_frame, text="Submit", command=self.get_values)
        submit_button.grid(row=row + 1, column=0, columnspan=3, pady=10)

    def get_values(self):
        """Collect and print values from inputs tab"""
        values = {}
        for label, widget in self.entries.items():
            if isinstance(widget, tk.StringVar):  # dropdown
                values[label] = widget.get()
            else:
                values[label] = widget.get()

        print("User Inputs:")
        for k, v in values.items():
            print(f"{k}: {v}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SandProductionGUI(root)
    root.mainloop()
