import os

location = '/Users/harry/Dropbox (OpenDesk)/06_Production/07_Inventor/09_temp_publish/ATF/OTS/PUB/STD'

for dirpath, dirnames, filenames in os.walk(location):
	print(dirpath)
	print(filenames)