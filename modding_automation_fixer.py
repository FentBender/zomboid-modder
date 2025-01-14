import json
import os
import subprocess

class ModAutomation:
    def __init__(self, json_path, mod_dir, repo_dir, update_file=None):
        """Initialize the automation with file paths and optional update instructions."""
        self.json_path = json_path
        self.mod_dir = mod_dir
        self.repo_dir = repo_dir
        self.update_file = update_file  # Optional: File containing dynamic updates (JSON format)
        self.data = self.load_json()

    def load_json(self):
        """Load the JSON data from file."""
        if not os.path.exists(self.json_path):
            raise FileNotFoundError(f"Error: {self.json_path} does not exist.")
        with open(self.json_path, 'r') as file:
            return json.load(file)

    def save_json(self):
        """Save the updated JSON data back to file."""
        with open(self.json_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def modify_property(self, file_key, property_name, new_value):
        """Modify a specific property for a given mod."""
        if file_key not in self.data:
            print(f"Error: {file_key} not found in the data.")
            return
        
        if property_name not in self.data[file_key]:
            print(f"Error: {property_name} not found in {file_key}.")
            return
        
        try:
            # Convert the new value to an integer if necessary
            new_value = int(new_value)
        except ValueError:
            print(f"Error: Invalid value '{new_value}' for {property_name}. Must be an integer.")
            return

        # Update the property
        self.data[file_key][property_name] = new_value
        print(f"Updated {property_name} to {new_value} in {file_key}")

    def generate_mod_files(self):
        """Automatically generate mod files based on the JSON data."""
        for file_key, properties in self.data.items():
            mod_file_path = os.path.join(self.mod_dir, f"{file_key}")
            try:
                with open(mod_file_path, 'w') as mod_file:
                    json.dump(properties, mod_file, indent=4)
                print(f"Generated mod file: {mod_file_path}")
            except IOError as e:
                print(f"Error: Could not write file {mod_file_path}: {e}")

    def commit_changes(self):
        """Commit changes to Git and push to the remote repository."""
        try:
            subprocess.run(["git", "add", "."], cwd=self.repo_dir, check=True)
            subprocess.run(['git', 'commit', '-m', 'Auto commit from mod automation'], cwd=self.repo_dir, check=True)
            subprocess.run(['git', 'push'], cwd=self.repo_dir, check=True)
            print("Changes pushed to GitHub.")
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {e}")

    def apply_dynamic_updates(self):
        """Apply dynamic updates from a JSON file."""
        if self.update_file and os.path.exists(self.update_file):
            try:
                with open(self.update_file, 'r') as file:
                    updates = json.load(file)
                    for update in updates:
                        file_key = update.get("file_key")
                        property_name = update.get("property_name")
                        new_value = update.get("new_value")
                        if file_key and property_name and new_value is not None:
                            self.modify_property(file_key, property_name, new_value)
            except Exception as e:
                print(f"Error: Failed to apply dynamic updates from {self.update_file}: {e}")
        else:
            print("No dynamic update file provided or file does not exist.")

    def run(self):
        """Execute the automation process."""
        # Apply dynamic updates first if a file is provided
        self.apply_dynamic_updates()
        
        # Generate the mod files after modifying the properties
        self.generate_mod_files()
        
        # Commit and push changes (optional)
        self.commit_changes()


if __name__ == "__main__":
    # Define correct paths
    json_path = "D:/SSDUSER/Documents/GitHub/Zomboid-modder/objects.json"
    mod_dir = "D:/SSDUSER/Documents/GitHub/Zomboid-modder/mods/"
    repo_dir = "D:/SSDUSER/Documents/GitHub/Zomboid-modder/"
    update_file = "D:/SSDUSER/Documents/GitHub/Zomboid-modder/updates.json"  # Optional

    # Instantiate and run the automation
    automation = ModAutomation(json_path, mod_dir, repo_dir, update_file)
    automation.run()
