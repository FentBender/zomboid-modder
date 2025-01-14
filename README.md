# Zomboid Modder

## Overview
This tool allows you to easily modify and generate mod files for the Zomboid game. It interacts with a JSON configuration file to automate the process of updating mod properties and creating mod files.

## Project Structure
- **`objects.json`**: Contains the main data for your mods.
- **`mods/`**: Generated mod files will be placed here.
- **`mod_automation.py`**: Core logic for modifying the JSON and generating mod files.
- **`modding_automation_tool.py`**: Central tool for managing dynamic updates and more.
- **`zomboid_modder_gui.py`**: GUI for interacting with the tool.

## Usage

### 1. Run the GUI
To launch the Tkinter-based GUI, run the `zomboid_modder_gui.py` script. The GUI allows you to modify properties and generate mod files easily.

```bash
python zomboid_modder_gui.py
