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
   dims_list = []
   if zero_dim_var.get():
      dims_list.append("0D")
   if one_dim_var.get():
      dims_list.append("1D")
   if two_dim_var.get():
      dims_list.append("2D")
   if three_dim_var.get():
      dims_list.append("3D")
   dims_string = ", ".join(dims_list)
   output["dimensionality"] = dims_string



   output["temporal resolution"] = entry_temporal_resolution.get()
   output["variable temporal resolution"] = var_temp_v.get()

   input_data = []
   if input_entries:
      for (iname,idescription,iunits) in input_entries:
         od = OrderedDict()
         if iname.get() and idescription.get() and iunits.get():
            od["name"] = iname.get()
            od["description"] = idescription.get()
            od["units"] = iunits.get()
            input_data.append(od)
   output["input data"] = input_data

   output_data = []
   if output_entries:
      for (oname,odescription,ounits) in output_entries:
         od = OrderedDict()
         if oname.get() and odescription.get() and ounits.get():
            od["name"] = oname.get()
            od["description"] = odescription.get()
            od["units"] = ounits.get()
            output_data.append(od)
   output["output data"] = output_data

   calibration_vars_data = []
   if calibration_vars_entries:
      for (cname,cdescription,cunits) in calibration_vars_entries:
         od = OrderedDict()
         if cname.get() and cdescription.get() and cunits.get():
            od["name"] = cname.get()
            od["description"] = cdescription.get()
            od["units"] = cunits.get()
            calibration_vars_data.append(od)
   output["calibration variables"] = calibration_vars_data
   
   comp_reqs_data = []
   if comp_reqs_entries:
      for (rkey, rvalue) in comp_reqs_entries:
         od = OrderedDict()
         if rkey.get() and rvalue.get():
            od[rkey.get()] = rvalue.get()
            comp_reqs_data.append(od)
   output["computational requirements"] = comp_reqs_data
   
   
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

# canvas = tk.Canvas(main_frame)
# canvas.pack(side="left", fill="both", expand="1")

# scroll = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
# scroll.pack(side="right", fill="y")

# canvas.configure(yscrollcommand=scroll.set)
# canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
# root = tk.Frame(canvas)

# canvas.create_window((0,0), window=root, anchor="nw")

# def updateScrollRegion(region):
# 	canvas.update_idletasks()
# 	canvas.config(scrollregion=region)

input_frame = customtkinter.CTkScrollableFrame(main_frame, width=400, height=300)
output_frame = customtkinter.CTkScrollableFrame(main_frame, width=400, height=300)
calibration_frame = customtkinter.CTkScrollableFrame(main_frame, width=400, height=300)
comp_reqs_frame = customtkinter.CTkScrollableFrame(main_frame, width=400, height=300)




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

label_comp_reqs = ttk.Label(main_frame, text="Computational Requirements:", foreground="black")
label_comp_reqs_name = ttk.Label(comp_reqs_frame, text="Key:", foreground="black")
label_comp_reqs_value = ttk.Label(comp_reqs_frame, text="Value:", foreground="black")

label_calibration_vars = ttk.Label(main_frame, text="Calibration Varables", foreground="black")
label_calibration_vars_name = ttk.Label(calibration_frame, text="Name:", foreground="black")
label_calibration_vars_description = ttk.Label(calibration_frame, text="Description:", foreground="black")
label_calibration_vars_units = ttk.Label(calibration_frame, text="Units:", foreground="black")


entry_name = ttk.Entry(main_frame) 
entry_spatial_resolution = ttk.Entry(main_frame) 
entry_variable_spatial_resolution = ttk.Entry(main_frame) 
entry_temporal_resolution = ttk.Entry(main_frame)
entry_temporal_resolution.insert(0, "P0Y0M0DT0H0M0S")
entry_variable_temporal_resolution = ttk.Entry(main_frame)


submit_button = ttk.Button(root, text="Submit", command=submit_form, style="TButton")


result_label = ttk.Label(root, text="", foreground="blue")


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

entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="w")
entry_spatial_resolution.grid(row=1, column=1, padx=10, pady=5, sticky="w")
entry_temporal_resolution.grid(row=4, column=1, padx=10, pady=5, sticky="w")
# entry_computational_reqs.grid(row=6, column=1, padx=10, pady=5, sticky="w")
# entry_calibration_vars.grid(row=9, column=1, padx=10, pady=5, sticky="w")


result_label.pack(side="bottom", padx=10, pady=5)
submit_button.pack(side="bottom", padx=10, pady=5)


input_entries = []
input_count = 1

def add_input():
   global input_count
   input_entries.append((ttk.Entry(input_frame),ttk.Entry(input_frame),ttk.Entry(input_frame)))
   (name, description, units) = input_entries[-1]
   name.grid(row=input_count, column=0, padx=5, pady=5)
   description.grid(row=input_count, column=1, padx=5, pady=5)
   units.grid(row=input_count, column=2, padx=5, pady=5)
   input_count += 1
   # updateScrollRegion(main_frame.bbox())

add_input()

ttk.Button(main_frame, text='Add', command=add_input).grid(row=0, column=4, padx=10, pady=5)

output_entries = []
output_count = 1

def add_output():
   global output_count
   output_entries.append((ttk.Entry(output_frame),ttk.Entry(output_frame),ttk.Entry(output_frame)))
   (name, description, units) = output_entries[-1]
   name.grid(row=output_count, column=0, padx=5, pady=5)
   description.grid(row=output_count, column=1, padx=5, pady=5)
   units.grid(row=output_count, column=2, padx=5, pady=5)
   output_count += 1
   # updateScrollRegion(main_frame.bbox())

add_output()

ttk.Button(main_frame, text='Add', command=add_output).grid(row=0, column=7, padx=10, pady=5)

calibration_vars_entries = []
calibration_vars_count = 1

def add_calibration_var():
   global calibration_vars_count
   calibration_vars_entries.append((ttk.Entry(calibration_frame),ttk.Entry(calibration_frame),ttk.Entry(calibration_frame)))
   (name, description, units) = calibration_vars_entries[-1]
   name.grid(row= 8 + calibration_vars_count, column=0, padx=5, pady=5, sticky="w")
   description.grid(row= 8 + calibration_vars_count, column=1, padx=5, pady=5, sticky="w")
   units.grid(row= 8 + calibration_vars_count, column=2, padx=5, pady=5, sticky="w")
   calibration_vars_count += 1
   # updateScrollRegion(main_frame.bbox())

add_calibration_var()

ttk.Button(main_frame, text='Add', command=add_calibration_var).grid(row=11, column=4, padx=10, pady=5)

comp_reqs_entries = []
comp_reqs_count = 1

def add_comp_reqs_var():
   global comp_reqs_count
   comp_reqs_entries.append((ttk.Entry(comp_reqs_frame),ttk.Entry(comp_reqs_frame)))
   (name, description) = comp_reqs_entries[-1]
   name.grid(row= 8 + comp_reqs_count, column=0, padx=5, pady=5, sticky="w")
   description.grid(row= 8 + comp_reqs_count, column=1, padx=5, pady=5, sticky="w")
   comp_reqs_count += 1
   # updateScrollRegion(main_frame.bbox())

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