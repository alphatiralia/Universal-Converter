from Tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.create_widgets()

    def create_widgets(self):
        Label(root, text="Choose the kind of unit").pack()
        Button(root, text="Angle", width=25, command=Angle).pack()
        Button(root, text="Area", width=25, command=Area).pack()
        Button(root, text="Bit Byte", width=25, command=Bitbyte).pack()
        Button(root, text="Density", width=25, command=Density).pack()
        Button(root, text="Electric Current", width=25, command=Electriccurrent).pack()
        Button(root, text="Energy", width=25, command=Energy).pack()
        Button(root, text="Force", width=25, command=Force).pack()
        Button(root, text="Fuel Consumption", width=25, command=Fuelconsumption).pack()
        Button(root, text="Length", width=25, command=Length).pack()
        Button(root, text="Mass", width=25, command=Mass).pack()
        Button(root, text="Power", width=25, command=Power).pack()
        Button(root, text="Pressure", width=25, command=Pressure).pack()
        Button(root, text="Speed", width=25, command=Speed).pack()
        Button(root, text="Temperature", width=25, command=Temperature).pack()
        Button(root, text="Time", width=25, command=Time).pack()
        Button(root, text="Volume", width=25, command=Volume).pack()
        Frame(root, height=20).pack()

#Start of Program Section
class Angle(object):
    """docstring for Angle"""
    def __init__(self):
        super(Angle, self).__init__()
        top = self.top = Toplevel()
        top.title("Angle")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['arcminute', 'arcsecond', 'circle', 'degree', 'gon', 'grad',
                'mil(Nato)', 'mil(Soviet Union)', 'mil(Sweden)', 'octant',
                'quadrant', 'radian', 'revolution', 'sextant', 'sign', 'turn']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [0.016667, 0.000278, 360, 1.0, 0.9, 0.9, 0.05625,
                        0.06, 0.057143, 45.0, 90.0, 57.29578, 360.0, 60.0,
                        30.0, 360.0]
        unit = ['arcminute', 'arcsecond', 'circle', 'degree', 'gon', 'grad',
                'mil(Nato)', 'mil(Soviet Union)', 'mil(Sweden)', 'octant',
                'quadrant', 'radian', 'revolution', 'sextant', 'sign', 'turn']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Area(object):
    """docstring for Area"""
    def __init__(self):
        super(Area, self).__init__()
        top = self.top = Toplevel()
        top.title("Area")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['acres', 'ares', 'circular inches', 'hectares', 'hides',
                'roods', 'square centimeters', 'square feet(US & UK)',
                'square feet(US survey)', 'square inches', 'square kilometers',
                'square meters', 'square miles', 'square millimeters',
                'square of timber', 'square rods or poles', 'square yards',
                'townships']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [4046.8564224, 100.0, 0.0005067,  10000.0, 485000.0,
                        1011.7141056, 0.0001, 0.092903,  0.092903, 0.000645,
                        1000000.0, 1.0, 2589988.110336, 0.000001, 9.290304,
                        25.29285264, 0.83612736, 93239571.972]
        unit = ['acres', 'ares', 'circular inches', 'hectares', 'hides',
                'roods', 'square centimeters', 'square feet(US & UK)',
                'square feet(US survey)', 'square inches', 'square kilometers',
                'square meters', 'square miles', 'square millimeters',
                'square of timber', 'square rods or poles', 'square yards',
                'townships']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Bitbyte(object):
    """docstring for Bitbyte"""
    def __init__(self):
        super(Bitbyte, self).__init__()
        top = self.top = Toplevel()
        top.title("Bit Byte")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['bits', 'bytes', 'exabits', 'exabytes', 'gigabits',
                'gigabytes', 'kilobits', 'kilobytes', 'megabits', 'megabytes',
                'petabits', 'petabytes', 'terabits', 'terabytes']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [1.192093e-07, 9.53674316e-07, 137438953472.0,
                        1099511627776.0, 128.0, 1024.0, 0.0001220703125,
                        0.0009765625, 0.125, 1.0, 134217728.0, 1073741824.0,
                        131072.0, 1048576.0]
        unit = ['bits', 'bytes', 'exabits', 'exabytes', 'gigabits',
                'gigabytes', 'kilobits', 'kilobytes', 'megabits', 'megabytes',
                'petabits', 'petabytes', 'terabits', 'terabytes']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Density(object):
    """docstring for Density"""
    def __init__(self):
        super(Density, self).__init__()
        top = self.top = Toplevel()
        top.title("Density")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['grains/gallon(UK)', 'grains/gallon(US)',
                'grams/cubic centimeters', 'grams/liter', 'grams/millimeters',
                'kilograms/cubic meters', 'kilograms/liter',
                'megagrams/cubic meter', 'milligrams/liter',
                'milligrams/millimeters', 'ounces/cubic inch',
                'ounces/gallon(UK)', 'ounces/gallon(US)', 'pounds/cubic foot',
                'pounds/cubic inch', 'pounds/gallon(UK)', 'pounds/gallon(US)',
                'slugs/cubic foot', 'tonnes/cubic meter',
                'tons(UK)/cubic yard', 'tons(US)/cubic yard']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [1.43e-05, 1.7e-05, 1.0, 0.001, 1.0, 0.001, 1.0, 1.0,
                        1e-06, 0.001, 1.729994, 0.006236, 0.007489, 0.016018,
                        27.679904, 0.099776, 0.119826, 0.515318, 1.0, 1.328939,
                        1.186553]
        unit = ['grains/gallon(UK)', 'grains/gallon(US)',
                'grams/cubic centimeters', 'grams/liter', 'grams/millimeters',
                'kilograms/cubic meters', 'kilograms/liter',
                'megagrams/cubic meter', 'milligrams/liter',
                'milligrams/millimeters', 'ounces/cubic inch',
                'ounces/gallon(UK)', 'ounces/gallon(US)', 'pounds/cubic foot',
                'pounds/cubic inch', 'pounds/gallon(UK)', 'pounds/gallon(US)',
                'slugs/cubic foot', 'tonnes/cubic meter',
                'tons(UK)/cubic yard', 'tons(US)/cubic yard']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Electriccurrent(object):
    """docstring for Electric_Current"""
    def __init__(self):
        super(Electriccurrent, self).__init__()
        top = self.top = Toplevel()
        top.title("Electric Current")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['EMU of current', 'ESU of current', 'abampere', 'ampere',
                'biot', 'centiampere', 'coulomb/second', 'franklin/second',
                'gaussian electric current', 'gigaampere', 'gilbert',
                'kiloampere', 'megaampere', 'microampere', 'milliamp',
                'milliampere', 'nanoampere', 'picoampere', 'siemens volt',
                'statampere', 'teraampere', 'volt/ohm', 'watt/volt',
                'weber/henry']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [10.0, 3.335641e-10, 10.0, 1.0, 10.0, 0.01, 1.0,
                        3.335641e-10, 3.335641e-10, 1000000000.0, 0.79577472,
                        1000.0, 1000000.0, 1e-06, 0.001, 0.001, 1e-09,
                        1000000000000.0, 1.0, 3.335641e-10, 1000000000000.0,
                        1.0, 1.0, 1.0]
        unit = ['EMU of current', 'ESU of current', 'abampere', 'ampere',
                'biot', 'centiampere', 'coulomb/second', 'franklin/second',
                'gaussian electric current', 'gigaampere', 'gilbert',
                'kiloampere', 'megaampere', 'microampere', 'milliamp',
                'milliampere', 'nanoampere', 'picoampere', 'siemens volt',
                'statampere', 'teraampere', 'volt/ohm', 'watt/volt',
                'weber/henry']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Energy(object):
    """docstring for Energy"""
    def __init__(self):
        super(Energy, self).__init__()
        top = self.top = Toplevel()
        top.title("Energy")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['Btu(mean)', 'Btu(th)', 'calories(15C)', 'calories(20C)',
                'calories(IT)', 'calories(food)', 'calories(mean)',
                'calories(th)', 'centigrade heat units', 'electron volts',
                'ergs', 'foot poundals', 'foot-pound force', 'gigajoules',
                'horsepower hours', 'inch-pound force', 'joules',
                'kilocalories(IT)', 'kilocalories(th)',
                'kilogram-force meters', 'kilojoules', 'kilowatt hours',
                'megajoules', 'newton meters', 'therms', 'watt hours',
                'watt seconds']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [1055.87, 1054.35, 4.1858, 4.1819, 4.1868, 4186.0,
                        4.19002, 4.184, 1900.4, 1.60219e-19, 1e-07, 0.04214,
                        1.355818, 1000000000.0, 2684520.0, 0.112985, 1.0,
                        4186.8, 4184.0, 9.80665, 1000.0, 3600000.0, 1000000.0,
                        1.0, 105505585.257348, 3600.0, 1.0]
        unit = ['Btu(mean)', 'Btu(th)', 'calories(15C)', 'calories(20C)',
                'calories(IT)', 'calories(food)', 'calories(mean)',
                'calories(th)', 'centigrade heat units', 'electron volts',
                'ergs', 'foot poundals', 'foot-pound force', 'gigajoules',
                'horsepower hours', 'inch-pound force', 'joules',
                'kilocalories(IT)', 'kilocalories(th)',
                'kilogram-force meters', 'kilojoules', 'kilowatt hours',
                'megajoules', 'newton meters', 'therms', 'watt hours',
                'watt seconds']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Force(object):
    """docstring for Force"""
    def __init__(self):
        super(Force, self).__init__()
        top = self.top = Toplevel()
        top.title("Force")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['dynes', 'kilograms force', 'kilonewtons', 'kips',
                'meganewtons', 'newtons', 'poundals', 'pounds force',
                'sthene', 'tonnes force', 'tons force(UK)', 'tons force(US)']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [1e-05, 9.80665, 1000.0, 4448.222, 1000000.0, 1.0,
                        0.138255, 4.448222, 1000.0, 9806.65, 9964.016418,
                        8896.443231]
        unit = ['dynes', 'kilograms force', 'kilonewtons', 'kips',
                'meganewtons', 'newtons', 'poundals', 'pounds force',
                'sthene', 'tonnes force', 'tons force(UK)', 'tons force(US)']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Fuelconsumption(object):
    """docstring for Fuel_Consumption"""
    def __init__(self):
        super(Fuelconsumption, self).__init__()
        top = self.top = Toplevel()
        top.title("Fuel Consumption")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['car(2014 US Average)', 'gallon(UK)/100 miles',
                'gallon(US)/100 miles', 'kilometer/liter',
                'liters/100 kilometer', 'liters/meter', 'miles/gallon(UK)',
                'miles/gallon(US)']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [9.260417, 2.824809, 2.352146,
                        100.0 / (self.v.get() ** 2), 1.0, 100000.0,
                        282.480936 / (self.v.get() ** 2),
                        235.214583 / (self.v.get() ** 2)]
        unit = ['car(2014 US Average)', 'gallon(UK)/100 miles',
                'gallon(US)/100 miles', 'kilometer/liter',
                'liters/100 kilometer', 'liters/meter', 'miles/gallon(UK)',
                'miles/gallon(US)']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Length(object):
    """docstring for Length"""
    def __init__(self):
        super(Length, self).__init__()
        top = self.top = Toplevel()
        top.title("Length")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['Scandinavian mile', 'angstroms', 'au', 'barleycorns',
                'cables', 'centimeters', 'chains', 'decimeters', 'ells', 'ems',
                'fathoms', 'feet(UK & US)', 'feet(US survey)', 'furlongs',
                'hands', 'hectometers', 'inches', 'kilometers', 'light years',
                'meters', 'micrometers', 'mil', 'miles(UK & US)',
                'miles(nautical, UK)', 'miles(nautical, international',
                'millimeters', 'nanometers', 'parsecs', 'picometers', 'thou',
                'yards']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [10000.0, 1e-10, 149598550000.0, 0.008467,
                        182.88, 0.01, 20.11684, 0.1, 0.875, 0.004233,
                        1.8288, 0.3048, 0.304801, 201.168, 0.1016, 100.0,
                        0.0254, 1000.0, 9460528405000000.0, 1.0, 1e-06,
                        2.54e-05, 1609.344, 1853.184, 1852.0, 0.001, 1e-09,
                        3.0856776e+16, 1e-12, 2.54e-05, 0.9144]
        unit = ['Scandinavian mile', 'angstroms', 'au', 'barleycorns',
                'cables', 'centimeters', 'chains', 'decimeters', 'ells', 'ems',
                'fathoms', 'feet(UK & US)', 'feet(US survey)', 'furlongs',
                'hands', 'hectometers', 'inches', 'kilometers', 'light years',
                'meters', 'micrometers', 'mil', 'miles(UK & US)',
                'miles(nautical, UK)', 'miles(nautical, international',
                'millimeters', 'nanometers', 'parsecs', 'picometers', 'thou',
                'yards']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Mass(object):
    """docstring for Mass"""
    def __init__(self):
        super(Mass, self).__init__()
        top = self.top = Toplevel()
        top.title("Mass")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['Earth masses', 'Solar masses', 'carats', 'cental',
                'decagrams', 'femtograms', 'grains', 'grams', 'hectograms',
                'hundredweights', 'kilograms', 'kilotonnes', 'megatonnes',
                'micrograms', 'milligrams', 'nanograms', 'ounces(US & UK)',
                'ounces(precious metals)', 'picograms', 'pounds(US & UK)',
                'pounds(precious metals)', 'slugs', 'stones', 'tonnes(metric)',
                'tons(UK)', 'tons(US)']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [5.97219e+24, 1.9890000000000002e+30, 0.0002,
                        45.359237, 0.01, 1e-18, 6.479891000000001e-05, 0.001,
                        0.1, 50.802345, 1.0, 1000000.0, 1000000000.0, 1e-09,
                        1e-06, 1e-12, 0.02835, 0.031103, 1e-15, 0.453592,
                        0.373242, 14.593903, 6.350293, 1000.0, 1016.046909,
                        907.18474]
        unit = ['Earth masses', 'Solar masses', 'carats', 'cental',
                'decagrams', 'femtograms', 'grains', 'grams', 'hectograms',
                'hundredweights', 'kilograms', 'kilotonnes', 'megatonnes',
                'micrograms', 'milligrams', 'nanograms', 'ounces(US & UK)',
                'ounces(precious metals)', 'picograms', 'pounds(US & UK)',
                'pounds(precious metals)', 'slugs', 'stones', 'tonnes(metric)',
                'tons(UK)', 'tons(US)']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Power(object):
    """docstring for Power"""
    def __init__(self):
        super(Power, self).__init__()
        top = self.top = Toplevel()
        top.title("Power")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['Btu/hour', 'Btu/minute', 'Btu/second', 'calories(th)/hour',
                'calories(th)/minute', 'calories(th)/second',
                'foot pounds-force/minute', 'foot pounds-force/second',
                'gigawatts', 'horsepowers(electric)',
                'horsepowers(international)', 'horsepowers(metric)',
                'horsepowers(water)', 'joules/hour', 'joules/minute',
                'joules/second', 'kilocalories(th)/hour',
                'kilocalories(th)/minute', 'kilogram-force meters/hour',
                'kilograms-force meters/minute', 'kilowatts', 'megawatts',
                'petawatts', 'terawatts', 'watts']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [0.293071, 17.584267, 1055.056, 0.001162, 0.069733,
                        4.184, 0.022597, 1.35582, 1000000000.0, 746.0,
                        745.699872, 735.4988, 746.043, 0.000278, 0.016667, 1.0,
                        1.162222, 69.733333, 0.002724, 0.163444, 1000.0,
                        1000000.0, 1000000000000000.0, 1000000000000.0, 1.0]
        unit = ['Btu/hour', 'Btu/minute', 'Btu/second', 'calories(th)/hour',
                'calories(th)/minute', 'calories(th)/second',
                'foot pounds-force/minute', 'foot pounds-force/second',
                'gigawatts', 'horsepowers(electric)',
                'horsepowers(international)', 'horsepowers(metric)',
                'horsepowers(water)', 'joules/hour', 'joules/minute',
                'joules/second', 'kilocalories(th)/hour',
                'kilocalories(th)/minute', 'kilogram-force meters/hour',
                'kilograms-force meters/minute', 'kilowatts', 'megawatts',
                'petawatts', 'terawatts', 'watts']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Pressure(object):
    """docstring for Pressure"""
    def __init__(self):
        super(Pressure, self).__init__()
        top = self.top = Toplevel()
        top.title("Pressure")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['atm', 'bars', 'centimeters mercury', 'centimeters water',
                'feet of water', 'hectopascals', 'inches of mercury',
                'inches of water', 'kilogram-force/sq.centimeter',
                'kilogram-force/sq.meter', 'kilonewtons/sq.meter',
                'kilonewtons/sq.millimeter', 'kilopascals', 'kips/sq.inch',
                'meganewtons/sq.meter', 'meganewtons/sq.millimeter',
                'meters of water', 'millibars', 'millimeters of mercury',
                'millimeters of water', 'newtons/sq.centimeter',
                'newtons/sq.meter', 'newtons/sq.millimeter', 'pascals',
                'poundals/sq.foot', 'pounds-force/sq.foot',
                'pounds-force/sq.inch', 'tonnes-force/sq.cm',
                'tonnes-force/sq.meter', 'tons(UK)-force/sq.foot',
                'tons(UK)-force/sq.inch', 'tons(US)-force/sq.foot',
                'tons(US)-force/sq.inch', 'torr']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [101325.0, 100000.0, 1333.22, 98.0665, 2989.06692,
                        100.0, 3386.388, 249.08891, 98066.5, 9.80665, 1000.0,
                        1000000000.0, 1000.0, 6894760.0, 1000000.0,
                        1000000000000.0, 9806.65, 100.0, 133.322, 9.80665,
                        10000.0, 1.0, 1000000.0, 1.0, 1.44816, 47.88, 6894.757,
                        98066500.0, 9806.65, 107251.0, 15444300.0, 95760.0,
                        13789500.0, 133.322]
        unit = ['atm', 'bars', 'centimeters mercury', 'centimeters water',
                'feet of water', 'hectopascals', 'inches of mercury',
                'inches of water', 'kilogram-force/sq.centimeter',
                'kilogram-force/sq.meter', 'kilonewtons/sq.meter',
                'kilonewtons/sq.millimeter', 'kilopascals', 'kips/sq.inch',
                'meganewtons/sq.meter', 'meganewtons/sq.millimeter',
                'meters of water', 'millibars', 'millimeters of mercury',
                'millimeters of water', 'newtons/sq.centimeter',
                'newtons/sq.meter', 'newtons/sq.millimeter', 'pascals',
                'poundals/sq.foot', 'pounds-force/sq.foot',
                'pounds-force/sq.inch', 'tonnes-force/sq.cm',
                'tonnes-force/sq.meter', 'tons(UK)-force/sq.foot',
                'tons(UK)-force/sq.inch', 'tons(US)-force/sq.foot',
                'tons(US)-force/sq.inch', 'torr']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Speed(object):
    """docstring for Speed"""
    def __init__(self):
        super(Speed, self).__init__()
        top = self.top = Toplevel()
        top.title("Speed")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['Mach number', 'Nm/24hr', 'centimeters/minute',
                'centimeters/second', 'feet/hour', 'feet/minute',
                'feet/second', 'inches/minute', 'inches/second',
                'kilometers/hour', 'kilometers/second', 'knots', 'meters/hour',
                'meters/minute', 'meters/second', 'miles/hour', 'miles/minute',
                'miles/second', 'nautical miles/hour', 'speed of light',
                'speed of sound', 'yards/hour', 'yards/minute', 'yards/second']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [340.2933, 0.021435, 0.000167, 0.01, 8.5e-05, 0.00508,
                        0.3048, 0.000423, 0.0254, 0.277778, 1000.0, 0.514444,
                        0.000278, 0.016667, 1.0, 0.44704, 26.8224, 1609.344,
                        0.514444, 299790000.0, 343.0, 0.000254, 0.01524,
                        0.9144]
        unit = ['Mach number', 'Nm/24hr', 'centimeters/minute',
                'centimeters/second', 'feet/hour', 'feet/minute',
                'feet/second', 'inches/minute', 'inches/second',
                'kilometers/hour', 'kilometers/second', 'knots', 'meters/hour',
                'meters/minute', 'meters/second', 'miles/hour', 'miles/minute',
                'miles/second', 'nautical miles/hour', 'speed of light',
                'speed of sound', 'yards/hour', 'yards/minute', 'yards/second']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Temperature(object):
    """docstring for Temperature"""
    def __init__(self):
        super(Temperature, self).__init__()
        top = self.top = Toplevel()
        top.title("Temperature")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['Celsius', 'Fahrenheit', 'Kelvin', 'Rankine', 'Reaumur']  
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        unit_comp_main = {"Celsius": self.v.get() * 1.0,
        "Fahrenheit": (self.v.get() - 32) / 1.8,
        "Kelvin": self.v.get() - 273.15, "Reaumur": self.v.get() / 0.8,
        "Rankine": (self.v.get() - 491.67) / 1.8}
        unit = ['Celsius', 'Fahrenheit', 'Kelvin', 'Rankine', 'Reaumur']
        new_value = [unit_comp_main[unit[self.unit.get()]],
                    unit_comp_main[unit[self.unit.get()]] * 1.8 + 32,
                    unit_comp_main[unit[self.unit.get()]] + 273.15,
                    unit_comp_main[unit[self.unit.get()]] * 1.8 + 491.67,
                    unit_comp_main[unit[self.unit.get()]] * 0.8]
        printer = ''
        for i in range(len(new_value)):
            printer += str(new_value[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Time(object):
    """docstring for Time"""
    def __init__(self):
        super(Time, self).__init__()
        top = self.top = Toplevel()
        top.title("Time")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['centuries', 'days', 'decades', 'femtoseconds', 'fortnights',
                'hours', 'microseconds', 'millenia', 'milliseconds', 'minutes',
                'months(Common)', 'months(Synodic)', 'nanoseconds',
                'picoseconds', 'quarters(Common)', 'seconds', 'shakes',
                'weeks', 'years(Average Gregorian)', 'years(Common)',
                'years(Julian)', 'years(Leap)', 'years(Tropical)']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [3153600000.0, 86400.0, 315360000.0, 1e-15, 1209600.0,
                        3600.0, 1e-06, 31536000000.0, 0.001, 60.0, 2628000.0,
                        2551442.8896, 1e-09, 1e-12, 7884000.0, 1.0, 1e-08,
                        604800.0, 31556952.0, 31536000.0, 31557600.0,
                        31622400.0, 31556925.216]
        unit = ['centuries', 'days', 'decades', 'femtoseconds', 'fortnights',
                'hours', 'microseconds', 'millenia', 'milliseconds', 'minutes',
                'months(Common)', 'months(Synodic)', 'nanoseconds',
                'picoseconds', 'quarters(Common)', 'seconds', 'shakes',
                'weeks', 'years(Average Gregorian)', 'years(Common)',
                'years(Julian)', 'years(Leap)', 'years(Tropical)']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
class Volume(object):
    """docstring for Volume"""
    def __init__(self):
        super(Volume, self).__init__()
        top = self.top = Toplevel()
        top.title("Volume")
        self.v = IntVar()
        self.value = Entry(top, textvariable=self.v).pack()
        self.unit = IntVar()
        unit_list = self.unit_list = ['acre foot', 'barrels', 'bushels(UK)', 'bushels(US)',
                'centiliters', 'cubic centimeters', 'cubic decameters',
                'cubic decimeters', 'cubic feet', 'cubic inches',
                'cubic kilometers', 'cubic meters', 'cubic mile',
                'cubic millimeters', 'cubic yards', 'cups', 'deciliters',
                'dram', 'dram(imperial)', 'fluid ounces(US)',
                'fluid ounces(imperial)', 'gallons(US,dry)',
                'gallons(US,liquid)', 'gallons(imperial)', 'gill(US)',
                'gill(imperial)', 'liters', 'liters(1901-1964)', 'microliters',
                'milliliters', 'nanoliters', 'picoliters', 'pints(US,dry)',
                'pints(US,liquid)', 'pints(imperial)', 'quarts(UK,dry)',
                'quarts(US,liquid)', 'quarts(imperial)', 'table spoons',
                'tea spoons']
        for i in range(len(unit_list)):
            Radiobutton(top, text=unit_list[i], variable=self.unit, value=i).pack(side="left")
        Button(top, text="convert", command=self.change_old_unit).pack()
    def change_old_unit(self):
        """Return the converted value and new unit."""
        unit_comp_main = [1233481.837548, 158.987295, 36.36872, 35.23907, 0.01,
                        0.001, 1000000.0, 1.0, 28.316847, 0.016387,
                        1000000000000.0, 1000.0, 4168181825000.0, 1e-06,
                        764.554858, 0.236588, 0.1, 0.003697, 0.003552,
                        0.029574, 0.028413, 4.404884, 3.785412, 4.54609,
                        0.118294, 0.142065, 1.0, 1.000028, 1e-06, 0.001, 1e-09,
                        1e-12, 0.55061, 0.473176, 0.568261, 1.101221, 0.946353,
                        1.136523, 0.014787, 0.004929]
        unit = ['acre foot', 'barrels', 'bushels(UK)', 'bushels(US)',
                'centiliters', 'cubic centimeters', 'cubic decameters',
                'cubic decimeters', 'cubic feet', 'cubic inches',
                'cubic kilometers', 'cubic meters', 'cubic mile',
                'cubic millimeters', 'cubic yards', 'cups', 'deciliters',
                'dram', 'dram(imperial)', 'fluid ounces(US)',
                'fluid ounces(imperial)', 'gallons(US,dry)',
                'gallons(US,liquid)', 'gallons(imperial)', 'gill(US)',
                'gill(imperial)', 'liters', 'liters(1901-1964)', 'microliters',
                'milliliters', 'nanoliters', 'picoliters', 'pints(US,dry)',
                'pints(US,liquid)', 'pints(imperial)', 'quarts(UK,dry)',
                'quarts(US,liquid)', 'quarts(imperial)', 'table spoons',
                'tea spoons']
        value_comp_main, printer = self.v.get() * unit_comp_main[self.unit.get()], ""
        for i in range(len(unit_comp_main)):
            printer += str(value_comp_main / unit_comp_main[i]) + ' ' + str(unit[i]) + "\n"
        print printer
#End of Program section
root = Tk()
root.title("Universal Converter")
root.geometry("250x450")
app = Application(root)
root.mainloop()
