from tkinter import *                                                                       # IMPORTS //////////////////
import random

root = Tk()                                                                                 # WINDOW ATTRIBUTES ////////
width = root.winfo_screenwidth() / 2.5
height = root.winfo_screenheight() / 3.5
root.geometry("400x400+%d+%d" % (width, height))
root.attributes("-transparent", "red")
root.overrideredirect(1)


def circular():                                                                             # LABEL // CANVAS OUTSIDE //
    global GLOBAL_STATE, EXTENT                                                             # FUNC()
    if GLOBAL_STATE == 0:
        main_canvas.itemconfig(outer_arc, extent=EXTENT, start=EXTENT,
                               fill="#"+("%06x"%random.randint(0,16777215)))
        main_label.configure(text="CPU-HEAT\n"+("%d"%random.randint(0,9999999)+"°C"),
                             fg="#"+("%06x"%random.randint(0,16777215)))
        exit_button.configure(fg="#"+("%06x"%random.randint(0,16777215)),
                              activeforeground="#"+("%06x"%random.randint(0,16777215)))
        main_canvas.after(10, circular)
        EXTENT += 3.6

def circular_in():                                                                          # CANVAS INSIDE FUNC() /////
    global GLOBAL_STATE, EXTENT_IN
    if GLOBAL_STATE == 0:
        main_canvas.itemconfig(inner_arc, extent=EXTENT_IN, start=EXTENT_IN,
                               fill="#"+("%06x"%random.randint(0,16777215)))
        main_canvas.itemconfig(oval_blink, fill="#"+("%06x"%random.randint(0,16777215)))
        main_canvas.after(15, circular_in)
        EXTENT_IN -= 3.6

GLOBAL_STATE = 0                                                                            # STATEMENTS // GLOBAL /////
EXTENT = 0
EXTENT_IN = 0

main_canvas = Canvas(root, bg="red", highlightthickness=0)                                      ##==> CREATE CANVAS
oval_blink = main_canvas.create_oval(10, 10, 390, 390)                                          ##==> OVAL BLINKING
oval_main = main_canvas.create_oval(15, 15, 385, 385, fill="#050707")                           ##==> OVAL CONTAINER
outer_arc = main_canvas.create_arc(22, 22, 378, 378, fill="red", start=90)                      ##==> CREATE ARC
oval_inner = main_canvas.create_oval(26, 26, 374, 374, fill="black")                            ##==> CREAT INNER LINE
oval_main = main_canvas.create_oval(40, 40, 360, 360, fill="#050707")                           ##==> OVAL CONTAINER
inner_arc = main_canvas.create_arc(60, 60, 340, 340, fill="red", start=90)                      ##==> CREATE ARC
oval_lblcon = main_canvas.create_oval(65, 65, 335, 335, fill="#080a0b")                         ##==> OVAL LBL CONT.

main_canvas.pack(fill=BOTH, expand=YES)

main_label = Label(main_canvas, font=("Consolas", 30), bg="#080a0b")
main_label.place(x=105, y=145)

exit_button = Button(main_canvas, bg="#080a0b", text="\u26CC", bd=0, font=("Segoe UI", 22),     ##==> EXIT APP /////////
                     activebackground="#080a0b", command=root.destroy)
exit_button.place(x=175, y=80)


if __name__ == '__main__':                                                                  # RUN APP //////////////////
    circular()
    circular_in()
    root.mainloop()
