import os,shutil
path=r"A://python//Files"
file_name=os.listdir(path)
folder_names=['csv files','image files']
for l in range(len(folder_names)):
    if not os.path.exists(os.path.join(path, folder_names[l])):
        os.makedirs(os.path.join(path,folder_names[l]))
print("Moving Files...")
count1,count2=0,0
for i in file_name:  
    if '.csv' in i : 
        shutil.move(os.path.join(path,i),os.path.join(path,'csv files',i))
        count1+=1
    elif '.jpeg'in i:
        shutil.move(os.path.join(path,i),os.path.join(path,'image files',i))
        count2+=1
    else:
        print('{} is not a valid format'.format(i))
print("Number of csv files moved are {}".format(count1))
print("Number of image files moved are {}".format(count2))