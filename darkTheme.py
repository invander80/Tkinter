from tkinter import *
from tkinter import ttk
from custom_btn import CustomButton

"""
Hierfür die custom_btn.py importieren
"""

class Database:
    def __init__(self):
        self.b1 = Button( text="YELL")

class MyApp(Tk):
    def __init__(self, parent=None,
                 lblbg=None,
                 fg="#c3d2ff",
                 bg="#1a1c22",
                 box="#252830",
                 flog="#272c35",
                 *args, **kwargs
                 ):
        Tk.__init__(self, parent, *args, **kwargs)                                # WINDOW OPTIONS #
        self.geometry("1300x900")                                        # window geometry, default = 1300x900
        self.minsize(500, 500)                                           # minsize of the window
        self.overrideredirect(1)                                         # removes the status bar

        self.fg = fg                                                     # INITIALIZING foreground
        self.bg = bg
        self.box = box
        self.flog = flog

        self.lblbg = lblbg

        self.da = Database()


        self.btn_style = ttk.Style()                                 # set ttk button style sheet for "THEME-BAR"
        self.btn_style.theme_use("clam")
        self.btn_style.configure("TButton",
                                 font=("Space Age", 16),
                                 background=self.flog,
                                 foreground=self.fg,
                                 borderwidth=1,
                                 bordercolor=self.box,
                                 lightcolor=self.box,
                                 darkcolor=self.box,
                                 focusthickness=2,
                                 focuscolor="none"
                                 )

        self.btn_style.map("TButton",
                           foreground=[("pressed", self.bg), ("active", self.fg)],
                           background=[("pressed", "active", self.box), ("active", self.bg)],
                           bordercolor=[("active", self.fg)],
                           borderwidth=[("active", 1)]
                           )

        self.btn_stylenavi = ttk.Style()                                 # set ttk button style sheet for "THEME-BAR"
        self.btn_stylenavi.theme_use("clam")
        self.btn_stylenavi.configure("N.TButton",
                                     font=("Space Age", 10),
                                     background=self.box,
                                     foreground=self.fg,
                                     focusthickness=2,
                                     focuscolor="none"
                                     )
        self.btn_stylenavi.map("N.TButton",
                               foreground=[("pressed", self.bg), ("active", self.fg)],
                               background=[("pressed", "active", self.box), ("active", self.bg)],
                               bordercolor=[("active", self.fg)],
                               borderwidth=[("active", 0)]
                               )

        self.border = Frame(self, bg=self.bg,                          # Border frame and background
                            highlightcolor=self.bg,
                            highlightbackground=self.bg,
                            highlightthickness=2)
        self.border.pack(expand=YES, fill=BOTH)

        self.headline = Label(self.border, bg=self.box,                 # Headline Label for App name and exit button
                              text="App Name",
                              fg=self.fg,
                              anchor=W,
                              padx=27,
                              font=("Space Age", 17)
                              )
        self.headline.pack(fill=X, ipady=2)
        self.headline.bind("<Button-1>", self.clickwin)                  # binding click on window function
        self.headline.bind("<B1-Motion>", self.dragwin)                  # binding drag win
        self.headline.bind("<Map>", lambda event: self.showwin(event))   # after minimize, reopen window
        self.headline.bind("<Double-Button-1>", self.maxwindblclick)     # double click to expand window to a fullscreen
        self.headline.bind("<ButtonRelease-1>", self.maxwinmove)         # maximize window by drag the window

        self.exit = ttk.Button(self.headline,                          # exit button
                               text="\u26CC",
                               command=self.destroy,                    # destroy window function
                               style="N.TButton"
                               )
        self.exit.pack(side="right")
        self.exit.configure(width=2)

        self.maximize = ttk.Button(self.headline,                      # maximize button
                                   text="\u2610",
                                   command=self.maxwin,                 # changes the states between zoomed and normal
                                   style="N.TButton"
                                   )
        self.maximize.pack(side="right")
        self.maximize.configure(width=2)

        self.minimize = ttk.Button(self.headline,                      # minimize button
                                   text="\u268A",
                                   command=self.minimize,               # minimize the window function
                                   style="N.TButton"
                                   )
        self.minimize.pack(side="right")
        self.minimize.configure(width=2)

        self.statusbar = Label(self.border, bg=self.flog,                # Status Bar on the bottom
                               text="StatusBar",
                               fg=self.fg,
                               anchor=W,
                               padx=20,
                               font=("Space Age", 12)
                               )
        self.statusbar.pack(side="bottom", fill=X, ipady=2)

        self.grip = Label(self.statusbar, text="\u2B78",                  # size grip in the status bar as label
                          font=("Bahnschrift", 20),
                          cursor="sizing",
                          bg=self.flog,
                          fg=self.fg)
        self.grip.place(relx=1, x=-23, y=-10)
        self.grip.bind("<B1-Motion>", self.sizegrip)

        self.navibar = Frame(self.border, bg=self.box,                   # navigation bar with function
                             highlightcolor=self.bg,
                             highlightbackground=self.bg,
                             highlightthickness=0
                             )
        self.navibar.pack(side="left", fill=Y, ipadx=40)

        self.descfrm = Frame(self.border, bg=self.box,                   # frame for description label
                             highlightcolor=self.bg,
                             highlightbackground=self.bg,
                             highlightthickness=2)
        self.descfrm.pack(fill=X)

        self.description = Label(self.descfrm, bg=self.flog,              # Description Label under the headline
                                 text="Description",
                                 fg=self.fg,
                                 anchor=W,
                                 padx=20,
                                 font=("Space Age", 10)
                                 )
        self.description.pack(fill=X, ipady=2)

        self.navibaroptions = Frame(self.border, bg=self.flog,            # navigation options bar
                                    highlightcolor=self.bg,
                                    highlightbackground=self.bg,
                                    highlightthickness=2
                                    )
        self.navibaroptions.pack(side="left", fill=Y, ipadx=0)

        self.lblbg = Label(self.border, bg=self.bg,                     # Screen Label with Unicode
                           text="\u2623",
                           fg=self.fg,
                           font=("Calibri", 300)
                           )
        self.lblbg.pack(fill=BOTH, expand=YES)

        self.navibtn = CustomButton(self.navibar,                       # "Home" custom button for the navi bar.
                                    text="\u2630".ljust(5)+" HOME",
                                    statusleft=True,
                                    fg=self.fg,
                                    height=2,
                                    command=self.navi,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    bg=self.box,
                                    anchor=W,
                                    padx=23,
                                    status=5,
                                    )
        self.navibtn.place(x=0, y=0, relwidth=1)

        self.naviopt = CustomButton(self.navibar,                       # "THEMES" custom button for the navi bar.
                                    text="\u2699".ljust(5)+"THEMES",
                                    statusleft=True,
                                    height=2,
                                    fg=self.fg,
                                    command=self.navioptions,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    anchor=W,
                                    bg=self.box,
                                    padx=19,
                                    status=5,
                                    )
        self.naviopt.place(x=0, y=46, relwidth=1)

        self.darktheme = ttk.Button(self.navibaroptions,             # "DarkTheme" custom button for the option bar.
                                    text="DarkTheme",
                                    command=self.themedark
                                    )
        self.darktheme.place(x=0, y=0, relwidth=1, height=137)

        self.brighttheme = ttk.Button(self.navibaroptions,           # "BrightTheme" custom button for the option bar.
                                      text="BrightTheme",
                                      command=self.themebright,
                                      )
        self.brighttheme.place(x=0, y=137, relwidth=1, height=137)

        self.darkbill = ttk.Button(self.navibaroptions,              # "DarkBill" custom button for the option bar.
                                   text="DarkBill",
                                   command=self.themebill
                                   )
        self.darkbill.place(x=0, y=274, relwidth=1, height=137)

        self.bla = ttk.Button(self.navibaroptions,
                              text="TEST",
                              command=self.themediff)
        self.bla.place(x=0, y=411, relwidth=1, height=137)

        self.da.b1.pack(before=self.lblbg)

        self.count = 40                                         # counting index for the navibar function. 40 is default
        self.count2 = 0                                         # counting index for the options bar. 0 is default
        self.btn_STATE = False                                  # statement for the navigation bar
        self.btn_STATE2 = False                                 # statement for the options bar.
        self.btn_MAXWIN = False                                 # statement for the maximize function (and button)
        self.dbl_CLICKED = False                                # doubleclick statement for expand the screen

        self._offsetx = 0
        self._offsety = 0

    def themedark(self):                                        # DARK THEME
        self.fg = "#c3d2ff"
        self.bg = "#1a1c22"
        self.box = "#252830"
        self.flog = "#272c35"
        self.configure(bg=self.box)
        self.btn_style.configure("TButton",
                                 font=("Space Age", 16),
                                 background=self.flog,
                                 foreground=self.fg,
                                 borderwidth=1,
                                 bordercolor=self.box,
                                 lightcolor=self.box,
                                 darkcolor=self.box,
                                 focusthickness=0,
                                 focuscolor="none"
                                 )
        self.btn_style.map("TButton",
                           foreground=[("pressed", "green"), ("active", self.fg)],
                           background=[("pressed", "active", self.box), ("active", self.bg)],
                           bordercolor=[("active", self.fg)],
                           borderwidth=[("active", 1)])
        self.btn_stylenavi = ttk.Style()                                 # set ttk button style sheet for "THEME-BAR"
        self.btn_stylenavi.theme_use("clam")
        self.btn_stylenavi.configure("N.TButton",
                                     font=("Space Age", 10),
                                     background=self.box,
                                     foreground=self.fg,
                                     focusthickness=2,
                                     focuscolor="none"
                                     )

        self.btn_stylenavi.map("N.TButton",
                               foreground=[("pressed", self.bg), ("active", self.fg)],
                               background=[("pressed", "active", self.box), ("active", self.bg)],
                               bordercolor=[("active", self.fg)],
                               borderwidth=[("active", 0)])
        self.lblbg.configure(bg=self.bg, fg=self.fg)
        self.navibaroptions.configure(bg=self.flog,
                                      highlightcolor=self.bg,
                                      highlightbackground=self.bg)
        self.description.configure(bg=self.flog, fg=self.fg)
        self.descfrm.configure(bg=self.box,
                               highlightcolor=self.bg,
                               highlightbackground=self.bg)
        self.navibar.configure(bg=self.box,
                               highlightcolor=self.bg,
                               highlightbackground=self.bg)
        self.grip.configure(bg=self.flog, fg=self.fg)
        self.statusbar.configure(bg=self.flog, fg=self.fg)
        self.border.configure(bg=self.bg,
                              highlightcolor=self.bg,
                              highlightbackground=self.bg)
        self.headline.configure(bg=self.box, fg=self.fg)
        self.navibtn.destroy()
        self.navibtn = CustomButton(self.navibar,                       # "Home" custom button for the navi bar.
                                    text="\u2630".ljust(5)+" HOME",
                                    statusleft=True,
                                    fg=self.fg,
                                    height=2,
                                    command=self.navi,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    bg=self.box,
                                    anchor=W,
                                    padx=23,
                                    status=5,
                                    )
        self.navibtn.place(x=0, y=0, relwidth=1)
        self.naviopt.destroy()
        self.naviopt = CustomButton(self.navibar,                       # "Option" custom button for the navi bar.
                                    text="\u2699".ljust(5)+"OPTIONS",
                                    statusleft=True,
                                    height=2,
                                    fg=self.fg,
                                    command=self.navioptions,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    anchor=W,
                                    bg=self.box,
                                    padx=19,
                                    status=5,
                                    )
        self.naviopt.place(x=0, y=46, relwidth=1)

    def themebright(self):
        self.fg = "#1e2027"
        self.bg = "#c4d2ff"
        self.box = "#767f9a"
        self.flog = "#9faacf"
        self.configure(bg=self.box)
        self.btn_style.configure("TButton",
                                 font=("Space Age", 16),
                                 background=self.flog,
                                 foreground=self.fg,
                                 borderwidth=1,
                                 bordercolor=self.box,
                                 lightcolor=self.box,
                                 darkcolor=self.box,
                                 focusthickness=0,
                                 focuscolor="none"
                                 )
        self.btn_style.map("TButton",
                           foreground=[("pressed", "green"), ("active", self.fg)],
                           background=[("pressed", "active", self.box), ("active", self.bg)],
                           bordercolor=[("active", self.fg)],
                           borderwidth=[("active", 1)])

        self.btn_stylenavi = ttk.Style()  # set ttk button style sheet for "THEME-BAR"
        self.btn_stylenavi.theme_use("clam")
        self.btn_stylenavi.configure("N.TButton",
                                     font=("Space Age", 10),
                                     background=self.box,
                                     foreground=self.fg,
                                     focusthickness=2,
                                     focuscolor="none"
                                     )

        self.btn_stylenavi.map("N.TButton",
                               foreground=[("pressed", self.bg), ("active", self.fg)],
                               background=[("pressed", "active", self.box), ("active", self.bg)],
                               bordercolor=[("active", self.fg)],
                               borderwidth=[("active", 0)])
        self.lblbg.configure(bg=self.bg, fg=self.fg)
        self.navibaroptions.configure(bg=self.flog,
                                      highlightcolor=self.bg,
                                      highlightbackground=self.bg)
        self.description.configure(bg=self.flog, fg=self.fg)
        self.descfrm.configure(bg=self.box,
                               highlightcolor=self.bg,
                               highlightbackground=self.bg)
        self.navibar.configure(bg=self.box,
                               highlightcolor=self.bg,
                               highlightbackground=self.bg)
        self.grip.configure(bg=self.flog, fg=self.fg)
        self.statusbar.configure(bg=self.flog, fg=self.fg)
        self.border.configure(bg=self.bg,
                              highlightcolor=self.bg,
                              highlightbackground=self.bg)
        self.headline.configure(bg=self.box, fg=self.fg)
        self.navibtn.destroy()
        self.navibtn = CustomButton(self.navibar,                       # "Home" custom button for the navi bar.
                                    text="\u2630".ljust(5)+" HOME",
                                    statusleft=True,
                                    fg=self.fg,
                                    height=2,
                                    command=self.navi,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    bg=self.box,
                                    anchor=W,
                                    padx=23,
                                    status=5,
                                    )
        self.navibtn.place(x=0, y=0, relwidth=1)
        self.naviopt.destroy()
        self.naviopt = CustomButton(self.navibar,                       # "Option" custom button for the navi bar.
                                    text="\u2699".ljust(5)+"OPTIONS",
                                    statusleft=True,
                                    height=2,
                                    fg=self.fg,
                                    command=self.navioptions,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    anchor=W,
                                    bg=self.box,
                                    padx=19,
                                    status=5,
                                    )
        self.naviopt.place(x=0, y=46, relwidth=1)

    def themebill(self):
        self.fg = "yellow"
        self.bg = "#131519"
        self.box = "#131519"
        self.flog = "#1c1e24"
        self.configure(bg=self.box)
        self.btn_style.configure("TButton",
                                 font=("Space Age", 16),
                                 background=self.flog,
                                 foreground=self.fg,
                                 borderwidth=1,
                                 bordercolor=self.box,
                                 lightcolor=self.box,
                                 darkcolor=self.box,
                                 focusthickness=0,
                                 focuscolor="none"
                                 )
        self.btn_style.map("TButton",
                           foreground=[("pressed", "green"), ("active", self.fg)],
                           background=[("pressed", "active", self.box), ("active", self.bg)],
                           bordercolor=[("active", self.fg)],
                           borderwidth=[("active", 1)])

        self.btn_stylenavi = ttk.Style()  # set ttk button style sheet for "THEME-BAR"
        self.btn_stylenavi.theme_use("clam")
        self.btn_stylenavi.configure("N.TButton",
                                     font=("Space Age", 10),
                                     background=self.box,
                                     foreground=self.fg,
                                     focusthickness=2,
                                     focuscolor="none"
                                     )

        self.btn_stylenavi.map("N.TButton",
                               foreground=[("pressed", self.bg), ("active", self.fg)],
                               background=[("pressed", "active", self.box), ("active", self.bg)],
                               bordercolor=[("active", self.fg)],
                               borderwidth=[("active", 0)])
        self.lblbg.configure(bg=self.bg, fg=self.fg)
        self.navibaroptions.configure(bg=self.flog,
                                      highlightcolor=self.bg,
                                      highlightbackground=self.bg)
        self.description.configure(bg=self.flog, fg=self.fg)
        self.descfrm.configure(bg=self.box,
                               highlightcolor=self.bg,
                               highlightbackground=self.bg)
        self.navibar.configure(bg=self.box,
                               highlightcolor=self.bg,
                               highlightbackground=self.bg)
        self.grip.configure(bg=self.flog, fg=self.fg)
        self.statusbar.configure(bg=self.flog, fg=self.fg)
        self.border.configure(bg=self.bg,
                              highlightcolor=self.bg,
                              highlightbackground=self.bg)
        self.headline.configure(bg=self.box, fg=self.fg)
        self.navibtn.destroy()
        self.navibtn = CustomButton(self.navibar,  # "Home" custom button for the navi bar.
                                    text="\u2630".ljust(5) + " HOME",
                                    statusleft=True,
                                    fg=self.fg,
                                    height=2,
                                    command=self.navi,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    bg=self.box,
                                    anchor=W,
                                    padx=23,
                                    status=5,
                                    )
        self.navibtn.place(x=0, y=0, relwidth=1)
        self.naviopt.destroy()
        self.naviopt = CustomButton(self.navibar,  # "Option" custom button for the navi bar.
                                    text="\u2699".ljust(5) + "OPTIONS",
                                    statusleft=True,
                                    height=2,
                                    fg=self.fg,
                                    command=self.navioptions,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    anchor=W,
                                    bg=self.box,
                                    padx=19,
                                    status=5,
                                    )
        self.naviopt.place(x=0, y=46, relwidth=1)

    def themediff(self):
        self.fg = "red"
        self.bg = "#1a1c22"
        self.box = "#252830"
        self.flog = "#272c35"
        self.configure(bg=self.box)
        self.btn_style.configure("TButton",
                                 font=("Space Age", 16),
                                 background=self.flog,
                                 foreground=self.fg,
                                 borderwidth=1,
                                 bordercolor=self.box,
                                 lightcolor=self.box,
                                 darkcolor=self.box,
                                 focusthickness=0,
                                 focuscolor="none"
                                 )
        self.btn_style.map("TButton",
                           foreground=[("pressed", "green"), ("active", self.fg)],
                           background=[("pressed", "active", self.box), ("active", self.bg)],
                           bordercolor=[("active", self.fg)],
                           borderwidth=[("active", 1)])

        self.btn_stylenavi = ttk.Style()  # set ttk button style sheet for "THEME-BAR"
        self.btn_stylenavi.theme_use("clam")
        self.btn_stylenavi.configure("N.TButton",
                                     font=("Space Age", 10),
                                     background=self.box,
                                     foreground=self.fg,
                                     focusthickness=2,
                                     focuscolor="none"
                                     )

        self.btn_stylenavi.map("N.TButton",
                               foreground=[("pressed", self.bg), ("active", self.fg)],
                               background=[("pressed", "active", self.box), ("active", self.bg)],
                               bordercolor=[("active", self.fg)],
                               borderwidth=[("active", 0)])
        self.lblbg.configure(bg=self.bg, fg=self.fg)
        self.navibaroptions.configure(bg=self.flog,
                                      highlightcolor=self.bg,
                                      highlightbackground=self.bg)
        self.description.configure(bg=self.flog, fg=self.fg)
        self.descfrm.configure(bg=self.box,
                               highlightcolor=self.bg,
                               highlightbackground=self.bg)
        self.navibar.configure(bg=self.box,
                               highlightcolor=self.bg,
                               highlightbackground=self.bg)
        self.grip.configure(bg=self.flog, fg=self.fg)
        self.statusbar.configure(bg=self.flog, fg=self.fg)
        self.border.configure(bg=self.bg,
                              highlightcolor=self.bg,
                              highlightbackground=self.bg)
        self.headline.configure(bg=self.box, fg=self.fg)
        self.navibtn.destroy()
        self.navibtn = CustomButton(self.navibar,  # "Home" custom button for the navi bar.
                                    text="\u2630".ljust(5) + " HOME",
                                    statusleft=True,
                                    fg=self.fg,
                                    height=2,
                                    command=self.navi,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    bg=self.box,
                                    anchor=W,
                                    padx=23,
                                    status=5,
                                    )
        self.navibtn.place(x=0, y=0, relwidth=1)
        self.naviopt.destroy()
        self.naviopt = CustomButton(self.navibar,  # "Option" custom button for the navi bar.
                                    text="\u2699".ljust(5) + "OPTIONS",
                                    statusleft=True,
                                    height=2,
                                    fg=self.fg,
                                    command=self.navioptions,
                                    hoverfg=self.fg,
                                    hover=self.bg,
                                    statushover=self.fg,
                                    statuscolor=self.box,
                                    anchor=W,
                                    bg=self.box,
                                    padx=19,
                                    status=5,
                                    )
        self.naviopt.place(x=0, y=46, relwidth=1)

    def sizegrip(self, event):                                  # SIZEGRIP FUNCTION TO SET RANDOM SCREENSIZE
        try:                                                    # EVENT BINDING IN self.grip
            x1 = self.winfo_pointerx() - self.winfo_rootx()
            y2 = self.winfo_pointery() - self.winfo_rooty()
            self.geometry("%dx%d" % (x1, y2))
            self.state("normal")
            print(x1)
            if x1 < 900:
                self.navibar.pack_configure(ipadx=40)
                self.btn_STATE = False
                self.count = 40
            if x1 < 700:
                self.navibaroptions.pack_configure(ipadx=0)
                self.btn_STATE2 = False
                self.count2 = 0
        except TclError:
            print()

    def maxwin(self):                                           # MAXIMIZE WINDOW FUNCTION FOR MAXIMIZE BUTTON
        if self.btn_MAXWIN is False:                            # FUNCTION IN self.maximize
            self.state('zoomed')
            self.btn_MAXWIN = True
            self.dbl_CLICKED = True
        else:
            self.state('normal')
            self.btn_MAXWIN = False
            self.dbl_CLICKED = False

    def maxwindblclick(self, event):                            # DOUBLE CLICK EVENT TO SET WINDOW IN 'zoomed' AND
        if self.dbl_CLICKED is False:                           # 'normal' STATE
            self.state('zoomed')                                # BIND IN self.headline
            self.dbl_CLICKED = True
            self.btn_MAXWIN = True
        else:
            self.state('normal')
            self.dbl_CLICKED = False
            self.btn_MAXWIN = False

    def minimize(self):                                         # FUNCTION IN self.minimize TO MINIMIZE THE WINDOW
        self.overrideredirect(0)
        self.iconify()

    def showwin(self, event):
        self.overrideredirect(1)

    def maxwinmove(self, event):                                # MAXIMIZE THE WINDOW IF THE POSITION IS <2
        y = self.winfo_pointery() - self._offsety               # EVENT BINDING IN self.headline
        if y < -2:
            self.state('zoomed')
            self.dbl_CLICKED = True
            self.btn_MAXWIN = True

    def dragwin(self, event):                                   # EVENT TO MOVE THE OVERRIDEREDIRECT WINDOW
        x = self.winfo_pointerx() - self._offsetx               # IN self.headlines
        y = self.winfo_pointery() - self._offsety
        self.geometry("+%d+%d" % (x, y))

    def clickwin(self, event):                                  # POSITION FOR THE MOUSE AFTER CLICK ON HEADLINE
        self._offsetx = event.widget.winfo_rootx() - self.winfo_rootx() + event.x
        self._offsety = event.widget.winfo_rooty() - self.winfo_rooty() + event.y
        print(self._offsety)

    def navi(self):                                             # NAVIBAR FUNCTION WITH LOOPING TO CHANGE THE WIDTH
        if self.btn_STATE is False:
            if self.count < 150:
                self.navibar.pack_configure(ipadx=self.count)
                self.navibar.after(15, lambda:self.navi())
                self.count += 10
            else:
                self.btn_STATE = True
            print(self.btn_STATE)
            print(self.count)
        else:
            self.navibar.pack_configure(ipadx=40)
            self.btn_STATE = False
            self.count = 40
            print(self.btn_STATE)
            print(self.count)

    def navioptions(self):
        if self.btn_STATE2 is False:
            if self.count2 < 150:
                self.navibaroptions.pack_configure(ipadx=self.count2)
                self.navibaroptions.after(15, lambda:self.navioptions())
                self.count2 += 10
            else:
                self.btn_STATE2 = True
        else:
            self.navibaroptions.pack_configure(ipadx=0)
            self.btn_STATE2 = False
            self.count2 = 0



def db():
    Database()


if __name__ == "__main__":
    #Database()
    MyApp()
    mainloop()
