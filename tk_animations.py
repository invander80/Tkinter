from tkinter import *
import random
import time

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(1)

        self.animate = TPropertyAnimation(self)
        self.tk_function = TkFunctions(self)

        self.titleBar = Frame(self, bg="red")
        self.titleBar.pack(fill="x", ipady= 20)
        self.titleBar.bind("<B1-Motion>",  self.tk_function.dragWindow)
        self.titleBar.bind("<Button-1>", self.tk_function.clickWindow)

        self.lbl = Label(self, bg="#1a2021",  text="Moin", font=("Unispace", 40))
        self.lbl.pack()
        self.btn = Button(self, text="move me")
        self.btn.pack()
        self.btn.bind("<B1-Motion>", self.tk_function.clickWidget)
        self.btn.bind("<Button-1>", self.tk_function.dragWidget)
        self.btn.bind("<Enter>", lambda event: event.widget.config(bg="blue"))

        self.animate.fgColorAnimation(self.lbl, [255, 77, 97], [5, 2, 255], 5)


class TPropertyAnimation(Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def rgbColor(self, rgb):
        return "#{0:02x}{1:02x}{2:02x}".format(*rgb)

    def simileTwoLists(self, start:list, end:list):
        """Vergleicht zwei Listen und bringt die 'start'- Liste auf den Wert der 'end'- Liste"""
        if start != end:
            for i in range(len(end)):
                for r in range(start[i]-end[i]):
                    start[i] -= 1
                    return start
                if start <= end:
                    for i in range(len(end)):
                        for r in range(end[i] - start[i]):
                            start[i] += 1
                            return start

    def fgColorAnimate(self, widget, rgb: list, end=255):
        """TPropertyAnimation: fgColorAnimate animiert den Text von dunkel bis hell."""
        if any(x >= end for x in rgb):
            return
        rgb = [x+1 for x in rgb]
        widget.config(fg="#{0:02x}{1:02x}{2:02x}".format(*rgb))
        widget.after(10, self.fgColorAnimate, widget, rgb)

    def fgColorAnimation(self, widget, start: list, end: list, speed: int):
        """TPropertyAnimation: fgColorAnimate animiert den Text von dunkel bis hell."""
        if all(start[x] == end[x] for x in range(0, len(start))):
            return
        self.simileTwoLists(start, end)
        widget.config(fg="#{0:02x}{1:02x}{2:02x}".format(*start))
        widget.after(speed, self.fgColorAnimation, widget, start, end, speed)
        print(start)

    def typeWriter(self, widget, txt: str, speed: int, counter=1):
        """TPropertyAnimation: typeWriter gibt den Text in einzelnden Buchstaben aus."""
        widget.config(text=txt[:counter])
        if counter < len(txt):
            widget.after(speed, lambda: self.typeWriter(widget, txt, speed, counter+1))

    def bgChanger(self, widget, colors: list, speed: int, counter=-1):
        """TPropertyAnimation: bgChanger ändert die Hintergrundfarben mit einem Zeitintervall."""
        if counter < len(colors):
            widget.config(bg=colors[counter])
            widget.after(speed, lambda: self.bgChanger(widget, colors, speed, counter+1))

### SPEZIELLE FRAME ANIMATIONEN ////////////////////////////////////////////////////////////////////////////////////////
    def padOut(self, widget, start: int, end: int):
        """TPropertyAnimation: padOut expandiert das Widget auf eine bestimmte Größe"""
        if start < end:
            widget.pack_configure(ipadx=start, ipady=start)
            widget.after(15, lambda: self.padOut(widget, start + 10, end))

    def padIn(self, widget, end: int, start: int):
        """TPropertyAnimation: padIn minimiert das Widget auf eine bestimmte Größe"""
        if start < end:
            widget.pack_configure(ipadx=end, ipady=end)
            widget.after(15, lambda: self.padIn(widget, end - 10, start))


class TkFunctions:
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.offSetX = 0
        self.offSetY = 0

    def dragWindow(self, event):
        x = self.parent.winfo_pointerx() - self.offSetX
        y = self.parent.winfo_pointery() - self.offSetY
        self.parent.geometry("+%d+%d" % (x,y))

    def clickWindow(self, event):
        self.offSetX = event.widget.winfo_rootx() - event.widget.winfo_rootx() + event.x
        self.offSetY = event.widget.winfo_rooty() - event.widget.winfo_rooty() + event.y

    def dragWidget(self, event):
        self.widget = event.widget
        self.widget.startX = event.x
        self.widget.startY = event.y

    def clickWidget(self, event):
        self.widget = event.widget
        x = self.widget.winfo_x() - self.widget.startX + event.x
        y = self.widget.winfo_y() - self.widget.startY + event.y
        self.widget.place(x=x, y=y)


if __name__ == '__main__':
    mw = MainWindow()
    mw.geometry("1000x750")
    mw.configure(bg="#1a2021", highlightthickness=2,
                 highlightbackground="#29e0ff",
                 highlightcolor="#29e0ff")
    mw.mainloop()
