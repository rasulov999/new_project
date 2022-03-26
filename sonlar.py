a=int(input("120 xonaligacha son kiriting, minusda sinmidi, noldayam😂:"))
b=a
d=a
k=0
qwer=0
list=list()
if a<0:
    a=a+(2*(a*-1))
    qwer=1
b=a
d=a
while a!=0:
    a=a//10
    k=k+1
bir=b%10
if b==0:
   list.append("nol")
if bir==1:
   list.append("bir")
if bir==2:
   list.append("ikki")
if bir==3:
   list.append("uch")
if bir==4:
   list.append("to'rt")
if bir==5:
   list.append("besh")
if bir==6:
   list.append("olti")
if bir==7:
   list.append("yetti")
if bir==8:
   list.append("sakkiz")
if bir==9:
   list.append("to'qqiz")
on=(b%100)//10
if on==1:
   list.append("o'n")
if on==2:
   list.append("yigirma")
if on==3:
   list.append("o'ttiz")
if on==4:
   list.append("qirq")
if on==5:
   list.append("ellik")
if on==6:
   list.append("oltmush")
if on==7:
   list.append("yetmush")
if on==8:
   list.append("sakson")
if on==9:
   list.append("to'qson")
yuz=(b%1000)//100
if b==100:
   list.append("yuz")
elif yuz==1:
   list.append("bir yuz")
if yuz==2:
   list.append("ikki yuz")
if yuz==3:
   list.append("uch yuz")
if yuz==4:
   list.append("to'rt yuz")
if yuz==5:
   list.append("besh yuz")
if yuz==6:
   list.append("olti yuz")
if yuz==7:
   list.append("yetti yuz")
if yuz==8:
   list.append("sakkiz yuz")
if yuz==9:
   list.append("to'qqiz yuz")
bir=(b%10000)//1000
on=(b%100000)//10000
yuz=(b%1000000)//100000
if b==1000:
    list.append("ming")
elif bir==1 and b>1000:
    list.append("bir ming")
elif b>1999 and (bir!=0 or on!=0 or yuz!=0):
    list.append("ming")
if bir==2:
   list.append("ikki")
if bir==3:
   list.append("uch")
if bir==4:
   list.append("to'rt")
if bir==5:
   list.append("besh")
if bir==6:
   list.append("olti")
if bir==7:
   list.append("yetti")
if bir==8:
   list.append("sakkiz")
if bir==9:
   list.append("to'qqiz")
if on==1:
   list.append("o'n")
if on==2:
   list.append("yigirma")
if on==3:
   list.append("o'ttiz")
if on==4:
   list.append("qirq")
if on==5:
   list.append("ellik")
if on==6:
   list.append("oltmush")
if on==7:
   list.append("yetmush")
if on==8:
   list.append("sakson")
if on==9:
   list.append("to'qson")
if yuz==1 and (on!=0 or b>200000):
   list.append("bir yuz")
elif yuz==1 and on==0 and b<200000:
    list.append("yuz")
if yuz==2:
   list.append("ikki yuz")
if yuz==3:
   list.append("uch yuz")
if yuz==4:
   list.append("to'rt yuz")
if yuz==5:
   list.append("besh yuz")
if yuz==6:
   list.append("olti yuz")
if yuz==7:
   list.append("yetti yuz")
if yuz==8:
   list.append("sakkiz yuz")
if yuz==9:
   list.append("to'qqiz yuz")
bir=(b%10000000)//1000000
on=(b%100000000)//10000000
yuz=(b%1000000000)//100000000
if b==1000000:
    list.append("bir million")
elif bir==1 and b>1000:
    list.append("bir million")
elif b>1999999 and (bir!=0 or on!=0 or yuz!=0):
    list.append("million")
if bir==2:
   list.append("ikki")
if bir==3:
   list.append("uch")
if bir==4:
   list.append("to'rt")
if bir==5:
   list.append("besh")
if bir==6:
   list.append("olti")
if bir==7:
   list.append("yetti")
if bir==8:
   list.append("sakkiz")
if bir==9:
   list.append("to'qqiz")
if on==1:
   list.append("o'n")
if on==2:
   list.append("yigirma")
if on==3:
   list.append("o'ttiz")
if on==4:
   list.append("qirq")
if on==5:
   list.append("ellik")
if on==6:
   list.append("oltmush")
if on==7:
   list.append("yetmush")
if on==8:
   list.append("sakson")
if on==9:
   list.append("to'qson")
if yuz==1 and (on!=0 or b>200000000):
   list.append("bir yuz")
elif yuz==1 and on==0 and b<200000000:
    list.append("yuz")
if yuz==2:
   list.append("ikki yuz")
if yuz==3:
   list.append("uch yuz")
