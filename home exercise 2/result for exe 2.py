

from pathlib import Path
import os
import glob


# exersice 2

##############################################################################################

# 2

# using os.walk to get all info from folder.
#folderlist = list(os.walk("C:\\Users\\Itay Zrihan\\Desktop\\main_folder"))
#print(folderlist)

##############################################################################################

# 3

#using list, map and glob glob with os path base on name to find the name of each picture.

#pictures_names = list(map(os.path.basename, glob.glob("C:\\Users\\Itay Zrihan\\Desktop\\main_folder" + '/**/*.jpg', recursive=True)))
#print(pictures_names)

##############################################################################################

# 4
#using glob glob and print len for get the number of pictures.
#numofpics = (glob.glob("C:\\Users\\Itay Zrihan\\Desktop\\main_folder" + '/**/*.jpg', recursive=True))
#print(len(numofpics))


##############################################################################################

# 5

# print len on os.walk to get the number of folders.

#folderlist = list(os.walk("C:\\Users\\Itay Zrihan\\Desktop\\main_folder"))
#print(len(folderlist))

##############################################################################################

# 6

# using os.path to get that path of each folder

#folder_path = (glob.glob("C:\\Users\\Itay Zrihan\\Desktop\\main_folder" + '/**/', recursive=True))
#print(folder_path)

##############################################################################################

# 7

#slice_list = []
#path_list = list((glob.glob("C:\\Users\\Itay Zrihan\\Desktop\\main_folder" + '/**/*.jpg', recursive=True)))
#list(filter(lambda x: slice_list.append(x.split(os.sep)), path_list))  # Creates a list of lists that holds a sliced
# version of the path_list
#final_dict = {}  # An empty dictionary for later use.
#list(filter(lambda x: final_dict.update({x[-2]: [x[-1]]}) if x[-2] not in final_dict else final_dict[x[-2]].append(x[-1]), slice_list))
# Using Filter with lambda: Runs on the entire slice list
# and checks if current key is already in list if so append value.
# else: Add new key and value to the dictionary.
#print(final_dict)

##############################################################################################


#8
#using lambda glob and path to get the folders with 'i' letter.
# print(list(map(lambda p: p.name, filter(lambda p: p.is_dir(), Path(r"C:\\Users\\Itay Zrihan\\Desktop\\main_folder").rglob('*i*')))))

##############################################################################################
