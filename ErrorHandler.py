## KNOWN ERRORS
# 1) If the log file is deleted but the containing directory remains an error will be caused.

## THINGS TO ADD
# 1) Implement Entry IDs. This should be a unique ID for each entry into the log file.
# 2) Implement a function that allows for reading a specific entry ID
# 3) Allow display of error upon writing.
# 4) Rework to import and write data only once.

import datetime as dt
from csv import writer, DictReader
import os

class ErrorHandler():
    def __init__(self, code:int=None, description:str=None):
        self.LogFile = './logs/errors.csv'
        self.error_entry = [code, description, self.build_timestamp()]
    
    #### Initialization Methods ###  
    def build_timestamp(self)->str:
        current_datetime = dt.datetime.now()
        return(current_datetime.strftime(" %A, %B %d - %H:%M:%S"))
    
    #### Logging Methods ####
    def write_error(self):
        if os.path.exists(self.LogFile):
            with open(self.LogFile, 'a', newline='') as write_file:
                writer_object = writer(write_file)
                writer_object.writerow(self.error_entry)
                write_file.close()
        else:
            os.mkdir('/'.join(self.LogFile.split('/')[:-1]))
            with open(self.LogFile, 'w', newline='') as write_file:
                writer_object = writer(write_file)
                writer_object.writerow(["ERROR_CODE","ERROR_MESSAGE","TIME_ERROR"])
                writer_object.writerow(self.error_entry)
                write_file.close()
            
    #### Read Methods ####
    def read_errors(self):
        error_history = []
        
        with open(self.LogFile, 'r') as read_file:
            reader_object = DictReader(read_file)
            for row in reader_object:
                error_history.append(row)
            read_file.close()
        
        print(" <><><> ERROR HSTORY <><><>") 
        for entry in error_history:            
            print(f"Error Code: {entry["ERROR_CODE"]}")
            print(f"Error Code: {entry["ERROR_MESSAGE"]}")
            print(f"Error Code: {entry["TIME_ERROR"]}")
            print("")