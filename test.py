from Tkinter import *
class Force(object):
    """docstring for Force"""
    def __init__(self, value=0, old_unit=0):
        super(Force, self).__init__()
        self.value = value
        self.old_unit = old_unit
        top = Toplevel()
        top.title("Force")
        entry = Entry(top, textvariable=value).pack()
        unit_list = ["dynes", "kilograms force", "kilonewtons", "kips", "meganewtons",
                        "newtons", "pounds force", "poundals", "sthene", "tonnes force",
                        "tons force(UK)", "tons force(US)"]
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=unit, value=i).pack(side="left")
        button = Button(top, text="convert", command=printer).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [0.00001, 9.80665,
        1000.0, 4448.222, 1.0 * 10 ** 6,
        1.0, 4.448222, 0.138255,
        1000.0, 9806.65,
        9964.016418 , 8896.443231]
        unit = ["dynes", "kilograms force", "kilonewtons", "kips", "meganewtons",
                "newtons", "pounds force", "poundals", "sthene", "tonnes force",
                "tons force(UK)", "tons force(US)"]
        value_comp_main = self.value * unit_comp_main[self.old_unit]
        printer = ''
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        return printer
def printer():
    values = value.get()
    units = unit.get()
    print Force(values, units).change_old_unit()
root = Tk()
root.title("Universal Converter!!")
force_button = Button(root, text="Force", command=Force).pack()
value = IntVar()
unit = IntVar()






root.mainloop()
