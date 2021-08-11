from tkinter import*
def bus_main():

    def addbus():

        root.destroy()
        root1 = Tk()

        #root1.geometry("444x234")
        #width, Height
        #root1.minsize(700,500)
        #root1.maxsize(800,500)
        title_label=Label(root1,text = "Welcome To Bus Booking Service",bg ="grey",fg="yellow",padx=4,pady=6,font="comicsansms 19 bold",borderwidth=9,relief=GROOVE)
        title_label.grid(row=1,column=1)
        photo=PhotoImage(file="img_2.png")
        y_label = Label(image=photo)
        y_label.grid(row=2,column=1)
        middle_label=Label(root1,text="Bus Operator Details Filling",bg="grey",fg="black",padx=9,pady=7,font="comicsansms 20 bold")
        middle_label.grid(row=3,column=1)
        #TEXT FOR OUR FORM
        fullname=Label(root1,text="FullName:",font="comicsansms 8 bold")
        contactno=Label(root1,text="Contact No:",font="comicsansms 8 bold")
        Address =Label(root1,text="Address:",font="comicsansms 8 bold")
            #PACK TEXT  FOR OUR FORM
        fullname.grid(row=4,column=1)
        contactno.grid(row=5,column=1)
        Address.grid(row=6,column=1)
            #TKINTER VARIABLE FOR SORTING VALUES
        fullnamevalue=StringVar()
        contactnovalue=StringVar()
        Addressvalue=StringVar()
            #ENTRIES FOR OUR FORM
        fullnameentry=Entry(root1,textvariable=fullnamevalue)
        contactnoentry=Entry(root1,textvariable=contactnovalue)
        Addressentry=Entry(root1,textvariable=Addressvalue)
            #PACKING THE ENTRY
        fullnameentry.grid(row=4,column=2)
        contactnoentry.grid(row=5,column=2)
        Addressentry.grid(row=6,column=2)


        def adddetails():



                # root1.geometry("444x234")
                # width, Height
                # root1.minsize(700,500)
                # root1.maxsize(800,500)
                #title_label = Label(root1, text="Welcome To Bus Booking Service", bg="grey", fg="yellow", padx=4, pady=6,
                                    #font="comicsansms 19 bold", borderwidth=9, relief=GROOVE)
                #title_label.grid(row=8, column=1)
                #photo = PhotoImage(file="img_2.png")
                #y_label = Label(image=photo)
                #y_label.grid(row=9, column=1)
                #middle_label = Label(root1, text="More details", bg="grey", fg="black", padx=9, pady=7,
                                     #font="comicsansms 20 bold")
                #middle_label.grid(row=10, column=1)
                # TEXT FOR OUR FORM
            operatorid = Label(root1, text="Operator Id:", font="comicsansms 8 bold")
            Bustype = Label(root1, text="Bus Type:", font="comicsansms 8 bold")
            From = Label(root1, text="From:", font="comicsansms 8 bold")
            To = Label(root1, text="To:", font="comicsansms 8 bold")
            Date = Label(root1, text="Date:", font="comicsansms 8 bold")
            deptime = Label(root1, text="Dep Time:", font="comicsansms 8 bold")
            arivtime = Label(root1, text="Ariv Time:", font="comicsansms 8 bold")
            Seats = Label(root1, text="Seats:", font="comicsansms 8 bold")
                # PACK TEXT  FOR OUR FORM
            operatorid.grid(row=11, column=1)
            Bustype.grid(row=12, column=1)
            From.grid(row=13, column=1)
            To.grid(row=14, column=1)
            Date.grid(row=15, column=1)
            deptime.grid(row=16, column=1)
            arivtime.grid(row=17, column=1)
            Seats.grid(row=18, column=1)
                # TKINTER VARIABLE FOR SORTING VALUES
            operatoridvalue = StringVar()
            Bustypevalue = StringVar()
            Fromvalue = StringVar()
            Tovalue = StringVar()
            Datevalue = StringVar()
            deptimevalue = StringVar()
            arivtimevalue = StringVar()
            Seatsvalue = StringVar()
                # ENTRIES FOR OUR FORM
            operatoridentry = Entry(root1, textvariable=operatoridvalue)
            Bustypeentry = Entry(root1, textvariable=Bustypevalue)
            Fromentry = Entry(root1, textvariable=Fromvalue)
            Toentry = Entry(root1, textvariable=Tovalue)
            Dateentry = Entry(root1, textvariable=Datevalue)
            deptimeentry = Entry(root1, textvariable=deptimevalue)
            arivtimeentry = Entry(root1, textvariable=arivtimevalue)
            Seatsentry = Entry(root1, textvariable=Seatsvalue)
                # PACKING THE ENTRY
            operatoridentry.grid(row=11, column=2)
            Bustypeentry.grid(row=12, column=2)
            Fromentry.grid(row=13, column=2)
            Toentry.grid(row=14, column=2)
            Dateentry.grid(row=15, column=2)
            deptimeentry.grid(row=16, column=2)
            arivtimeentry.grid(row=17, column=2)
            Seatsentry.grid(row=18, column=2)
            def homepage():
             root1.destroy()
             bus_main()

            Button(root1, text="Save", font="comicsansms 9 bold",command=homepage).grid(row=19, column=1)
        Button(root1,text="ADD DETAILS", font="comicsansms 9 bold",command=adddetails).grid(row=7,column=1)
        root1.mainloop()
    def searchbus():
        root.destroy()
        root2 = Tk()
        root2.geometry("444x234")
            #with, Height
        root2.minsize(700,500)
        root2.maxsize(800,500)
        title_label=Label(root2,text = "Welcome To Bus Booking Service",bg ="grey",fg="yellow",padx=4,pady=6,font="comicsansms 19 bold",borderwidth=9,relief=GROOVE)
        title_label.grid(row=1,column=1)
        photo = PhotoImage(file="img_2.png")
        y_label = Label(image=photo)
        y_label.grid(row=2,column=1)
        middle_label=Label(root2,text="Listing of bus",bg="grey",fg="black",padx=9,pady=7,font="comicsansms 20 bold")
        middle_label.grid(row=3,column=1)
            #TEXT FOR OUR FORM
        def show():
            clicked = StringVar()
            mylabel=Label(root2,text=clicked.get()).grid(row=4,column=1)
            options = [
                    "All Type",
                    "AC Bus",
                    "NON-AC Bus",
                    "Sleeper",
                    "Seater"
                ]
            clicked.set(options[0])
            drop= OptionMenu(root2,clicked,*options).grid(row=4,column=2)
        bustypebutton=Button(root2,command=show).grid(row=4,column=2)
        typeofbus=Label(root2,text="Bus Type:",font="comicsansms 10 bold")
        fromno=Label(root2,text="From:",font="comicsansms 10 bold")
        tono =Label(root2,text="To:",font="comicsansms 10 bold")
        dateno = Label(root2, text="Date:", font="comicsansms 10 bold")
            #PACK TEXT  FOR OUR FORM
        typeofbus.grid(row=4,column=1)
        fromno.grid(row=5,column=1)
        tono.grid(row=6,column=1)
        dateno.grid(row=7, column=1)
            #TKINh==TER VARIABLE FOR SORTING VALUES
            #typesofbusvalue=StringVar()
        fromnovalue=StringVar()
        tonovalue=StringVar()
        datenovalue = StringVar()
            #ENTRIES FOR OUR FORM
            #typesofbusentry=Entry(root2,textvariable=typesofbusvalue)
        fromnoentry=Entry(root2,textvariable=fromnovalue)
        tonoentry=Entry(root2,textvariable=tonovalue)
        datenoentry =Entry(root2,textvariable=datenovalue)
            #PACKING THE ENTRY
            #typesofbusentry.grid(row=4,column=2)
        fromnoentry.grid(row=5,column=2)
        tonoentry.grid(row=6,column=2)
        datenoentry.grid(row=7,column=2)
        def bookingwindow():
                root2.destroy()
                root4 = Tk()
                # widht X height
                root4.geometry("444x234")
                # width, Height
                root4.minsize(700, 500)
                root4.maxsize(800, 500)
                title_label = Label(text="Welcome To Bus Booking Service", bg="grey", fg="yellow", padx=8, pady=22,
                                    font="comicsansms 19 bold", borderwidth=9, relief=GROOVE)
                title_label.grid(row=1, column=1)
                photo = PhotoImage(file="img_2.png")
                y_label = Label(image=photo)
                y_label.grid(row=2, column=1)
                typeofbus = Label(root4, text="Bus Type:", font="comicsansms 10 bold")
                fromno = Label(root4, text="From:", font="comicsansms 10 bold")
                tono = Label(root4, text="To:", font="comicsansms 10 bold")
                dateno = Label(root4, text="Date:", font="comicsansms 10 bold")
                seat= Label(root4,text="Seat Available:",font="comicsansma 10 bold")
                # PACK TEXT  FOR OUR FORM
                typeofbus.grid(row=3, column=1)
                fromno.grid(row=4, column=1)
                tono.grid(row=5, column=1)
                dateno.grid(row=6, column=1)
                seat.grid(row=7,column=1)
                # TKINh==TER VARIABLE FOR SORTING VALUES
                typeofbusvalue=StringVar()
                fromnovalue = StringVar()
                tonovalue = StringVar()
                datenovalue = StringVar()
                # ENTRIES FOR OUR FORM
                typeofbusentry=Entry(root4,textvariable=typeofbusvalue)
                fromnoentry = Entry(root4, textvariable=fromnovalue)
                tonoentry = Entry(root4, textvariable=tonovalue)
                datenoentry = Entry(root4, textvariable=datenovalue)
                # PACKING THE ENTRY
                typeofbusentry.grid(row=3,column=2)
                fromnoentry.grid(row=4, column=2)
                tonoentry.grid(row=5, column=2)
                datenoentry.grid(row=6, column=2)
                def seat():
                    clicked = IntVar()
                    mylabel = Label(root4, text=clicked.get()).grid(row=7, column=2)
                    options = [
                          1,
                          2,
                         3,
                        4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

                    clicked.set(options[0])
                    drop = OptionMenu(root4, clicked, *options).grid(row=7, column=2)

                seatnobutton = Button(root4, command=seat).grid(row=7, column=2)
                def homepage1():
                    root4.destroy()
                    bus_main()
                Button(root4, text="Book", font="comicsansms 9 bold", command=homepage1).grid(row=8, column=1)

                root4.mainloop()

        Button(root2,text="Search", font="comicsansms 12 bold",command=bookingwindow).grid(row=8,column=1)
        def searchhome():
                root2.destroy()
                bus_main()
        Button(root2, text="home", font="comicsansms 12 bold",command=searchhome).grid(row=8, column=0)
        root2.mainloop()
    root = Tk()
            #widht X height
    root.geometry("444x234")
            #width, Height
    root.minsize(700,500)
    root.maxsize(800,500)
    title_label=Label(text="Welcome To Bus Booking Service",bg ="grey",fg="yellow",padx=8,pady=22,font="comicsansms 19 bold",borderwidth=9,relief=GROOVE)
    title_label.pack(fill=X)
    Bottom_label=Label(text="Made by Asmita Porwal(191B078)",bg="grey",fg="blue",padx=10,pady=10,font="comicsansms 8 bold")
    Bottom_label.pack(side=BOTTOM,anchor="center",fill=X)
    x=Frame(root,bg="white",padx=8,pady=10,borderwidth=9,relief=GROOVE)
    x.pack(side=LEFT,anchor="se")
    b1=Button(x,fg="black",text="Add Bus",font="comicsansms 19 bold",command=addbus)
    b1.pack()
    y=Frame(root,bg="white",padx=8,pady=10,borderwidth=9,relief=GROOVE)
    y.pack(side=RIGHT,anchor="sw")
    b2=Button(y,fg="black",text="Search Bus",font="comicsansms 19 bold",command=searchbus)
    b2.pack()
    photo=PhotoImage(file="img_2.png")
    y_label = Label(image=photo)
    y_label.pack()
            #gui logic here
    root.mainloop()

bus_main()
