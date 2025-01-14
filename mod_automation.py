import os
import time

# Path to your modding directory
repo_path = "D:/SSDUSER/Documents/GitHub/zomboid-modder"

# Create a new mod file (for demonstration)
def create_new_mod_file():
    mod_file_path = os.path.join(repo_path, "new_mod_file.txt")
    
    with open(mod_file_path, "w") as file:
        file.write("This is an auto-generated mod file.")
    
    print(f"New mod file created at {mod_file_path}")

# List current files in the repository
def list_files_in_repo():
    files = os.listdir(repo_path)
    print(f"Current files in repo: {files}")

# Main function to automate tasks
def main():
    print("Starting modding automation...")
    
    # List files
    list_files_in_repo()

    # Simulate delay (e.g., if you want to do something periodically)
    time.sleep(2)

    # Create a new mod file
    create_new_mod_file()

    # List files again to show the new file
    list_files_in_repo()

if __name__ == "__main__":
    main()
