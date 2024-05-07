import tkinter
from tkinter import Tk, StringVar, ttk, messagebox
import random
from tkinter import *



root = tkinter.Tk()
root.title("KCC ICE CREAM")
root.configure(background="light blue")
root.geometry("2500x800")

Tops = tkinter.Frame(root, width=1200, height=100, bd=12, relief="raise")
Tops.pack(side=tkinter.TOP)
lblTitle = tkinter.Label(Tops, font=('arial', 30, 'bold'), text="      KCC MENU      ")
lblTitle.grid(row=0, column=0)

Bottommainframe = tkinter.Frame(root, width=1200, height=540, bd=12, relief="raise")
Bottommainframe.pack(side=tkinter.BOTTOM)

f1 = tkinter.Frame(Bottommainframe, width=400, height=540, bd=12, relief="raise")
f1.pack(side=tkinter.LEFT)
f2 = tkinter.Frame(Bottommainframe, width=400, height=540, bd=12, relief="raise")
f2.pack(side=tkinter.LEFT)
f3 = tkinter.Frame(Bottommainframe, width=400, height=540, bd=12, relief="raise")
f3.pack(side=tkinter.RIGHT)

f2top = tkinter.Frame(f2, width=400, height=360, bd=12, relief="raise")
f2top.pack(side=tkinter.TOP)
f2bottom = tkinter.Frame(f2, width=400, height=140, bd=12, relief="raise")
f2bottom.pack(side=tkinter.BOTTOM)

canvas = Canvas(root, width = 600, height = 600)
canvas.pack()
img = PhotoImage(file="B:\coding projects\Delicious-ice-cream-cone-clip-art-PNG.ppm")
canvas.create_image(20,20, anchor=NW, image=img)
canvas.place(x=0, y=0)

canvas1 = Canvas(root, width = 400, height = 400)
canvas1.pack()
img1 = PhotoImage(file="B:\coding projects\pngtree-hand-drawn-ice-cream-sundae-vector-illustration-png-image_2695373 (1) [MConverter.eu].ppm")
canvas1.create_image(20,20, anchor=NW, image=img1)
canvas1.place(x=1900, y=0)

var1 = tkinter.IntVar()
var2 = tkinter.IntVar()
var3 = tkinter.IntVar()
var4 = tkinter.IntVar()
var5 = tkinter.IntVar()
var6 = tkinter.IntVar()
var7 = tkinter.IntVar()
var8 = tkinter.IntVar()
var9 = tkinter.IntVar()
var10 = tkinter.IntVar()
var11 = tkinter.IntVar()
var12 = tkinter.IntVar()
var13 = tkinter.IntVar()
var14 = tkinter.IntVar()
var15 = tkinter.IntVar()
var16 = tkinter.IntVar()
var17 = tkinter.IntVar()
var18 = tkinter.IntVar()
var19 = tkinter.IntVar()
var20 = tkinter.IntVar()
var21 = tkinter.IntVar()
var22 = tkinter.IntVar()
var23 = tkinter.IntVar()


var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)


varredvelvet = StringVar()
varoreo = StringVar()
varblackforest = StringVar()
varferrero = StringVar()
varnutty = StringVar()
varcream = StringVar()
varstraw = StringVar()
varlitchee = StringVar()
varbelgium = StringVar()
varcaramel = StringVar()
varchoco = StringVar()
varbrownie = StringVar()
varfrench = StringVar()
varfrench1 = StringVar()
varfrench2 = StringVar()
varfrench3 = StringVar()
varnutella = StringVar()
varstrawberry = StringVar()
varcafe = StringVar()
varfruit = StringVar()
varcreamy = StringVar()
varhot = StringVar()
vardeath = StringVar()
varnut = StringVar()
varchange = StringVar()
vartax = StringVar()
varsubtotal = StringVar()
vartotal = StringVar()
varpayment = StringVar()
Name = StringVar()
Receipt_no = StringVar()




