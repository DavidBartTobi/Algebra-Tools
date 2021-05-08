from tkinter import *


def Coordinate_Entry(top, entries, dimension_status3, dimension_status4, dimension_status5, dimension_status6):

    entries[0].append(Entry(top, width=3, justify='center', state='normal'))
    entries[0][0].grid(row=1, column=0, pady=15, padx=(10, 0))

    entries[0].append(Entry(top, width=3, justify='center', state='normal'))
    entries[0][1].grid(row=1, column=1, pady=15)

    entries[0].append(Entry(top, width=3, justify='center', state=dimension_status3, disabledbackground='gray'))
    entries[0][2].grid(row=1, column=2, pady=15)

    entries[0].append(Entry(top, width=3, justify='center', state=dimension_status4, disabledbackground='gray'))
    entries[0][3].grid(row=1, column=3, pady=15)

    entries[0].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[0][4].grid(row=1, column=4, pady=15)

    entries[0].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[0][5].grid(row=1, column=5, pady=15, padx=(0, 10))


    entries[1].append(Entry(top, width=3, justify='center', state='normal'))
    entries[1][0].grid(row=2, column=0, padx=(10, 0))

    entries[1].append(Entry(top, width=3, justify='center', state='normal'))
    entries[1][1].grid(row=2, column=1)

    entries[1].append(Entry(top, width=3, justify='center', state=dimension_status3, disabledbackground='gray'))
    entries[1][2].grid(row=2, column=2)

    entries[1].append(Entry(top, width=3, justify='center', state=dimension_status4, disabledbackground='gray'))
    entries[1][3].grid(row=2, column=3)

    entries[1].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[1][4].grid(row=2, column=4)

    entries[1].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[1][5].grid(row=2, column=5, padx=(0 ,10))


    entries[2].append(Entry(top, width=3, justify='center', state=dimension_status3, disabledbackground='gray'))
    entries[2][0].grid(row=3, column=0, pady=(15,0), padx=(10, 0))

    entries[2].append(Entry(top, width=3, justify='center', state=dimension_status3, disabledbackground='gray'))
    entries[2][1].grid(row=3, column=1, pady=(15,0))

    entries[2].append(Entry(top, width=3, justify='center', state=dimension_status3, disabledbackground='gray'))
    entries[2][2].grid(row=3, column=2, pady=(15,0))

    entries[2].append(Entry(top, width=3, justify='center', state=dimension_status4, disabledbackground='gray'))
    entries[2][3].grid(row=3, column=3, pady=(15,0))

    entries[2].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[2][4].grid(row=3, column=4, pady=(15,0))

    entries[2].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[2][5].grid(row=3, column=5, pady=(15,0), padx=(0, 10))


    entries[3].append(Entry(top, width=3, justify='center', state=dimension_status4, disabledbackground='gray'))
    entries[3][0].grid(row=4, column=0, pady=(15,0), padx=(10, 0))

    entries[3].append(Entry(top, width=3, justify='center', state=dimension_status4, disabledbackground='gray'))
    entries[3][1].grid(row=4, column=1, pady=(15,0))

    entries[3].append(Entry(top, width=3, justify='center', state=dimension_status4, disabledbackground='gray'))
    entries[3][2].grid(row=4, column=2, pady=(15,0))

    entries[3].append(Entry(top, width=3, justify='center', state=dimension_status4, disabledbackground='gray'))
    entries[3][3].grid(row=4, column=3, pady=(15,0))

    entries[3].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[3][4].grid(row=4, column=4, pady=(15,0))

    entries[3].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[3][5].grid(row=4, column=5, pady=(15,0), padx=(0, 10))


    entries[4].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[4][0].grid(row=5, column=0, pady=(15,0), padx=(10, 0))

    entries[4].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[4][1].grid(row=5, column=1, pady=(15,0))

    entries[4].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[4][2].grid(row=5, column=2, pady=(15,0))

    entries[4].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[4][3].grid(row=5, column=3, pady=(15,0))

    entries[4].append(Entry(top, width=3, justify='center', state=dimension_status5, disabledbackground='gray'))
    entries[4][4].grid(row=5, column=4, pady=(15,0))

    entries[4].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[4][5].grid(row=5, column=5, pady=(15,0), padx=(0, 10))


    entries[5].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[5][0].grid(row=6, column=0, pady=(15,0), padx=(10, 0))

    entries[5].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[5][1].grid(row=6, column=1, pady=(15,0))

    entries[5].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[5][2].grid(row=6, column=2, pady=(15,0))

    entries[5].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[5][3].grid(row=6, column=3, pady=(15,0))

    entries[5].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[5][4].grid(row=6, column=4, pady=(15,0))

    entries[5].append(Entry(top, width=3, justify='center', state=dimension_status6, disabledbackground='gray'))
    entries[5][5].grid(row=6, column=5, pady=(15,0), padx=(0, 10))