import tkinter as tk

class RiseTimeBudget:
    def __init__(self, ttx:float, trx:float, tmod:float, tgvd:float) -> None:
        self.ttx = ttx
        self.trx = trx
        self.tmod = tmod
        self.tgvd = tgvd
        self.tsys = None

        # calc params
        self.tsys = self.calc_tsys()
        self.brz = self.calc_brz() 
        self.bnrz = self.calc_bnrz() 

    def calc_tsys(self):
        return ((self.ttx)**2 + (self.trx)**2 + (self.tmod)**2 + (self.tgvd)**2)**0.5
    
    def calc_brz(self):
        if not self.tsys:
            self.calc_tsys()

        return 0.35/self.tsys * 1000 # convert to mbps
    
    def calc_bnrz(self):
        if not self.tsys:
            self.calc_tsys()

        return 0.7/self.tsys * 1000 # convert to mbps
    

# Create the main window
root = tk.Tk()
root.title("Rise Time budget Analysis")

# Create the input labels
tk.Label(root, text="Ttx (ns):").grid(row=0, column=0)
tk.Label(root, text="Trx (ns):").grid(row=1, column=0)
tk.Label(root, text="Tmod (ns):").grid(row=2, column=0)
tk.Label(root, text="Tgvd (ns):").grid(row=3, column=0)

# Create the input fields
ttx = tk.Entry(root)
trx = tk.Entry(root)
tmod = tk.Entry(root)
tgvd = tk.Entry(root)

# Position the input fields
ttx.grid(row=0, column=1)
trx.grid(row=1, column=1)
tmod.grid(row=2, column=1)
tgvd.grid(row=3, column=1)

# Create the output label
tsys_label = tk.Label(root, text="Tsys (ns):")
tsys_label.grid(row=4, column=0)
BRZ_label = tk.Label(root, text="Brz (Mbps):")
BRZ_label.grid(row=5, column=0)
BNRZ_label = tk.Label(root, text="Bnrz (Mbps):")
BNRZ_label.grid(row=6, column=0)

# Create the output field
tsys_output = tk.Label(root, text="")
tsys_output.grid(row=4, column=1)
BRZ_output = tk.Label(root, text="")
BRZ_output.grid(row=5, column=1)
BNRZ_output = tk.Label(root, text="")
BNRZ_output.grid(row=6, column=1)

# Define the function to update the output
def update_output():
    ttx_val = float(ttx.get())
    trx_val = float(trx.get())
    tmod_val = float(tmod.get())
    tgvd_val = float(tgvd.get())
    
    # Do some calculation with the inputs
    rise_time_calc = RiseTimeBudget(
        ttx=ttx_val,
        trx=trx_val,
        tmod=tmod_val,
        tgvd=tgvd_val,
    )
    
    # Update the output field
    tsys_output.config(text=str(rise_time_calc.tsys))
    BRZ_output.config(text=str(rise_time_calc.brz))
    BNRZ_output.config(text=str(rise_time_calc.bnrz))


# Create the submit button
submit_button = tk.Button(root, text="Submit", command=update_output)
submit_button.grid(row=9, column=0, columnspan=2)

# Start the main event loop
root.mainloop()