if yuz==4:
   list.append("to'rt yuz")
if yuz==5:
   list.append("besh yuz")
if yuz==6:
   list.append("olti yuz")
if yuz==7:
   list.append("yetti yuz")
if yuz==8:
   list.append("sakkiz yuz")
if yuz==9:
   list.append("to'qqiz yuz")
on=(b%100000000000)//10000000000
bir=(b%10000000000)//1000000000
yuz=(b%1000000000000)//100000000000
if b>999999999 and (bir!=0 or on!=0 or yuz!=0):
    list.append("milliard")
if bir==1:
   list.append("bir")
if bir==2:
   list.append("ikki")
if bir==3:
   list.append("uch")
if bir==4:
   list.append("to'rt")
if bir==5:
   list.append("besh")
if bir==6:
   list.append("olti")
if bir==7:
   list.append("yetti")
if bir==8:
   list.append("sakkiz")
if bir==9:
   list.append("to'qqiz")
if on==1:
   list.append("o'n")
if on==2:
   list.append("yigirma")
if on==3:
   list.append("o'ttiz")
if on==4:
   list.append("qirq")
if on==5:
   list.append("ellik")
if on==6:
   list.append("oltmush")
if on==7:
   list.append("yetmush")
if on==8:
   list.append("sakson")
if on==9:
   list.append("to'qson")
if yuz==1 and (on!=0 or b>200000000000):
   list.append("bir yuz")
elif yuz==1 and on==0 and b<200000000000:
    list.append("yuz")
if yuz==2:
   list.append("ikki yuz")
if yuz==3:
   list.append("uch yuz")
if yuz==4:
   list.append("to'rt yuz")
if yuz==5:
   list.append("besh yuz")
if yuz==6:
   list.append("olti yuz")
if yuz==7:
   list.append("yetti yuz")
if yuz==8:
   list.append("sakkiz yuz")
if yuz==9:
   list.append("to'qqiz yuz")
sonningkat=9999999999
qw=10000000000000
wq=1000000000000
oppo=1000000000000
kl=['trillion','trilliard','kvadrillion','kvadrilliard','kvintillion','kvintilliard','sekstillion','sekstilliard','septillion','septilliard','oktillion','oktilliard','nonillion','nonilliard','desillion','desilliard','undesillion','undesilliard','duodesillion','duodesilliard','tredesillion','tredesilliard','kvattuordesillion','kvattuordesilliard','kvindesillion','kvindesilliard','seksdesillion','seksdesilliard','septdesillion','septdesilliard','oktodesillion','oktodesilliard','novemdesillion','novemdesilliard','vigintillion','vigintilliard']
i=0
for i in range(0,37,1):
    bir = (b % qw) // wq
    qw = qw * 10
    wq = wq * 10
    if d>sonningkat and bir!=0:
       list.append(kl[i])
       sonningkat=(sonningkat*10)+9
    if bir == 1:
        list.append("bir")
    if bir == 2:
        list.append("ikki")
    if bir == 3:
        list.append("uch")
    if bir == 4:
        list.append("to'rt")
    if bir == 5:
        list.append("besh")
    if bir == 6:
        list.append("olti")
    if bir == 7:
        list.append("yetti")
    if bir == 8:
        list.append("sakkiz")
    if bir == 9:
        list.append("to'qqiz")
    on = (b % qw) // wq
    qw=qw*10
    wq=wq*10
    if d>sonningkat and on!=0 and (bir==0 and yuz==0):
       list.append(kl[i])
    if on == 1:
        list.append("o'n")
    if on == 2:
        list.append("yigirma")
    if on == 3:
        list.append("o'ttiz")
    if on == 4:
        list.append("qirq")
    if on == 5:
        list.append("ellik")
    if on == 6:
        list.append("oltmush")
    if on == 7:
        list.append("yetmush")
    if on == 8:
        list.append("sakson")
    if on == 9:
        list.append("to'qson")
    yuz = (b%qw)//wq
    if d>sonningkat and yuz!=0 and (bir==0 or on==0):
       list.append(kl[i])
    if yuz == 1:
        list.append("bir yuz")
    if yuz == 2:
        list.append("ikki yuz")
    if yuz == 3:
        list.append("uch yuz")
    if yuz == 4:
        list.append("to'rt yuz")
    if yuz == 5:
        list.append("besh yuz")
    if yuz == 6:
        list.append("olti yuz")
    if yuz == 7:
        list.append("yetti yuz")
    if yuz == 8:
        list.append("sakkiz yuz")
    if yuz == 9:
        list.append("to'qqiz yuz")
    qw = qw * 10
    wq = wq * 10
if qwer==1:
    list.append("minus")
list.reverse()
for i in range(len(list)):
    print(list[i],end=' ')
    