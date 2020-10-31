from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
win =Tk()
win.title("PENSION CALCULATOR")
win.geometry("1680x800")
win.iconphoto(True, PhotoImage(file='logo.png'))
tabbase = "#66c4de"
extra = "#5e5e5e"
backg = "#111112"
tabselect = "#2351a1"
s = ttk.Style()

s.theme_create( "project", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [0, 5, 5, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5,1], "background": tabbase },
            "map":       {"background": [("selected", tabselect)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

s.theme_use("project")
s.configure("TNotebook", background=extra, borderwidth=0)
s.configure("TFrame", background=backg, foreground=extra, borderwidth=0)
# s.configure("tab1", background=backg1, foreground=extra, borderwidth=0)

s.configure('TNotebook.Tab', font=('URW Gothic L','18','bold'), padding=15)
tabs = ttk.Notebook(win, width = 1480, height = 710)
tabs.place(x = 25, y = 25)
tabs.pack(fill=BOTH, expand=1)

tab1 = ttk.Frame(tabs, width = 50, height = 50)
tab2 = ttk.Frame(tabs, width = 50, height = 50)
tab3 = ttk.Frame(tabs, width = 50, height = 50)
tab4 = ttk.Frame(tabs, width = 50, height = 50)
tab5 = ttk.Frame(tabs, width = 50, height = 50)

tabs.add(tab1, text = "HOME")
tabs.add(tab2, text = "PENSION")
tabs.add(tab3, text = "COMMUTATION")
tabs.add(tab4, text = "GRATUITY")
tabs.add(tab5, text = "C_FACTOR")

img1 = ImageTk.PhotoImage(file="background.jpg")
Label(tab1, image=img1).place(x=0, y=0)

img5 = ImageTk.PhotoImage(file="imaget5.jpeg")
Label(tab5, image=img5).place(x=65, y=0)



class Home:
	def __init__(self):
		Label(tab1, text="TO KNOW YOUR COMMUTATION FACTOR", font=("Arial Bold", 16), bg="#111112", fg="white").place(x=1100, y=320)
		btClickHere = Button(tab1, text = "CLICK HERE",command=self.ClickHere, bg="yellow", fg="black", width=19, height=2, font=("Arial Bold", 10)).place(x=1230,y=370)
	def ClickHere(self):
		tabs.select(4)
Home()

		
		
class GratuityCalculator:
    def __init__(self): 
        readOnlyText = Text(tab4)


        CheckVar1 = IntVar()
        Checkbutton(tab4, text = "Award Staff",variable = CheckVar1,onvalue = 1, offvalue=0, font=("Arial Bold", 20), bg="#111112", fg="white").place(x=800, y=50)
        Checkbutton(tab4, text = "Officer", variable = CheckVar1, onvalue = 0, offvalue =1, font=("Arial Bold", 20), bg="#111112", fg="white").place(x=1000, y=50)
        Label(tab4, text = "THE POSITION YOU HOLD? ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=250, y=50)
        Label(tab4, text = "Basic Pay ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250,y=100)
        Label(tab4, text = "Dearness Allowance (D.A) ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250, y=150)
        Label(tab4, text = "Personal Allowance ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250, y=200) 
        Label(tab4, text = "Acting Allowance ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250, y=250)
        Label(tab4, text = "Fixed Personal Allowance (F.P.A) ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250, y=300)
        Label(tab4, text = "Professional Qualification Pay (P.Q.P) ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250, y=350)
        Label(tab4, text = "WAGES ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250, y=400)
        Label(tab4, text = "Years Of Service ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250, y=450)
        Label(tab4, text = "GRATUITY ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=250, y=500)


        self.basicVar = StringVar()  
        Entry(tab4, textvariable = self.basicVar, 
                     justify = LEFT, font=("Arial Bold", 19)).place(x=850,y=100)

        self.dearnessVar = StringVar() 
        Entry(tab4, textvariable = self.dearnessVar, 
                 justify = LEFT, font=("Arial Bold", 19)).place(x=850,y=150)

        self.personalVar = StringVar() 
        Entry(tab4, textvariable = self.personalVar, 
              justify = LEFT, font=("Arial Bold", 19)).place(x=850,y=200)

        self.actingVar = StringVar() 
        Entry(tab4, textvariable = self.actingVar, 
              justify = LEFT, font=("Arial Bold", 19)).place(x=850,y=250)

        self.fixedVar = StringVar() 
        Entry(tab4, textvariable = self.fixedVar, 
              justify = LEFT, font=("Arial Bold", 19)).place(x=850,y=300)

        self.professionalVar = StringVar() 
        Entry(tab4, textvariable = self.professionalVar, 
              justify = LEFT, font=("Arial Bold", 19)).place(x=850,y=350)

        self.wagesVar = StringVar() 
        lblWages = Label(tab4, textvariable = 
                           self.wagesVar, font=("Arial Bold", 19)).place(x=850,y=400)

        self.yearsVar = StringVar() 
        Entry(tab4, textvariable = self.yearsVar, 
              justify = LEFT, font=("Arial Bold", 19)).place(x=850,y=450)

        self.gratuityVar = StringVar() 
        lblGratuity = Label(tab4, textvariable = 
                           self.gratuityVar, font=("Arial Bold", 19)).place(x=850,y=500)

        btCalculateGratuity = Button(tab4, text = "CALCULATE GRATUITY", 
                                  command = self.CalculateGratuity, bg="#2351a1", fg="black", width=19, height=2, font=("Arial Bold", 15)).place(x=560,y=550)
    

    def CalculateGratuity(self):
        wages = self.getWages( 
        float(self.basicVar.get()), 
        float(self.dearnessVar.get()), 
        float(self.personalVar.get()),
        float(self.actingVar.get()),
        float(self.fixedVar.get()),
        float(self.professionalVar.get()))

        self.wagesVar.set(format(wages, '10.2f'))

        gratuity = float(self.wagesVar.get()) * 15 * int(self.yearsVar.get()) / 26
        self.gratuityVar.set(format(gratuity, '10.2f')) 

    def getWages(self, basic, dearness, personal, acting, fixed, professional):
        wages = basic + dearness + personal + acting + fixed + professional

        return wages; 

GratuityCalculator()





class CommutationCalculator:
    def __init__(self): 
        readOnlyText = Text(win)

        Label(tab3, text = "Basic Pension ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=250, y=130)
        Label(tab3, text = "Age By Next Birthday ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=250, y=190)
        Label(tab3, text = "Commutation Factor ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=250, y=250)
        Label(tab3, text = "COMMUTATION ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=250, y=310)
        Label(tab3, text = "Total Pension ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=250, y=370)
        Label(tab3, text = "FINAL PENSION AFTER COMMUTATION ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=250, y=430)

        self.basicVar = StringVar()  
        Entry(tab3, textvariable = self.basicVar, 
                     justify = LEFT, font=("Arial Bold", 20)).place(x=850,y=130)

        self.ageVar = StringVar() 
        Entry(tab3, textvariable = self.ageVar, 
                 justify = LEFT, font=("Arial Bold", 20)).place(x=850,y=190)

        self.factorVar = StringVar() 
        Entry(tab3, textvariable = self.factorVar, 
                 justify = LEFT, font=("Arial Bold", 20)).place(x=850,y=250)

        self.commutationVar = StringVar() 
        lblCommutation = Label(tab3, textvariable = 
                           self.commutationVar, font=("Arial Bold", 20)).place(x=850,y=310)

        self.totalVar = StringVar() 
        Entry(tab3, textvariable = self.totalVar, 
              justify = LEFT, font=("Arial Bold", 20)).place(x=850,y=370)   

        self.finalVar = StringVar() 
        lblFinal = Label(tab3, textvariable = 
                           self.finalVar, font=("Arial Bold", 20)).place(x=850,y=430)

        btCalculateCommutation = Button(tab3, text = "CALCULATE COMMUTATION", 
                                  command = self.CalculateCommutation, bg="#2351a1", fg="black", width=23, height=2, font=("Arial Bold", 15)).place(x=600,y=500)
        
    def CalculateCommutation(self):
        commutation = self.getCommutation( 
        float(self.basicVar.get()), 
        float(self.factorVar.get()))
        self.commutationVar.set(format(commutation, '10.2f'))

        final = float(self.totalVar.get()) - float(self.commutationVar.get())
        self.finalVar.set(format(final, '10.2f')) 

    def getCommutation(self, basic, factor):
        commutation = basic + factor * 12 
        return commutation; 
        root = Tk()

CommutationCalculator()




class PensionCalculator:
    def __init__(self):
        readOnlyText = Text(tab2)
        Label(tab2, text="Enter MONTH Of JOINING ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=50, y=50)
        Label(tab2, text="Enter YEAR Of JOINING ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=800, y=50)
        Label(tab2, text="Enter MONTH Of RETIREMENT ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=50, y=110)
        Label(tab2, text="Enter YEAR Of RETIREMENT ", font=("Arial Bold", 19), bg="#111112", fg="white").place(x=800, y=110)
        Label(tab2, text="Total Pensionable Service (IN MONTHS) ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=150, y=170)
        Label(tab2, text="Basic Pay ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=150, y=230)
        Label(tab2, text="Dearness Allowance (D.A) ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=150, y=290)
        Label(tab2, text="Fixed Personal Allowance (F.P.A) ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=150, y=350)
        Label(tab2, text="Professional Qualification Pay (P.Q.A) ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=150, y=410)
        Label(tab2, text="TOTAL PENSION ", font=("Arial Bold", 20), bg="#111112", fg="white").place(x=150, y=470)
        self.monthjoiningVar = StringVar()
        Entry(tab2, textvariable=self.monthjoiningVar,
              justify=LEFT, font=("Arial Bold", 19)).place(x=450, y=50)

        self.yearjoiningVar = StringVar()
        Entry(tab2, textvariable=self.yearjoiningVar,
              justify=LEFT, font=("Arial Bold", 19)).place(x=1200, y=50)

        self.monthretirementVar = StringVar()
        Entry(tab2, textvariable=self.monthretirementVar,
              justify=LEFT, font=("Arial Bold", 19)).place(x=450, y=110)

        self.yearretirementVar = StringVar()
        Entry(tab2, textvariable=self.yearretirementVar,
              justify=LEFT, font=("Arial Bold", 19)).place(x=1200, y=110)

        self.totalserviceVar = StringVar()
        lblService = Label(tab2, textvariable=
        self.totalserviceVar, font=("Arial Bold", 20)).place(x=850, y=170)

        self.basicpayVar = StringVar()
        Entry(tab2, textvariable=self.basicpayVar,
              justify=LEFT, font=("Arial Bold", 20)).place(x=850, y=230)

        self.dapayVar = StringVar()
        Entry(tab2, textvariable=self.dapayVar,
              justify=LEFT, font=("Arial Bold", 20)).place(x=850, y=290)

        self.fpapayVar = StringVar()
        Entry(tab2, textvariable=self.fpapayVar,
              justify=LEFT, font=("Arial Bold", 20)).place(x=850, y=350)

        self.pqapayVar = StringVar()
        Entry(tab2, textvariable=self.pqapayVar,
              justify=LEFT, font=("Arial Bold", 20)).place(x=850, y=410)

        self.totalpensionVar = StringVar()
        lblTotalpension = Label(tab2, textvariable=
        self.totalpensionVar, font=("Arial Bold", 20)).place(x=850, y=470)

        global basicpension
        self.basicpension = StringVar()
        global basicpensiona
        self.basicpensiona = StringVar()
        global basicpensionb
        self.basicpensionb = StringVar()
     
        btCalculatePension = Button(tab2, text="CALCULATE PENSION",
                                    command=self.btCalculatePension, bg="#2351a1",
                                    fg="black", width=18, height=2, font=("Arial Bold", 15)).place(x=600,y=540)
        win.mainloop()

    def btCalculatePension(self):
        totalservice = self.getTotalservice(
            int(self.monthjoiningVar.get()),
            int(self.yearjoiningVar.get()),
            int(self.monthretirementVar.get()),
            int(self.yearretirementVar.get()))
        self.totalserviceVar.set(format(totalservice, '3'))

        totalpension = self.getTotalpension(
            int(self.dapayVar.get()),
            int(self.basicpayVar.get()))
        self.totalpensionVar.set(format(totalpension, '5'))

        (self.basicpensiona) = int(self.basicpayVar) * int(self.totalserviceVar) / (60 * 12)
        if self.basicpayVar < 51490:
            self.basicpensionb = ((50 * self.basicpayVar / 100) + (self.fpapayVar.get() / 2) + (self.pqapayVar / 2))
        else:
            self.basicpensionb = ((40 * self.basicpayVar) / 100) + (self.fpapayVar.get() / 2) + (self.pqapayVar / 2)

        if self.basicpensiona < self.basicpensionb:
            self.basicpension = self.basicpensiona
        else:
            self.basicpension = self.basicpensionb
        return self.basicpension

    def getTotalpension(self, dapay, basicpension):
        totalpension = (basicpension + ((52.7 * dapay) / 100))
        return totalpension

    def getTotalservice(self, monthjoining, yearjoining, monthretirement, yearretirement):
        totalservice = (yearretirement - yearjoining) * 12 + (monthretirement - monthjoining)
        return totalservice



PensionCalculator()