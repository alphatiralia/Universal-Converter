from Tkinter import *
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()
    def create_widgets(self):
        self.frame = Frame(root).grid(row = 0, column = 0)
        Label(self.frame, text="Choose the kind of unit").grid(column = 0, row = 0)
        Button(self.frame, text="Angle", width=30, command=Angle).grid(column = 0, row = 1)
        Button(self.frame, text="Area", width=30, command=Area).grid(column = 0, row = 2)
        Button(self.frame, text="Bit Byte", width=30, command=Bitbyte).grid(column = 0, row = 3)
        Button(self.frame, text="Density", width=30, command=Density).grid(column = 0, row = 4)
        Button(self.frame, text="Electric Current", width=30, command=Electriccurrent).grid(column = 0, row = 5)
        Button(self.frame, text="Energy", width=30, command=Energy).grid(column = 0, row = 6)
        Button(self.frame, text="Force", width=30, command=Force).grid(column = 0, row = 7)
        Button(self.frame, text="Fuel Consumption", width=30, command=Fuelconsumption).grid(column = 0, row = 8)
        Button(self.frame, text="Length", width=30, command=Length).grid(column = 0, row = 9)
        Button(self.frame, text="Mass", width=30, command=Mass).grid(column = 0, row = 10)
        Button(self.frame, text="Power", width=30, command=Power).grid(column = 0, row = 11)
        Button(self.frame, text="Pressure", width=30, command=Pressure).grid(column = 0, row = 12)
        Button(self.frame, text="Speed", width=30, command=Speed).grid(column = 0, row = 13)
        Button(self.frame, text="Temperature", width=30, command=Temperature).grid(column = 0, row = 14)
        Button(self.frame, text="Time", width=30, command=Time).grid(column = 0, row = 15)
        Button(self.frame, text="Volume", width=30, command=Volume).grid(column = 0, row = 16)
        

