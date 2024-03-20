import os


input_path=r"C:\Task_Zip\DXC_SP\Input"   #provide the path of the folder in which we need to check for .xlsx

def check_xlsx(input_path):

    # list_input=os.listdir(input_path)
    # print(list_input)

    excel_files = []            #this list is used to store .xlsx file paths if there are more than one .xlsx
    
    for root, dirs, files in os.walk(input_path):
        for file in files:
            if file.endswith('.xlsx'):
                excel_path=os.path.join(root, file)
                excel_files.append(excel_path)      #storing each .xlsx path to the list

#-------------------checks whether the folder contains atleast one .xlsx-----------------------------------------------------------------------            
    if excel_files:                 
        return True, excel_files
    else:
        return False, None

status, excel = check_xlsx(input_path)
print(status)

#---------------------If the folder contains .xlsx then all the .xlsx paths are printed by looping the list of excel paths-----------------------
if status:
    for excel_file in excel:
        print(excel_file)
else:
    print("No .xlsx files found.")
          

                




