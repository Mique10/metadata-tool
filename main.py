import tkinter as tk
from tkinter import ttk

def submit_form():
   # Retrieve values from the form
    name = entry_name.get()
    spatial_resolution = entry_spatial_resolution.get()
    variable_spatial_resolution = entry_variable_spatial_resolution.get()
    dims = dims_var.get()
    temporal_resolution = entry_temporal_resolution.get()
    variable_temporal_resolution = entry_variable_temporal_resolution.get()
   #  input_data = entry_input_data.get()
   #  output_data = entry_output_data.get()
    calibration_vars = entry_calibration_vars.get()
    computational_reqs = entry_computational_reqs.get()

    input_data = []
    if input_entries:
      for (name,value,units) in input_entries:
         input_data.append({"name":name.get(), "value":value.get(), "units":units.get()})


    # Success message
    result_label.config(text=f"YAML File Successfully Created!\n"
                           #   f"Name: {name}\n"
                           #   f"Spatial Resolution: {spatial_resolution}\n"
                           #   f"Variable Spatial Resolution: {variable_spatial_resolution}\n"
                           #   f"Dimensionality: {dims}\n"
                           #   f"Temporal Resolution: {temporal_resolution}\n"
                           #   f"Variable Temporal Resolution: {variable_temporal_resolution}\n"
                           #   f"Input Data: {input_data}\n"
                           #   f"Output Data: {output_data}\n"
                           #   f"Calibration Variables: {calibration_vars}\n"
                           #   f"Comutational Requirements: {computational_reqs}\n"
                             , foreground="blue")


root = tk.Tk()
root.title("Flood-Registration Form")
root.geometry("1000x800")
root.configure(bg="lightgreen")


label_name = ttk.Label(root, text="Name:", foreground="purple")
label_spatial_resolution = ttk.Label(root, text="Spatial Resolution:", foreground="purple")
label_variable_spatial_resolution = ttk.Label(root, text="Variable Spatial Resolution:", foreground="purple")
label_dims = ttk.Label(root, text="Dimensionality:", foreground="purple")
label_temporal_resolution = ttk.Label(root, text="Temporal Resolution:", foreground="purple")
label_variable_temporal_resolution = ttk.Label(root, text="Variable Temporal Resolution:", foreground="purple")
label_input_data = ttk.Label(root, text="Input Data:", foreground="purple")
label_input_data_name = ttk.Label(root, text="Name:", foreground="purple")
label_input_data_value = ttk.Label(root, text="Value:", foreground="purple")
label_input_data_units = ttk.Label(root, text="Units:", foreground="purple")
label_output_data = ttk.Label(root, text="Output Data:", foreground="purple")
label_calibration_vars = ttk.Label(root, text="Calibration Varables:", foreground="purple")
label_computational_reqs = ttk.Label(root, text="Computational Requirements:", foreground="purple")


entry_name = ttk.Entry(root) 
entry_spatial_resolution = ttk.Entry(root) 
entry_variable_spatial_resolution = ttk.Entry(root) 
# entry_dims = ttk.Entry(root) 
entry_temporal_resolution = ttk.Entry(root) 
entry_variable_temporal_resolution = ttk.Entry(root) 
# entry_input_data = ttk.Entry(root) 
entry_output_data = ttk.Entry(root) 
entry_calibration_vars = ttk.Entry(root) 
entry_computational_reqs = ttk.Entry(root) 

# Create a Combobox for gender
dims_var = tk.StringVar()
dims_combobox = ttk.Combobox(root, textvariable=dims_var, values=["0D", "1D", "2D", "3D"], state="readonly")
dims_combobox.set("0D")  # Default value


# Create submit button
submit_button = ttk.Button(root, text="Submit", command=submit_form, style="TButton")


# Create label for displaying the result
result_label = ttk.Label(root, text="", foreground="blue")


label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_spatial_resolution.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_variable_spatial_resolution.grid(row=2, column=0, padx=10, pady=5, sticky="w")
label_dims.grid(row=3, column=0, padx=10, pady=5, sticky="w")
label_temporal_resolution.grid(row=4, column=0, padx=10, pady=5, sticky="w")
label_variable_temporal_resolution.grid(row=5, column=0, padx=10, pady=5, sticky="w")
label_output_data.grid(row=6, column=0, padx=10, pady=5, sticky="w")
label_calibration_vars.grid(row=7, column=0, padx=10, pady=5, sticky="w")
label_computational_reqs.grid(row=8, column=0, padx=10, pady=5, sticky="w")

label_input_data.grid(row=0, column=3, padx=10, pady=5, sticky="w")
label_input_data_name.grid(row=0, column=4, padx=10, pady=5, sticky="w")
label_input_data_value.grid(row=0, column=5, padx=10, pady=5, sticky="w")
label_input_data_units.grid(row=0, column=6, padx=10, pady=5, sticky="w")


entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_spatial_resolution.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_variable_spatial_resolution.grid(row=2, column=1, padx=10, pady=5, sticky="w")
# entry_dims.grid(row=3, column=1, padx=10, pady=5, sticky="w")
dims_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")
entry_temporal_resolution.grid(row=4, column=1, padx=10, pady=5, sticky="w")
entry_variable_temporal_resolution.grid(row=5, column=1, padx=10, pady=5, sticky="w")
# entry_input_data.grid(row=6, column=1, padx=10, pady=5, sticky="w")
entry_output_data.grid(row=6, column=1, padx=10, pady=5, sticky="w")
entry_calibration_vars.grid(row=7, column=1, padx=10, pady=5, sticky="w")
entry_computational_reqs.grid(row=8, column=1, padx=10, pady=5, sticky="w")


submit_button.grid(row=10, column=0, columnspan=2, pady=10)
result_label.grid(row=11, column=0, columnspan=2, pady=10)


# Configure style for the submit button
style = ttk.Style()
style.configure("TButton", foreground="red")

input_entries = []
label_input_entries = []
count = 1 # To keep track of inserted entries


def add():
   global count
   input_entries.append((ttk.Entry(root),ttk.Entry(root),ttk.Entry(root)))
   (name, value, units) = input_entries[-1]
   name.grid(row=count, column=4, padx=5)
   value.grid(row=count, column=5, padx=5)
   units.grid(row=count, column=6, padx=5)
   count += 1 # Increase the count by 1

add()

ttk.Button(root, text='Add', command=add).grid(row=1, column=3, padx=10)


# Run the Tkinter main loop
root.mainloop()