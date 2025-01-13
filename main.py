import tkinter as tk
from tkinter import ttk
import customtkinter
import yaml

from collections import OrderedDict

def submit_form():
   # Retrieve values from the form
   output = OrderedDict()

   output["name"] = entry_name.get()
   output["spatial resolution"] = entry_spatial_resolution.get()
   output["variable spatial resolution"] = var_space_v.get()
   output["dimensionality"] = dims_var.get()
   output["temporal resolution"] = entry_temporal_resolution.get()
   output["variable temporal resolution"] = var_temp_v.get()

   input_data = []
   if input_entries:
      for (iname,idescription,iunits) in input_entries:
         od = OrderedDict()
         od["name"] = iname.get()
         od["description"] = idescription.get()
         od["units"] = iunits.get()
         input_data.append(od)
   output["input data"] = input_data

   output_data = []
   if output_entries:
      for (oname,odescription,ounits) in output_entries:
         od = OrderedDict()
         od["name"] = oname.get()
         od["description"] = odescription.get()
         od["units"] = ounits.get()
         output_data.append(od)
   output["output data"] = output_data

   calibration_vars_data = []
   if calibration_vars_entries:
      for (cname,cdescription,cunits) in calibration_vars_entries:
         od = OrderedDict()
         od["name"] = cname.get()
         od["description"] = cdescription.get()
         od["units"] = cunits.get()
         calibration_vars_data.append(od)
   output["calibration variables"] = calibration_vars_data
   
   # comp_reqs_data = []
   # if comp_reqs_entries:
   #    for (rname,rvalue) in comp_reqs_entries:
   #       od = OrderedDict()
   #       od[rname.get()] = rvalue.get()
   #       comp_reqs_data.append(od)
   # output["computational requirements"] = comp_reqs_data
   
   
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


root = customtkinter.CTk()
root.title("Model Metadata Form")
root.geometry("1600x800")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand="1")

canvas = tk.Canvas(main_frame)
canvas.pack(side="left", fill="both", expand="1")

scroll = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scroll.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scroll.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
secondairy_frame = tk.Frame(canvas)

canvas.create_window((0,0), window=secondairy_frame, anchor="nw")

def updateScrollRegion(region):
	canvas.update_idletasks()
	canvas.config(scrollregion=region)

input_frame = customtkinter.CTKScrollableFrame(main_frame)




label_name = ttk.Label(secondairy_frame, text="Name:", foreground="black")
label_spatial_resolution = ttk.Label(secondairy_frame, text="Spatial Resolution:", foreground="black")
label_variable_spatial_resolution = ttk.Label(secondairy_frame, text="Variable Spatial Resolution:", foreground="black")
label_dims = ttk.Label(secondairy_frame, text="Dimensionality:", foreground="black")
label_temporal_resolution = ttk.Label(secondairy_frame, text="Temporal Resolution:", foreground="black")
label_variable_temporal_resolution = ttk.Label(secondairy_frame, text="Variable Temporal Resolution:", foreground="black")

label_input_data = ttk.Label(secondairy_frame, text="Input Data:", foreground="black")
label_input_data_name = ttk.Label(secondairy_frame, text="Name:", foreground="black")
label_input_data_description = ttk.Label(secondairy_frame, text="Description:", foreground="black")
label_input_data_units = ttk.Label(secondairy_frame, text="Units:", foreground="black")
label_output_data = ttk.Label(secondairy_frame, text="Output Data:", foreground="black")
label_output_data_name = ttk.Label(secondairy_frame, text="Name:", foreground="black")
label_output_data_description = ttk.Label(secondairy_frame, text="Description:", foreground="black")
label_output_data_units = ttk.Label(secondairy_frame, text="Units:", foreground="black")

label_computational_reqs = ttk.Label(secondairy_frame, text="Computational Requirements:", foreground="black")
label_calibration_vars = ttk.Label(secondairy_frame, text="Calibration Varables", foreground="black")
label_calibration_vars_name = ttk.Label(secondairy_frame, text="Name:", foreground="black")
label_calibration_vars_description = ttk.Label(secondairy_frame, text="Description:", foreground="black")
label_calibration_vars_units = ttk.Label(secondairy_frame, text="Units:", foreground="black")


entry_name = ttk.Entry(secondairy_frame) 
entry_spatial_resolution = ttk.Entry(secondairy_frame) 
entry_variable_spatial_resolution = ttk.Entry(secondairy_frame) 
entry_temporal_resolution = ttk.Entry(secondairy_frame)
entry_temporal_resolution.insert(0, "P0Y0M0DT0H0M0S")
entry_variable_temporal_resolution = ttk.Entry(secondairy_frame)
entry_computational_reqs = ttk.Entry(secondairy_frame)


dims_var = tk.StringVar()
dims_combobox = ttk.Combobox(secondairy_frame, textvariable=dims_var, values=["0D", "1D", "2D", "3D"], state="readonly")
dims_combobox.set("0D")  # Default value


submit_button = ttk.Button(root, text="Submit", command=submit_form, style="TButton")


result_label = ttk.Label(root, text="", foreground="blue")


label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_spatial_resolution.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_variable_spatial_resolution.grid(row=2, column=0, padx=10, pady=5, sticky="w")
label_dims.grid(row=3, column=0, padx=10, pady=5, sticky="w")
label_temporal_resolution.grid(row=4, column=0, padx=10, pady=5, sticky="w")