varferrero.set("0")
varnutty.set("0")
varblackforest.set("0")
varredvelvet.set("0")
varoreo.set("0")
varcream.set("0")
varstraw.set("0")
varlitchee.set("0")
varbelgium.set("0")
varcaramel.set("0")
varchoco.set("0")
varbrownie.set("0")
varfrench.set("0")
varfrench1.set("0")
varfrench2.set("0")
varfrench3.set("0")
varnutella.set("0")
varstrawberry.set("0")
varcafe.set("0")
varfruit.set("0")
varcreamy.set("0")
varhot.set("0")
vardeath.set("0")
varnut.set("0")
varchange.set("0")
vartax.set("0")
varsubtotal.set("0")
vartotal.set("0")
varpayment.set("0")



def exit_button():
    button = messagebox.askyesno("KCC STORE", "Do you want to exit?")
    if button > 0:
        root.destroy()
        return


def reset():
    varferrero.set("0")
    varnutty.set("0")
    varblackforest.set("0")
    varredvelvet.set("0")
    varoreo.set("0")
    varcream.set("0")
    varstraw.set("0")
    varlitchee.set("0")
    varbelgium.set("0")
    varcaramel.set("0")
    varchoco.set("0")
    varbrownie.set("0")
    varfrench.set("0")
    varfrench1.set("0")
    varfrench2.set("0")
    varfrench3.set("0")
    varnutella.set("0")
    varstrawberry.set("0")
    varcafe.set("0")
    varfruit.set("0")
    varcreamy.set("0")
    varhot.set("0")
    vardeath.set("0")
    varnut.set("0")
    varchange.set("0")
    vartax.set("0")
    varsubtotal.set("0")
    vartotal.set("0")
    varpayment.set("0")
    #txtferrero.configure(state=tkinter.DISABLED)
    txtbelgium.configure(state=tkinter.DISABLED)
    #txtblackforest.configure(state=tkinter.DISABLED)
    txtbrownie.configure(state=tkinter.DISABLED)
    #txtcafe.configure(state=tkinter.DISABLED)
    txtcaramel.configure(state=tkinter.DISABLED)
    txtchange.configure(state=tkinter.DISABLED)
    txtchoco.configure(state=tkinter.DISABLED)
    #txtcream.configure(state=tkinter.DISABLED)
    #txtcreamy.configure(state=tkinter.DISABLED)
    #txtdeath.configure(state=tkinter.DISABLED)
    txtfrench.configure(state=tkinter.DISABLED)
    txtfrench1.configure(state=tkinter.DISABLED)
    txtfrench2.configure(state=tkinter.DISABLED)
    txtfrench3.configure(state=tkinter.DISABLED)
    #txtfruit.configure(state=tkinter.DISABLED)
    #txthot.configure(state=tkinter.DISABLED)
    #txtlitchee.configure(state=tkinter.DISABLED)
    #txtnut.configure(state=tkinter.DISABLED)
    #txtnutella.configure(state=tkinter.DISABLED)
    #txtnutty.configure(state=tkinter.DISABLED)
    #txtoreo.configure(state=tkinter.DISABLED)
    #txtpayment.configure(state=tkinter.DISABLED)
    #txtredvelvet.configure(state=tkinter.DISABLED)
    #txtstraw.configure(state=tkinter.DISABLED)
    #txtstrawberry.configure(state=tkinter.DISABLED)
    txtsubtotal.configure(state=tkinter.DISABLED)
    txttax.configure(state=tkinter.DISABLED)
    txttotal.configure(state=tkinter.DISABLED)



def chkbelgium():
    if var9.get() == 1:
        txtbelgium.configure(state=tkinter.NORMAL)
        varbelgium.set("")
    elif var9.get() == 0:
        txtbelgium.configure(state=tkinter.DISABLED)
        varbelgium.set("0")


def chkcaramel():
    if var10.get() == 1:
        txtcaramel.configure(state=tkinter.NORMAL)
        varcaramel.set("")
    elif var10.get() == 0:
        txtcaramel.configure(state=tkinter.DISABLED)
        varcaramel.set("0")


