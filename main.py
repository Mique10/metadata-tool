import tkinter as tk
from tkinter import ttk
import customtkinter
import yaml

from collections import OrderedDict


class MultiInputs():
   """
   Class that handles creation of new input fields upon button press
   """
   frame = None
   
   def __init__(self, frame, button_row, button_column):
      """
      Initialize variables and create button and add first row of input fields
      """
      self.frame = frame
      self.entries = []
      ttk.Button(main_frame, text='Add', command=self.add_input_field).grid(row=button_row, column=button_column, padx=10, pady=5)
      self.add_input_field()

   def add_input_field(self):
      """
      Add new row of input fields
      """
      self.entries.append((ttk.Entry(self.frame),ttk.Entry(self.frame),ttk.Entry(self.frame)))
      (name, description, units) = self.entries[-1]
      count = len(self.entries)
      name.grid(row=count, column=0, padx=5, pady=5)
      description.grid(row=count, column=1, padx=5, pady=5)
      units.grid(row=count, column=2, padx=5, pady=5)

def submit_form():
   """
   Retrieve values from the form. Save values in correct format to a .YAML file
   """
   output = OrderedDict()

   output["name"] = entry_name.get()
   output["spatial resolution"] = entry_spatial_resolution.get()
   output["variable spatial resolution"] = var_space_v.get()
   output["dimensionality"] = get_dimensions()
   output["temporal resolution"] = entry_temporal_resolution.get()
   output["variable temporal resolution"] = var_temp_v.get()
   print(inputs.entries)
   output["input data"] = get_multi_entry(inputs.entries)
   output["output data"] = get_multi_entry(outputs.entries)
   output["calibration variables"] = get_multi_entry(calibration_vars.entries)
   output["computational requirements"] = get_comp_reqs()
   
   #Allow ordered dict to be dumped to yaml
   """ http://stackoverflow.com/a/8661021 """
   represent_dict_order = lambda self, data:  self.represent_mapping('tag:yaml.org,2002:map', data.items())
   yaml.add_representer(OrderedDict, represent_dict_order)

   with open('data.yml', 'w') as outfile:
      yaml.dump(output, outfile, default_flow_style=False)

   # Success message
   result_label.config(text=f"YAML File Successfully Created!\n"
                        #   f"Name: {name}\n"
                        #   f"Spatial Resolution: {spatial_resolution}\n"
                        #   f"Variable Spatial Resolution: {var_space_v.get()}\n"
                        #   f"Dimensionality: {dims}\n"
                        #   f"Temporal Resolution: {temporal_resolution}\n"
                        #   f"Variable Temporal Resolution: {var_temp_v.get()}\n"
                        #   f"Input Data: {input_data}\n"
                        #   f"Output Data: {output_data}\n"
                        #   f"Calibration Variables: {calibration_vars}\n"
                        #   f"Comutational Requirements: {computational_reqs}\n"
                           , foreground="blue")
   
def get_dimensions():
   """
   Get the dimensional data from the form
   """
   dims_list = []
   if zero_dim_var.get():
      dims_list.append("0D")
   if one_dim_var.get():
      dims_list.append("1D")
   if two_dim_var.get():
      dims_list.append("2D")
   if three_dim_var.get():
      dims_list.append("3D")
   return ", ".join(dims_list)

def get_multi_entry(entries):
   """
   Get the data from the form for a metadata point with multiple entries
   """
   results = []
   if entries:
      for (name,description,units) in entries:
         od = OrderedDict()
         if name.get() or description.get() or units.get():
            od["name"] = name.get()
            od["description"] = description.get()
            od["units"] = units.get()
            results.append(od)
   return results

def get_comp_reqs():
   """
   Get the computational requirements data from the form
   """
   comp_reqs_data = []
   if comp_reqs_entries:
      for (rkey, rvalue) in comp_reqs_entries:
         od = OrderedDict()
         if rkey.get() and rvalue.get():
            od[rkey.get()] = rvalue.get()
            comp_reqs_data.append(od)
   return comp_reqs_data


root = customtkinter.CTk()
root.title("Model Metadata Form")
root.geometry("1300x800")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand="1")

