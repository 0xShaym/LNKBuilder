# LNKBuilder

A python script that allows you to create completely customizable LNK files on Windows.

## Installation : 

Create venv python
```
python3 -m venv env

Windows

cmd.exe
- C:\> <venv>\Scripts\activate.bat
PowerShell
- PS C:\> <venv>\Scripts\Activate.ps1
```
Python modules
```
pip install -r requirements.txt
```
## How to config : 

### lnk_filename
Put the name of the output LNK file

### lnk_description
Put the descritpion of the output LNK file

### lnk_icon
Put the local file path of the icon of the output LNK file

### exe_path
Put the local file path of the of the executable which will launch the content of the payload.
In my example I use the lolbas [conhost](https://lolbas-project.github.io/lolbas/Binaries/Conhost/) with the --headless option.

### payload
Put the payload run by LNK file.

## How to use : 
Pass the config file as an argument to the python script. 
```
PS D:\Project\LNKBuilder> python3 .\create_lnk.py .\config.json
        
  _      _   _ _  __  ____        _ _     _
 | |    | \ | | |/ / |  _ \      (_) |   | |
 | |    |  \| | ' /  | |_) |_   _ _| | __| | ___ _ __
 | |    | . ` |  <   |  _ <| | | | | |/ _` |/ _ \ '__|
 | |____| |\  | . \  | |_) | |_| | | | (_| |  __/ |
 |______|_| \_|_|\_\ |____/ \__,_|_|_|\__,_|\___|_|

  [+] LNK Generated
The script executed successfully. Temporary directory: D:\Project\LNKBuilder\tmpgcn8n7gt
```

