import threading
import random as ran
import tkinter as tk
import time
import tkinter.messagebox
def feasele(e):
    rel=[]
    cel=[]
    bel=[]
    for i in range(1,10):
        for j in range(1,10):
            if int(e[-2])==i:
                if int(e[-1])!=j:
                    rel.append("e"+str(i)+str(j))
            elif int(e[-1])==j:
                cel.append("e"+str(i)+str(j))
    bx=[]
    for i in tu:
        if e in i:
            bx=i
    for i in bx:
        if i!=e:
            bel.append(i)
    return((rel , cel , bel))

def getele(rwe,clme,bxe):
    r=[]
    c=[]
    b=[]
    for i in rwe:
        r.append(elems[i])
    for i in clme:
        c.append(elems[i])
    for i in bxe:
        b.append(elems[i])
    return((r,c,b))

def gen():
    global elems
    for i in range(1,10):
        chk=0
        while chk<=10:
            l=[1,2,3,4,5,6,7,8,9]
            for j in range(1,10):
                e="e"+str(i)+str(j)
                if elems[e]==0:
                    r1,c1,b1=feasele(e)
                    r,c,b=getele(r1,c1,b1)
                    ly=r+c+b
                    ch=0
                    for q in range(1,10):
                        if q in ly:
                            ch+=1
                    lx=[]
                    for k in range(1,10):
                        if k not in ly:
                            lx.append(k)
                    if ch==9 or (ch==8 and len(lx)==1 and (lx[0] in ly)):
                        for k in range(1,10):
                            E="e"+str(i)+str(k)
                            elems[E]=0
                        chk+=1
                        break
                    else:
                        while True:
                            x=ran.choice(l)
                            if x not in ly:
                                elems[e]=x
                                l.remove(x)
                                break
            if len(l)==0:
                break
        if chk>10:
            elems=dict.fromkeys(['e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19',
                                 'e21', 'e22', 'e23', 'e24', 'e25', 'e26', 'e27', 'e28', 'e29',
                                 'e31', 'e32', 'e33', 'e34', 'e35', 'e36', 'e37', 'e38', 'e39',
                                 'e41', 'e42', 'e43', 'e44', 'e45', 'e46', 'e47', 'e48', 'e49',
                                 'e51', 'e52', 'e53', 'e54', 'e55', 'e56', 'e57', 'e58', 'e59',
                                 'e61', 'e62', 'e63', 'e64', 'e65', 'e66', 'e67', 'e68', 'e69',
                                 'e71', 'e72', 'e73', 'e74', 'e75', 'e76', 'e77', 'e78', 'e79',
                                 'e81', 'e82', 'e83', 'e84', 'e85', 'e86', 'e87', 'e88', 'e89',
                                 'e91', 'e92', 'e93', 'e94', 'e95', 'e96', 'e97', 'e98', 'e99'] , 0)
            break
    return chk
def submit(di , FR1 , FR2 , FR3 , FBM):
    temp={}
    temp=dict.fromkeys(list(elems.keys()) , 0)
    for i in range(1,10):
        for j in range(1,10):
            mle="e"+str(i)+str(j)
            try:
                temp[mle]=int(di[mle].get())
            except AttributeError:
                temp[mle]=elemshow[mle]
            except ValueError:
                temp[mle]=0
    mist=[]
    for i in range(1,10):
        for j in range(1,10):
            elmen="e"+str(i)+str(j)
            nu=temp[elmen]
            r1,c1,b1=feasele(elmen)
            r,c,b=getele(r1,c1,b1)
            lis=r+c+b
            if not((nu not in lis) and (nu in (1,2,3,4,5,6,7,8,9))):
                mist.append(elmen)
    if mist==[]:
        FBM.configure(bg="SpringGreen2")
        FR1.configure(bg="SpringGreen2")
        FR2.configure(bg="SpringGreen2")
        FR3.configure(bg="SpringGreen2")
        tk.messagebox.showinfo("SUDOKU PUZZLE" , "PUZZLE SOLVED!!!")
        return
    else:
        for i in mist:
            di[i].configure(bg="#FF7F7F")


def acheck(di , FR1 , FR2 , FR3 , FBM):
    temp={}
    temp=dict.fromkeys(list(elems.keys()) , 0)
    for i in range(1,10):
        for j in range(1,10):
            mle="e"+str(i)+str(j)
            try:
                temp[mle]=int(di[mle].get())
            except AttributeError:
                temp[mle]=elemshow[mle]
            except ValueError:
                temp[mle]=0
    chkcnt=0
    for i in range(1,10):
        for j in range(1,10):
            elmen="e"+str(i)+str(j)
            nu=temp[elmen]
            r1,c1,b1=feasele(elmen)
            r,c,b=getele(r1,c1,b1)
            lis=r+c+b
            if nu not in lis and nu in (1,2,3,4,5,6,7,8,9):
                chkcnt+=1
            
    if chkcnt==81:
        FBM.configure(bg="SpringGreen2")
        FR1.configure(bg="SpringGreen2")
        FR2.configure(bg="SpringGreen2")
        FR3.configure(bg="SpringGreen2")
        tk.messagebox.showinfo("SUDOKU PUZZLE" , "PUZZLE SOLVED!!!")
        return
    else:
        mainsec.after(100 , lambda : acheck(di , FR1 , FR2 , FR3 , FBM))