#Scrollable frames for multi entry metadata points
input_frame = customtkinter.CTkScrollableFrame(main_frame, width=400, height=300)
output_frame = customtkinter.CTkScrollableFrame(main_frame, width=400, height=300)
calibration_frame = customtkinter.CTkScrollableFrame(main_frame, width=400, height=300)
comp_reqs_frame = customtkinter.CTkScrollableFrame(main_frame, width=400, height=300)


#All labels in the program
label_name = ttk.Label(main_frame, text="Name:", foreground="black")
label_spatial_resolution = ttk.Label(main_frame, text="Spatial Resolution:", foreground="black")
label_variable_spatial_resolution = ttk.Label(main_frame, text="Variable Spatial Resolution:", foreground="black")
label_dims = ttk.Label(main_frame, text="Dimensionality:", foreground="black")
label_temporal_resolution = ttk.Label(main_frame, text="Temporal Resolution:", foreground="black")
label_variable_temporal_resolution = ttk.Label(main_frame, text="Variable Temporal Resolution:", foreground="black")

label_input_data = ttk.Label(main_frame, text="Input Data:", foreground="black")
label_input_data_name = ttk.Label(input_frame, text="Name:", foreground="black")
label_input_data_description = ttk.Label(input_frame, text="Description:", foreground="black")
label_input_data_units = ttk.Label(input_frame, text="Units:", foreground="black")

label_output_data = ttk.Label(main_frame, text="Output Data:", foreground="black")
label_output_data_name = ttk.Label(output_frame, text="Name:", foreground="black")
label_output_data_description = ttk.Label(output_frame, text="Description:", foreground="black")
label_output_data_units = ttk.Label(output_frame, text="Units:", foreground="black")

label_calibration_vars = ttk.Label(main_frame, text="Calibration Varables", foreground="black")
label_calibration_vars_name = ttk.Label(calibration_frame, text="Name:", foreground="black")
label_calibration_vars_description = ttk.Label(calibration_frame, text="Description:", foreground="black")
label_calibration_vars_units = ttk.Label(calibration_frame, text="Units:", foreground="black")

label_comp_reqs = ttk.Label(main_frame, text="Computational Requirements:", foreground="black")
label_comp_reqs_name = ttk.Label(comp_reqs_frame, text="Key:", foreground="black")
label_comp_reqs_value = ttk.Label(comp_reqs_frame, text="Value:", foreground="black")

#Entry boxes
entry_name = ttk.Entry(main_frame) 
entry_spatial_resolution = ttk.Entry(main_frame) 
entry_variable_spatial_resolution = ttk.Entry(main_frame) 
entry_temporal_resolution = ttk.Entry(main_frame)
entry_temporal_resolution.insert(0, "P0Y0M0DT0H0M0S")
entry_variable_temporal_resolution = ttk.Entry(main_frame)

#Submit button and label for results
submit_button = ttk.Button(root, text="Submit", command=submit_form, style="TButton")
result_label = ttk.Label(root, text="", foreground="blue")

#Label Positions
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_spatial_resolution.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_variable_spatial_resolution.grid(row=2, column=0, padx=10, pady=5, sticky="w")
label_dims.grid(row=3, column=0, padx=10, pady=5, sticky="w")
label_temporal_resolution.grid(row=4, column=0, padx=10, pady=5, sticky="w")
label_variable_temporal_resolution.grid(row=5, column=0, padx=10, pady=5, sticky="w")

#Input variables frame
label_input_data.grid(row=0, column=2, padx=10, pady=5, sticky="w")
input_frame.grid(row=1, column=2, padx=10, pady=5, rowspan=10, columnspan=3)
label_input_data_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_input_data_description.grid(row=0, column=1, padx=10, pady=5, sticky="w")
label_input_data_units.grid(row=0, column=2, padx=10, pady=5, sticky="w")

#output variables frame
label_output_data.grid(row=0, column=5, padx=10, pady=5, sticky="w")
output_frame.grid(row=1, column=5, padx=10, pady=5, rowspan=10, columnspan=3)
label_output_data_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_output_data_description.grid(row=0, column=1, padx=10, pady=5, sticky="w")
label_output_data_units.grid(row=0, column=2, padx=10, pady=5, sticky="w")

#Calibration variables frame
label_calibration_vars.grid(row=11, column=2, padx=10, pady=5, sticky="w")
calibration_frame.grid(row=12, column=2, padx=10, pady=5, rowspan=10, columnspan=3)
label_calibration_vars_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_calibration_vars_description.grid(row=0, column=1, padx=10, pady=5, sticky="w")
label_calibration_vars_units.grid(row=0, column=2, padx=10, pady=5, sticky="w")

