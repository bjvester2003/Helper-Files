import datetime as dt # EH, MM
from csv import writer, reader # EH
from os import system, name # MM
import os # EH

# <><><> ERROR HANDLER <><><> #
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
            
# <><><> MENU MAKER  <><><> #
class MenuMaker():
    def __init__(self, menu_options, logo_file=None, enable_timestamp=False):
        self.menu_options = menu_options
        self.logo = self.import_logo(logo_file)
        self.timestamp = self.build_timestamp(enable_timestamp)
    
    #### Initialization Methods ###    
    def import_logo(self, logo_file)->str:
        """If file ends in .txt, imports the logo."""
        if (logo_file != None) and (logo_file.split('.')[-1] == 'txt'):
            with open(logo_file, "r") as file:
                logo = file.read()
                return logo
        else:
            return None

    def build_timestamp(self, enable_timestamp:bool)->str:
        if enable_timestamp:
            current_datetime = dt.datetime.now()
            return(current_datetime.strftime(" %A, %B %d - %H:%M:%S"))
        else:
            return None 
        
    #### Menu Display Methods ###
    def clear_screen(self):
         # for windows
        if name == 'nt':
            return system('cls')
            
        # for mac and linux(here, os.name is 'posix')
        else:
            return system('clear')
        
    def display_menu_options(self):
        menu_divider = " "+"".join(["_" for _ in range(71)])+"\n"
        
        # Add Extra Information # 
        if self.logo != None:
            print(self.logo)
        if self.timestamp != None:
            print(self.timestamp)    
        
        print(menu_divider)
        for num, op in enumerate(self.menu_options):
            print(f" [{num+1}] {op}")
        print(menu_divider)
        
    def get_menu_selection(self):
        valid_selections = [str(num+1) for num in range(0, len(self.menu_options))]
        menu_selection = input(" Menu Selection : ")
        
        if menu_selection not in valid_selections:
            print(f"This selection, '{menu_selection}', is invalid. Please enter a valid selection.")
            input()
            self.clear_screen()
            self.build_menu()
        else:
            return self.menu_options[int(menu_selection)-1]
            
    def build_menu(self):
        self.display_menu_options()
        return self.get_menu_selection()
    
# <><><> PyColor_V3 <><><> #
class PyColor():
    def __init__(self, fgc:str="default", bgc:str="default", underline:bool=False, msg:str="default"):
        self.fgc_code = self.set_foreground_color_code(fgc)
        self.bgc_code = self.set_background_color_code(bgc)
        self.underline_val = underline
        self.message = msg
        
        self.colored_text = self.color_text()
        
    def set_foreground_color_code(fgc):
        foreground_color_codes = {
            "black"	         :30,
            "red"	         :31,
            "green"	         :32,
            "yellow"	     :33,
            "blue"	         :34,
            "magenta"	     :35,
            "cyan"	         :36,
            "white"	         :37,
            "default"	     :39,
            "bright_black"	 :90,
            "bright_red"	 :91,
            "bright_green"	 :92,
            "bright_yellow"	 :93,
            "bright_blue"	 :94,
            "bright_magenta" :95,
            "bright_cyan"	 :96,
            "bright_white"	 :97,
        }
    
        if fgc in foreground_color_codes:
            return foreground_color_codes[fgc]
        else:
            return foreground_color_codes["default"]
        
    def set_background_color_code(bgc):
        background_color_codes = {
            "black"	         :40,
            "red"	         :41,
            "green"	         :42,
            "yellow"	     :43,
            "blue"	         :44,
            "magenta"	     :45,
            "cyan"	         :46,
            "white"	         :47,
            "default"	     :49,
            "bright_black"	 :100,
            "bright_red"	 :101,
            "bright_green"	 :102,
            "bright_yellow"	 :103,
            "bright_blue"	 :104,
            "bright_magenta" :105,
            "bright_cyan"	 :106,
            "bright_white"	 :107,
        }

        if bgc in background_color_codes:
            return background_color_codes[bgc]
        else:
            return background_color_codes["default"]
        
    def color_text(self):
        reset_code = f"\033[0m"
        
        if self.underline_val == True:
            color_code = f"\033[4;{self.fgc_code};{self.bgc_code}m"
        elif self.underline_val == False:
            color_code = f"\033[{self.fgc_code};{self.bgc_code}m"
            
        modified_message = f"{color_code}{self.message}{reset_code}"
        
        return modified_message