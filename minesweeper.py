import random as ran
import tkinter as tk
import tkinter.messagebox as mbox
first_click=False
flag=False
unflag=False
gfr=None
gamwin=None
flgbut=None
unflgbut=None
mainsec=None
def check():
    global bomb,wid,gamwin,fset
    num=100-len(bomb)
    cnt=0
    for i in wid:
        if isinstance(wid[i],tk.Label):
            cnt+=1
    if cnt==num and cnt+len(fset)==100:
        mbox.showinfo("Puzzle complete" , "Field Cleared!!!!")
        mainsec.after(5000,gamwin.destroy)
    else:
        mainsec.after(2000,check)
    
def extend(n):
    global wid
    global gfr, gamwin, flgbut
    dic=surround(n)
    lst=[]
    for i in dic:
        if (dic[i]!="b") and isinstance(wid[i],tk.Button):
            if (dic[i]==" "):
                lst.append(i)
                wid[i].destroy()
                if (int(i[1])+int(i[2]))%2==0:
                    btn=tk.Label(gfr,bg="bisque",height=1,width=2,font=("Georgia" , 13),text=elems[i])
                    btn.grid(row=int(i[1]),column=int(i[2]),sticky="nsew")
                    wid[i]=btn
                    
                else:
                    btn=tk.Label(gfr,bg="lemon chiffon",font=("Georgia" , 13),text=elems[i])
                    btn.grid(row=int(i[1]),column=int(i[2]),sticky="nsew")
                    wid[i]=btn
            else:
                wid[i].destroy()
                if (int(i[1])+int(i[2]))%2==0:
                    btn=tk.Label(gfr,bg="bisque",height=1,width=2,font=("Georgia" , 13),text=elems[i])
                    btn.grid(row=int(i[1]),column=int(i[2]),sticky="nsew")
                    wid[i]=btn
                    
                else:
                    btn=tk.Label(gfr,bg="lemon chiffon",font=("Georgia" , 13),text=elems[i])
                    btn.grid(row=int(i[1]),column=int(i[2]),sticky="nsew")
                    wid[i]=btn
    for i in lst:
        extend(i)
            
def surround(el):
    global gfr, gamwin, flgbut
    temp={}
    row=int(el[1])
    col=int(el[2])
    a=max(0,row-1)
    b=max(0,col-1)
    a1=min(9,row+1)
    b1=min(9,col+1)
    for i in range(a,a1+1):
        for j in range(b,b1+1):
            ex=f"e{i}{j}"
            temp[ex]=elems[ex]
    return temp
def bom(el):
    dic=surround(el)
    return (list(dic.values()).count("b"))
def clicked(lev,n):
    global first_click,fset,flag,unflag
    global gfr, gamwin, flgbut,unflgbut
    global wid
    if not first_click:
        gen(lev,n)
        if (int(n[1])+int(n[2]))%2==0:
            btn=tk.Label(gfr,bg="bisque",height=1,width=2,font=("Georgia" , 13),text=elems[n])
            btn.grid(row=int(n[1]),column=int(n[2]),sticky="nsew")
            wid[n]=btn
        else:
            btn=tk.Label(gfr,bg="lemon chiffon",font=("Georgia" , 13),text=elems[n])
            btn.grid(row=int(n[1]),column=int(n[2]),sticky="nsew")
            wid[n]=btn
        extend(n)
        first_click=True
    else:
        if flag and (n not in fset):
            wid[n].configure(bg="orange red")
            fset.append(n)
        elif unflag and (n in fset):
            if ((int(n[1]) + int(n[2])) % 2 == 0):
                wid[n].configure(bg="SpringGreen3")
            else:
                wid[n].configure(bg="PaleGreen1")
            fset.remove(n)
        elif not(flag) and not(unflag):
            if elems[n]!="b":
                if n not in fset:
                    if (int(n[1])+int(n[2]))%2==0:
                        btn=tk.Label(gfr,bg="bisque",height=1,width=2,font=("Georgia" , 13),text=elems[n])
                        btn.grid(row=int(n[1]),column=int(n[2]),sticky="nsew")
                        wid[n]=btn
                    
                    else:
                        btn=tk.Label(gfr,bg="lemon chiffon",font=("Georgia" , 13),text=elems[n])
                        btn.grid(row=int(n[1]),column=int(n[2]),sticky="nsew")
                        wid[n]=btn
                    if elems[n]==" ":
                        extend(n)
            else:
                mbox.showerror("BOOM!!!!!" , "Mine Exploded !GAME OVER!")
                mainsec.after(5000,gamwin.destroy)
        else:
            mbox.showwarning("WARNING!!" , "Resetting flag and unflag status")
            flag=False
            unflag=False
            flgbut.configure(bg="orange red")
            unflgbut.configure(bg="cornflower blue")

