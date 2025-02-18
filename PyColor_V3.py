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