def chkchoco():
    if var11.get() == 1:
        txtchoco.configure(state=tkinter.NORMAL)
        varchoco.set("")
    elif var11.get() == 0:
        txtchoco.configure(state=tkinter.DISABLED)
        varchoco.set("0")


def chkbrownie():
    if var12.get() == 1:
        txtbrownie.configure(state=tkinter.NORMAL)
        varbrownie.set("")
    elif var12.get() == 0:
        txtbrownie.configure(state=tkinter.DISABLED)
        varbrownie.set("0")


def chkfrench():
    if var13.get() == 1:
        txtfrench.configure(state=tkinter.NORMAL)
        varfrench.set("")
    elif var13.get() == 0:
        txtfrench.configure(state=tkinter.DISABLED)
        varfrench.set("0")

def chkfrench1():
    if var13.get() == 1:
        txtfrench1.configure(state=tkinter.NORMAL)
        varfrench1.set("")
    elif var13.get() == 0:
        txtfrench1.configure(state=tkinter.DISABLED)
        varfrench1.set("0")

def chkfrench2():
    if var13.get() == 1:
        txtfrench2.configure(state=tkinter.NORMAL)
        varfrench2.set("")
    elif var13.get() == 0:
        txtfrench2.configure(state=tkinter.DISABLED)
        varfrench2.set("0")

def chkfrench3():
    if var13.get() == 1:
        txtfrench3.configure(state=tkinter.NORMAL)
        varfrench3.set("")
    elif var13.get() == 0:
        txtfrench3.configure(state=tkinter.DISABLED)
        varfrench3.set("0")


def costofmeal():
    m1 = float(varstraw.get())
    m2 = float(varbelgium.get())
    m3 = float(varblackforest.get())
    m4 = float(varbrownie.get())
    m5 = float(varcream.get())
    m6 = float(varcafe.get())
    m7 = float(varcaramel.get())
    m8 = float(varchoco.get())
    m9 = float(varcreamy.get())
    m10 = float(vardeath.get())
    m11 = float(varferrero.get())
    m12 = float(varfrench.get() + varfrench1.get() + varfrench2.get() + varfrench3.get())
    m13 = float(varfruit.get())
    m14 = float(varhot.get())
    m15 = float(varlitchee.get())
    m16 = float(varnut.get())
    m17 = float(varnutella.get())
    m18 = float(varnutty.get())
    m19 = float(varoreo.get())
    m20 = float(varredvelvet.get())
    m21 = float(varstrawberry.get())

    t1 = (m1*139)+(m2*79)+(m3*550)+(m4*75)+(m5*119)+(m6*199)+(m7*70)+(m8*70)+(m9*179)+(m10*175)+(m21*179)
    t2 = (m11*799)+(m12*60)+(m13*179)+(m14*150)+(m15*139)+(m16*199)+(m17*199)+(m18*699)+(m19*550)+(m20*650)

    cost = (t1 + t2)
    tax = (cost * 18)/100
    vartotal.set(cost + tax)
    vartax.set(tax)

    if (txtpayment.get() == "Cash"):
        change = float(txtpayment.get())
        cost = (t1 + t2)
        tax = (cost * 3.4) / 100
        tax2 = "Rs", str('%.2f'%(tax))
        vartax.set(tax2)

        cost2 = "Rs", str('%.2f'%(cost))
        varsubtotal.set(cost2)
        total2 = "Rs", str('%.2f'%(cost + tax))
        vartotal.set(total2)
        change2 = (change - (cost + tax))
        change3 = "Rs", str('%.2f'%(change2))
        varchange.set(change3)

    elif(txtpayment.get() == "MasterCard" or "DebitCard" or "VisaCard"):
        varpayment.set(" ")
        cost = (t1 + t2)
        tax = (cost * 3.4) / 100
        tax2 = "Rs", str('%.2f' % (tax))
        vartax.set(tax2)

        cost2 = "Rs", str('%.2f' % (cost))
        varsubtotal.set(cost2)
        total2 = "Rs", str('%.1f' % (cost + tax))
        vartotal.set(total2)
        varchange.set(" ")



