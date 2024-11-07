import tkinter as tk
from tkinter import ttk
import yaml

def submit_form():
   # Retrieve values from the form
   output = {}

   output["name"] = entry_name.get()
   output["spatial resolution"] = entry_spatial_resolution.get()
   output["variable spatial resolution"] = entry_variable_spatial_resolution.get()
   output["dimensionality"] = dims_var.get()
   output["temporal resolution"] = entry_temporal_resolution.get()
   output["variable temporal resolution"] = entry_variable_temporal_resolution.get()
   output["calibration variables"] = entry_calibration_vars.get()
   output["computatioal requirements"] = entry_computational_reqs.get()

   input_data = []
   if input_entries:
      for (iname,ivalue,iunits) in input_entries:
         input_data.append({"name":iname.get(), "value":ivalue.get(), "units":iunits.get()})
   output["input data"] = input_data

   output_data = []
   if output_entries:
      for (oname,ovalue,ounits) in output_entries:
         output_data.append({"name":oname.get(), "value":ovalue.get(), "units":ounits.get()})
   output["output data"] = output_data
   

   with open('data.yml', 'w') as outfile:
    yaml.dump(output, outfile, default_flow_style=False)

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
root.geometry("1500x800")
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
label_output_data_name = ttk.Label(root, text="Name:", foreground="purple")
label_output_data_value = ttk.Label(root, text="Value:", foreground="purple")
label_output_data_units = ttk.Label(root, text="Units:", foreground="purple")
label_calibration_vars = ttk.Label(root, text="Calibration Varables:", foreground="purple")
label_computational_reqs = ttk.Label(root, text="Computational Requirements:", foreground="purple")


entry_name = ttk.Entry(root) 
entry_spatial_resolution = ttk.Entry(root) 
entry_variable_spatial_resolution = ttk.Entry(root) 
# entry_dims = ttk.Entry(root) 
entry_temporal_resolution = ttk.Entry(root) 
entry_variable_temporal_resolution = ttk.Entry(root) 
# entry_input_data = ttk.Entry(root) 
# entry_output_data = ttk.Entry(root) 
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
# label_output_data.grid(row=6, column=0, padx=10, pady=5, sticky="w")
label_calibration_vars.grid(row=6, column=0, padx=10, pady=5, sticky="w")
label_computational_reqs.grid(row=7, column=0, padx=10, pady=5, sticky="w")

label_input_data.grid(row=0, column=3, padx=10, pady=5, sticky="w")
label_input_data_name.grid(row=0, column=4, padx=10, pady=5, sticky="w")
label_input_data_value.grid(row=0, column=5, padx=10, pady=5, sticky="w")
label_input_data_units.grid(row=0, column=6, padx=10, pady=5, sticky="w")
label_output_data.grid(row=0, column=7, padx=10, pady=5, sticky="w")
label_output_data_name.grid(row=0, column=8, padx=10, pady=5, sticky="w")
label_output_data_value.grid(row=0, column=9, padx=10, pady=5, sticky="w")
label_output_data_units.grid(row=0, column=10, padx=10, pady=5, sticky="w")


entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_spatial_resolution.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_variable_spatial_resolution.grid(row=2, column=1, padx=10, pady=5, sticky="w")
# entry_dims.grid(row=3, column=1, padx=10, pady=5, sticky="w")
dims_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")
entry_temporal_resolution.grid(row=4, column=1, padx=10, pady=5, sticky="w")
entry_variable_temporal_resolution.grid(row=5, column=1, padx=10, pady=5, sticky="w")
# entry_input_data.grid(row=6, column=1, padx=10, pady=5, sticky="w")
# entry_output_data.grid(row=6, column=1, padx=10, pady=5, sticky="w")
entry_calibration_vars.grid(row=6, column=1, padx=10, pady=5, sticky="w")
entry_computational_reqs.grid(row=7, column=1, padx=10, pady=5, sticky="w")


submit_button.grid(row=8, column=0, columnspan=2, pady=5)
result_label.grid(row=9, column=0, columnspan=2, pady=5)


# Configure style for the submit button
style = ttk.Style()
style.configure("TButton", foreground="red")

input_entries = []
input_count = 1 # To keep track of inserted entries

def add_input():
   global input_count
   input_entries.append((ttk.Entry(root),ttk.Entry(root),ttk.Entry(root)))
   (name, value, units) = input_entries[-1]
   name.grid(row=input_count, column=4, padx=5, pady=5)
   value.grid(row=input_count, column=5, padx=5, pady=5)
   units.grid(row=input_count, column=6, padx=5, pady=5)
   input_count += 1 # Increase the count by 1

add_input()

ttk.Button(root, text='Add', command=add_input).grid(row=1, column=3, padx=10, pady=5)

output_entries = []
output_count = 1 # To keep track of inserted entries

def add_output():
   global output_count
   output_entries.append((ttk.Entry(root),ttk.Entry(root),ttk.Entry(root)))
   (name, value, units) = output_entries[-1]
   name.grid(row=output_count, column=8, padx=5, pady=5)
   value.grid(row=output_count, column=9, padx=5, pady=5)
   units.grid(row=output_count, column=10, padx=5, pady=5)
   output_count += 1 # Increase the count by 1

add_output()

ttk.Button(root, text='Add', command=add_output).grid(row=1, column=7, padx=10, pady=5)


# Run the Tkinter main loop
root.mainloop()