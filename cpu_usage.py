import tkinter as tk
import psutil

def run_canvas():
    global count, extent, extent_out
    if count < 100:
        canvas.itemconfig(arc, extent=extent, fill="#d8b7e6", start=90,width=0)
        canvas.itemconfig(arc_in, extent=extent_out, fill="#d8b7e6", start=180, width=0)
        extent -= 3.6
        extent_out += 3.6
        canvas.after(10, run_canvas)

def cpu_temp():
    global count
    if count < 100:
        al = psutil.cpu_freq()
        cpu_usage = psutil.cpu_percent()
        label.configure(text=" CPU-Usage\n {}% ".format(cpu_usage))
        label_freq.configure(text="{} GHz".format(int(al[0])))
        label.after(1000, cpu_temp)

count = 0
extent = 0
extent_out = 0

root = tk.Tk()
width = root.winfo_screenwidth() / 2.5
height = root.winfo_screenheight() / 3.5
root.geometry("400x400+%d+%d" % (width, height))
root.attributes("-transparent", "red")
root.overrideredirect(1)

canvas = tk.Canvas(root, bg="red", highlightthickness=0)
canvas.pack(fill="both", expand="yes")

arc = canvas.create_arc(25,25,375,375,  extent=0, width=0)
inside_oval = canvas.create_oval(35, 35, 365, 365, fill="#29222b")
arc_in = canvas.create_arc(70,70,330,330,  extent=0, width=0)
inside_oval = canvas.create_oval(75, 75, 325, 325, fill="#362d39")

label = tk.Label(canvas, font=("Space Age", 16), bg="#362d39", fg="#d8b7e6")
label.place(x=120, y=170)

label_freq = tk.Label(canvas, font=("Space Age", 12), bg="#362d39", fg="#d8b7e6")
label_freq.place(x=150, y=260)

exit_btn = tk.Button(canvas, text="\u2656", bd=0, bg="#362d39", fg="#d8b7e6", command=root.destroy)
exit_btn.place(x=175, y=90, width=50)


run_canvas()
cpu_temp()


if __name__ == '__main__':
    tk.mainloop()