#Start of Program Section
class Angle(object):
    """docstring for Angle"""
    def __init__(self):
        super(Angle, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Angle")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "arcminute")
        OptionMenu(top, self.unit, "arcminute", "arcsecond", "circle",
                    "degree", "gon", "grad", "mil(Nato)", "mil(Soviet Union)",
                    "mil(Sweden)", "octant", "quadrant", "radian",
                    "revolution", "sextant", "sign", "turn").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"arcminute": 0.016667, "arcsecond": 0.000278,
                    "circle": 360, "degree": 1.0, "gon": 0.9, "grad": 0.9,
                    "mil(Nato)": 0.05625, "mil(Soviet Union)": 0.06,
                    "mil(Sweden)": 0.057143, "octant": 45.0,
                    "quadrant": 90.0, "radian": 57.29578,
                    "revolution": 360.0, "sextant": 60.0,
                    "sign": 30.0, "turn": 360.0}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Area(object):
    """docstring for Area"""
    def __init__(self):
        super(Area, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Area")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "acres")
        OptionMenu(top, self.unit, "acres", "ares", "circular inches",
                    "hectares", "hides", "roods", "square centimeters",
                    "square feet(US & UK)", "square feet(US survey)",
                    "square inches", "square kilometers", "square meters",
                    "square miles", "square millimeters", "square of timber",
                    "square rods or poles", "square yards", "townships").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"acres": 4046.8564224, "ares" :100.0,
                    "circular inches": 0.0005067, "hectares": 10000.0,
                    "hides": 485000.0, "roods": 1011.7141056,
                    "square centimeters": 0.0001,
                    "square feet(US & UK)": 0.092903,
                    "square feet(US survey)": 0.092903,
                    "square inches": 0.000645, "square kilometers": 1000000.0,
                    "square meters": 1.0, "square miles": 2589988.110336,
                    "square millimeters": 0.000001, 
                    "square of timber": 9.290304,
                    "square rods or poles": 25.29285264,
                    "square yards": 0.83612736, "townships": 93239571.972}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Bitbyte(object):
    """docstring for Bitbyte"""
    def __init__(self):
        super(Bitbyte, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Bit Byte")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "bits")
        OptionMenu(top, self.unit, "bits", "bytes", "exabits", "exabytes",
                    "gigabits", "gigabytes", "kilobits", "kilobytes",
                    "megabits", "megabytes", "petabits", "petabytes",
                    "terabits", "terabytes").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"bits": 1.192093 * 10 ** -7,
                    "bytes": 9.53674316 * 10 ** -7,
                    "kilobits": 1.220703125 * 10 ** -4,
                    "kilobytes": 9.765625 * 10 ** -4, "megabits": 0.125,
                    "megabytes": 1.0, "gigabits": 128.0, "gigabytes": 1024.0,
                    "terabits": 131072.0, "terabytes": 1048576.0,
                    "petabits": 134217728.0, "petabytes": 1073741824.0,
                    "exabits": 137438953472.0, "exabytes": 1099511627776.0}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Density(object):
    """docstring for Density"""
    def __init__(self):
        super(Density, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Density")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "grains/gallon(UK)")
        OptionMenu(top, self.unit, "grains/gallon(UK)", "grains/gallon(US)",
                    "grams/cubic centimeters", "grams/liter",
                    "grams/millimeters", "kilograms/cubic meters",
                    "kilograms/liter", "megagrams/cubic meter",
                    "milligrams/liter", "milligrams/millimeters",
                    "ounces/cubic inch", "ounces/gallon(UK)",
                    "ounces/gallon(US)", "pounds/cubic foot",
                    "pounds/cubic inch", "pounds/gallon(UK)",
                    "pounds/gallon(US)", "slugs/cubic foot",
                    "tonnes/cubic meter", "tons(UK)/cubic yard",
                    "tons(US)/cubic yard").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"grains/gallon(UK)": 0.0000143,
                    "grains/gallon(US)": 0.000017,
                    "grams/cubic centimeters": 1.0, "grams/liter": 0.001,
                    "grams/millimeters": 1.0, "kilograms/cubic meters": 0.001,
                    "kilograms/liter": 1.0, "megagrams/cubic meter": 1.0,
                    "milligrams/millimeters": 0.001,
                    "milligrams/liter": 0.000001,
                    "ounces/cubic inch": 1.729994,
                    "ounces/gallon(UK)": 0.006236,
                    "ounces/gallon(US)": 0.007489,
                    "pounds/cubic inch": 27.679904,
                    "pounds/cubic foot": 0.016018,
                    "pounds/gallon(UK)": 0.099776,
                    "pounds/gallon(US)": 0.119826, 
                    "slugs/cubic foot": 0.515318, "tonnes/cubic meter": 1.0,
                    "tons(UK)/cubic yard": 1.328939,
                    "tons(US)/cubic yard": 1.186553}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Electriccurrent(object):
    """docstring for Electric_Current"""
    def __init__(self):
        super(Electriccurrent, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Electric Current")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value= "EMU of current")
        OptionMenu(top, self.unit, "EMU of current", "ESU of current",
                    "abampere", "ampere", "biot", "centiampere",
                    "coulomb/second", "franklin/second",
                    "gaussian electric current", "gigaampere", "gilbert",
                    "kiloampere", "megaampere", "microampere", "milliamp",
                    "milliampere", "nanoampere", "picoampere", "siemens volt",
                    "statampere", "teraampere", "volt/ohm", "watt/volt",
                    "weber/henry").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"abampere": 10.0, "ampere": 1.0, "biot": 10.0,
                    "centiampere": 0.01, "coulomb/second": 1.0,
                    "EMU of current": 10.0,
                    "ESU of current": 3.335641 * 10 ** -10,
                    "franklin/second": 3.335641 * 10 ** -10,
                    "gaussian electric current": 3.335641 * 10 ** -10,
                    "gigaampere": 1.0 * 10 ** 9, "gilbert": 0.79577472,
                    "kiloampere": 1000.0, "megaampere": 1000000.0,
                    "microampere": 0.000001,
                    "milliampere": 0.001, "milliamp": 0.001,
                    "nanoampere": 1.0 * 10 ** -9,
                    "picoampere": 1.0 * 10 ** 12, "siemens volt": 1.0, 
                    "statampere": 3.335641 * 10 ** -10,
                    "teraampere": 1.0 * 10 ** 12, "volt/ohm": 1.0,
                    "watt/volt": 1.0, "weber/henry": 1.0}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Energy(object):
    """docstring for Energy"""
    def __init__(self):
        super(Energy, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Energy")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "Btu(mean)")
        OptionMenu(top, self.unit, "Btu(mean)", "Btu(th)", "calories(15C)",
                    "calories(20C)", "calories(IT)", "calories(food)",
                    "calories(mean)", "calories(th)", "centigrade heat units",
                    "electron volts", "ergs", "foot poundals",
                    "foot-pound force", "gigajoules", "horsepower hours",
                    "inch-pound force", "joules", "kilocalories(IT)",
                    "kilocalories(th)", "kilogram-force meters", "kilojoules",
                    "kilowatt hours", "megajoules", "newton meters", "therms",
                    "watt hours", "watt seconds").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"Btu(th)": 1054.35, "Btu(mean)": 1055.87,
                    "calories(IT)": 4.1868, "calories(th)": 4.184,
                    "calories(mean)": 4.19002, "calories(15C)": 4.1858,
                    "calories(20C)": 4.1819, "calories(food)": 4186.0,
                    "centigrade heat units": 1900.4,
                    "electron volts": 1.60219 * 10 ** -19,
                    "ergs": 1.0 * 10 ** -7, "foot-pound force": 1.355818,
                    "foot poundals": 0.04214, "gigajoules": 1.0 * 10 ** 9,
                    "horsepower hours": 2684520.0,
                    "inch-pound force": 0.112985, "joules": 1.0,
                    "kilocalories(IT)": 4186.8, "kilocalories(th)": 4184.0,
                    "kilogram-force meters": 9.80665, "kilojoules": 1000.0,
                    "kilowatt hours": 3600000.0, "megajoules": 1.0 * 10 ** 6,
                    "newton meters": 1.0, "therms": 105505585.257348,
                    "watt seconds": 1.0, "watt hours" : 3600.0}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Force(object):
    """docstring for Force"""
    def __init__(self):
        super(Force, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Force")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "dynes")
        OptionMenu(top, self.unit, "dynes", "kilograms force", "kilonewtons",
                    "kips", "meganewtons", "newtons", "poundals",
                    "pounds force", "sthene", "tonnes force", "tons force(UK)",
                    "tons force(US)").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"dynes": 0.00001, "kilograms force": 9.80665,
                    "kilonewtons": 1000.0, "kips": 4448.222,
                    "meganewtons": 1.0 * 10 ** 6, "newtons": 1.0,
                    "pounds force": 4.448222, "poundals": 0.138255,
                    "sthene": 1000.0, "tonnes force": 9806.65,
                    "tons force(UK)": 9964.016418,
                    "tons force(US)": 8896.443231}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Fuelconsumption(object):
    """docstring for Fuel_Consumption"""
    def __init__(self):
        super(Fuelconsumption, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Fuel Consumption")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "car(2014 US Average)")
        OptionMenu(top, self.unit, "car(2014 US Average)",
                    "gallon(UK)/100 miles", "gallon(US)/100 miles",
                    "kilometer/liter", "liters/100 kilometer",
                    "liters/meter", "miles/gallon(UK)",
                    "miles/gallon(US)").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        if self.v.get() != 0:
            unit_comp = {"car(2014 US Average)": 9.260417,
                        "gallon(UK)/100 miles": 2.824809,
                        "gallon(US)/100 miles": 2.352146,
                        "kilometer/liter": 100.0 / (self.v.get() ** 2),
                        "liters/100 kilometer": 1.0, "liters/meter": 100000.0,
                        "miles/gallon(UK)": 282.480936 / (self.v.get() ** 2),
                        "miles/gallon(US)": 235.214583 / (self.v.get() ** 2)}
        else:
            unit_comp = {"car(2014 US Average)": 1.0,
                        "gallon(UK)/100 miles": 1.0,
                        "gallon(US)/100 miles": 1.0, "kilometer/liter": 1.0,
                        "liters/100 kilometer": 1.0, "liters/meter": 1.0,
                        "miles/gallon(UK)": 1.0, "miles/gallon(US)": 1.0}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Length(object):
    """docstring for Length"""
    def __init__(self):
        super(Length, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Length")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "Scandinavian mile")
        OptionMenu(top, self.unit, "Scandinavian mile", "angstroms", "au",
                    "barleycorns", "cables", "centimeters", "chains",
                    "decimeters", "ells", "ems", "fathoms", "feet(UK & US)",
                    "feet(US survey)", "furlongs", "hands", "hectometers",
                    "inches", "kilometers", "light years", "meters",
                    "micrometers", "mil", "miles(UK & US)",
                    "miles(nautical, UK)", "miles(nautical, international)",
                    "millimeters", "nanometers", "parsecs", "picometers",
                    "thou", "yards").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"angstroms": 10 ** -10, "au": 149598550000.0,
                    "barleycorns": 0.008467, "cables": 182.88,
                    "centimeters": 0.01, "chains": 20.11684, "decimeters": 0.1,
                    "ells": 0.875, "ems" : 0.004233, "fathoms": 1.8288,
                    "feet(UK & US)": 0.3048,  "feet(US survey)": 0.304801,
                    "furlongs": 201.168, "hands": 0.1016, "hectometers": 100.0,
                    "inches": 0.0254, "kilometers": 1000.0,
                    "light years": 9460528405000000.0, "meters": 1.0,
                    "micrometers": 0.000001, "mil": 0.0000254,
                    "miles(UK & US)": 1609.344,
                    "miles(nautical, international)": 1852.0,
                    "miles(nautical, UK)": 1853.184, "millimeters": 0.001,
                    "nanometers": 10 ** -9, "parsecs": 30856776000000000.0,
                    "picometers": 10 ** -12, "Scandinavian mile": 10000.0,
                    "thou": 0.0000254, "yards": 0.9144}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Mass(object):
    """docstring for Mass"""
    def __init__(self):
        super(Mass, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Mass")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "Earth masses")
        OptionMenu(top, self.unit, "Earth masses", "Solar masses", "carats",
                    "cental", "decagrams", "femtograms", "grains", "grams",
                    "hectograms", "hundredweights", "kilograms", "kilotonnes",
                    "megatonnes", "micrograms", "milligrams", "nanograms",
                    "ounces(US & UK)", "ounces(precious metals)", "picograms",
                    "pounds(US & UK)", "pounds(precious metals)", "slugs",
                    "stones", "tonnes(metric)", "tons(UK)", "tons(US)").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"Earth masses": 5.97219e+24,
                    "Solar masses": 1.9890000000000002e+30, "carats": 0.0002,
                    "cental": 45.359237, "decagrams": 0.01,
                    "femtograms": 1e-18, "grains": 6.479891000000001e-05,
                    "grams": 0.001, "hectograms": 0.1,
                    "hundredweights": 50.802345, "kilograms": 1.0,
                    "kilotonnes": 1000000.0, "megatonnes": 1000000000.0,
                    "micrograms": 1e-09, "milligrams": 1e-06,
                    "nanograms": 1e-12, "ounces(US & UK)": 0.02835,
                    "ounces(precious metals)": 0.031103, "picograms": 1e-15,
                    "pounds(US & UK)": 0.453592,
                    "pounds(precious metals)": 0.373242, "slugs": 14.593903,
                    "stones": 6.350293, "tonnes(metric)": 1000.0,
                    "tons(UK)": 1016.046909, "tons(US)": 907.18474}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Power(object):
    """docstring for Power"""
    def __init__(self):
        super(Power, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Power")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value= "Btu/hour")
        OptionMenu(top, self.unit, "Btu/hour", "Btu/minute", "Btu/second",
                    "calories(th)/hour", "calories(th)/minute",
                    "calories(th)/second", "foot pounds-force/minute",
                    "foot pounds-force/second", "gigawatts",
                    "horsepowers(electric)", "horsepowers(international)",
                    "horsepowers(metric)", "horsepowers(water)",
                    "joules/hour", "joules/minute", "joules/second",
                    "kilocalories(th)/hour", "kilocalories(th)/minute",
                    "kilogram-force meters/hour",
                    "kilograms-force meters/minute", "kilowatts", "megawatts",
                    "petawatts", "terawatts", "watts").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"Btu/hour": 0.293071, "Btu/minute": 17.584267,
                    "Btu/second": 1055.056, "calories(th)/hour": 0.001162,
                    "calories(th)/minute": 0.069733,
                    "calories(th)/second": 4.184,
                    "foot pounds-force/minute": 0.022597,
                    "foot pounds-force/second": 1.35582,
                    "gigawatts": 1000000000.0, "horsepowers(electric)": 746.0,
                    "horsepowers(international)": 745.699872,
                    "horsepowers(metric)": 735.4988,
                    "horsepowers(water)": 746.043, "joules/hour": 0.000278,
                    "joules/minute": 0.016667, "joules/second": 1.0,
                    "kilocalories(th)/hour": 1.162222,
                    "kilocalories(th)/minute": 69.733333,
                    "kilogram-force meters/hour": 0.002724,
                    "kilograms-force meters/minute": 0.163444,
                    "kilowatts": 1000.0, "megawatts": 1000000.0,
                    "petawatts": 1000000000000000.0,
                    "terawatts": 1000000000000.0, "watts": 1.0}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Pressure(object):
    """docstring for Pressure"""
    def __init__(self):
        super(Pressure, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Pressure")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value="atm")
        OptionMenu(top, self.unit, "atm", "bars", "centimeters mercury",
                    "centimeters water", "feet of water", "hectopascals",
                    "inches of mercury", "inches of water",
                    "kilogram-force/sq.centimeter", "kilogram-force/sq.meter",
                    "kilonewtons/sq.meter", "kilonewtons/sq.millimeter",
                    "kilopascals", "kips/sq.inch", "meganewtons/sq.meter",
                    "meganewtons/sq.millimeter", "meters of water",
                    "millibars", "millimeters of mercury",
                    "millimeters of water", "newtons/sq.centimeter",
                    "newtons/sq.meter", "newtons/sq.millimeter", "pascals",
                    "poundals/sq.foot", "pounds-force/sq.foot",
                    "pounds-force/sq.inch", "tonnes-force/sq.cm",
                    "tonnes-force/sq.meter", "tons(UK)-force/sq.foot",
                    "tons(UK)-force/sq.inch", "tons(US)-force/sq.foot",
                    "tons(US)-force/sq.inch", "torr").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"atm": 101325.0, "bars": 100000.0,
                    "centimeters mercury": 1333.22,
                    "centimeters water": 98.0665, "feet of water": 2989.06692,
                    "hectopascals": 100.0, "inches of mercury": 3386.388,
                    "inches of water": 249.08891,
                    "kilogram-force/sq.centimeter": 98066.5,
                    "kilogram-force/sq.meter": 9.80665,
                    "kilonewtons/sq.meter": 1000.0,
                    "kilonewtons/sq.millimeter": 1000000000.0,
                    "kilopascals": 1000.0, "kips/sq.inch": 6894760.0,
                    "meganewtons/sq.meter": 1000000.0,
                    "meganewtons/sq.millimeter": 1000000000000.0,
                    "meters of water": 9806.65, "millibars": 100.0,
                    "millimeters of mercury": 133.322,
                    "millimeters of water": 9.80665,
                    "newtons/sq.centimeter": 10000.0,
                    "newtons/sq.meter": 1.0,
                    "newtons/sq.millimeter": 1000000.0, "pascals": 1.0,
                    "poundals/sq.foot": 1.44816, "pounds-force/sq.foot": 47.88,
                    "pounds-force/sq.inch": 6894.757,
                    "tonnes-force/sq.cm": 98066500.0,
                    "tonnes-force/sq.meter": 9806.65,
                    "tons(UK)-force/sq.foot": 107251.0,
                    "tons(UK)-force/sq.inch": 15444300.0,
                    "tons(US)-force/sq.foot": 95760.0,
                    "tons(US)-force/sq.inch": 13789500.0, "torr": 133.322}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Speed(object):
    """docstring for Speed"""
    def __init__(self):
        super(Speed, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Speed")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "Mach number")
        OptionMenu(top, self.unit, "Mach number", "Nm/24hr",
                    "centimeters/minute", "centimeters/second", "feet/hour",
                    "feet/minute", "feet/second", "inches/minute",
                    "inches/second", "kilometers/hour", "kilometers/second",
                    "knots", "meters/hour", "meters/minute", "meters/second",
                    "miles/hour", "miles/minute", "miles/second",
                    "nautical miles/hour", "speed of light", "speed of sound",
                    "yards/hour", "yards/minute", "yards/second").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"Mach number": 340.2933, "Nm/24hr": 0.021435,
                    "centimeters/minute": 0.000167, "centimeters/second": 0.01,
                    "feet/hour": 8.5e-05, "feet/minute": 0.00508,
                    "feet/second": 0.3048, "inches/minute": 0.000423,
                    "inches/second": 0.0254, "kilometers/hour": 0.277778,
                    "kilometers/second": 1000.0, "knots": 0.514444,
                    "meters/hour": 0.000278, "meters/minute": 0.016667,
                    "meters/second": 1.0, "miles/hour": 0.44704,
                    "miles/minute": 26.8224, "miles/second": 1609.344,
                    "nautical miles/hour": 0.514444,
                    "speed of light": 299790000.0, "speed of sound": 343.0,
                    "yards/hour": 0.000254, "yards/minute": 0.01524,
                    "yards/second": 0.9144}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Temperature(object):
    """docstring for Temperature"""
    def __init__(self):
        super(Temperature, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Temperature")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "Celsius")
        OptionMenu(top, self.unit, "Celsius", "Fahrenheit", "Kelvin", "Rankine",
                    "Reaumur").pack() 
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        unit_comp = {"Celsius": self.v.get() * 1.0,
                    "Fahrenheit": (self.v.get() - 32) / 1.8,
                    "Kelvin": self.v.get() - 273.15,
                    "Reaumur": self.v.get() / 0.8,
                    "Rankine": (self.v.get() - 491.67) / 1.8}
        new_value = {"Celsius": unit_comp[self.unit.get()],
                    "Fahrenheit": unit_comp[self.unit.get()] * 1.8 + 32,
                    "Kelvin": unit_comp[self.unit.get()] + 273.15,
                    "Reaumur": unit_comp[self.unit.get()] * 0.8,
                    "Rankine": unit_comp[self.unit.get()] * 1.8 + 491.67}
        printer = ""
        for i in new_value:
            printer += str(new_value[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Time(object):
    """docstring for Time"""
    def __init__(self):
        super(Time, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Time")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "centuries")
        OptionMenu(top, self.unit, "centuries", "days", "decades",
                    "femtoseconds", "fortnights", "hours", "microseconds",
                    "millenia", "milliseconds", "minutes", "months(Common)",
                    "months(Synodic)", "nanoseconds", "picoseconds",
                    "quarters(Common)", "seconds", "shakes", "weeks",
                    "years(Average Gregorian)", "years(Common)",
                    "years(Julian)", "years(Leap)", "years(Tropical)").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"centuries": 3153600000.0, "days": 86400.0,
                    "decades": 315360000.0, "femtoseconds": 1e-15,
                    "fortnights": 1209600.0, "hours": 3600.0,
                    "microseconds": 1e-06, "millenia": 31536000000.0,
                    "milliseconds": 0.001, "minutes": 60.0,
                    "months(Common)": 2628000.0,
                    "months(Synodic)": 2551442.8896, "nanoseconds": 1e-09,
                    "picoseconds": 1e-12, "quarters(Common)": 7884000.0,
                    "seconds": 1.0, "shakes": 1e-08, "weeks": 604800.0,
                    "years(Average Gregorian)": 31556952.0,
                    "years(Common)": 31536000.0, "years(Julian)": 31557600.0,
                    "years(Leap)": 31622400.0, "years(Tropical)": 31556925.216}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
class Volume(object):
    """docstring for Volume"""
    def __init__(self):
        super(Volume, self).__init__()
        self.create_widgets()
    def create_widgets(self):
        top = self.top = Toplevel()
        top.title("Volume")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = StringVar(value = "acre foot")
        OptionMenu(top, self.unit, "acre foot", "barrels", "bushels(UK)",
                    "bushels(US)", "centiliters", "cubic centimeters",
                    "cubic decameters", "cubic decimeters", "cubic feet",
                    "cubic inches", "cubic kilometers", "cubic meters",
                    "cubic mile", "cubic millimeters", "cubic yards",
                    "cups", "deciliters", "dram", "dram(imperial)",
                    "fluid ounces(US)", "fluid ounces(imperial)",
                    "gallons(US,dry)", "gallons(US,liquid)",
                    "gallons(imperial)", "gill(US)", "gill(imperial)",
                    "liters", "liters(1901-1964)", "microliters",
                    "milliliters", "nanoliters", "picoliters", "pints(US,dry)",
                    "pints(US,liquid)", "pints(imperial)", "quarts(UK,dry)",
                    "quarts(US,liquid)", "quarts(imperial)", "table spoons",
                    "tea spoons").pack()
        self.text = Text(top)
        self.text.pack()
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp = {"acre foot": 1233481.837548, "barrels": 158.987295,
                    "bushels(UK)": 36.36872, "bushels(US)": 35.23907,
                    "centiliters": 0.01, "cubic centimeters": 0.001,
                    "cubic decameters": 1000000.0, "cubic decimeters": 1.0,
                    "cubic feet": 28.316847, "cubic inches": 0.016387,
                    "cubic kilometers": 1000000000000.0,
                    "cubic meters": 1000.0, "cubic mile": 4168181825000.0,
                    "cubic millimeters": 1e-06, "cubic yards": 764.554858,
                    "cups": 0.236588, "deciliters": 0.1, "dram": 0.003697,
                    "dram(imperial)": 0.003552, "fluid ounces(US)": 0.029574,
                    "fluid ounces(imperial)": 0.028413,
                    "gallons(US,dry)": 4.404884,
                    "gallons(US,liquid)": 3.785412,
                    "gallons(imperial)": 4.54609, "gill(US)": 0.118294,
                    "gill(imperial)": 0.142065, "liters": 1.0,
                    "liters(1901-1964)": 1.000028, "microliters": 1e-06,
                    "milliliters": 0.001, "nanoliters": 1e-09,
                    "picoliters": 1e-12, "pints(US,dry)": 0.55061,
                    "pints(US,liquid)": 0.473176, "pints(imperial)": 0.568261,
                    "quarts(UK,dry)": 1.101221, "quarts(US,liquid)": 0.946353,
                    "quarts(imperial)": 1.136523, "table spoons": 0.014787,
                    "tea spoons": 0.004929}
        value_comp, printer = self.v.get() * unit_comp[self.unit.get()], ""
        for i in unit_comp:
            printer += str(value_comp / unit_comp[i]) + " " + str(i) + "\n"
        self.text.delete(0.0, END)
        self.text.insert(0.0, printer)
#End of Program section
root = Tk()
root.title("Universal Converter")
root.geometry("220x435")
app = Application(root)
root.mainloop()
