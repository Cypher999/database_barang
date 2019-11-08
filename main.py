import xml.dom.minidom as mndom
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import datetime as waktu
from threading import Timer
import barang as brg
import suplier as sup
import jual as jl
import beli as bl

class bantu:
    def __init__(this):
        this.win=Tk()
        this.Lb_kd=Label(this.win,text="Pilih menu pada menu bar")
        this.Lb_kd.grid(column=0,row=0)
        this.win.mainloop()

class tentang:
    def __init__(this):
        this.win=Tk()
        this.Lb_kd=Label(this.win,text="Program data barang")
        this.Lb_ke=Label(this.win,text="Bahasa PYTHON")
        this.Lb_kf=Label(this.win,text="versi Beta")
        this.Lb_kd.grid(column=0,row=0)
        this.Lb_ke.grid(column=0,row=1)
        this.Lb_kf.grid(column=0,row=2)
        this.win.mainloop()


win=Tk()
win.title('Data Barang')
mn=Menu(win)
item_baru=Menu(mn,tearoff=0)
bantuan=Menu(mn,tearoff=0)
item_baru.add_command(label='Barang',command=brg.barang)
item_baru.add_separator()
item_baru.add_command(label='Suplier',command=sup.suplier)
item_baru.add_separator()
item_baru.add_command(label='Penjualan',command=jl.jual)
item_baru.add_separator()
item_baru.add_command(label='Pembelian',command=bl.beli)
item_baru.add_separator()
bantuan.add_command(label='Help',command=bantu)
bantuan.add_command(label='tentang',command=tentang)
mn.add_cascade(label='File',menu=item_baru)
mn.add_cascade(label='Bantuan',menu=bantuan)
win.config(menu=mn)
win.mainloop()
	
