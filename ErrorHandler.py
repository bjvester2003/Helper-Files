import datetime as dt
from csv import writer, reader
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
            with open(self.LogFile, 'w', newline='') as write_file:
                writer_object = writer(write_file)
                writer_object.writerow(["ERROR_CODE","ERROR_MESSAGE","TIME_ERROR"])
                writer_object.writerow(self.error_entry)
                write_file.close()
            
    #### Read Methods ####
    def read_errors(self):
        error_history = []
        
        with open(self.LogFile, 'r') as read_file:
            reader_object = reader(read_file)
            for row in reader_object:
                error_history.append(row)
            read_file.close()