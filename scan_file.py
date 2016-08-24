import os
import os.path

location = '/Users/harry/Dropbox (OpenDesk)/06_Production/07_Inventor/09_temp_publish/LEN/BKO'
bad_list = []

for dirpath, dirnames, filenames in os.walk(location):
  for filename in [f for f in filenames if f.endswith(".dxf")]:
    
    file_path = os.path.join(dirpath, filename)

    if '(3/4")' in open(file_path).read() and filename[:-20] not in bad_list:
      bad_list.append(filename[:-20])
      break

  # for filename in [f for f in filenames if f.endswith(".dxf")]:
    
  #   file_path = os.path.join(dirpath, filename)

  #   if '(3/4")' in open(file_path).read() and filename[:-20] not in bad_list:
  #     bad_list.append(filename[:-20])
  #     break

  # for filename in [f for f in filenames if f.endswith("12.00~0.0.dxf")]:
    
  #   file_path = os.path.join(dirpath, filename)

  #   if '(3/4")' in open(file_path).read() and filename[:-20] not in bad_list:
  #     bad_list.append(filename[:-20])
  #     break

print("\n".join(bad_list))