label_variable_temporal_resolution.grid(row=5, column=0, padx=10, pady=5, sticky="w")
label_computational_reqs.grid(row=6, column=0, padx=10, pady=5, sticky="w")

label_input_data.grid(row=0, column=3, padx=10, pady=5, sticky="w")
label_input_data_name.grid(row=0, column=4, padx=10, pady=5, sticky="w")
label_input_data_description.grid(row=0, column=5, padx=10, pady=5, sticky="w")
label_input_data_units.grid(row=0, column=6, padx=10, pady=5, sticky="w")
label_output_data.grid(row=0, column=7, padx=10, pady=5, sticky="w")
label_output_data_name.grid(row=0, column=8, padx=10, pady=5, sticky="w")
label_output_data_description.grid(row=0, column=9, padx=10, pady=5, sticky="w")
label_output_data_units.grid(row=0, column=10, padx=10, pady=5, sticky="w")
label_calibration_vars.grid(row=7, column=0, padx=10, pady=5, sticky="w")
label_calibration_vars_name.grid(row=8, column=0, padx=10, pady=5, sticky="w")
label_calibration_vars_description.grid(row=8, column=1, padx=10, pady=5, sticky="w")
label_calibration_vars_units.grid(row=8, column=2, padx=10, pady=5, sticky="w")



entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_spatial_resolution.grid(row=1, column=1, padx=10, pady=5, sticky="w")
dims_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="w")
entry_temporal_resolution.grid(row=4, column=1, padx=10, pady=5, sticky="w")
entry_computational_reqs.grid(row=6, column=1, padx=10, pady=5, sticky="w")
# entry_calibration_vars.grid(row=9, column=1, padx=10, pady=5, sticky="w")


result_label.pack(side="bottom", padx=10, pady=5)
submit_button.pack(side="bottom", padx=10, pady=5)


input_entries = []
input_count = 1

def add_input():
   global input_count
   input_entries.append((ttk.Entry(secondairy_frame),ttk.Entry(secondairy_frame),ttk.Entry(secondairy_frame)))
   (name, description, units) = input_entries[-1]
   name.grid(row=input_count, column=4, padx=5, pady=5)
   description.grid(row=input_count, column=5, padx=5, pady=5)
   units.grid(row=input_count, column=6, padx=5, pady=5)
   input_count += 1
   updateScrollRegion(secondairy_frame.bbox())

add_input()

ttk.Button(secondairy_frame, text='Add', command=add_input).grid(row=1, column=3, padx=10, pady=5)

output_entries = []
output_count = 1

def add_output():
   global output_count
   output_entries.append((ttk.Entry(secondairy_frame),ttk.Entry(secondairy_frame),ttk.Entry(secondairy_frame)))
   (name, description, units) = output_entries[-1]
   name.grid(row=output_count, column=8, padx=5, pady=5)
   description.grid(row=output_count, column=9, padx=5, pady=5)
   units.grid(row=output_count, column=10, padx=5, pady=5)
   output_count += 1
   updateScrollRegion(secondairy_frame.bbox())

add_output()

ttk.Button(secondairy_frame, text='Add', command=add_output).grid(row=1, column=7, padx=10, pady=5)

calibration_vars_entries = []
calibration_vars_count = 1

def add_calibration_var():
   global calibration_vars_count
   calibration_vars_entries.append((ttk.Entry(secondairy_frame),ttk.Entry(secondairy_frame),ttk.Entry(secondairy_frame)))
   (name, description, units) = calibration_vars_entries[-1]
   name.grid(row= 8 + calibration_vars_count, column=0, padx=5, pady=5, sticky="w")
   description.grid(row= 8 + calibration_vars_count, column=1, padx=5, pady=5, sticky="w")
   units.grid(row= 8 + calibration_vars_count, column=2, padx=5, pady=5, sticky="w")
   calibration_vars_count += 1
   updateScrollRegion(secondairy_frame.bbox())

add_calibration_var()

ttk.Button(secondairy_frame, text='Add', command=add_calibration_var).grid(row=7, column=1, padx=10, pady=5, sticky="w")

#radio button for variable spatial resolution
button_frame_var_space = tk.Frame(secondairy_frame)
button_frame_var_space.grid(row=2, column=1)
var_space_v= tk.StringVar()
r1 = ttk.Radiobutton(button_frame_var_space, text='Yes', variable=var_space_v, value='Yes')
r1.grid(row=0,column=0, padx=10) 
r2 = ttk.Radiobutton(button_frame_var_space, text='No', variable=var_space_v, value='No')
r2.grid(row=0,column=1,padx=10) 
r3 = ttk.Radiobutton(button_frame_var_space, text='Configurable', variable=var_space_v, value='Configurable')
r3.grid(row=0,column=2, padx=10)

#radio buttons for variable temporal resolution
button_frame_var_temp = tk.Frame(secondairy_frame)
button_frame_var_temp.grid(row=5, column=1)
var_temp_v = tk.StringVar()
r4 = ttk.Radiobutton(button_frame_var_temp, text='Yes', variable=var_temp_v, value='Yes')
r4.grid(row=0,column=0, padx=10) 
r5 = ttk.Radiobutton(button_frame_var_temp, text='No', variable=var_temp_v, value='No')
r5.grid(row=0,column=1,padx=10) 
r6 = ttk.Radiobutton(button_frame_var_temp, text='Configurable', variable=var_temp_v, value='Configurable')
r6.grid(row=0,column=2, padx=10)




# Run the Tkinter main loop
root.mainloop()