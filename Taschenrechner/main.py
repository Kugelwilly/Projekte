### Imports ###

import customtkinter as ctk

editedText = ''
calculation = ''
modeState = False

class App(ctk.CTk):
### App design ###
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("Taschenrechner") 
        self.setWindow(330,425)
        self.resizable(False, False)
        self._set_appearance_mode("system")

### Background ###
        self.background = ctk.CTkFrame(self, width=330, height=425, fg_color="#0F0F0F")
        self.background.place(anchor="center", relx= 0.5, rely= 0.5)

### Frame ###
        self.frame = ctk.CTkFrame(self.background, width=305, height=55, fg_color="#1B1B1A", border_width=1, border_color="#000000")
        self.frame.place(anchor="center",relx=0.5, rely=0.1)

        self.label = ctk.CTkLabel(self.frame, text="0", fg_color="transparent", font=("Roboto", 35))
        self.label.place(anchor = "center", relx=0.5, rely=0.5)

### Buttons ###
    ## Arithmetic methods ##
        self.plusButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#EEEEED", text_color="#010100", hover_color="#33332C", border_width=1, border_color="#050505", text="+", font=("Roboto", 50), command=lambda:self.calculator("+"))
        self.plusButton.place(anchor="center", relx=0.86, rely=0.74)

        self.minusButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#EEEEED", text_color="#010100", hover_color="#33332C", border_width=1, border_color="#050505", text="-", font=("Roboto", 50), command=lambda:self.calculator("-"))
        self.minusButton.place(anchor="center", relx=0.86, rely=0.58)

        self.multiplicationButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#EEEEED", text_color="#010100", hover_color="#33332C", border_width=1, border_color="#050505", text="×", font=("Roboto", 50), command=lambda:self.calculator("*"))
        self.multiplicationButton.place(anchor="center", relx=0.86, rely=0.42)

        self.divisonButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#EEEEED", text_color="#010100", hover_color="#33332C", border_width=1, border_color="#050505", text="÷", font=("Roboto", 50), command=lambda:self.calculator("/"))
        self.divisonButton.place(anchor="center", relx=0.86, rely=0.26)

    ## Digits ##
        self.oneButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="1", font=("Roboto", 50), command=lambda:self.calculator("1"))
        self.oneButton.place(anchor="center", relx=0.155, rely=0.74)

        self.twoButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="2", font=("Roboto", 50), command=lambda:self.calculator("2"))
        self.twoButton.place(anchor="center", relx=0.39, rely=0.74)

        self.threeButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="3", font=("Roboto", 50), command=lambda:self.calculator("3"))
        self.threeButton.place(anchor="center", relx=0.625, rely=0.74)

        self.fourButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="4", font=("Roboto", 50), command=lambda:self.calculator("4"))
        self.fourButton.place(anchor="center", relx=0.155, rely=0.58)

        self.fiveButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="5", font=("Roboto", 50), command=lambda:self.calculator("5"))
        self.fiveButton.place(anchor="center", relx=0.39, rely=0.58)

        self.sixButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="6", font=("Roboto", 50), command=lambda:self.calculator("6"))
        self.sixButton.place(anchor="center", relx=0.625, rely=0.58)

        self.sevenButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="7", font=("Roboto", 50), command=lambda:self.calculator("7"))
        self.sevenButton.place(anchor="center", relx=0.155, rely=0.42)

        self.eightButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="8", font=("Roboto", 50), command=lambda:self.calculator("8"))
        self.eightButton.place(anchor="center", relx=0.39, rely=0.42)

        self.nineButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="9", font=("Roboto", 50), command=lambda:self.calculator("9"))
        self.nineButton.place(anchor="center", relx=0.625, rely=0.42)

        self.zeroButton = ctk.CTkButton(self.background, width=150, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text="0", font=("Roboto", 50), command=lambda:self.calculator("0"))
        self.zeroButton.place(anchor="center", relx=0.272, rely=0.9)

    ## Other ##
        self.equalButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#EEEEED", text_color="#010100", hover_color="#33332C", border_width=1, border_color="#050505", text="=", font=("Roboto", 50), command=lambda:self.calculator("="))
        self.equalButton.place(anchor="center", relx=0.86, rely=0.9)
    
        self.commaButton = ctk.CTkButton(self.background, width=75, height=40, fg_color="#201F1F", text_color="#EEEEED", hover_color="#414244", border_width=1, border_color="#050505", text=".", font=("Roboto", 50), command=lambda:self.calculator("."))
        self.commaButton.place(anchor="center", relx=0.625, rely=0.9)

        self.clearButton = ctk.CTkButton(self.background, width=115, height=40, fg_color="#EEEEED", text_color="#010100", hover_color="#33332C", border_width=1, border_color="#050505", text="C", font=("Roboto", 50), command=lambda:self.calculator("C"))
        self.clearButton.place(anchor="center", relx=0.57, rely=0.26)

        self.removeButton = ctk.CTkButton(self.background, width=115, height=40, fg_color="#EEEEED", text_color="#010100", hover_color="#33332C", border_width=1, border_color="#050505", text="⌫", font=("Roboto", 50), command=lambda:self.calculator("remove"))
        self.removeButton.place(anchor="center", relx=0.215, rely=0.26)

