from tkinter import Tk, Button


class MainWindow(Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # ------------------------ Buttons erstellen ----------------------------- #
        # Liste:
        self.btns = [Button(self, text=f"Btn{x+1}") for x in range(15)]      
        
        # Position & Bind Methode (Button-1 #> LinksKlick):
        for x in range(len(self.btns)):
            self.btns[x].pack(fill="x")
            self.btns[x].bind("<Button-1>", self.flagBtn)
    
    # ------------------------ Flag Funktion ----------------------------- #
    def flagBtn(self, event):
        #=> Vergleich: Button Liste == Event Widgets; Background setzen <=#
        if any(self.btns[x].config(bg="blue") if self.btns[x] == event.widget
               else self.btns[x].config(bg="white") for x in range(len(self.btns))):
            return


if __name__ == '__main__':
    mw = MainWindow()
    mw.mainloop()
