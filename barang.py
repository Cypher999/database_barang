import xml.dom.minidom as mndom
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import datetime as waktu
from threading import Timer
class barang:
    def __init__(this):
        this.win=Tk()
        this.Lb_kd=Label(this.win,text="Kode Barang")
        this.Lb_nm=Label(this.win,text="Nama Barang")
        this.Lb_hr=Label(this.win,text="Harga")
        this.Lb_st=Label(this.win,text="Stok")
        this.tx_kd=Entry(this.win,text="")
        this.tx_nm=Entry(this.win,text="")
        this.tx_hr=Entry(this.win,text="")
        this.tx_st=Entry(this.win,text="")
        this.bt_sm=Button(this.win,text="Simpan",command=this.simpan)
        this.bt_ed=Button(this.win,text="Edit",command=this.edit)
        this.bt_hp=Button(this.win,text="Hapus",command=this.hapus)
        this.bt_btl=Button(this.win,text="Batal",command=this.batal)
        this.bt_kl=Button(this.win,text="Keluar",command=this.win.destroy)
        this.bt_dt=Button(this.win,text="Lihat data",command=this.isi_tabel)
        this.Lb_kd.grid(column=0,row=0)
        this.Lb_nm.grid(column=0,row=1)
        this.Lb_hr.grid(column=0,row=2)
        this.Lb_st.grid(column=0,row=3)
        this.tx_kd.grid(column=1,row=0)
        this.tx_nm.grid(column=1,row=1)
        this.tx_hr.grid(column=1,row=2)
        this.tx_st.grid(column=1,row=3)
        this.bt_sm.grid(column=0,row=4)
        this.bt_ed.grid(column=1,row=4)
        this.bt_hp.grid(column=0,row=5)
        this.bt_kl.grid(column=1,row=5)
        this.bt_btl.grid(column=0,row=6)
        this.bt_dt.grid(column=1,row=6)
        this.tx_kd.bind('<Return>',this.cari)
        this.awal()
   
        this.win.mainloop()
    def isi_tabel(this):
        this.win_isi=Tk()
        i=1;
        this.th_kd=Label(this.win_isi,text="Kode Barang",borderwidth=6,relief="groove")
        this.th_nm=Label(this.win_isi,text="Nama Barang",borderwidth=6,relief="groove")
        this.th_hr=Label(this.win_isi,text="Harga",borderwidth=6,relief="groove")
        this.th_st=Label(this.win_isi,text="Stok",borderwidth=6,relief="groove")
        this.th_kd.grid(column=0,row=0)
        this.th_nm.grid(column=1,row=0)
        this.th_hr.grid(column=2,row=0)
        this.th_st.grid(column=3,row=0)
        this.dok=mndom.parse("dbbrg.xml")
        this.isi_tr=this.dok.getElementsByTagName("barang")
        for this.tr in this.isi_tr:
            this.tr_kd=Label(this.win_isi)
            this.tr_nm=Label(this.win_isi)
            this.tr_hr=Label(this.win_isi)
            this.tr_st=Label(this.win_isi)
            this.tr_kd.configure(text="")
            this.tr_nm.configure(text="")
            this.tr_hr.configure(text="")
            this.tr_kd.configure(text=this.tr.getAttribute("kd_brg"))
            this.tr_nm.configure(text=this.tr.getAttribute("nm_brg"))
            this.tr_hr.configure(text=this.tr.getAttribute("hrg"))
            this.tr_st.configure(text=this.tr.getAttribute("stok"))
            this.tr_kd.grid(column=0,row=i)
            this.tr_nm.grid(column=1,row=i)
            this.tr_hr.grid(column=2,row=i)
            this.tr_st.grid(column=3,row=i)
            i=i+1
        this.win_isi.mainloop()
    def simpan(this):
        this.dok=mndom.parse("dbbrg.xml")
        this.tabel=this.dok.createElement("barang")
        if(this.tx_kd.get()=='')or(this.tx_nm.get()=='')or(this.tx_hr.get()==''):
            messagebox.showinfo("Pesan","Data Tidak Lengkap")
        else :
            this.tabel.setAttribute("kd_brg",this.tx_kd.get())
            this.tabel.setAttribute("nm_brg",this.tx_nm.get())
            this.tabel.setAttribute("hrg",this.tx_hr.get())
            this.tabel.setAttribute("stok",this.tx_st.get())
            this.dok.getElementsByTagName("dbbrg")[0].appendChild(this.tabel);
            this.file_xml=open("dbbrg.xml","w")
            this.dok.writexml(this.file_xml);
            this.file_xml.close()
            this.bersih()
    def edit(this):
        i=0
        ada=0
        i_h=''
        this.dok=mndom.parse("dbbrg.xml")
        this.tx_kd.configure(state=NORMAL)
        this.isi_kd=this.tx_kd.get()
        this.isi_rek=this.dok.getElementsByTagName("barang")
        for this.isi in this.isi_rek:
            if(this.isi_kd==this.isi.getAttribute("kd_brg")):
                ada=1
                i_h=i
            i=i+1
        if(ada==1):
            if((this.tx_nm.get()=='')or(this.tx_hr.get()=='')):
                messagebox.showinfo("pesan","data tidak lengkap")
            else:
                this.dok.getElementsByTagName("barang")[i_h].setAttribute("nm_brg",this.tx_nm.get())
                this.dok.getElementsByTagName("barang")[i_h].setAttribute("hrg",this.tx_hr.get())
                this.dok.getElementsByTagName("barang")[i_h].setAttribute("stok",this.tx_st.get())
                
                this.file_xml=open("dbbrg.xml","w")
                this.dok.writexml(this.file_xml)
                this.file_xml.close()
                this.bersih()
                this.awal()
        
    def hapus(this):
        i=0
        i_h=''
        ada=0
        this.dok=mndom.parse("dbbrg.xml")
        this.tx_kd.configure(state=NORMAL)
        this.cr=this.tx_kd.get()
        this.isi_tbl=this.dok.getElementsByTagName("barang")
        for this.isi in this.isi_tbl:
            if(this.cr==this.isi.getAttribute("kd_brg")):
                i_h=i
                ada=1
            i=i+1
        if(ada==1):
            hps=this.dok.getElementsByTagName("barang")[i_h]
            this.dok.documentElement.removeChild(hps)
            this.file_xml=open("dbbrg.xml","w")
            this.dok.writexml(this.file_xml)
            this.file_xml.close()
            this.bersih()
        
            this.awal()
            
    def cari(this,aaa):
        i=0;
        i_h='';
        ada=0;
        this.cr=this.tx_kd.get()
        this.dok=mndom.parse("dbbrg.xml")
        this.isi=this.dok.getElementsByTagName("barang")
        for this.hasil in this.isi:
            if(this.cr==this.hasil.getAttribute("kd_brg")):
              ada=1
              i_h=i
            i=i+1
        if(ada==1):
            if(this.tx_nm.get()!='')or(this.tx_hr.get()!=''):
                this.tx_nm.delete(0, END)
                this.tx_hr.delete(0, END)
            this.tx_nm.insert(INSERT,this.dok.getElementsByTagName("barang")[i_h].getAttribute("nm_brg"))
            this.tx_hr.insert(INSERT,this.dok.getElementsByTagName("barang")[i_h].getAttribute("hrg"))
            this.tx_st.insert(INSERT,this.dok.getElementsByTagName("barang")[i_h].getAttribute("stok"))
            this.tx_nm.focus()
            this.ada()
        else:
            this.tx_nm.focus()
    def awal(this):
        this.bt_sm.configure(state=NORMAL)
        this.bt_ed.configure(state=DISABLED)
        this.bt_hp.configure(state=DISABLED)
        this.bt_btl.configure(state=DISABLED)
        this.bt_kl.configure(state=NORMAL)
    def ada(this):
        this.tx_kd.configure(state=DISABLED)
        this.bt_sm.configure(state=DISABLED)
        this.bt_ed.configure(state=NORMAL)
        this.bt_hp.configure(state=NORMAL)
        this.bt_btl.configure(state=NORMAL)
        this.bt_kl.configure(state=DISABLED)
    def batal(this):
        this.bersih()
        this.awal()
    def bersih(this):
        this.tx_kd.configure(state=NORMAL)
        this.tx_kd.delete(0, END)
        this.tx_nm.delete(0, END)
        this.tx_hr.delete(0, END)
        this.tx_st.delete(0, END)
