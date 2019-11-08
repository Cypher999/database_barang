import xml.dom.minidom as mndom
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import datetime as waktu
from threading import Timer

class beli:
    def daftar(this):
        i=1
        this.win_df=Tk()
        this.dok=mndom.parse("dbbrg.xml")
        this.tr_no=Label(this.win_df,text="No. Beli",borderwidth=2,relief="groove")
        this.tr_sup=Label(this.win_df,text="Nama Suplier",borderwidth=2,relief="groove")
        this.tr_nm=Label(this.win_df,text="Nama Barang",borderwidth=2,relief="groove")
        this.tr_hrg=Label(this.win_df,text="Harga",borderwidth=2,relief="groove")
        this.tr_jm=Label(this.win_df,text="Jumlah Pesanan",borderwidth=2,relief="groove")
        this.tr_tot=Label(this.win_df,text="Total Bayar",borderwidth=2,relief="groove")
        this.tr_tgl=Label(this.win_df,text="Tanggal Pemesanan",borderwidth=2,relief="groove")
        this.tabel=this.dok.getElementsByTagName("beli")
        for this.tb in this.tabel:
            j=0
            j_h=''
            k=0
            k_h=''
            this.td_no=Label(this.win_df,text=this.tb.getAttribute("no_beli"))
            kode_barang=this.tb.getAttribute("kd_brg")
            isi_barang=this.dok.getElementsByTagName("barang")
            for isi_br in isi_barang:
                if(isi_br.getAttribute("kd_brg")==kode_barang):
                    j_h=j
                j=j+1
            kode_sup=this.tb.getAttribute("kd_sup")
            isi_sup=this.dok.getElementsByTagName("suplier")
            for isi_sp in isi_sup:
                if(isi_sp.getAttribute("kd_sup")==kode_sup):
                    k_h=k
                k=k+1
            hasil_barang=this.dok.getElementsByTagName("barang")[j_h]
            hasil_suplier=this.dok.getElementsByTagName("suplier")[k_h]
            this.td_nm=Label(this.win_df,text=hasil_barang.getAttribute("nm_brg"))
            this.td_sup=Label(this.win_df,text=hasil_suplier.getAttribute("nm_sup"))
            hrg_brg=float(this.tb.getAttribute("hrg"))
            this.td_hrg=Label(this.win_df,text=hrg_brg)
            jumlah_psn=int(this.tb.getAttribute("jml"))
            this.td_jml=Label(this.win_df,text=jumlah_psn)
            this.td_tot=Label(this.win_df,text=hrg_brg*jumlah_psn)
            this.td_tgl=Label(this.win_df,text=this.tb.getAttribute("tgl"))
            this.td_no.grid(column=0,row=i)
            this.td_nm.grid(column=1,row=i)
            this.td_sup.grid(column=2,row=i)
            this.td_hrg.grid(column=3,row=i)
            this.td_jml.grid(column=4,row=i)
            this.td_tot.grid(column=5,row=i)
            this.td_tgl.grid(column=6,row=i)
            i=i+1
                              
        this.tr_no.grid(column=0,row=0)
        this.tr_nm.grid(column=1,row=0)
        this.tr_sup.grid(column=2,row=0)
        this.tr_hrg.grid(column=3,row=0)
        this.tr_jm.grid(column=4,row=0)
        this.tr_tot.grid(column=5,row=0)
        this.tr_tgl.grid(column=6,row=0)
        this.win_df.mainloop()
        
    def simpan(this):
        i=0
        ii=''
        j=0
        jj=''
        
        this.kini=waktu.datetime.now()
        this.dok=mndom.parse("dbbrg.xml")
        abc=this.dok.createElement("beli")
        kd_brg=this.cb_brg.get()
        isi_brg=(kd_brg.split(" | "))
        kd_sup=this.cb_sup.get()
        isi_sup=(kd_sup.split(" | "))
        isi_barang=this.dok.getElementsByTagName("barang")
        
        for is_brg in isi_barang:
            if(isi_brg[0]==is_brg.getAttribute("kd_brg")):
                ii=i
            i=i+1
        
        isi_stok=this.dok.getElementsByTagName("barang")[ii].getAttribute("stok")
        abc.setAttribute("kd_brg",isi_brg[0])
        abc.setAttribute("kd_sup",isi_sup[0])
        abc.setAttribute("jml",this.tx_jm.get())
        abc.setAttribute("hrg",this.tx_hg.get())
        abc.setAttribute("tgl",this.kini.strftime("%Y/%m/%d"))
        this.tx_no.configure(state=NORMAL)
        abc.setAttribute("no_beli",this.tx_no.get())
        jml=this.tx_jm.get()
        stok_akhir=int(isi_stok)+int(jml)
        this.dok.getElementsByTagName("barang")[ii].setAttribute("stok",str(stok_akhir))
        this.dok.getElementsByTagName("dbbrg")[0].appendChild(abc)
        this.file_isi=open("dbbrg.xml","w")
        this.dok.writexml(this.file_isi)
        this.file_isi.close()
        this.bersih()
        this.no_pes()
        
    def __init__(this):
        this.kini=waktu.datetime.now()
        this.win=Tk()
        this.dbase=mndom.parse("dbbrg.xml")
        this.isi_brg_cmb=[]
        this.isi_sup_cmb=[]
        this.bt_sm=Button(this.win,text="SIMPAN",command=this.simpan)
        this.bt_kl=Button(this.win,text="KELUAR",command=this.win.destroy)
        this.bt_df=Button(this.win,text="DAFTAR",command=this.daftar)
        this.bt_hps=Button(this.win,text="HAPUS",command=this.cm_hapus)
        this.lb_no=Label(this.win,text="No Pesan")
        this.tx_no=Entry(this.win,text="",state=DISABLED)
        this.isi_sup_var=this.dbase.getElementsByTagName("suplier")
        this.isi_brg_var=this.dbase.getElementsByTagName("barang")
        for this.isi_1 in this.isi_sup_var:
            this.kd=this.isi_1.getAttribute("kd_sup")
            this.nm=this.isi_1.getAttribute("nm_sup")
            this.isi_sup_cmb.append(this.kd+" | "+this.nm)
        this.cb_sup=Combobox(this.win)
        this.cb_sup['values']=this.isi_sup_cmb
        for this.isi_2 in this.isi_brg_var:
            this.kd1=this.isi_2.getAttribute("kd_brg")
            this.nm1=this.isi_2.getAttribute("nm_brg")
            this.isi_brg_cmb.append(this.kd1+" | "+this.nm1)
        this.cb_brg=Combobox(this.win)
        this.cb_brg['values']=this.isi_brg_cmb
        if(len(this.isi_brg_cmb)>0):
            this.cb_brg.current(0)
        if(len(this.isi_sup_cmb)>0):
            this.cb_sup.current(0)
        this.lb_sup=Label(this.win,text="Nama Suplier")
        this.lb_brg=Label(this.win,text="Nama Barang")
        this.lb_jm=Label(this.win,text="Jumlah Beli")
        this.tx_jm=Entry(this.win)
        this.tx_hg=Entry(this.win)
        this.lb_tot=Label(this.win,text="Total bayar")
        this.lb_hrg=Label(this.win,text="Harga Barang")
        this.tx_tot=Entry(this.win,text="",state=DISABLED)
        this.lb_tgl=Label(this.win,text="Tanggal")
        this.tx_tgl=Label(this.win,text=this.kini.strftime("%Y/%m/%d"))
        this.lb_brg.grid(column=0,row=1)
        this.lb_sup.grid(column=0,row=2)
        this.lb_no.grid(column=0,row=0)
        this.tx_no.grid(column=1,row=0)
        this.tx_jm.bind('<KeyPress>',this.hitung)
        this.tx_jm.bind('<KeyRelease>',this.hitung)
        this.tx_hg.bind('<KeyPress>',this.hitung)
        this.tx_hg.bind('<KeyRelease>',this.hitung)
        this.cb_brg.grid(column=1,row=1)
        this.cb_sup.grid(column=1,row=2)
        this.tx_jm.grid(column=1,row=3)
        this.lb_jm.grid(column=0,row=3)
        this.tx_hg.grid(column=1,row=4)
        this.lb_hrg.grid(column=0,row=4)
        this.lb_tot.grid(column=0,row=5)
        this.tx_tot.grid(column=1,row=5)
        this.lb_tgl.grid(column=0,row=6)
        this.tx_tgl.grid(column=1,row=6)
        this.bt_sm.grid(column=0,row=7)
        this.bt_kl.grid(column=1,row=7)
        this.bt_df.grid(column=0,row=8)
        this.bt_hps.grid(column=1,row=8)
        this.no_pes()
        this.win.mainloop()
    def bersih(this):
        this.tx_no.configure(state=NORMAL)
        this.tx_tot.configure(state=NORMAL)
        this.tx_tot.delete(0,END)
        this.tx_jm.delete(0,END)
        this.tx_hg.delete(0,END)
        this.tx_no.delete(0,END)
        this.tx_no.configure(state=DISABLED)
        this.tx_tot.configure(state=DISABLED)
    def hitung(this,aaa):
        this.tx_tot.configure(state=NORMAL)
        if(this.tx_jm.get()=='')or(this.tx_hg.get()==''):
            this.tx_tot.insert(INSERT,"0")
        else:
            this.tx_tot.delete(0,END)
            total_bayar=(float(this.tx_jm.get()))*float(this.tx_hg.get())
            this.tx_tot.insert(INSERT,total_bayar)
        this.tx_tot.configure(state=DISABLED)
    def no_pes(this):
        no=1
        this.dok=mndom.parse("dbbrg.xml")
        this.isi_pes=this.dok.getElementsByTagName("beli")
        if(len(this.isi_pes)!=0):
            for this.isi_ps in this.isi_pes:
                if(float(this.isi_ps.getAttribute("no_beli"))>no):
                    no=int(this.isi_ps.getAttribute("no_beli"))
                no=no+1
        this.tx_no.configure(state=NORMAL)
        this.tx_no.delete(0,END)
        this.tx_no.insert(INSERT,no)
        this.tx_no.configure(state=DISABLED)
    def cm_hapus(this):
        this.dok=mndom.parse("dbbrg.xml")
        this.win_hp=Tk()
        this.lb_hp=Label(this.win_hp,text="Masukkan No. Pembelian")
        this.tx_hp=Entry(this.win_hp,text='')
        this.bt_hp=Button(this.win_hp,text="hapus",command=this.hapus)
        this.bt_bk=Button(this.win_hp,text="kembali",command=this.win_hp.destroy)
        this.lb_hp.grid(column=0,row=0)
        this.tx_hp.grid(column=1,row=0)
        this.bt_hp.grid(column=0,row=1)
        this.bt_bk.grid(column=1,row=1)
        this.win_hp.mainloop()
    def hapus(this):
        i=0
        i_h=''
        ada=0
        this.dok=mndom.parse("dbbrg.xml")
        no_pes_hp=this.tx_hp.get()
        this.isi=this.dok.getElementsByTagName("beli")
        for this.ii in this.isi:
            if(this.ii.getAttribute("no_bel")==no_pes_hp):
                i_h=i
                ada=1
            i=i+1
        if(ada==1):
            yg_hapus=this.dok.getElementsByTagName("jual")[i_h]
            this.dok.documentElement.removeChild(yg_hapus)
            this.file=open("dbbrg.xml","w")
            this.dok.writexml(this.file)
            this.file.close()
            messagebox.showinfo("pesan","Data sudah Dihapus")
            this.win_hp.destroy()
            this.no_pes()
        else:
            messagebox.showinfo("pesan","Data Tidak Ada")
            this.win_hp.destroy()
            this.no_pes()