def gridview(x):
    global elems
    print(elems)
    for i in range(1,10):
        for j in range(1,10):
            print(elems["e"+str(i)+str(j)] , end=" ")
            if j%3==0:
                print("\t" , end="")
        print()
        if i%3==0:
            print()
        
    grd=tk.Toplevel(mainsec)
    grd.title("SUDOKU GRID GENERATION")
    grd.configure(bg="lemonchiffon")
    sud=tk.Label(grd , text="SUDOKU" , font=("default" , 30) , bg="lavender").pack()
    FBM=tk.Frame(grd , bg="red")
    FBM.pack()
    FR1=tk.Frame(FBM , bg="red")
    FR1.pack()
    FB1=tk.Frame(FR1)
    FB1.pack(side=tk.LEFT , padx=5 , pady=5)
    FB2=tk.Frame(FR1)
    FB2.pack(side=tk.LEFT , padx=5 , pady=5)
    FB3=tk.Frame(FR1)
    FB3.pack(side=tk.LEFT , padx=5 , pady=5)
    FR2=tk.Frame(FBM , bg="red")
    FR2.pack()
    FB4=tk.Frame(FR2)
    FB4.pack(side=tk.LEFT , padx=5 , pady=5)
    FB5=tk.Frame(FR2)
    FB5.pack(side=tk.LEFT , padx=5 , pady=5)
    FB6=tk.Frame(FR2)
    FB6.pack(side=tk.LEFT , padx=5 , pady=5)
    FR3=tk.Frame(FBM , bg="red")
    FR3.pack()
    FB7=tk.Frame(FR3)
    FB7.pack(side=tk.LEFT , padx=5 , pady=5)
    FB8=tk.Frame(FR3)
    FB8.pack(side=tk.LEFT , padx=5 , pady=5)
    FB9=tk.Frame(FR3)
    FB9.pack(side=tk.LEFT , padx=5 , pady=5)
    wid={}
    wid=dict.fromkeys(list(x.keys()) , 0)
    wpre=False
    for i in range(1,10):
        for j in range(1,10):
            els="e"+str(i)+str(j)
            if x[els]==" ":
                wpre=True
                if els in b1:
                    wid[els]= tk.Entry(FB1, font=("Georgia", 30), width=2, bg="lavender" , justify="center")
                    wid[els].grid(row=(i-1) , column=(j-1))
                elif els in b3:
                    wid[els]= tk.Entry(FB3, font=("Georgia", 30), width=2, bg="lavender" , justify="center")
                    wid[els].grid(row=(i-1) , column=(j-7))
                elif els in b5:
                    wid[els]= tk.Entry(FB5, font=("Georgia", 30), width=2, bg="lavender" , justify="center")
                    wid[els].grid(row=(i-4) , column=(j-4))
                elif els in b7:
                    wid[els]= tk.Entry(FB7, font=("Georgia", 30), width=2, bg="lavender" , justify="center")
                    wid[els].grid(row=(i-7) , column=(j-1))
                elif els in b9:
                    wid[els]= tk.Entry(FB9, font=("Georgia", 30), width=2, bg="lavender" , justify="center")
                    wid[els].grid(row=(i-7) , column=(j-7))
                elif els in b2:
                    wid[els]= tk.Entry(FB2, font=("Georgia", 30), width=2, bg="mint cream" , justify="center")
                    wid[els].grid(row=(i-1) , column=(j-4))
                elif els in b4:
                    wid[els]= tk.Entry(FB4, font=("Georgia", 30), width=2, bg="mint cream" , justify="center")
                    wid[els].grid(row=(i-4) , column=(j-1))
                elif els in b6:
                    wid[els]= tk.Entry(FB6, font=("Georgia", 30), width=2, bg="mint cream" , justify="center")
                    wid[els].grid(row=(i-4) , column=(j-7))
                elif els in b8:
                    wid[els]= tk.Entry(FB8, font=("Georgia", 30), width=2, bg="mint cream" , justify="center")
                    wid[els].grid(row=(i-7) , column=(j-4))
            else:
                if els in b1:
                    wid[els]= tk.Label(FB1, font=("Georgia", 30), width=2, bg="lavender" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-1) , column=(j-1))
                elif els in b3:
                    wid[els]= tk.Label(FB3, font=("Georgia", 30), width=2, bg="lavender" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-1) , column=(j-7))
                elif els in b5:
                    wid[els]= tk.Label(FB5, font=("Georgia", 30), width=2, bg="lavender" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-4) , column=(j-4))
                elif els in b7:
                    wid[els]= tk.Label(FB7, font=("Georgia", 30), width=2, bg="lavender" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-7) , column=(j-1))
                elif els in b9:
                    wid[els]= tk.Label(FB9, font=("Georgia", 30), width=2, bg="lavender" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-7) , column=(j-7))
                elif els in b2:
                    wid[els]= tk.Label(FB2, font=("Georgia", 30), width=2, bg="mint cream" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-1) , column=(j-4))
                elif els in b4:
                    wid[els]= tk.Label(FB4, font=("Georgia", 30), width=2, bg="mint cream" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-4) , column=(j-1))
                elif els in b6:
                    wid[els]= tk.Label(FB6, font=("Georgia", 30), width=2, bg="mint cream" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-4) , column=(j-7))
                elif els in b8:
                    wid[els]= tk.Label(FB8, font=("Georgia", 30), width=2, bg="mint cream" , justify="center" , text=x[els] , borderwidth=1 , relief="solid")
                    wid[els].grid(row=(i-7) , column=(j-4))
    if wpre:
        sbtn=tk.Button(grd , height=1 , text="SUBMIT" , font=("Georgia" , 13) , bg="salmon" , fg="floral white" , command=lambda : submit(wid , FR1 , FR2 , FR3 , FBM)).pack()
        mainsec.after(100 , lambda : acheck(wid , FR1 , FR2 , FR3 , FBM))
    clgrbt=tk.Button(grd , height=1 , text="CLOSE" , font=("Georgia" , 13) , bg="salmon" , fg="floral white" , command=grd.destroy).pack()
