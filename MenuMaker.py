import datetime as dt
from os import system, name

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
            
            
        
        