def flg_clk():
    global flag,unflag
    global gfr, gamwin, flgbut,unflgbut
    flag=not(flag)
    unflag=False
    unflgbut.configure(bg="cornflower blue")
    if flag and not(unflag):
        flgbut.configure(bg="bisque2")
    else:
        flgbut.configure(bg="orange red")
def unflg_clk():
    global unflag,flag,flgbut
    global gfr, gamwin, unflgbut
    flag=False
    unflag=not(unflag)
    flgbut.configure(bg="orange red")
    if unflag and not(flag):
        unflgbut.configure(bg="light blue")
    else:
        unflgbut.configure(bg="cornflower blue")
def gridview(lev):
    global wid,mainsec,gamwin,gfr,flgbut,unflgbut
    gamwin=tk.Toplevel(mainsec)
    gfr=tk.Frame(gamwin)
    gfr.grid(row=0,column=0)
    for i in range(0,10):
        for j in range(0,10):
            if (i+j)%2==0:
                btn=tk.Button(gfr,bg="SpringGreen3",height=1,width=2,font=("Georgia" , 13),command=lambda l=lev,e=f"e{i}{j}":clicked(l,e))
                btn.grid(row=i,column=j,sticky="nsew")
                wid[f"e{i}{j}"]=btn
            else:
                btn=tk.Button(gfr,bg="PaleGreen1",font=("Georgia" , 13),width=2,height=1,command=lambda l=lev,e=f"e{i}{j}":clicked(l,e))
                btn.grid(row=i,column=j,sticky="nsew")
                wid[f"e{i}{j}"]=btn
    flgbut=tk.Button(gamwin,bg="orange red",font=("Georgia" , 13),text="Flag",command=flg_clk)
    flgbut.grid(row=1,column=0)
    unflgbut=tk.Button(gamwin,bg="cornflower blue",font=("Georgia" , 13),text="Unflag",command=unflg_clk)
    unflgbut.grid(row=2,column=0)
    mainsec.after(2000,check)
def gen(lev,e):
    global elems,mainsec
    global bomb
    lst=list(elems.keys())
    lst.remove(e)
    if lev.lower()=="easy":
        for i in range(ran.randint(10,15)):
            el=ran.choice(lst)
            bomb.append(el)
            lst.remove(el)
            elems[el]="b"
    if lev.lower()=="medium":
        for i in range(ran.randint(15,20)):
            el=ran.choice(lst)
            bomb.append(el)
            lst.remove(el)
            elems[el]="b"
    if lev.lower()=="hard":
        for i in range(ran.randint(25,30)):
            el=ran.choice(lst)
            bomb.append(el)
            lst.remove(el)
            elems[el]="b"
    for i in range(0,10):
        for j in range(0,10):
            ex=f"e{i}{j}"
            if elems[ex]==" ":
                if bom(ex)!=0:
                    elems[ex]=bom(ex)
                else:
                    elems[ex]=" "
    
            
def main():
    global first_click
    global lev
    global mainsec
    reset()   
    mainsec=tk.Tk()
    tk.Label(mainsec,text="MINESWEEPER",font=("Georgia" , 16),bg="pale green").grid(row=0,column=0)
    tk.Button(mainsec,text="Easy",font=("Georgia" , 16),bg="burlywood3",command=lambda : set_level("easy")).grid(row=1,column=0)
    tk.Button(mainsec,text="Medium",font=("Georgia" , 16),bg="burlywood3",command=lambda : set_level("medium")).grid(row=2,column=0)
    tk.Button(mainsec,text="Hard",font=("Georgia" , 16),bg="burlywood3",command=lambda : set_level("hard")).grid(row=3,column=0)
    tk.Button(mainsec,text="Close",font=("Georgia" , 16),bg="light salmon",command=mainsec.destroy).grid(row=4,column=0)
    mainsec.mainloop()
    
elems={}
wid={}
bomb=[]
fset=[]
def reset():
    global first_click,flag,unflag,gfr,gamwin,flgbut
    for i in range(0,10):
        for j in range(0,10):
            elems[f"e{i}{j}"]=" "
    first_click=False
    flag=False
    unflag=False
    gfr=None
    gamwin=None
    flgbut=None
lev=""
def set_level(st):
    global lev
    lev=st
    reset()
    gridview(lev)
main()
