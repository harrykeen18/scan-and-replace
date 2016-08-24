import os
import os.path

location = '/Users/harry/Dropbox (OpenDesk)/06_Production/07_Inventor/01_ranges/LEN/LFT/PUB/STD/W-915/L-2335/C-ST/A-SA/M-AP/publish'
# bad_list = []

for dirpath, dirnames, filenames in os.walk(location):
  for filename in filenames:
    
    file_path = os.path.join(dirpath, filename)

    if filename.endswith(".dxf"):

      # Read in the file
      filedata = None
      with open(file_path, 'r') as file:
        filedata = file.read()

      # Replace the target string
      filedata = filedata.replace('(3/4")', '(1/4")')

      # Write the file out again
      with open(file_path, 'w') as file:
        file.write(filedata)

    if filename.endswith(".dwg"):

      os.remove(file_path)