### Sets the Window in the center ###
    def setWindow(self, width: int, height: int):
        x = int((self.winfo_screenwidth() / 2) - (width / 2))
        y = int((self.winfo_screenheight() / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")

### Commands ###
    def configureButtons(self, mode):
        # numbers
        self.zeroButton.configure(state=mode)
        self.oneButton.configure(state=mode)
        self.twoButton.configure(state=mode)
        self.threeButton.configure(state=mode)
        self.fourButton.configure(state=mode)
        self.fiveButton.configure(state=mode)
        self.sixButton.configure(state=mode)
        self.sevenButton.configure(state=mode)
        self.eightButton.configure(state=mode)
        self.nineButton.configure(state=mode)
        # operators
        self.plusButton.configure(state=mode)
        self.minusButton.configure(state=mode)
        self.multiplicationButton.configure(state=mode)
        self.divisonButton.configure(state=mode)
        self.commaButton.configure(state=mode)
    
    def checkLenText(self):
        global modeState
        if len(editedText) < 5:
            self.label.configure(font=("Roboto", 35))
        
        elif len(editedText) < 10:
            self.label.configure(font=("Roboto", 25))

        elif len(editedText) < 20:
            self.label.configure(font=("Roboto", 18))

        elif len(editedText) == 25:
            modeState = True
            self.configureButtons("disabled")

    def calculator(self, option):
        global editedText, calculation
        if option == 'remove':
            editedText = editedText[:-1]
            calculation = calculation[:-1]
            if len(editedText) == 0:
                self.label.configure(text=0)
            else:
                self.label.configure(text=editedText)
            return

        if option == 'C':
            calculation = ''
            editedText = ''
            self.label.configure(text=0)
            self.label.configure(font=("Roboto", 35))
            if modeState:
                self.configureButtons("normal")
            return

        self.checkLenText()
        
        if option == '0':
            calculation += '0'
        if option == '1':
            calculation += '1'
        if option == '2':
            calculation += '2'
        if option == '3':
            calculation += '3'
        if option == '4':
            calculation += '4'
        if option == '5':
            calculation += '5'
        if option == '6':
            calculation += '6'
        if option == '7':
            calculation += '7'
        if option == '8':
            calculation += '8'
        if option == '9':
            calculation += '9'

        try:
            operator = ['+', '-', '/', '*']

            if option == '+':
                if editedText[-1] in operator:
                    return
                calculation += '+'

            if option == '-':
                if editedText[-1] in operator:
                    return
                calculation += '-'

            if option == '*':
                if editedText[-1] in operator:
                    return
                calculation += '*'

            if option == '/':
                if editedText[-1] in operator:
                    return
                calculation += '/'

            if option == '.':
                if editedText[-1] == '.':
                    return
                calculation += '.'

        except IndexError:
            self.label.configure(text="Du musst zuerst eine Zahl eingeben", font=("Roboto", 18))
            return
        
        try:
            if option== '=':
                result = eval(calculation)
                editedText = str(result)
                calculation = str(result)
                self.label.configure(text=str(result))
                self.checkLenText()
                return
            
        except ZeroDivisionError:
            self.label.configure(text="Du kannst nicht durch 0 dividieren", font=("Roboto", 18))
            return
        except SyntaxError:
            self.label.configure(text="0")
            return
        except Exception as e:
            self.label.configure(text=f"Technischer Fehler: {e}", font=("Roboto", 15))
            return
        
        editedText += option
        self.label.configure(text=editedText)

### Starting App ###
if __name__ == "__main__":
    app = App()
    app.mainloop()