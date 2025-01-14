import tkinter as tk
from tkinter import messagebox
import json

class ZomboidModderGUI:
    def __init__(self, root, json_path):
        self.root = root
        self.json_path = json_path
        self.data = self.load_json()

        # Set up the GUI layout
        self.setup_gui()

    def load_json(self):
        """ Load the JSON data from file """
        with open(self.json_path, 'r') as file:
            return json.load(file)

    def save_json(self):
        """ Save the JSON data back to file """
        with open(self.json_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def modify_property(self):
        """ Modify the selected property based on input fields """
        file_key = self.file_key_entry.get()
        property_name = self.property_name_entry.get()
        new_value = self.new_value_entry.get()

        if file_key in self.data and property_name in self.data[file_key]:
            self.data[file_key][property_name] = int(new_value)
            self.save_json()
            messagebox.showinfo("Success", f"Updated {property_name} to {new_value} in {file_key}")
        else:
            messagebox.showerror("Error", f"Invalid file key or property name")

    def setup_gui(self):
        """ Set up GUI widgets """
        tk.Label(self.root, text="File Key (e.g., 'gos_campfire.bin')").pack()
        self.file_key_entry = tk.Entry(self.root)
        self.file_key_entry.pack()

        tk.Label(self.root, text="Property Name (e.g., 'property_1')").pack()
        self.property_name_entry = tk.Entry(self.root)
        self.property_name_entry.pack()

        tk.Label(self.root, text="New Value (integer)").pack()
        self.new_value_entry = tk.Entry(self.root)
        self.new_value_entry.pack()

        self.modify_button = tk.Button(self.root, text="Modify Property", command=self.modify_property)
        self.modify_button.pack()

# Create the Tkinter window
root = tk.Tk()
root.title("Zomboid Modder GUI")

# Specify the path to your JSON file here
modder_gui = ZomboidModderGUI(root, "D:/SSDUSER/Documents/GitHub/zomboid-modder/objects.json")



root.mainloop()