#################################################  Frame1  ###########################################################

Lname = tkinter.Label(f1, text = "Customer Name: ", font=('arial', 12, 'bold'))
Lname.grid(row=0, column=0, padx=2, pady=2, sticky='w')
Ename = tkinter.Entry(f1, textvariable=Name, font=('arial', 12, 'bold'), width=18)
Ename.place(x=180, y=5)


Lreceipt = tkinter.Label(f1, text="Receipt No:  ", font=('arial', 12, 'bold'))
Lreceipt.grid(row=1, column=0,padx=2, pady=2, sticky='w')
Ereceipt = tkinter.Entry(f1, textvariable=Receipt_no, font=('arial', 12, 'bold'), width=18)
Ereceipt.place(x=180, y=32)
Receipt_no.set(random.randint(0, 1000))


lblIcecake = tkinter.Label(f1, font=('comic sans MS', 18, 'bold'), text="Dine In or Carry Out")
lblIcecake.grid(row=3, column=0, padx=2, pady=2, sticky='w')

btnDinein = tkinter.Button(f1,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Dine In').grid(row=5,column=0)

btnCarryout = tkinter.Button(f1,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Carry Out').grid(row=6,column=0)

###################################################### Frame2  ##################################################################################

lblIcecake = tkinter.Label(f2top, font=('comic sans MS', 18, 'bold'), text="SIMPLY DELICIOUS TOPPINGS")
lblIcecake.grid(row=0, column=0)

belgium = tkinter.Checkbutton(f2top, text="Nuts\t\t79", variable=var9, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkbelgium).grid(row=1, column=0)
txtbelgium = tkinter.Entry(f2top, font=('arial', 12), textvariable=varbelgium, width=6, justify='left', state=tkinter.DISABLED)
txtbelgium.grid(row=1, column=1)

caramel = tkinter.Checkbutton(f2top, text="Chocolate\t\t\t70", variable=var10, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkcaramel).grid(row=2, column=0)
txtcaramel = tkinter.Entry(f2top, font=('arial', 12), textvariable=varcaramel, width=6, justify='left', state=tkinter.DISABLED)
txtcaramel.grid(row=2, column=1)

choco = tkinter.Checkbutton(f2top, text="Strawb and pine syrup\t\t\t70", variable=var11, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkchoco).grid(row=3, column=0)
txtchoco = tkinter.Entry(f2top, font=('arial', 12), textvariable=varchoco, width=6, justify='left', state=tkinter.DISABLED)
txtchoco.grid(row=3, column=1)

brownie = tkinter.Checkbutton(f2top, text="Whipped creaam\t\t\t75", variable=var12, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkbrownie).grid(row=4, column=0)
txtbrownie = tkinter.Entry(f2top, font=('arial', 12), textvariable=varbrownie, width=6, justify='left', state=tkinter.DISABLED)
txtbrownie.grid(row=4, column=1)

french = tkinter.Checkbutton(f2top, text="Sprinkles\t\t\t60", variable=var13, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkfrench).grid(row=5, column=0)
txtfrench = tkinter.Entry(f2top, font=('arial', 12), textvariable=varfrench, width=6, justify='left', state=tkinter.DISABLED)
txtfrench.grid(row=5, column=1)

french1 = tkinter.Checkbutton(f2top, text="Sugar cookies\t\t\t60", variable=var13, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkfrench).grid(row=6, column=0)
txtfrench1 = tkinter.Entry(f2top, font=('arial', 12), textvariable=varfrench1, width=6, justify='left', state=tkinter.DISABLED)
txtfrench1.grid(row=6, column=1)

french2 = tkinter.Checkbutton(f2top, text="Bananas\t\t\t60", variable=var13, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkfrench).grid(row=7, column=0)
txtfrench2 = tkinter.Entry(f2top, font=('arial', 12), textvariable=varfrench2, width=6, justify='left', state=tkinter.DISABLED)
txtfrench2.grid(row=7, column=1)

french3 = tkinter.Checkbutton(f2top, text="A cherry\t\t\t60", variable=var13, onvalue=1, offvalue=0,
                            font=('Microsoft New Tai Lue', 12), command=chkfrench).grid(row=8, column=0)
txtfrench3 = tkinter.Entry(f2top, font=('arial', 12), textvariable=varfrench3, width=6, justify='left', state=tkinter.DISABLED)
txtfrench3.grid(row=8, column=1)
#################################################3    Frame 2 bottom  ###########################################################################

lblPayment = tkinter.Label(f2bottom, font=('arial', 14, 'bold'), text="PAYMENT METHOD", bd=10, width=16, anchor='w')
lblPayment.grid(row=0, column=0)

lblchange = tkinter.Label(f2bottom, font=('arial', 18, 'bold'), text="Change   ", bd=10, anchor='w')
lblchange.grid(row=0, column=1)
txtchange = tkinter.Entry(f2bottom, font=('arial', 14, 'bold'), textvariable=varchange, width=10, justify='left', state=tkinter.DISABLED)
txtchange.grid(row=0, column=2)

cmbPayment = ttk.Combobox(f2bottom, textvariable = var22, state='readonly', font=('arial', 10, 'bold'), width=20)
cmbPayment['value'] = ('Cash','MasterCard', 'DebitCard', 'VisaCard')
cmbPayment.current(0)
cmbPayment.grid(row=1, column=0)

lbltax = tkinter.Label(f2bottom, font=('arial', 18, 'bold'), text="Tax   ", bd=10, anchor='w')
lbltax.grid(row=1, column=1)
txttax = tkinter.Entry(f2bottom, font=('arial', 14, 'bold'), textvariable=vartax, width=10, justify='left', state=tkinter.DISABLED)
txttax.grid(row=1, column=2)

txtpayment = tkinter.Entry(f2bottom, font=('arial', 12, 'bold'), textvariable=varpayment, width=6, justify='left', state=tkinter.DISABLED)
txtpayment.grid(row=2, column=0)
lblsubtotal = tkinter.Label(f2bottom, font=('arial', 14, 'bold'), text="Subtotal   ", bd=10, anchor='w')
lblsubtotal.grid(row=2, column=1)
txtsubtotal = tkinter.Entry(f2bottom, font=('arial', 14, 'bold'), textvariable=varsubtotal, width=10, justify='left',
                            state=tkinter.DISABLED)
txtsubtotal.grid(row=2, column=2)

lbltotal = tkinter.Label(f2bottom, font=('arial', 14, 'bold'), text="Total   ", bd=10, anchor='w')
lbltotal.grid(row=3, column=1)
txttotal = tkinter.Entry(f2bottom, font=('arial', 14, 'bold'), textvariable=vartotal, width=10, justify='left',
                         state=tkinter.DISABLED)
txttotal.grid(row=3, column=2)



########################################################   Frame 3     ##########################################################################

lblIcecake = tkinter.Label(f3, font=('comic sans MS', 18, 'bold'), text="Soops")
lblIcecake.grid(row=0, column=0)

btnonescoop = tkinter.Button(f3,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='1 scoop').grid(row=1,column=0)

btntwoscoop = tkinter.Button(f3,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='2 scoops').grid(row=2,column=0)

btnthreescoop = tkinter.Button(f3,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='3 scoops').grid(row=3,column=0)


############################################################ Button  ######################################################################
btntotal = tkinter.Button(f2bottom, padx=16, pady=1, bd=4, fg='black', font=('arial',16,'bold'), width=5, text='Total', command = costofmeal)\
    .grid(row=5, column=0)


btnreset = tkinter.Button(f2bottom,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Reset',
                          command=reset).grid(row=5,column=1)

btnexit = tkinter.Button(f2bottom,padx=16,pady=1,bd=4,fg='black',font=('arial',16,'bold'),width=5,text='Exit',
                          command=lambda: exit_button()).grid(row=5,column=2)

lblspace=tkinter.Label(f2bottom,text='\n\n\n\n\n\n\n\n\n')
lblspace.grid(row=5,column=0)
root.mainloop()