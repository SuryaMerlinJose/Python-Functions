import os
import shutil
import  zipfile

#-----------Required paths are defined here ------------------------------------

download_path = r"C:\Users\Surya\Downloads\2024-02-28.zip"
DXC_SP = r"C:\Task_Zip\DXC_SP"
Processed_path = r"C:\Task_Zip\Processed"

#name of the zipped folder
folder_name="2024-02-28.zip" 

#---------- Function for moving and unzipping folder----------------------------
def DXC_SP_File_Move():
    Len_DXC = len(os.listdir(DXC_SP))
    list_dxc = os.listdir(DXC_SP)  # processed data in dxc
    # print(Len_DXC)
    print(list_dxc)

    if Len_DXC == 0:
        #moving zip file to DXC_SP 
        move_and_unzip()

    else:
        for file_name in list_dxc:
            source = os.path.join(DXC_SP, file_name)
            destination = os.path.join(Processed_path, file_name)
            shutil.move(source, destination)
        #moving zip file to DXC_SP    
        move_and_unzip()

#------------moving the zip from downloads to DXC_SP--------------------------
        
def move_and_unzip():
        shutil.move(download_path, DXC_SP)
        with zipfile.ZipFile(os.path.join(DXC_SP, folder_name), 'r') as zip_ref:
            zip_ref.extractall(DXC_SP)
        os.remove(os.path.join(DXC_SP, folder_name))

#--------------call the main function-------------------
        

DXC_SP_File_Move()


#---------------Description---------------------------------------------------------------
""" 
zipfile.ZipFile: This is a class from Python's zipfile module used to work with ZIP archives.

"""
    