#computational Requirements frame
label_comp_reqs.grid(row=11, column=5, padx=10, pady=5, sticky="w")
comp_reqs_frame.grid(row=12, column=5, padx=10, pady=5, rowspan=10, columnspan=3)
label_comp_reqs_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_comp_reqs_value.grid(row=0, column=1, padx=10, pady=5, sticky="w")

#Entry boxes positions
entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_spatial_resolution.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_temporal_resolution.grid(row=4, column=1, padx=10, pady=5, sticky="w")

#Submit button and result label position
result_label.pack(side="bottom", padx=10, pady=5)
submit_button.pack(side="bottom", padx=10, pady=5)

# classes for MultiInputs
inputs = MultiInputs(input_frame, 0, 4)
outputs = MultiInputs(output_frame, 0, 7)
calibration_vars = MultiInputs(calibration_frame, 11, 4)

# Computational Requirements multi input
comp_reqs_entries = []
comp_reqs_count = 1

def add_comp_reqs_var():
   global comp_reqs_count
   comp_reqs_entries.append((ttk.Entry(comp_reqs_frame),ttk.Entry(comp_reqs_frame)))
   (name, description) = comp_reqs_entries[-1]
   name.grid(row= 8 + comp_reqs_count, column=0, padx=5, pady=5, sticky="w")
   description.grid(row= 8 + comp_reqs_count, column=1, padx=5, pady=5, sticky="w")
   comp_reqs_count += 1

add_comp_reqs_var()
ttk.Button(main_frame, text='Add', command=add_comp_reqs_var).grid(row=11, column=7, padx=10, pady=5)

#radio button for variable spatial resolution
button_frame_var_space = tk.Frame(main_frame)
button_frame_var_space.grid(row=2, column=1)
var_space_v= tk.StringVar()
r1 = ttk.Radiobutton(button_frame_var_space, text='Yes', variable=var_space_v, value='Yes')
r1.grid(row=0,column=0, padx=10) 
r2 = ttk.Radiobutton(button_frame_var_space, text='No', variable=var_space_v, value='No')
r2.grid(row=0,column=1,padx=10) 
r3 = ttk.Radiobutton(button_frame_var_space, text='Configurable', variable=var_space_v, value='Configurable')
r3.grid(row=0,column=2, padx=10)

#radio buttons for variable temporal resolution
button_frame_var_temp = tk.Frame(main_frame)
button_frame_var_temp.grid(row=5, column=1)
var_temp_v = tk.StringVar()
r4 = ttk.Radiobutton(button_frame_var_temp, text='Yes', variable=var_temp_v, value='Yes')
r4.grid(row=0,column=0, padx=10) 
r5 = ttk.Radiobutton(button_frame_var_temp, text='No', variable=var_temp_v, value='No')
r5.grid(row=0,column=1,padx=10) 
r6 = ttk.Radiobutton(button_frame_var_temp, text='Configurable', variable=var_temp_v, value='Configurable')
r6.grid(row=0,column=2, padx=10)

#Checkboxes for dimensions
button_frame_dims = tk.Frame(main_frame)
button_frame_dims.grid(row=3, column=1)
zero_dim_var = tk.IntVar()
zero_dim = ttk.Checkbutton(button_frame_dims, text="0D", onvalue=1, offvalue=0, variable=zero_dim_var)
zero_dim.grid(row=0,column=0, padx=10)
one_dim_var = tk.IntVar()
one_dim = ttk.Checkbutton(button_frame_dims, text="1D", onvalue=1, offvalue=0, variable=one_dim_var)
one_dim.grid(row=0,column=1, padx=10)
two_dim_var = tk.IntVar()
two_dim = ttk.Checkbutton(button_frame_dims, text="2D", onvalue=1, offvalue=0, variable=two_dim_var)
two_dim.grid(row=0,column=2, padx=10)
three_dim_var = tk.IntVar()
three_dim = ttk.Checkbutton(button_frame_dims, text="3D", onvalue=1, offvalue=0, variable=three_dim_var)
three_dim.grid(row=0,column=3, padx=10)

# Run the Tkinter main loop
root.mainloop()