def genbutf():
    global elems
    elems=dict.fromkeys(['e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19',
                         'e21', 'e22', 'e23', 'e24', 'e25', 'e26', 'e27', 'e28', 'e29',
                         'e31', 'e32', 'e33', 'e34', 'e35', 'e36', 'e37', 'e38', 'e39',
                         'e41', 'e42', 'e43', 'e44', 'e45', 'e46', 'e47', 'e48', 'e49',
                         'e51', 'e52', 'e53', 'e54', 'e55', 'e56', 'e57', 'e58', 'e59',
                         'e61', 'e62', 'e63', 'e64', 'e65', 'e66', 'e67', 'e68', 'e69',
                         'e71', 'e72', 'e73', 'e74', 'e75', 'e76', 'e77', 'e78', 'e79',
                         'e81', 'e82', 'e83', 'e84', 'e85', 'e86', 'e87', 'e88', 'e89',
                         'e91', 'e92', 'e93', 'e94', 'e95', 'e96', 'e97', 'e98', 'e99'] , 0)
    check=gen()
    flag=0
    while check>10:
        check=gen()
        flag+=1
        if flag>5:
            break
    gridview(elems)

def qshow(a):
    global elemshow
    for i in elemshow:
        elemshow[i]=" "
    if a=="es":
        elnum=ran.randint(36,45)
        Z=list(t)
        for i in range(elnum):
            el=ran.choice(Z)
            Z.remove(el)
            elemshow[el]=elems[el]
    elif a=="m":
        elnum=ran.randint(32,35)
        Z=list(t)
        for i in range(elnum):
            el=ran.choice(Z)
            Z.remove(el)
            elemshow[el]=elems[el]
    elif a=="h":
        elnum=ran.randint(28,31)
        Z=list(t)
        for i in range(elnum):
            el=ran.choice(Z)
            Z.remove(el)
            elemshow[el]=elems[el]
    elif a=="ex":
        elnum=ran.randint(22,27)
        Z=list(t)
        for i in range(elnum):
            el=ran.choice(Z)
            Z.remove(el)
            elemshow[el]=elems[el]
    elif a=="ev":
        elnum=ran.randint(17,21)
        Z=list(t)
        for i in range(elnum):
            el=ran.choice(Z)
            Z.remove(el)
            elemshow[el]=elems[el]
    mainsec.after(0 , lambda : gridview(elemshow))

