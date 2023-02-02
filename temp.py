import os
import tempfile

# Create a batch file with the commands to delete the temporary files
batch_file = os.path.join(tempfile.gettempdir(), "clear_temp.bat")
with open(batch_file, "w") as f:
    f.write("@echo off\n")
    f.write("del /s /q %temp%\n")

# Add the batch file to the startup folder
startup_folder = os.path.join(os.environ["USERPROFILE"], "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
shutil.copy(batch_file, startup_folder)
