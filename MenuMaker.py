import datetime as dt
from os import system, name

class MenuMaker():
    def __init__(self, menu_options:dict | list, logo_file:str=None, enable_timestamp:bool=False, submenu:bool=False):
        self.menu_options = menu_options
        self.logo = (self.import_logo(logo_file), None)[(logo_file != None) and (logo_file.split('.')[-1] == 'txt')]
        self.timestamp = (self.build_timestamp(), None)[enable_timestamp]
        self.submenu = submenu
    
    #### Initialization Methods ###    
    def import_logo(self, logo_file)->str:
        with open(logo_file, "r") as file:
            logo = file.read()
            return logo

    def build_timestamp(self)->str:
        current_datetime = dt.datetime.now()
        return(current_datetime.strftime(" %A, %B %d - %H:%M:%S"))
        
    #### Menu Display Methods ###
    def clear_screen(self):
        if name == 'nt': # for windows
            return system('cls')
        elif name == 'posfix': # for mac and linux
            return system('clear')
        
    def display_logo(self):
        print(self.logo)
        
    def display_timestamp(self):
        print(self.timestamp)
        
    def display_menu_options(self):
        menu_divider = " "+"".join(["_" for _ in range(71)])+"\n"
        
        print(menu_divider)
        for option_number, option in enumerate(self.menu_options):
            print(f" [{option_number+1}] {option}")
        print(menu_divider)
        
    #### Selection Functions ####
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
    
    #### Run Function ####        
    def build_menu(self):
        self.display_menu_options()
        return self.get_menu_selection()
            
            
        
        