def genq():
    opt=tk.Toplevel(mainsec)
    opt.configure(bg='floral white')
    opt.title("Sudoku question generator".upper())
    opt.geometry("500x500")
    lbl=tk.Label(opt , text="CHOOSE LEVEL")
    global elems
    elems=dict.fromkeys(['e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19',
                         'e21', 'e22', 'e23', 'e24', 'e25', 'e26', 'e27', 'e28', 'e29',
                         'e31', 'e32', 'e33', 'e34', 'e35', 'e36', 'e37', 'e38', 'e39',
                         'e41', 'e42', 'e43', 'e44', 'e45', 'e46', 'e47', 'e48', 'e49',
                         'e51', 'e52', 'e53', 'e54', 'e55', 'e56', 'e57', 'e58', 'e59',
                         'e61', 'e62', 'e63', 'e64', 'e65', 'e66', 'e67', 'e68', 'e69',
                         'e71', 'e72', 'e73', 'e74', 'e75', 'e76', 'e77', 'e78', 'e79',
                         'e81', 'e82', 'e83', 'e84', 'e85', 'e86', 'e87', 'e88', 'e89',
                         'e91', 'e92', 'e93', 'e94', 'e95', 'e96', 'e97', 'e98', 'e99'] , 0)    
    check1=gen()
    while check1>10:
        check1=gen()
    esbut=tk.Button(opt , text="Easy" , font=("default" , 19) , height=1 , command=lambda : threading.Thread(target=qshow, args=("es",)).start() , bg='LightPink1' , fg='indian red').pack(expand=True)
    mbut=tk.Button(opt , text="Medium" , font=("default" , 19) , height=1, command=lambda : threading.Thread(target=qshow, args=("h",)).start() , bg='LightPink1' , fg='indian red').pack(expand=True)
    hbut=tk.Button(opt , text="Hard" ,font=("default" , 19) , height=1, command=lambda : threading.Thread(target=qshow, args=("m",)).start() , bg='LightPink1' , fg='indian red').pack(expand=True)
    exbut=tk.Button(opt , text="Extreme" ,font=("default" , 19) , height=1, command=lambda : threading.Thread(target=qshow, args=("ex",)).start() , bg='LightPink1' , fg='indian red').pack(expand=True)
    evbut=tk.Button(opt , text="Evil" , font=("default" , 19) , height=1, command=lambda : threading.Thread(target=qshow, args=("ev",)).start() , bg='LightPink1' , fg='indian red').pack(expand=True)
    clbut=tk.Button(opt , text="CLOSE" , height=1, font=("default" , 19) ,command=opt.destroy , bg="salmon" , fg="floral white").pack(expand=True)
elems={}
elems=dict.fromkeys(['e11', 'e12', 'e13', 'e14', 'e15', 'e16', 'e17', 'e18', 'e19',
                     'e21', 'e22', 'e23', 'e24', 'e25', 'e26', 'e27', 'e28', 'e29',
                     'e31', 'e32', 'e33', 'e34', 'e35', 'e36', 'e37', 'e38', 'e39',
                     'e41', 'e42', 'e43', 'e44', 'e45', 'e46', 'e47', 'e48', 'e49',
                     'e51', 'e52', 'e53', 'e54', 'e55', 'e56', 'e57', 'e58', 'e59',
                     'e61', 'e62', 'e63', 'e64', 'e65', 'e66', 'e67', 'e68', 'e69',
                     'e71', 'e72', 'e73', 'e74', 'e75', 'e76', 'e77', 'e78', 'e79',
                     'e81', 'e82', 'e83', 'e84', 'e85', 'e86', 'e87', 'e88', 'e89',
                     'e91', 'e92', 'e93', 'e94', 'e95', 'e96', 'e97', 'e98', 'e99'] , 0)
elemshow={}
elemshow=dict.fromkeys(list(elems.keys()) , " ")
t=list(elemshow.keys())
tu=[]
l=[[1,2,3],[4,5,6],[7,8,9]]
for i in l:
    for j in l:
        ll=[]
        for x in i:
            for y in j:
                ll.append("e"+str(x)+str(y))
        tu.append(ll)

b1,b2,b3,b4,b5,b6,b7,b8,b9=tu
mainsec=tk.Tk()
mainsec.configure(bg="floral white")
mainsec.title("SUDOKU PUZZLE")
mainsec.geometry("1000x1000")
mlab=tk.Label(mainsec , text="SUDOKU" , font=("default" , 26) , height=1 , bg="floral white" , fg='indian red').pack(expand=True)
genbut=tk.Button(mainsec , height=1 , text="GENERATE GRID" , font=("Georgia" , 21) , command=genbutf , bg='LightPink1' , fg='indian red').pack(expand=True)
genpubut=tk.Button(mainsec , height=2 , text="GENERATE PUZZLE" , font=("Georgia" , 21) , command=genq , bg='LightPink1' , fg='indian red').pack(expand=True)
clbut=tk.Button(mainsec , height=1 , text="CLOSE" , font=("Georgia" , 21) , bg="salmon" , fg="floral white" , command=mainsec.destroy).pack(expand=True)
mainsec.mainloop()


 
