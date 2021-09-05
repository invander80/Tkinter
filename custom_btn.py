from tkinter import *

'''
    master ; 
    bg ;            set the background for the button
    fg ;            foreground for the button
    font ;          font is Space Age (downloaded), size 16
    text ;          CustomButton as default
    border ;        border width is set 0
    bordercolor ;   border color
    hover ;         hover color to change the background when hovering
    hoverfg ;       hover foreground changes the foreground when hovering
    status ;        set width and height for status bar
    statusleft ;    status bar on the left side, False is default
    statusright ;   status bar on the right side, False is default
    statustop ;     status bar on top, False is default
    statusbottom ;  status bar on the bottom, False is default
    statuscolor ;   changes the status bar color of the button
    statushover ;   changes the status bar color when hovering
    height ;        changes the button size and status bar
    width ;         changes the button size and status bar
    
    ***status bar stands for the frames inside the button***
'''


class CustomButton(Frame):
    def __init__(self,
                 master=None,
                 bg="#252830",
                 fg="#c2d4ff",
                 font=("Space Age", 16),
                 text="CustomButton",
                 border=0,
                 bordercolor="#252830",
                 hover="#353944",
                 hoverfg="#c2d4ff",
                 status=2,
                 statusleft=False,
                 statusright=False,
                 statustop=False,
                 statusbottom=False,
                 statuscolor="#252830",
                 statushover="#c2d4ff",
                 height=4,
                 width=20,
                 command=None,
                 anchor=None,
                 padx=None,
                 *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.bg = bg
        self.fg = fg
        self.font = font
        self.text = text
        self.border = border
        self.bordercolor = bordercolor
        self.hover = hover
        self.hoverfg = hoverfg
        self.status = status
        self.height = height
        self.width = width
        self.statusleft = statusleft
        self.statusright = statusright
        self.statustop = statustop
        self.statusbottom = statusbottom
        self.statuscolor = statuscolor
        self.statushover = statushover
        self.func = command
        self.anchor = anchor
        self.padx = padx

# create a frame for the background
        self.frame = Frame(self, bg=self.bg, highlightthickness=self.border, highlightbackground=self.bordercolor,
                              highlightcolor=self.bordercolor)
        self.frame.pack(expand=YES, fill=BOTH)
        self.frame.bind("<Enter>", self.enter)
        self.frame.bind("<Leave>", self.leave)
        self.frame.bind("<Button-1>", self.function)
        self.frame.bind("<ButtonRelease-1>", self.clicked)

# all status bars, left, right, bottom, top
    # top status bar
        if self.statustop is True:
            self.lbltop = Frame(self.frame, bg=self.statuscolor, height=self.status)
            self.lbltop.pack(side=TOP, fill=X)
            self.lbltop.bind("<Enter>", self.enter)
            self.lbltop.bind("<Leave>", self.leave)
            self.lbltop.bind("<Button-1>", self.function)
            self.lbltop.bind("<ButtonRelease-1>", self.clicked)

    # bottom status bar
        if self.statusbottom is True:
            self.lblbottom = Frame(self.frame, bg=self.statuscolor, height=self.status)
            self.lblbottom.pack(side=BOTTOM, fill=X)
            self.lblbottom.bind("<Enter>", self.enter)
            self.lblbottom.bind("<Leave>", self.leave)
            self.lblbottom.bind("<Button-1>", self.function)
            self.lblbottom.bind("<ButtonRelease-1>", self.clicked)

    # status bar for the left side in the button
        if self.statusleft is True:
            self.lblleft = Frame(self.frame, bg=self.statuscolor, width=self.status)
            self.lblleft.pack(side=LEFT, fill=Y)
            self.lblleft.bind("<Enter>", self.enter)
            self.lblleft.bind("<Leave>", self.leave)
            self.lblleft.bind("<Button-1>", self.function)
            self.lblleft.bind("<ButtonRelease-1>", self.clicked)

    # status bar for the right side in the button
        if self.statusright is True:
            self.lblright = Frame(self.frame, bg=self.statuscolor, width=self.status)
            self.lblright.pack(side=RIGHT, fill=Y)
            self.lblright.bind("<Enter>", self.enter)
            self.lblright.bind("<Leave>", self.leave)
            self.lblright.bind("<Button-1>", self.function)
            self.lblright.bind("<ButtonRelease-1>", self.clicked)

# Label with text, to add the text to the button
        self.label = Label(self.frame, bg=self.bg, text=self.text, font=self.font, fg=self.fg, height=self.height,
                              width=self.width, anchor=self.anchor, padx=self.padx)
        self.label.pack(expand=YES, fill=BOTH)
        self.label.bind("<Enter>", self.enter)
        self.label.bind("<Leave>", self.leave)
        self.label.bind("<Button-1>", self.function)
        self.label.bind("<ButtonRelease-1>", self.clicked)

# hovering effects
    # enter all
    def enter(self, event):
        self.frame.configure(highlightbackground=self.fg, highlightcolor=self.fg)
        self.label.configure(bg=self.hover, fg=self.hoverfg)
        if self.statustop is True:
            self.lbltop.configure(bg=self.statushover)
        if self.statusbottom is True:
            self.lblbottom.configure(bg=self.statushover)
        if self.statusleft is True:
            self.lblleft.configure(bg=self.statushover)
        if self.statusright is True:
            self.lblright.configure(bg=self.statushover)

    # leave all
    def leave(self, event):
        self.frame.configure(highlightbackground=self.bordercolor, highlightcolor=self.bordercolor)
        self.label.configure(bg=self.bg, fg=self.fg)
        if self.statustop is True:
            self.lbltop.configure(bg=self.statuscolor)
        if self.statusbottom is True:
            self.lblbottom.configure(bg=self.statuscolor)
        if self.statusleft is True:
            self.lblleft.configure(bg=self.statuscolor)
        if self.statusright is True:
            self.lblright.configure(bg=self.statuscolor)

    # clicked means, when the button will be released
    def clicked(self, event):
        self.label.configure(bg=self.hover, fg=self.fg)

    # command add when it isn't None.
    # when clicked changes the foreground
    def function(self, event):
        self.label.configure(fg=self.bg)
        if self.func is not None:
            self.func()
