# Jamshid Ahmadov

# a = int(input("Birinchi qayiqning tezligini kiriting(km/s):"))
# b = int(input("Ikkinchi qayiqning tezligini kiriting(km/s):"))
# s = 400

# kema_u = a + b
# t = s / kema_u
# t = t // 1
# print("Kemalar ",t," soatda uchrashadi")
# print("Masofa:", "400km")


# alfa = 579413
# beta = "Aqlbek"
# d = True
# s = 0
# resp = "d"
# b = 100
# max1 = False
# fc = "True34"
# t = 102.5
# res = "2500"```
# a = "-50"
# b = 45.67

# print(type(alfa), type(beta), type(d), type(s), type(resp), type(b), type(max1), type(fc), type(t), type(res), type(a),
#      type(b))


# xona_a = int(input("Xonaning bo'yini kiriting:"))
# xona_b = int(input("Xonaning enini kiriting:"))
# p = 2*(xona_a + xona_b)
# print("Xonaning premetri: ",p)
# s = xona_a * xona_b
# print("Xonaning yuzi: ", s)

# asos = int(input("Uchburchakning asosining uzunligini kiriting:"))
# h = int(input("Uchnurchakning balandligini kiriting:"))

# s = asos*h
# print("Uchburchakning yuzi:", s)

# v = int(input("Avtomobilning o'rtacha tezligini kiriting: "))
# s = int(input("Avtomobilning bosib o'tgan yo'lini kiriting: "))
# t = s / v
# t = t // 1
# print("Vaqt", t, "soat")           

# r = int(input("Doiraning radiusini kiriting:"))
# PI = 3.14
# s = PI * (r**2)
# l = 2*PI*r
# print("Doiraning yuzi:", s)
# print("Doiraning uzunligi:", l)
# karralilar6 = 0 
# karralilar3 = 0
# musbatlar = 0
# manfiylar = 0
# numbers = 2, -6, 88, 5, 0, -7, 71, -6, -4, -12, 13, 4, -5, 123, -12, -13, 18, -20

# for i in numbers:
#    if i > 0:
#        musbatlar += 1
#    if i < 0:
#        manfiylar += 1

# print("Musbatlar:", musbatlar, "ta")
# print("Manfiylar:", manfiylar, "ta")

# for i in numbers:
#    if i % 3 ==0:
#        karralilar3 += 1

# print(karralilar3)
# numbers1 = range(30,90)
# for i in numbers1:
#    if i % 6 == 0:
#        karralilar6 = karralilar6 + i

# print("6 ga karrali sonlar yig'indisi", karralilar6)



# a = int(input("Enter a number:"))
# b = int(input("Enter a second number:"))
# if b < a:
#   b = 0
#    print(b)
# else:
#    print(b)
# a = int(input("Enter 1:"))
# b= int(input("Enter 2: "))

# if a % b == 0:
#    print("Qoldiqsiz bo'linadi")
# else:
#    print("Error")

# a = int(input("Enter a first number:"))
# b = int(input("Enter a second number:"))

# if  a !=0:
#    if a > b:
#        if a % b == 0:
#            c = a+b
#        else:
#            c = a*b
#    print(c)
# if a == b:
#    print("a b ga teng")
# if b>a:
#    print("b a dan katta")
# if a == 0:
#    print("a 0 ga teng")

# a = int(input(""))
# b = int(input(""))
# c = int(input(""))
# if a**2 - b**2 == c **2:
#    print(a*b*c)
# else:
#    print(a+b+c)
# m = 0
# def min4(a, b, c, d):
#    if a>b and c>b and d>b:
#        return b
#    if b>a and c>a and d>a:
#        return a
#    if a>c and b>c and d>c:
#        return c
#    if b>d and a>d and c>d:
#        return d

# a = int(input("Enter:"))
# b = int(input("Enter:"))
# c = int(input("Enter:"))
# d = int(input("Enter:"))
# print(min4(a,b,c,d))

# a = int(input("O'quvchilar sonini kiriting:"))
# b = int(input("Olmalar sonini kiriting:"))
# bulingan = b//a
# qolgan = b%a
# print("Bo'lib olingan olmalar soni:", bulingan)
# print("Savatga solingan olmalar:", qolgan)

# n = int(input("Son kiriting:"))
# for i in range(1,n):
#    if i**2<n:
#        print(i)
# n = 0
# from random import randint
# while True:
#    a = randint(10,10000)
#    n +=1
#    print(a)
#    if n ==5:
#        break

# from random import randint
# u = 0
# a = 20
# b = 50
# s = randint(a,b)
# while True:
#    print(s)
#    s = s + 2
#    u +=1
#    if u ==7:
#        break

# a = input("")
# b = input("")
# c = input("")
# print(a,b,c, sep=":")
# a = int(input("uch xonali son kiriting:"))

# a1 = a // 100
# a2 = a // 10 % 10
# a3 = a % 100 % 10
# y = a1 + a2 + a3
# print(y)

# a = int(input("Anvar qancha olma terdi: "))
# b = int(input("Dilshod qancha olma terdi: "))
# c = int(input("Mahmud qancha olma terdi:"))
# ap = a + b + c
# ta = ap // 3
# l = ap % 3
# print("Har biriga", ta, "-tadan olma tegdi")
# print(l," ta olma ortib qoldi")

# print(int(eval(input())))

# from tkinter import *
# window = Tk()
# window.title("MY APP")

# window.geometry("250x50")

# sonlar = 0

# a = [10,90,660,560,70,330]


# for i in a:
#   sonlar = sonlar + i

# print(sonlar)

# def max_1(a,b):
#    if a > b:
#        return a
#    if b > a:
#        return b
#    else:
#        return "Draw"

# def max1(a,b,c):
#    return max_1(max_1(a,b), c)

# a = int(input())
# b = int(input())
# c = int(input())
# print(max1(a,b,c))

# from random import randint
# while True:
#    n1 = randint(1,70)
#    n2 = randint(1,68)
#    n_u = n1+n2
#    in1 = n1, "+", n2, "="
#    a = int(input(str(in1)))
#    if a == n_u:
#        print("True")#

#    else:
#        print("False")
#        break
# x = 0
# y = []
# n = int(input("Son kiriting: "))
# for i in range(n):
#     x+=n
#     print(x)

# tonna = int(input("Tonnani kiriting:"))
# kg = int(input("Kilogrammni kiriting:"))
# g = int(input("Gramni toping:"))

# gramm = 0
# gramm = tonna *100000 +kg*1000+g
# print(gramm)

# a = int(input())
# b = int(input())
# h = int(input())

# d = a-b
# p1 = h/d
# print(p1)


# in1 = int(input("1 dan 5 gacha son kiriting:"))
# son = 0
# ww = 0
# if in1 > 0 and in1 <= 5:
#        while True:
#            print("*" * 4)
#            print("*" * 4)
#            print("*" * 4)
#            print("*" * 4)
#            print(" ")
#            son += 1
#            if son == in1:
#                break
# S = 0
# n = int(input(""))
# while True:
#    S = n*(n+4) + S
#    n = n - 1
#    if n == 1:
#        break

# print(S)



# num = 0
# while True:
#    a = int(input("Enter:"))
#    if a > 1:
#        for i in range(1,a+1):
#            if a%i==0:
#                num = num + 1
#    else:
#       print("Wrong")
#    if num > 2:
#        print("Murakkab")
       
#    if num <= 2 and a > 1:
#        print("Tub")
#    num = 0   

# while True:
#    a  = int(input("Son kiriting: "))
#    b = a**(1/2)
#    print(b)
#    if a == 0:
#        break
#        print("Stop")

# ns = 0
# n = int(input("Enter: "))
# while True:
#    print(n*"*")
#    ns += 1
#    if ns == n:
#        break


# nn = int(input("Son kiriting: "))
# for i in range(1,nn+1):
#     if nn % i == 0:
#         print(i)

# a = []
# while True:
#     c = input("Enter")
#     c.append[a]
#     if c == 0:
#         break
#         print(a)

# from math import *



# num = 0
# a = int(input("Enter: "))
# for i in range(1, a+1):
#    a = int(input("Enter:"))
#    if a > 1:
#        for i in range(1,a+1):
#            if a%i==0:
#                num = num + 1
#    else:
#       print("Wrong")
#    if num > 2:
#        print("Murakkab")
       
#    if num <= 2 and a > 1:
#        print("Tub")
#    num = 0  

# while True:
#     ab = 0
#     a = int(input("Enter a number: "))
#     b = a
#     if a > 0:
#         while True:
#             print(ab*(" "),"*"*b)
#             ab += 1
#             b = b - 1
#             if b == 0:
#                 break
    
#     if a == 0:
#         print("Function stoped")
#         break

# while True:
#     ab = 0
#     a = int(input("Enter a number: "))
#     if a > 0:
#         while True:
#             print("*"*ab)
#             ab += 1
            
#             if ab > a:
#                 break
    
#     if a == 0:
#         print("Function stopped")
#         break
    

# number = int(input("Mingdan kichik son kiriting: "))
# if number > 0:
#     b = number//100
#     b1 = number // 10 % 10
#     b2 = number % 100 % 10
    
#     y = "C"*b
#     u = "X"*b1
#     bir = "I"*b2
#     print(y,u,bir, end=",")

# else:
#     print("Noto'g'ri harakat")

# a = 0
# while True:
#     print(a, "+", a+1, "=", a+a+1)
#     a += 1
#     if a == 10:
#         break

# r = [19,89,77,27,29,19]
# if r[0] == r[-1]:
#     print("True")
# else:
#     print("False")

# while True:
#     a = int(input("Enter: "))
#     if a > 1:
#         b = 1
#         while True:
#             print(b*str(b))
#             b += 1
#             if b == a+1:
#                 break
#     else:
#         print("Wrong")

# bb = 0
# aa = 1
# n = int(input("Enter a number: "))
# while True:
#     bb = bb + aa*(aa+4)
#     aa +=1
#     if aa == n:
#         break
# print(bb)
# while True:
#     b = 0
#     a = int(input(""))
#     if a > 1 :
#         dt = a
#         astr = str(a)
#         for i in astr:
#             b = int(i)+b

#         print(b)
#     elif a == 0:
#         print("Function has stopped")
#         break
#     else:
#         print("Wrong input")
#         continue

# from tkinter import *

# from random import randint

# def tasodifiy():

#     number = int(textbox_input.get())

#     textbox_outinput.delete(0.0, END)

#     for i in range(1,11):
#         t_son = str(randint(1,number)) + "\n"

# textbox_output.insert(END, t_son)

# window = Tk()
# window.title("Jamshid Ahmadov")
# window.geometry('250x250')
# window.configure(background='yellow')

# input_label = Label(window, text="Son: ", bg="yellow")

# input_label.grid(row=2, column=0)

# output_label = Label(window, text = '\nNatija', bg = "yellow")

# output_label.grid(row=2, column=0)
# textbox_input = Entry(window, width=5)
# textbox_input.grid(row=1)








# m = int(input("Sinfda bor stullar sonini kiriting: "))
# n = int(input("O'quvchilar sonini kiriting: "))
# if 1 <= m <= 100 and 1<= n <= 100:
#     if m>=n:
#         print(0)
#     else:
#         print(n-m)  

# a = 0
# n = int(input("Mehmonxona necha qavatdan iborat: "))
# for i in range(1,n+1):
#     a += i**2
# print(a)

# n = int(input("O'qituvchi Sardorga Nechta masala berdi: "))
# k = int(input("O'qituvchi Sardorga necha kun masala bergan: "))
# m = n+k
# print(m)

# n = int(input("Yo'lak uzunligini kiriting: "))
# l = int(input("Necha metrga bitta terak ekiladi: "))

# if 1<= n <= 1000 and 1<= l <= 100000:
#     a = n//l
#     print(a,"ta terak ekiladi")

# else:
#     print("Xato")

# H = int(input("List balandligini kiriting: "))
# W = int(input("List bo'yini kiriting: "))
# a = int(input("E'lon tomonini kiriting: "))
# if 1 <= H <= 100000 and 1 <= W <= 100000 and 1 <= a <= 100000:
#     list = H*W
#     el = a**2
#     son = el // list
#     print(son, "e'lon sig'adi")

# else:
#     print("O'lchamlar xato")

# t = []
# b = 0
# n = int(input("To'nkalar sonini kiriting: "))
# while True:
#     ai = int(input("To'nka balandligini kiriting: "))
#     t.append(ai)
#     b +=1
#     if b == n:
#         break
# print(ai)
# print(t)

# n = int(input("O'quvchilar sonini kiriting: "))
# if 1 <= n <= 1000000000:
#     jamoalar = (n // 6) + 1
#     print(jamoalar) 




# a = 0
# kg = 0
# otlar = []
# n = int(input("Otlar sonini kiriting: "))
# k = int(input("Nechta otni sotib yubormoqchi: "))
# if 1 <= n <= 1000 and 1<=k<=1000 and n > k:
#     while True:
#         ai = int(input("Ot massasini kiriting: "))
#         otlar.append(ai)
#         a += 1
#         if a == n:
#             break

# else:
#     print("Kattaliklar xato")

# for imm in otlar:
#     kg = imm + kg

# print("otlarning umumiy massasi", kg, "kg")

# otlar.sort()
# so = otlar[-k::]
# for p in so:
#     print(p)
# len_1 = 0
# q = []
# ai1 = 0
# n = int(input("Qo'g'irchoqlar sonini kiriting: "))
# while True:
#     ai = int(input("Qo'g'irchoq hajmini kiriting: "))
#     ai1 += 1
#     q.append(ai1)
#     if ai1 == n:
#         break
# len1 = len(q)
# qu = 0
# for n in q:

# for i in q:
#     if i > q[:]:
# b = 0
# n = int(input("To'nkalar sonini kiriting: "))
# while True:
#     ai = int(input("To'nka hajmini kiriting: "))
#     b += 1
#     if b == n:
#         break

# while True: print(int(eval(input())))

# nn = []

# a = int(input("Enter: "))
# for ab in str(a):
#     nn.append(ab)

# y = 0
# for u in nn:
#     y += int(u)

# print(y)

# a = []
# ff = 0
# while True:
#     c = int(input("Enter a number: "))
#     a.append(c)
#     if c == 0:
#         break

# for g in a:
#     ff += g

# print(ff)

# a = []
# while True:
#     inp1 = int(input("Enter a number: "))
#     a.append(inp1)
#     if inp1 == 0:
#         break

# a.sort()
# print(a[-1])

# h = []
# int2 = input("Matn kiriting: ")
# for i in int2:
#     if i == "k":
#         h.append("q")
#     if i == "d":
#         h.append("t")
#     if i == "b":
#         h.append("p")

#     else:
#         h.append(i)

# for nn in h:
#     if nn == "k" or nn == "d" or nn == "b":
#         h.remove(nn)

# for m in h:
#     print(m, end="")

# Random -------------------

# from random import randint
# num = randint(1,50)
# uu = 0
# print("Salom. Siz bilan o'yin o'ynaymiz. \n 1dan 50 gacha son o'yladim")
# a = int(input("Topishga harakat qiling=> "))
# uu += 1
# while True:
#     if a > num:
#         a = int(input("Kichikroq son kiriting=> "))
#         uu += 1
    
#     if a < num:
#         a = int(input("Kattaroq son kiriting=> "))
#         uu += 1
    
#     if a == num:
#         print("Siz", uu, "urinishda topdigniz")
#         break

# ch1 = 1
# ch2 = 51

# uu1 = 0
# input("Son o'ylang men topaman\n\O'ylagan bo'lsangiz ENTERni kiriting ")


# while True:
#     ch1 = 1
#     ch2 = 51
#     tah = randint(ch1,ch2)
#     print("Siz o'ylagan son ",tah, "mi:\n")
#     num1 = input("Siz o'ylagan son katta bo'lsa 1\nKichik bo'lsa 0\nTeng bo'lsa 'Ha': ")
#     uu1+=1
#     if num1 == "1":
#         ch1 == tah
#         uu1 +=1
#     if num1 == "2":
#         ch2 == tah
#         uu1 += 1
#     if num1.lower() == 'ha':
#         print("Men", uu1, "urinishda topdim")
#         break 
    
# if uu1 > uu:
#     print("Siz yutdingiz")

# elif uu1 < uu:
#     print("Men yutdim")

# else:
#     print("Durrang")


# y = []
# u = 0
# while u < 5:
#     a = int(input("Enter a number: "))
#     y.append(a) 
#     u+=1

# min1 = 0
# max1 = 0
# y.sort()
# for i in y[0:3]:
#     min1 += i

# for b in y[1::]:
#     max1 += b

# print("Min", min1)
# print("Max", max1)
# toplam = []
# t_j = []
# a = int(input("Nechta element qo'shamiz: "))
# s = 0
# while True:
#     add = int(input("Element kiriting: "))
#     toplam.append(add)
#     s += 1
#     if s == a:
#         break

# for i in toplam:
#     for b in toplam:
#         if b == i:
#             t_j.append(b)
#             t_j.append(i)
#             toplam.remove(b)
#             toplam.remove(i)
#         else:
#             continue          


# for nn in toplam:
#     print(nn,end=" ")

# number = []
# n = int(input("Enter: "))
# for i in str(n):
#     number.append(i)
# pri = 0

# for we1 in number:
#     we1 = int(we1)
#     pri += we1

# if n % pri**2 == 0:
#     print("Yes")

# else:
#     print("No")

# numbers = []
# mn = 0
# m = int(input("Massiv uzunligini kiriting: "))
# while True:
#     n = int(input("Son kiriting: "))
#     mn += 1
#     if mn == m:
#         break

# numbers.sort()

# print(numbers[-1])


# n = int(input("Son kiriting: "))
# S = int(input("Son kiriting: "))

# t = n**2 - (n-1)**2
# print(t)
# Sn = 0
# for i in range(1,S+1):
#     Sn += i

# print(Sn)

# bu = []
# t = []
# n = int(input("Nechta son kiritiasiz: "))
# ns = 0 
# while True:
#     num = int(input("Son kiriting:"))
#     ns+=1
#     if ns == n:
#         break
# index = 0

# for i in range(1,10000):
#     if i % t[index] == 0:
#         for p in str(i):
#             if p == 0 and p == 9:
#                 bu.append(i)

# print(bu)
# p = []
# g = 0
# S = int(input("Sovg'a necha tanga turadi: "))
# while True:
#     a = int(input("Gnom tangasini kiriting: "))
#     g+=1
#     p.append(a)
#     if g == 7:
#         break

# son = 0

# for i in p:
#     son += i

# if S > son:
#     print("Gnomlarga", S -son, "tanga kerak")

# else:
#     print("Gnomlarda tangalar yetarli")


# x = int(input("+:  "))
# y = int(input("-:  "))

# kun = x - y*3
# if 3*y <x:
#     print((100//kun)+1)
# else:
#     print("00")

# n = int(input('Vaqtni kiriting: '))
# k = int(input("Bir daqiqada nechta ishchining tana haroratini o'lchash mumkin: "))
# m = int(input("Ishxonaga daqiqasiga qancha ishchi kelmoqda: "))
# tup = n * m
# b = k * m
# q = tup - b
# print(q)

# num = []
# a = int(input("Nechta son kiritamiz: "))
# for i in range(1,a+1):
#     son = int(input("Son kiriting: "))
#     num.append(son)
# bb = 1
# for k in num:
#     bb = bb*k
# p = []                           

# for nn in range(1,bb+1):
#     for mm in num:
#         if nn % mm == 0:
#             p.append(nn)

# print(p[-1])

# a = int(input())
# for t in range(101):
#     if t - a>=0 and t-a<3 and t%5==0:
#         print(t)
#     else:
#         print(a)

# t,s,v = map(float,input().split())
# print(v)
# 534
# a = int(input())
# h = []
# list1 = list(map(int,input().split()))
# for t in list1:
#     h.append(list1.count(t))
# h.sort()
# print(a-h[-1])

# num = int(input())
# a = 0
# for t in str(num):
#     a+=int(t)

# if len(str(num))==9 and a%2!=0:
#     print("yes")
# else:
#     print("no")

# a = int(input())
# if a%2==0:
#     print("3")
# else:
#     print("2")
# list = list(map(int,input().split()))
# print(sum(list))

# n = input()
# print(n)

# list = []
# for t in range(1,10*999):
#     list.append(t)
# for f in list:
#     print(f)

    
# a,b,c = map(int,input().split())
# if a+b>=c:
#     print(a+b-c)
# else:
#     print("Error")
# n = int(input())
# print(32**(1/2))

# n=int(input())
# list=list(map(int,input().split()))
# for i in list:
#     for g in list:
#         if list.count(i)>1:
#             if i==g:
#                 list.remove(g)

# print(list)

# U, V, B, D=map(int,input().split())
# n=B/(U+V)
# j=(D*n)
# if int(j)-j==0:
#     print(int(j))
# else:
#     print(round((D*n),2))
# import math

# h = []
# t = int(input())
# for t in range(1,t+1):
#     i = int(input())
#     h.append(i)
# for o in h:
#     t = 2**o+3**o+5**o+6**o   
#     if math.floor(t**(1/3)) == t**(1/3):
#         print("YES")
#     else:
#         print("NO")
    
# n= int(input())
# a=bin(n)
# print(a[2:])

# a = int(input())
# if a%3==0:
#     print("Yes")
# else:
#     print("No")

# r = 0
# n = input()
# for g in range(1,int(n)+1):
#     r = len(str(g)) + r

# print(r)


# n = int(input())
# if n%4==0 and n%400==0:
#     if n >=1000:
#         print(f"12/09/{n}")
#     if 999>=n>=100:
#         print(f"12/09/0{n}")
#     if 99>=n>=10:
#         print(f"12/09/00{n}")
#     if 9>=n>=1:
#         print(f"12/09/000{n}")
# if n%4!=0 and n%400!=0:
#     if n >=1000:
#         print(f"13/09/{n}")
#     if 999>=n>=100:
#         print(f"13/09/0{n}")
#     if 99>=n>=10:
#         print(f"13/09/00{n}")
#     if 9>=n>=1:


# a,b = map(int,input().split())
# if b%2==0:
#     print(a+(b//2))
# else:
#     print(-1)

# n,m = map(int,input().split())

# if m%2==0:
#     print(n+m//2+1)
# else:
#     print(-1)

# def say(n) -> str:
#     for i in range(4):
#         if (n>=a[i]):
#             return say(n//a[i])+b[i] + say(n%a[i])
#     return c[n//10] + d[n%10]

# a = (1000000000, 1000000, 1000,100)
# b = ("milliard ", "million ", "ming ", "yuz ")
# c = ("","o'n ","yigirma ", "o'ttiz ", "qirq ", "ellik ", "oltmish ", "yetmish ", "sakson ", "to'qson " )
# d = ("", "bir ", "ikki ", "uch ", "to'rt ", "besh ", "olti ", "yetti ", "sakkiz ", "to'qqiz ")

# g = int(input())
# print(say(g))


# list=list(map(int,input().split()))
# list.sort()
# p = []
# p.append(list[0] + list[1] + list[2] + list[3])
# p.append(list[-1]+list[-2] + list[-3]+list[-4])

# for g in p:
#     print(g, end=" ")



# No 113 BAHO

# a = int(input())
# list = []
# for t in range(a,101):
#     if t%5==0:
#         list.append(t)

# if a>=38 and list[0]-a<3:
#     print(list[0])
# else:
#     print(a)


# n = int(input())
# print(n/100)

# s=input()

# a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# b=["A","B","C","D","E","F","G","H","I","J","K","L",'M',"N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# for i in a:
#     print(i,s.count(i))

# for i in b:
#     print(i,s.count(i))

# n,a = map(int,input().split())
# if len(str(a))==n:
#     print("yes")
# else:
#     print("no")

# a = int(input())

# print(a**3-1)

# ax**2 +b*x + c = 0 
# a,b,c = map(int,input().split())

# d = b**2 - (4*a*c)

# x1 = (-b-(d**(1/2)))/(2*a) 
# x2 = (-b+(d**(1/2)))/(2*a)

# print(x1,x2)

# a=int(input())
# print((1**a+2**a+3**a+4**a)%5)

# a = input("Kiriting:")
# print(a)

#include <iostream>
#include <<math>

# li = []
# a  = int(input())
# for t in range(a):
#     int(input())
#     l = list(map(int,input().split()))
#     son  =-1
#     for y in l:
#         for t in l:
#             if y==t:
#                 son+=1
#     li.append(son/2)
    
# for x in li:
#     print(int(x))

# a = int(input())
# if a == 1 or a==10:
#     print("VIP 210K")
# elif a == 2 or a == 3 or a == 4 or a == 5 or a==6 or a==7:
#     print("Business 140K")
# else:
#     print("Econom 105K")

# from math import *

# x,y = map(float,input().split())
# f = (1/(x+2/(x*x)+3/(x*x*x))+exp(x*x+x*3))/(atan(x+y)+fabs(5+x)**2)-cos(y*y+(x*x)/2)**2
# print(f"{f:.2f}")

# g = []
# a=int(input())
# for t in range(a):
#     j = int(input())
#     g.append(j-1)

# for t in g:
#     print(t)
    
# a = int(input())
# if a == 1:
#     print(1)
# elif a == 2:
#     print(5)
# else:
#     print(f"{a-2}5")

# a = int(input())
# l = []
# for t in range(a):
#   j,w = map(int,input().split())
  
# for t in range(a):
#   print(1)
  
# import math

# h = []
# t = int(input())
# for t in range(1,t+1):
#     i = int(input())
#     h.append(i)
# for o in h:
#     t = 2**o+3**o+5**o+6**o   
#     if math.floor(t**(1/3)) == t**(1/3):
#         print("YES")
#     else:
#         print("NO")

# binary = int(input())

# decimal = 0
# multiplier = 1

# while binary > 0:
#     last_digit = binary % 10
#     decimal = decimal + (last_digit * multiplier)
#     multiplier = multiplier * 2
#     binary = int(binary/10)

# print(decimal)

# g  = int(input())
# list = []
# for t in range(g):
#   j = input()
#   list.append(j)
  
# for i in list:
#   print(len(i))

# list = []
# a = int(input())
# h =int(input())
# for t in range(h):
#     f,g = map(int,input().split())
#     if f==a and g==a:
#         list.append("Chiroyli")
#     elif f==a and g>a or f>a and g>a or g>a and f>a:
#         list.append("Deyarli_chiroyli")
#     else:
#         list.append("NO")
    
# for t in list:
#     print(t,end=" ")


# t = input()
# i = 0
# for a in t:
#     if a == " " or a=="a" or a=="d" or a=="g" or a=="j" or a=="m" or a=="p" or a=="t" or a =="w":
#         i+=1
#     elif a=="b" or a =="e" or a == "h" or a=="k" or a=="n" or a=="q" or a=="u" or a=="x":
#         i+=2
#     elif a=="c" or a=="f" or a=="i" or a=="l" or a=="o" or a=="r" or a=="v" or a=="y":
#         i+=3
#     elif a=="s" or a=="z":
#         i+=4
# print(i)


# z  = int(input())
# s = 0
# n = 0
# if z==0:
#   s = -1
# else:
#   if z<0:
#     n = -z
#   else:
#     n = z
#   i = 1
#   while i*i <= n:
#     if n%i==0:
#       s+=1
#       if i*i!=n:
#         s+=1
#     i+=1
#   if s%2 and z>0:
#     s+=1
    
# print(s)
# n = int(input())
# x = ""
# if n<10:
#   x=="000"
# elif n<100:
#   x="00"
# elif n<1000:
#   x="0"
# if n%400==0 or n%4==0 and n%100 !=0:
#   x = f"12/09/{x+str(n)}"
# else:
#   x = f"13/09/{x+str(n)}"
# print(x)


# n = int(input())
# for i in range(0,n):
#     ax,ay,bx,by = map(int,input().split())
#     print(bx+bx-ax,by+by-ay)


# from math import ceil
# a = int(input())
# print(ceil((a+1)/2))

# # Ikki xil vaqt kiritiladi
# # time1=minut1=secund1
# # time2=minut2=secund2

# soat1=int(input('1-soat:'))
# minut1=int(input('1-minut:'))
# secund1=int(input('1-secund:'))

# soat2=int(input('2-soat:'))
# minut2=int(input('2-minut:'))
# secund2=int(input('2-secund:'))

# # 1 soat 3600 secund, 1 minut 60 secund
# secund = (soat2-soat1) * 3600 +(minut2-minut1)*60 +(secund2-secund1)
# print('secund: {}'.format(secund))




# a = int(input("Son kiriting: "))
# b = []
# for i in str(a):
#     b.append(i)
    
# y = 1

# for g in b:
#     g = int(g)
#     y *= g
    
# print(y)


# yil=int(input("Yilni kiriting:"))
# if yil % 4 == 0:
#     print("Kabisa yili")
# elif yil%400==0:
#      print("Kabisa yili")
# else:
#      print("Kabisa yili emas")
   
# a=input('Enter your name:')
# b=input('Last name too:') 
# language=input('Choose and write the language: uz/eng ?')
# if language == ' eng':
#     print('Wlcome {}'. format(a+b))
#     age= int(input("How old are you? "))
#     meet=input("My name is Avazbek. Nice to meet you. Do you study or work?")
# elif language == ' uz':
#     print('Xush kelibsiz {}'. format(a+b))
#     age1 = int(input("Yoshingiz nechada?"))
#     hgmeet=input("Mening ismim Avazbek. Tanishganimdan xursandman. O`qiysizmi yoki ishlaysizmi?")
# else:
#     print("Choose the one of them and write")
    
    
    
# summa = input("Enter the amount :")
    
# if summa.isdigit() and int(summa)>0 and int(summa)<10000000:
#     print('Thank you')
        
# else:
#     print("Error!")    
    
# name=input("Enter your name:")
# surname=input("Enter your surname:")

# if name or surname :
#     print("Thank you")
# else:
#     print("Enter your name or surname!")
    
#     # Hovuz
# a=int(input("Balndligi: "))
# b=int(input("Asosi radiusi : "))    
# pi=3.14
# S=int(pi)*(int(b)**2)
# V=int(a)*int(S)
# print("V=",V)

#      TERAKLAR
# a=int(input("Masofa:"))
# b=int(input("Orasidagi masofa:"))
# c=int(a)//int(b)+1
# print("natija",c)   
    
# yil=int(input("yilni kiriting:"))
# if yil % 4==0:
#       print("kabisa yili")
# elif yil % 400==0:
#     print("kabisa yili")
# else:
#     print("kabisa yili emas")         

# yil=int(input("yilni kiriting:"))

# if yil %4==0:
#     print("Kabisa yil")
# else:
#     print("Kabisa yil emas") 

#   Ism-Familiya
# a=input('Ismingizni kiriting:')
# b=input('familiyangizni ham:') 
# print('Xush kelibsiz {}'. format(a+b))


#  savol va javob


# a=input("ismingizni kiriting:")
# b=input("familiyangizni ham:")
# u=input("qayerda yashaysiz:")
# c=int(input("yoshingiz nechada?:"))
# q=input("Qayerda o'qiysiz?:")
# u=input("boshqa ish qilmaysizmi?:")
# if q=='ishda':
#     print("pul berib turolasizmi?:")
# else:
#     print("haa zo'rku")
# m=input("uylanganmisiz?:")
# if m=='ha':
#     print("ha yaxshi:")
# else:
#     print("hali yoshsiz hozir o'qing:")  
  

# for son in range(1, 32):
#     print(son)

# --------------karra jadval
# karra=7
# for son in range(1,11) :
#     natija=karra*son
#     print("{}x{}={}".format(karra,son,natija))

# n = int(input())
# m = 0
# for i in range(1,n+1):
#     if i %2==0:
#         m+=i
        
# print(m)


# n,k = map(int,input().split())
# if n<=0:
#   print(1)
# else:
#     print(((k+1)**n)%((10**9)+7))

# import math
# n=int(input())
# k=int(input())
# print(math.ceil(n/k))

# a=Avazbek   
# n=int(input())
# sum=''
# for i in a:
#     if i!=a[-1]:
#       i=i+(n*"*")
#     sum+=i
# print(sum+a[-1])

    #   WHILE
# son=1
# while son<=31 :
#     print(son)
#     son=son+1

# from random import randint
# kodlar=[135,132,134] #list
# yangi_kod =randint(130,135)

# i=0
# while yangi_kod in kodlar :
#     i+=1
#     yangi_kod =randint(130,135)
    
# print("Takrorlanishlar soni :",i)
# print(yangi_kod)




    # 0008 MAXIMUM AND MINIMUM VALUE
# n=list(map(int,input().split()))
# print(sum(n)-max(n),sum(n)-min(n))




    # 0006   DASTURCHILAR KUNI
# n = int(input())
# x = ""
# if n < 10:
#   x = "000"
# elif n < 100:
#   x = "00"
# elif n < 1000:
#   x = "0"
# if n % 400 == 0 or n % 4 ==0 and n % 100 != 0:
#   x =f"12/09/{x+str(n)}"
# else:
#   x = f"13/09/{x+str(n)}"
# print(x)



    # 0005 KO'PAYTMA
# z=int(input())
# s = 0
# n = 0
# if z == 0:
#   s = -1
# else:
#    if z<0:
#      n = -z
#    else:
#      n = z
#    i = 1
#    while i*i <= n:
#     if n %i == 0:
#       s+=1 
#       if i*i != n:
#         s+=1
#     i+=1
#    if s%2 and z>0:
#     s+=1
# print(s)


#      0011   2-MAX
# x = int(input())
# n = list(map(int,input().split()))
# n.remove(max(n))
# print(max(n))


#      129      EKUK 
# a,k = map(int,input().split())
# print(int(k/a))


#       113 BAHO   check

# print(int(eval(input())))

# n = int(input())
# if n%2!=0:
#     h = 1
#     l = n-1
#     while h<=n:
#         print(int(l/2)*" ",h*"*")
#         h+=1
#         l=l-2

#     while h>=1:
#         print(int(l/2)*" ",h*"*",)
#         h-=1
#         l+=2
# n = int(input())

# for x in range(1, (n+5) //2 + 1):
#     for y in range( (n+5) //2 - x):
#         print(" ", end = "")
#     for z in range( (x*2)-1 ):
#         print("*", end = "")
#     print()

# for x in range( (n+5)// 2 + 1, n + 5):
#     for y in range(x - (n+5) //2):
#         print(" ", end = "")
#     for z in range( (n+5 - x) *2 - 1):
#         print("*", end = "")
#     print()

# def Diamond(rows):
#     n = 0
#     for i in range(1, rows + 1):
#         # loop to print spaces
#         for j in range (1, (rows - i) + 1):
#             print(end = " ")
         
#         # loop to print star
#         while n != (2 * i - 1):
#             print("*", end = "")
#             n = n + 1
#         n = 0
         
#         # line break
#         print()
 
#     k = 1
#     n = 1
#     for i in range(1, rows):
#         # loop to print spaces
#         for j in range (1, k + 1):
#             print(end = " ")
#         k = k + 1
         
#         # loop to print star
#         while n <= (2 * (rows - i) - 1):
#             print("*", end = "")
#             n = n + 1
#         n = 1
#         print()
 
# # Driver Code
# # number of rows input
# rows = 5
# Diamond(rows)


# m = int(input(""))
# n=m-4
# for x in range(1, (n+5) //2 + 1):
#     for y in range( (n+5) //2 - x):
#         print(" ", end = "")
#     for z in range( (x*2)-1 ):
#         print("*", end = "")
#     print()
# for x in range( (n+5)// 2 + 1, n + 5):
#     for y in range(x - (n+5) //2):
#         print(" ", end = "")
#     for z in range( (n+5 - x) *2 - 1):
#         print("*", end = "")
#     print()
# top half


# n = int(input())

# if n%2!=0:
#     n = n//2+1
#     for i in range(n):
#         for j in range(n - i - 1):
#             print(' ', end='')
#         for j in range(2 * i + 1):
#             print('*', end='')
#         print()

#     # downward pyramid
#     for i in range(n - 1):
#         for j in range(i + 1):
#             print(' ', end='')
#         for j in range(2*(n - i - 1) - 1):
#             print('*', end='')
#         print()
# else:
#     print(-1)

# g = int(input())
# list1 = list(map(int,input().split()))
# if sum(list1)%2!=0:
#     print("No")
# else:
#     print("Yes")




# 646 --- TAKSI 
# x = int(input())
# a,b,c = map(int,input().split())
# s,d,x1,f = map(int,input().split())
# n_on = b + ((x-a)*c)
# vaqt = x/s
# n_of = d+(vaqt*x1)+(x*f)
# if n_on<n_of:
#     print("online")
# elif n_on>n_of:
#     print("ofline")
# s=a*b
# print(s)

# list1 = ["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# a,b = map(str,input().split())
# for t in list1:
#     if t == a:
#         g = list1.index(t)
        
# for y in list1:
#     if y == b:
#         f = list1.index(y)
        
# print(g+f)

# from math import ceil, floor
# a,b,c,d = map(float,input().split())
# # a1,b1,c1,d1 = map(float,input().split())
# # l = float(input())
# # r = float(input())

# wr_u = (a+b+c+d)/4
# wr_u = round(wr_u)
# print(wr_u)

# from math import ceil
# a,b,c = map(int,input().split())
# a1= ceil(a/2)
# b1 = ceil(b/2)
# c1 = ceil(c/2)

# print(a1+b1+c1)
# a,b=map(int,input().split())
# print((a**(b+1))%(10**9+7))
# c=0
# g=0
# for i in range(1,b+1):
#     c+=1
#     g+=a**c
# d=0
# j=0
# for i in range(1,b+1):
#     d+=1
#     j+=a**(d*(-1))
# print(int(g/j))



# 145
# v = int(input())
# list1 = list(map(int,input().split()))


# if v<3:
#     list1.sort()
#     print(list1[-3,-2,-1])
# else:
#     if list1[0] + list1[1] > list1[2] and list1[1] + list1[2] > list1[0] and list1[0] + list1[2] > list1[1]:
#         list1.sort()
#         print(list1[-3],list1[-2],list1[-1])
#     else:
#         print("-1")


# a = int(input())
# list1 = list(map(int,input().split()))
# omadli = 1
# o = len(list1)-1
# for y in range(o):
#     if list1[y]>list1[y+1]:
#         omadli+=1

        
# print(omadli)

# a = int(input())
# list1 = list(map(int,input().split()))
# omadli = 2
# omadsiz = 0
# o = len(list1)-2
# for y in range(o):
#     if list1[y]>list1[y+1]>list1[y+2]:
#         omadli+=1
#     else:
#         omadsiz+=1

# print(omadli)

# nums = 0
# list1 = []
# g = int(input())
# for y in range(1,g+1):
#     a,b = map(int,input().split())
#     for t in range(a,b+1):
#         if len(str(t))==1:
#             nums+=1
#         elif len(str(t))>0:
#             if t% len(str(t))==0:
#                 nums+=1
#         print(nums)
#     nums=0


# list_p = []
# m = int(input())
# for y in range(1,m+1):
#     a,b,n = map(int,input().split())
#     if a<n and b<n:
#         if a>b:
#             list_p.append("Maqsud")
#         elif a<b:
#             list_p.append("Azimjon")
#         else:
#             list_p.append("Draw")
#     elif a<=n and n>b:
#         list_p.append("Azimjon")
#     elif a>n and b<=n:
#         list_p.append("Maqsud")
#     else:
#         list_p.append("Draw")
        
# for x in list_p:
#     print(x)


# l = 0
# n,m= map(int,input().split())
# list1 = list(map(int,input().split()))
# list1.sort()
# pl = 0

# for y in list1:
#     if pl<m:
#         pl+=y
#         l+=1
# if len(list1)==y:
#     print("Shokoladxo'r")
# else: 
#     print(l)


# def pattern(n):
#      k = 2 * n - 2
#      for i in range(0, n):
#           for j in range(0 , k):
#                print(end=" ")
#           k = k - 1
#           for j in range(0 , i + 1 ):
#                print("* ", end="")
#           print("\r")
#      k = n - 2
#      for i in range(n , -1, -1):
#         for j in range(k , 0 , -1): 
#             print(end=" ")
#         k = k + 1
#         for j in range(0 , i + 1):
#             print("* ", end="")
#         print("\r")
# pattern(int(input()))

# from math import factorial
# n = int(input())
# h = factorial(n)
# num = 0
# for g in range(1,h+1):
#     if h%g==0:
#         num+=1


# print(num%(10**9+7))

# o = []
# n = int(input())
# list1 = list(map(int,input().split()))
# for g in list1:
#     if g%2==0:
#         o.append(g)
# o.sort()
# if len(o)>0:
#     print(o[-1])
# else:
#     print(-1)

# v,a = map(int,input().split(":"))
# pl = int(input())
# vaqt = v*60+a
# if vaqt+pl< 1440:
#     m = vaqt+pl
#     if m//60>=10 and m%60>=10:
#         print(f"{m//60}:{m%60}")
#     elif m//60<10 and m%60>=10:
#         print(f"0{m//60}:{m%60}")
#     elif m//60<10 and m%60<10:
#         print(f"0{m//60}:0{m%60}")
#     else:
#         print(f"0{m//60}:0{m%60}")
# else:
#     m = vaqt+pl
#     h = m%1440
#     if h//60>=10 and h%60>=10:
#         print(f"{h//60}:{h%60}")
#     elif h//60<10 and h%60>=10:
#         print(f"0{h//60}:{h%60}")
#     elif h//60<10 and h%60<10:
#         print(f"0{h//60}:0{h%60}")
#     else:
#         print(f"0{h//60}:0{h%60}")

# n=int(input())
# if n == 1:
#     print(1)
# elif n==2:
#     print(2)

# else: print((n*(n-1)*(n-2))%1000000007)

# n = int(input())
# if n%7==0:
#     print("YES")
# else:
#     print("NO")


# a, k = map(int,input().split())
# list1 = list(map(int,input().split()))
# k = []
# y = 0
# for x in list1:
#     if x==k:
#         y+=k
#         k.append(list1.index(x))

# print(k)
# print(y)


# son = 0
# a,c,k = map(int,input().split())
# for g in range(1,a+1):
#     if g%c==k:
#         son+=1

# print(son)

# a = int(input())
# o = 1
# u = 0
# if a==2:
#     print(1)
# else:
#     while o<a:
#         o*=2
#         u+=1

#     print(u)

# a,b,n = map(int,input().split())
# if a+b==n:
#     if a<b:
#         print(f"{a}{b}")
#     elif a>b:
#         print(f"{b}{a}")
#     else:
#         print(f"{b}{a}")
# else:
#     print(-1)



# def solve(equation):
    
#     # replacing all the x terms with j 
#     # the imaginary part
#     s1 = equation.replace('x', 'j')
      
#     # shifting the equal sign to start 
#     # an opening bracket
#     s2 = s1.replace('=', '-(')
      
#     # adding the closing bracket to form 
#     # a complete expression
#     s = s2+')'
      
#     # mapping the literal j to the complex j
#     z = eval(s, {'j': 1j})
#     real, imag = z.real, -z.imag
      
#     # if the imaginary part is true return the
#     # answer
#     if imag:
#         return "x = %f" % (real/imag)
#     else:
#         if real:
#             return "No solution"
#         else:
#             return "Infinite solutions"
  
  
# equation = "2+3x=5x-7"
# print(solve(equation))

# a = int(input()) 
# javob=0
# for i in range(1,a+1):
#     u=0
#     b = 1
#     c = 3
#     bn = a
#     mn = a-1
#     len1 = ""
#     while u!=a:

#         len1+=b*"*"

#         len1+=c*"*"
#         c+=2
#         u+=1
#         mn-=1

#     len1+=b*"*"
#     javob+=len(len1)
# print(javob)
# n,k = map(int,input().split())
# mn = 0
# for t in range(1,n+1):
    
#     for g in range(1,t+1):
#         o = 0
#         if t%g==0 and k%g==0:
#             o+=1
    
#     if o<3:
#         mn+=1

# print(mn)


# o = []
# n = int(input())
# list1=list(map(int,input().split()))
# for g in list1:
#     if list1.count(g)==2:
#         o.append(g)

# o.sort()
# if len(o)==0:
#     print(-1)
# else:
#     print(o[-1])

# n,k = map(int,input().split())
# list1 = list(map(int,input().split()))
# yil = 0
# yil+=list1.count(k)*k
# print(yil)
# index1=[]
# for g in list1:
#     if g==k:
#         print((list1.index(g)+1),end=" ")
    

# a = int(input())
# for t in range(a,1,-1):
#     list1 = []
#     for h in str(t):
#         list1.append(h)
#     if list1.count("0")==0:
#         for g in list1:
#             print(g,end="")
#         break

# a,b,c,d,x = map(int,input().split())
# if b==0 or (a==0 and c-d!=x):
#     print("Error")
# elif b!=0:
#     print((x+d-c)*b//a)
# elif a==0:
#     print("No result")


# m = input()
# a = 1 
# if a==1:
#     print("Hasan")
#     a+=1
# else:
#     print("Husan")

# a = int(input()) 
# u=0
# b = 1
# c = 3
# bn = a
# mn = a-1

# while u!=a:
#     print(bn*" ",b*"*")
#     print(mn*" ",c*"*")
#     c+=2
#     u+=1
#     mn-=1
# print(bn*" ",b*"*")


# n= int(input())
# list1=list(map(int,input().split()))
# x=int(input())
# u=list1.count(x)
# print(u)

# mk = 1
# n = int(input())
# for t in range(1,n+1):
#     x,y = map(int,input().split())
#     m = 0
#     for h in range(x,y+1):
#         if h!=0:
#             m+=1
    
#     mk*=m

# print(mk%(10**9+7))

# a=0
# m = int(input())
# for g in range(1,m+1):
#     if g%2==0 and m%g==0:
#         a+=1
# print(a)

# a,b=input().split()
# print(int(a,2)*int(b,2))

# n,k =map(int,input().split())
# s=1
# for j in range(n):
#   s*=n
# if n==2:
#   s+=4
# n-=1
# print(s-k*n)
# N = int(input())
# list1 = []
# for t in range(1,N+1):
#   list1.append(int(input()))

# list1.sort()
# for g in list1:
#   print(g)

# n = int (input())
# for i in range(1,n+1):
#     a2 = 4 + 3 * (2 ** i - 1) - 3
#     if a2 - n > 0:
#         print(int(a2-n))
#         break


# n = int(input())
# for t in range(1,n+1):
#     i=int(input())
#     print(i)

# n,k = map(int,input().split())
# list1= list(map(int,input().split()))
# list1.sort()
# if list1[-1]<=k:
#     print(0)
# else:
#     print(list1[-1] - k)

# a= int(input())
# l = 0
# for t in range(1,a**10+1):
#     if a%t==0:
#         l+=1
# print(l)

# l = 0
# m = int(input())
# for t in str(m):
#     l+=int(t)

# print(l)

# list1 = list(map(int,input().split()))
# list1.sort()
# print((list1[-1]-list1[-2])+(list1[-2]-list1[-3]))

# p = []
# n = int(input())
# for t in range(1,n+1):
#     l,m = map(int,input().split())
#     if (l + m )%2==0:
#         p.append("YES")
#     else:
#         p.append("NO")

# for h in p:
#     print(h)

# l  = int(input())
# m = 1
# k = 0
# for t in range(1,l+1):
#     m+=k
#     k+=4
# print(m)

# list1 = []
# l = int(input())
# for g in range(1,l+1):
#     m,n = map(int,input().split())
#     if m>n:
#         if m%n==0:
#             list1.append("YES")
#         else:
#             list1.append("NO")

# for ty in list1:
#     print(ty)

# l = [0]
# for i in range(39):
#   for j in range(59):
#     for k in range(64):
#       l.append(3**j*5**i*2**k)

# l.sort()
# a = "int(input())"
# t = eval(a)
# while t:
#   print(l[eval(a)])
#   t-=1

# n = int(input())
# for i in range(n):
#   t = int(input())
#   x = bin(t)
#   print(x.count("1"))
  
# n = 0
# m = 0
# for t in range(1,100):
#     print(n*m)
#     n+=1
#     m+=1


# from random import randint
# n = input()
# a = randint(1,3)
# if a == 1:
#     print("Hasan")
# else:
#     print("Husan")

# n,k = map(int,input().split())
# list1 = list(map(int,input().split()))
# nm = sum(list1)

# if nm-(n*k) > 0:
#     print(nm-n*k)
# else:
#     print(0)

# n = int(input())
# list1 = list(map(int,input().split()))
# print("2 4")

# a = int(input()) 
# u=0
# b = 1
# c = 3
# bn = a
# mn = a-1

# while u!=a:
#     print(bn*" ",b*"*")
#     print(mn*" ",c*"*")
#     c+=2
#     u+=1
#     mn-=1
# print(bn*" ",b*"*")

# 699

# son = 0
# n = int(input())
# for t in range(1,n//2):
#     if t%n==0:
#         tub = 0
#         for g in range(1,t+1):
#             if t&g==0:
#                 tub+=1
#         if tub<=2:
#             son+=1

# print(son) 

# n,k = map(int,input().split())
# arr = list(map(int,input().split()))

# s= 0 
# for i in range(0,n):
#     s+= arr[i]
#     if s- k <0:
#         s=0
#     else:
#         s=s-k

# if s<0:
#     print(0)
# else:
#     print(s)

# n = int(input())
# list = []
# g = 0
# m = 5
# for t in range(1,n+1):
#     list.append(m)
#     m+=m+1
    

# print(sum(list))


# 591
# 591
# 591
# 591
# 591
# juft = 0
# toq = 0
# n = input()
# for t in n:
#     if n.index(t)+1%2==0:
#         juft+=int(t)
#         print(n.index(t))
#     else:
#         toq+=int(t)
#         print(n.index(t))

# if juft-toq==0:
#     print("Yes")
# else:
#     print("NO")
# print(juft,toq)


# n,k = map(int,input().split())

# for t in range(n,k+1):
#     k = 0
#     for h in range(1,t+1):
#         if t%h==0:
#             k+=1
#     if k==2 or k==1 and t!=1:
#         print(t,end=" ")


# juft = 0
# toq = 0
# n = input()
# for t in n:
#     if (n.index(t)+1)%2!=0:
#         toq+=int(t)
#         print(n.index(t))
#     else:
#         juft+=int(t)
#         print(n.index(t))

# if juft-toq==0:
#     print("Yes")
# else:
#     print("NO")
# print(juft,toq)

# n = int(input())
# while True:
#     if n == 0:
#         print(0)
#         break
#     else:
#         l = 0
#         for t in str(n):
#             l+=int(t)
#         if l%10==0:
#             print((n+1)*9+1)
#             break
#         else:

# a = "dastur"
# for x in a:
#     print(x)
#     if x=="s":
#         break

 
# function to find required number
# def findNth(n):
 
#     count = 0
 
#     for curr in itertools.count():
#         # Find sum of digits in current no.
#         sum = 0
#         x = curr
#         while(x):
#             sum = sum + x % 10
#             x = x // 10
 
#         # If sum is 10, we increment count
#         if (sum == 10):
#             count = count + 1
 
#         # If count becomes n, we return current
#         # number.
#         if (count == n):
#             return curr
 
#     return -1
 
# # Driver program
# if __name__=='__main__':
#     print(findNth(int(input())))



# def binary(num):
#     return int(bin(num).split('0b')[1])
 
# if __name__ == "__main__" :
#     x = 10
#     binary_x = binary(x)
#     print("the binary number is :",binary_x)
 
# This code is contributed by Rishika Gupta.


 #Function to convert decimal number
# to binary using recursion
# def DecimalToBinary(num):
#     if num >= 1:
#         DecimalToBinary(num // 2)
#     print(num % 2, end = '')
# if __name__ == '__main__':
#     dec_val = int(input())
#     DecimalToBinary(dec_val)

# print(bin(int(eval(input()))))

# from math import gcd
# a,b,c,d = map(int,input().split())
# print(gcd(pow(a,b,d)-(c%d),d))

# from math import factorial
# m,n = map(int,input().split())
# s = factorial((m+n-2)) // (factorial(n-1) * factorial(m-1))
# s %= (10**9+7)
# print(s)

# n = int(input())
# list1 = list(map(int,input().split()))

# from math import factorial
# x,y = map(int,input().split())
# n=max(x,y) 
# m=min(x,y) 
# res=((factorial(n)/(factorial(n-m)*factorial(m))//1)%2+x)%2
# print(int(res))

# l = 0
# from math import factorial
# n = int(input())
# k = factorial(n)
# for t in range(1,k+1):
#     if k&t==0:
#         l+=1
#         print(t)

# print(l%(10**9+7))

# 704


# a,k,l,r = map(int,input().split())
# ty = 0
# for h in range(l,r+1):
#     if h%a==k:
#         ty+=1

# print(ty)

# n = int(input())
# if n == 1:
#   print(2)
# elif n == 2:
#   print(3)
# elif n == 3:
#     print(10)
# elif n == 4:
#   print(21)
# elif n == 5:
#   print(55)
# elif n == 6:
#   print(104)
# elif n == 7:
#   print(221)
# elif n == 8:
#   print(399)
# elif n == 9:
#   print(782)
# elif n == 10:
#   print(1595)
# elif n == 11:
#   print(2759)
# elif n == 12:
#   print(5328)
# elif n == 13:
#   print(9553)
# elif n == 14:
#   print(16211)
# elif n == 15:
#   print(28670)
# elif n == 16:
#   print(52311)
# elif n == 17:
#   print(94223)
# elif n == 18:
#   print(157624)
# elif n == 19:
#   print(280127)
# elif n == 20:
#   print(480315)


# from math import gcd,factorial
# a,b = map(int,input().split())
# print(gcd(factorial(a),factorial(b)))
# from math import factorial
# a,b = map(int,input().split())
# print(factorial(min(a,b))

# a,b,m = map(int,input().split())
# if m==1:
#     print(b)
# elif m==0:
#     print(a)
# else:
#     print(a|b)

#646 masala

# m = int(input())
# a,b,c = map(int,input().split())
# s,d,x,f = map(int,input().split())
# online = (a*b)+((m-a)*c)
# ofline = d+(x*(m/s))+(f*m)


# list1 = []
# from math import gcd,lcm
# n = int(input())
# for xy in range(1,n+1):
#     while True:
#         x = int(input())
#         for a in range(1,x+1):
#             for b in range(1,x+1):
#                 if gcd(a,b) + lcm(a,b)==x:
#                     print(a,b)
#                     break
#                 break
#         break



# n,t,k = map(int,input().split())
# a = []
# for i in range(n):
#   a.append(t)

# for i in range(k):
#   x = a[0]

#   index = a.index(x,0,n)
#   a.pop(index)
#   x-=1
#   a.append(x)
  
# if 0 in a:
#   print(1)
# else:
# 	print(-1)

# n = int(input())
# if n > 8 and n%3==0:
#   print(1)
# elif n > 8 and n%3 !=0:
#   print(3)
# else:
#   print(0)

# hh,mm = input().split(":")
# if hh == "23":
#   hh1 = "00"
# else:
#   hh1 = "o",{int(hh+1)}
# mm1 = hh1[::-1]
# print(hh1,":",mm1)

# n = int(input())
# a=list(map(int,input().split()))
# d,m = map(int,input().split())
# k = 0
# for i in range(n-m+1): 
#   if sum(a[i:i+m])==d: k+=1
# print(k)

# def is_prime(number):
#     if number > 1:
#         for num in range(2, number):
#             if number % num == 0:
#                 return False
#         return True
#     return False

# print(is_prime(4))


# def jamshid(i): 
#      return  max(map(len,i.split('1')))
# s = str(input())
# print(jamshid(s))




# Python3 program to find the position
# of the given prime number
# limit = 1000000
# position = [0]*(limit + 1)
  
# Function to precompute the position
# of every prime number using Sieve
# def sieve():
 
#     # 0 and 1 are not prime numbers
#     position[0] = -1
#     position[1] = -1
  
#     # Variable to store the position
#     pos = 0
#     for i in range(2, limit + 1):
#         if (position[i] == 0):
  
#             # Incrementing the position for
#             # every prime number
#             pos += 1
#             position[i] = pos
#             for j in range( i * 2, limit + 1 ,i):
#                 position[j] = -1
  
# # Driver code
# if __name__ == "__main__":
#     sieve()
  

    # n = int(input())
    # print(position[n])

# i = 1
# x = int(input())
# for k in range(1, x+1):
#     c = 0
#     for j in range(1, i+1):
#         a = i % j
#         if a == 0:
#             c = c + 1

#     if c == 2:
#         print(i)
#     else:
#         k = k - 1

#     i = i + 1

# n = int(input())
# strq = ""
# a = 2
# while True:
#     b = 0
#     for t in range(1,a+1):
#         if a%t==0:
#             b+=1
#         if b<=2:
#             strq+=str(a)
#     a+=1
#     if a>=len(strq):
#         break
# print(strq[n-1])

# from math import *
# a,b,x=map(int,input().split())
# assa=(x+a*(b**(1/2)))(3*x/(4*x+a*b))+abs((3*a-4*b)/(2*a-3*b-4))+e**(a/b)
# print('%.2f'%assa)

# n = int(input())

# for t in range(1,n+1):
#     for h in range(1,n+1):
#         g1=0
#         g2 = 0
#         for hj in range(1,t):
#             if t%hj==0:
#                 g1+=hj
#         for jh in range(1,h):
#             if h%jh==0:
#                 g2+=jh
#         if g1 == h and g2 == t:

#             print(t, h)
#             break

# from math import *
# a,b,x=map(int,input().split())
# hoji=(x+a*(b**(1/2)))**(3*x/(4*x+a*b))+abs((3*a-4*b)/(2*a-3*b-4))+e**(a/b)
# print('%.2f'%hoji)


# a = input()
# 
# s = a.count("1")

# if s%2!=0:
#     print("YES")
# else:
#     print("NO")


# Python 3 program to print
# prime numbers present in
# Fibonacci series.
# import math
 
# # Function to check perfect square
# def isSquare(n) :
#     sr = (int)(math.sqrt(n))
#     return (sr * sr == n)
 
 
# # Prints all numbers less than
# # or equal to n that  are
# # both Prime and Fibonacci.
# def printPrimeAndFib(n) :
     
#     # Using Sieve to generate all
#     # primes less than or equal to n.
#     prime =[True] * (n + 1)
#     p = 2
#     while(p * p <= n ):
         
#         # If prime[p] is not changed,
#         # then it is a prime
#         if (prime[p] == True) :
             
#             # Update all multiples of p
#             for i in range(p * 2, n + 1, p) :
#                 prime[i] = False
                 
#         p = p + 1
     
#     # Now traverse through the range
#     # and print numbers that are
#     # both prime and Fibonacci.
#     for i in range(1, n + 1) :
#         if (prime[i] and (isSquare(5 * i * i + 4) > 0 or
#              isSquare(5 * i * i - 4) > 0)) :
#             print( i , "",end="")
 
 
# # Driver function
# n = int(input())
# printPrimeAndFib(n)
 


 
# This code is contributed


# by Jamshid Ahmadov  >maenlaer<

# a = int(input())
# b = int(input())
# c = a+b
# print(c)    


# a = input()
# y2 = int(input())
# for t in range(1,y2+1):
#     k1 = 0
#     k2 = 0
#     j,k = map(int,input().split())
#     for fa in a[j-1:k]:
        
#         if fa == fa.lower():
#             k2 += 1
#         elif fa == fa.upper():
#             k1 += 1
#     if k1 < k2:
#         print("Kichik harflar")
#     elif k1 > k2:
#         print("Katta harflar")
#     else:
#         print("Teng")

# i = 0
# n,s,m = map(int,input().split())
# for kj in range(1,m+1):
#     a,b = map(str,input().split("-"))
#     hh1  = a[0] + a[1]
#     mm1 = a[3] + a[4]

#     hh2 = b[0] + b [1]
#     mm2 = b[3]+b[4]

#     vaqt1 = 60*int(hh1)+int(mm1)
#     vaqt2 = 60*int(hh2)+int(mm2)

#     vaqt_u = vaqt2+vaqt1
#     i+=vaqt_u
# i *= s
# if n>i:
#     print(n-i)
# else:
#     print(0)

# print(i)
# m = int(input())
# pa = ""
# a = input()
# for j in a:
#     if j == "a":
#         pa+="l"
#     elif j == "q":
#         pa+="p"
#     elif j == "w":
#         pa+="q"
#     elif j == "e":
#         pa+="w"
#     elif j == "r":
#         pa+="e"
#     elif j=="t":
#         pa+="r"
#     elif j == "y":
#         pa+="t"
#     elif j == "u":
#         pa+="y"
#     elif j == "i":
#         pa+="u"
#     elif j == "o":
#         pa+="i"
#     elif j == "p":
#         pa+="o"
#     elif j == "a":
#         pa+="l"
#     elif j == "s":
#         pa+="a"
#     elif j == "d":
#         pa+="s"
#     elif j == "f":
#         pa+="d"
#     elif j == "g":
#         pa+="f"
#     elif j == "h":
#         pa+="g"
#     elif j == "j":
#         pa+="h"
#     elif j == "k":
#         pa+="j"
#     elif j == "l":
#         pa+="k"
#     elif j == "z":
#         pa+="m"
#     elif j == "x":
#         pa+="z"
#     elif j == "c":
#         pa+="x"
#     elif j == "v":
#         pa+="c"
#     elif j== "b":
#         pa+="v"
#     elif j == "n":
#         pa+="b"
#     elif j == "m":
#         pa+="n"
#     else:
#         pa+=j
# print(pa)


 
# recursive function to generate all
# possible permutations of a string
# def generate_permutations(ch, idx, result):
#     # base case
#     if idx == len(ch):
#         str1 = ""
#         result.append(str1.join(ch))
#         return
 
#     # traverse string from idx to end
#     for i in range(idx, len(ch)):
#         ch[i], ch[idx] = ch[idx], ch[i]
#         generate_permutations(ch, idx + 1, result)
#         ch[i], ch[idx] = ch[idx], ch[i]
 
# # Function to find the
# # kth permutation of n numbers
# def findKthPermutation(n, k):
#     s = ""
#     result = []
 
#     # Insert all natural number
#     # upto n in string
#     for i in range(1, n + 1):
#         s += str(i)
 
#     ch = [*s]
#     generate_permutations(ch, 0, result)
 
#     # sort the generated permutations
#     result.sort()
 
#     # make k 0-based indexed to point to kth sequence
#     return result[k - 1]
 
 
# # Driver code
# if __name__ == "__main__":
#     n = int(input())
#     k = int(input())
 
#     # function call
#     kth_perm_seq = findKthPermutation(n, k)
#     print(kth_perm_seq)
 
# This code is contributed by Tapesh(tapeshdua420)




# a = input()
# y2 = int(input())
# for t in range(1,y2+1):
#     k1 = 0
#     k2 = 0
#     j,k = map(int,input().split())
#     for fa in a[j-1:k]:
#         if fa == fa.lower():
#             k2 += 1
#         elif fa == fa.upper():
#             k1 += 1
#     if k1 < k2:
#         print("Kichik harflar")
#     elif k1 > k2:
#         print("Katta harflar")
#     elif k1 == k2:
#         print("Teng")



# list2= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# a = input()
# n = int(input())
# list1 = []
# for mn in a:
#     for kl1 in list2:
#         if kl1.lower()==mn.lower():
#             if mn == mn.lower() and mn.lower()!=mn.upper():
#                 list1.append("1")
#             if mn == mn.upper()  and mn.lower()!=mn.upper():
#                 list1.append("0")
# for gh in range(1,n+1):
#     j,h = map(int,input().split())
#     a = list1[j-1:h].count("1")
#     b = list1[j-1:h].count("0")
#     if a>b:
#         print("Kichik harflar")
#     elif a<b:
#         print("Katta harflar")
#     elif a==b:
#         print("Teng")        



# Python program to convert Roman
# Numerals to Numbers

# This function returns value of
# each Roman symbol


# def value(r):
# 	if (r == 'I'):
# 		return 1
# 	if (r == 'V'):
# 		return 5
# 	if (r == 'X'):
# 		return 10
# 	if (r == 'L'):
# 		return 50
# 	if (r == 'C'):
# 		return 100
# 	if (r == 'D'):
# 		return 500
# 	if (r == 'M'):
# 		return 1000
# 	return -1

# def romanToDecimal(str):
# 	res = 0
# 	i = 0

# 	while (i < len(str)):

# 		# Getting value of symbol s[i]
# 		s1 = value(str[i])

# 		if (i + 1 < len(str)):

# 			# Getting value of symbol s[i + 1]
# 			s2 = value(str[i + 1])

# 			# Comparing both values
# 			if (s1 >= s2):

# 				# Value of current symbol is greater
# 				# or equal to the next symbol
# 				res = res + s1
# 				i = i + 1
# 			else:

# 				# Value of current symbol is greater
# 				# or equal to the next symbol
# 				res = res + s2 - s1
# 				i = i + 2
# 		else:
# 			res = res + s1
# 			i = i + 1

# 	return res

# # Driver code

# print(romanToDecimal(input()))




# class Solution(object):
#    def romanToInt(self, s):
#       """
#       :type s: str
#       :rtype: int
#       """
#       roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
#       i = 0
#       num = 0
#       while i < len(s):
#          if i+1<len(s) and s[i:i+2] in roman:
#             num+=roman[s[i:i+2]]
#             i+=2
#          else:
#             #print(i)
#             num+=roman[s[i]]
#             i+=1
#       return num
# ob1 = Solution()
# print(ob1.romanToInt(input()))


# Python3 program to convert
# integer value to roman values
  
# Function to convert integer to Roman values
# def printRoman(number):
#     num = [1, 4, 5, 9, 10, 40, 50, 90,
#         100, 400, 500, 900, 1000]
#     sym = ["I", "IV", "V", "IX", "X", "XL",
#         "L", "XC", "C", "CD", "D", "CM", "M"]
#     i = 12
      
#     while number:
#         div = number // num[i]
#         number %= num[i]
  
#         while div:
#             print(sym[i], end = "")
#             div -= 1
#         i -= 1
  
# # Driver code
# if __name__ == "__main__":
#     number = int(input())
#     printRoman(number)

# a = int(input()) 
# u=0
# b = 1
# c = 3
# bn = a
# mn = a-1

# while u!=a:
#     print((bn)*" ",b*"*")
#     print((mn)*" ",c*"*")
#     c+=2
#     u+=1
#     mn-=1
# print((bn)*" ","*")

# print("Jamshid" if(2%2) else "Antisocial")


# a = input()
# t = []
# for x in a:
#     if x=="1":
#         t.append("1")
#     elif x == "6":
#         t.append("9")
#     elif x =="0":
#         t.append("0")
#     elif x=="9":
#         t.append("6")
#     elif x=="8":
#         t.append("8")
#     elif x=="2":
#         t.append("2")
#     elif x=="3":
#         t.append("3")
#     elif x=="4":
#         t.append("4")
#     elif x=="5":
#         t.append("5")
#     elif x=="7":
#         t.append("7")
      
# t.reverse()
# g=""
# for n in t:
#     g+=n
# if a==g:
#     print("YES")
# else:
#     print("NO")

# from math import ceil
# a = int(input())
# if a ==1:
#     print(1)
# elif a==2:
#     print(2)
# elif a == 3:
#     print(2)
# elif a==4:
#     print(3)
# else:
#     print(ceil(a/2))
# a = input()
# if a == "00:00":
#   print("01:10")
# elif a == "01:10":
#   print("02:20")
# elif a == "02:20":
#   print("03:30")
# elif a == "03:30":
#   print("04:40")
# elif a == "05:50":
#   print("10:01")
# elif a == "10:01":
#   print("11:11")
# elif a=="12:21":
#   print("13:31")
# elif a == "13:31":
#   print("14:41")
# elif a == "14:41":
#   print("15:51")
# elif a == "15:51":
#   print("20:02")
# elif a == "20:02":
#   print("21:12")
# elif a == "21:12":
#   print("22:22")
# elif a == "22:22":
#   print("23:32")
# elif a == "23:32":
#   print("00:00")

# n = int(input())
# list1 = list(map(int,input().split()))
# jh = int(input())
# for th in range(1,jh+1):
#     l,r,x = map(int,input().split())
#     for el in list1[l-1:r]:
#         el+=x   
        
# for lkjh in list1:
#     print(lkjh, end=" ")

# python program to print prime factors
 

# list1= []
# import math
# def primefactors(n):
#    #even number divisible
#    while n % 2 == 0:
#       print (2),
#       n = n / 2
    
#    #n became odd
#    for i in range(3,int(math.sqrt(n))+1,2):
     
#       while (n % i == 0):
#          print (i)
#          n = n / i
    
#    if n > 2:
#       print (n)
 
# n = int(input())
# primefactors(n)

# def divisor(n):
#   x = len([i for i in range(1,n+1) if not n % i])
#   return x
# print(divisor(int(input())))


# import math as m
# l = input()
# r=m.trunc(m.sqrt(len(l)))
# c= r if r*r ==len(l) else r+1
# k=0
# m=["" for i in range(c)]
# for x in l:
#   m[k%c]+=x
#   k+=1
  
# for w in m:print(w,end=" ")
# ab=input()
# print(int(ab[0])+int(ab[1]))


# print_element = 0
# number = input()
# for t in number:
#     print_element+=int(t)

# print(print_element)

# a,b = map(int,input().split(" "))
# print(a+b)

# def jamshid(x1,x2,x3,x4,y1,y2,y3,y4):
#   a = (((x1-x2)**2)+((y1-y1)**2))
#   b = (((x1-x4)**2)+((y1-y4)**2))
#   if a == b:
#     return "YES"
#   else:
#     return "NO"

# t = int(input())
# for i in range(t):
#   x1,x2,x3,x4 = map(int,input().split())
#   y1,y2,y3,y4 = map(int,input().split())
#   print(jamshid(x1,x2,x3,x4,y1,y2,y3,y4))

# n = int(input())
# l=0
# for t in range(1,n+1):
#     l+=(n)/(1+(n**2)+(n**4))
    
# print('%.2f' % l)

# a,b = map(int,input().split(":"))
# print(a,b)


# from math import sqrt
# a,b,c = map(int,input().split())
# D = b**2 - (4*a*c)

# x1 = (-b+sqrt(D))/(2*a)
# x2 = (-b-sqrt(D))/(2*a)
# if x1 != x2:
#     print('%.4f' % x1, '%.4f' % x2)
# else:
#     print('%.4f' % x1)

# k = 0
# n = int(input())
# for t in range(n+1):
#     for x in range(n+1):
#         for g in range(n+1):
#             if t+x+g == n:
#                 k+=1

# print(k)

# list_n = ["1","2","3","4","5","6","7","8","9","0"]
# k = ""
# a = input()
# for t in a:
#     for lm in list_n:
#         if t == lm:
#             for qr in a[::t]:
#                 k+=t*qr
#             a.pop[::t]
# print(k)

# if = int(input())
# print(if)


# def smallest_num(a, b, n): 
  
#     # declaring variable 
#     k = n // (a + b) 

#     # calculating remainder 
#     r = n % (a + b) 

#     # if remainder is equal to a 
#     if (r == a): 
#         k += 1

#     # returning smallest number 
#     return (k * a + (k - 1) * b) 

# # Driver code 
# a,b,n = map(int,input().split())

# print(smallest_num(a, b, n))

# d,m,y = map(int,input().split())
# days = d+(m*30)+(y*365)
# mn = days%7
# if mn == 0:
#     print("SUNDAY")
# elif mn == 1:
#     print("DUSH")
# elif mn == 2:
#     print("SE")
# elif mn == 3:
#     print("CH")
# elif mn == 4:
#     print("PAY")
# elif mn == 5:
#     print("JU")
# elif mn == 6:
#     print("sh")


# import datetime

# # Enter day, month and year
# day,month,year = map(int,input().split())

# # Convert to datetime object
# date = datetime.date(year, month, day)

# # Output the day of the week
# print(date.strftime("%A").upper())

#     N = int(input())
# K = int(input())

# for i in range(1, N+1):
#     if i % K != 0:
#         print(i)

# function to convert krill script to latin
# def krillToLatin(text):
  # split the text into words
#   words = text.split()
#   # a python dictionary to hold the replacements
#   replacements = {
#       'ða': 'the',
#       'n': 'and',
#       'G': 'g',
#       'a': 'a',
#       'b': 'b',
#       'd': 'd',
#       'e': 'e',
#       'f': 'f',
#       'g': 'g',
#       'h': 'h',
#       'i': 'i',
#       'j': 'j',
#       'k': 'k',
#       'l': 'l',
#       'm': 'm',
#       'n': 'n',
#       'o': 'o',
#       'p': 'p',
#       'q': 'q',
#       'r': 'r',
#       's': 's',
#       't': 't',
#       'u': 'u',
#       'v': 'v',
#       'w': 'w',
#       'x': 'x',
#       'y': 'y',
#       'z': 'z'
#   }
#   # loop through the words
#   for i in range(len(words)):
#     # loop through each letter in the word
#     for j in range(len(words[i])):
#       # check if the letter is in the replacements
#       if words[i][j] in replacements:
#         # if it is, replace it with the correct letter
#         words[i] = words[i].replace(words[i][j], replacements[words[i][j]])
#   # return the translated text
#   return ' '.join(words)

# # test
# print(krillToLatin('ða n Gaj bd efghijklmnopqrstuvwxyz'))
# # output: the and Gag d efghijklmnopqrstuvwxyz

# def main():
#     russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#     english_alphabet = "abcdefghijklmnopqrstuvwxyz"

#     user_input = input("Enter a word or phrase in the Russian alphabet: ").lower()

#     english_translation = ""

#     for letter in user_input:
#         if letter in russian_alphabet:
#             index = russian_alphabet.find(letter)
#             english_translation += english_alphabet[index]
#         else:
#             english_translation += letter

#     print(english_translation)

# main()


# t = int(input())
# for y in range(1,t+1):
#     x,y,a,b = map(int,input().split())
#     if (y-x) % (a+b) == 0:
#         print(int((y-x)/(a+b)))    
#     else:
#         print(-1)
# n = int(input())
# a = input()
# L = a.count("L")
# R = a.count("R")
# print(L+R+1)

# t = int(input())
# for jh in range(1,t+1):
#     list1 = list(map(int,input().split()))
#     list1.sort()
#     if list1[0] + list1[1] >=list1[2]:
#         print("yes")
#     else:
#         print("no")

# n, q =map(int,input().split())
# list1 = list(map(int,input().split()))
# list1.sort()
# for yu in range(1,q+1):
#     l,r = map(int,input().split())

# o = []
# n,r = map(int,input().split())
# lis1 = list(map(int,input().split()))
# for h in lis1:
#     io =lis1.index(h)

#     if io==0 or lis1.index(h) == n-1:
#         o.append(h)
#     else:

# i = int(input("Enter a number: "))

# for x in range(1, i+1):
#     if x > 1:
#         for y in range(2, x):
#             if (x % y) == 0:
#                 print("mee")
#                 break
#         else:
#             print("pee")



# global_variable = 1
# if global_variable != 1:
#     for yt in range(2,global_variable):
#         if global_variable%yt==0:
#             print("Pee")
#         else:
#             print("Mee")
# else:
#     print("Mee")
# global_variable+=1

#!/usr/bin/env python3
# """       xturtle-example-suite:

#           xtx_kites_and_darts.py

# Constructs two aperiodic penrose-tilings,
# consisting of kites and darts, by the method
# of inflation in six steps.

# Starting points are the patterns "sun"
# consisting of five kites and "star"
# consisting of five darts.

# For more information see:
#  http://en.wikipedia.org/wiki/Penrose_tiling
#  -------------------------------------------
# """
# from turtle import *
# from math import cos, pi
# from time import perf_counter as clock, sleep

# f = (5**0.5-1)/2.0   # (sqrt(5)-1)/2 -- golden ratio
# d = 2 * cos(3*pi/10)

# def kite(l):
#     fl = f * l
#     lt(36)
#     fd(l)
#     rt(108)
#     fd(fl)
#     rt(36)
#     fd(fl)
#     rt(108)
#     fd(l)
#     rt(144)

# def dart(l):
#     fl = f * l
#     lt(36)
#     fd(l)
#     rt(144)
#     fd(fl)
#     lt(36)
#     fd(fl)
#     rt(144)
#     fd(l)
#     rt(144)

# def inflatekite(l, n):
#     if n == 0:
#         px, py = pos()
#         h, x, y = int(heading()), round(px,3), round(py,3)
#         tiledict[(h,x,y)] = True
#         return
#     fl = f * l
#     lt(36)
#     inflatedart(fl, n-1)
#     fd(l)
#     rt(144)
#     inflatekite(fl, n-1)
#     lt(18)
#     fd(l*d)
#     rt(162)
#     inflatekite(fl, n-1)
#     lt(36)
#     fd(l)
#     rt(180)
#     inflatedart(fl, n-1)
#     lt(36)

# def inflatedart(l, n):
#     if n == 0:
#         px, py = pos()
#         h, x, y = int(heading()), round(px,3), round(py,3)
#         tiledict[(h,x,y)] = False
#         return
#     fl = f * l
#     inflatekite(fl, n-1)
#     lt(36)
#     fd(l)
#     rt(180)
#     inflatedart(fl, n-1)
#     lt(54)
#     fd(l*d)
#     rt(126)
#     inflatedart(fl, n-1)
#     fd(l)
#     rt(144)

# def draw(l, n, th=2):
#     clear()
#     l = l * f**n
#     shapesize(l/100.0, l/100.0, th)
#     for k in tiledict:
#         h, x, y = k
#         setpos(x, y)
#         setheading(h)
#         if tiledict[k]:
#             shape("kite")
#             color("black", (0, 0.75, 0))
#         else:
#             shape("dart")
#             color("black", (0.75, 0, 0))
#         stamp()

# def sun(l, n):
#     for i in range(5):
#         inflatekite(l, n)
#         lt(72)

# def star(l,n):
#     for i in range(5):
#         inflatedart(l, n)
#         lt(72)

# def makeshapes():
#     tracer(0)
#     begin_poly()
#     kite(100)
#     end_poly()
#     register_shape("kite", get_poly())
#     begin_poly()
#     dart(100)
#     end_poly()
#     register_shape("dart", get_poly())
#     tracer(1)

# def start():
#     reset()
#     ht()
#     pu()
#     makeshapes()
#     resizemode("user")

# def test(l=200, n=4, fun=sun, startpos=(0,0), th=2):
#     global tiledict
#     goto(startpos)
#     setheading(0)
#     tiledict = {}
#     tracer(0)
#     fun(l, n)
#     draw(l, n, th)
#     tracer(1)
#     nk = len([x for x in tiledict if tiledict[x]])
#     nd = len([x for x in tiledict if not tiledict[x]])
#     print("%d kites and %d darts = %d pieces." % (nk, nd, nk+nd))

# def demo(fun=sun):
#     start()
#     for i in range(8):
#         a = clock()
#         test(300, i, fun)
#         b = clock()
#         t = b - a
#         if t < 2:
#             sleep(2 - t)

# def main():
#     #title("Penrose-tiling with kites and darts.")
#     mode("logo")
#     bgcolor(0.3, 0.3, 0)
#     demo(sun)
#     sleep(2)
#     demo(star)
#     pencolor("black")
#     goto(0,-200)
#     pencolor(0.7,0.7,1)
#     write("Please wait...",
#           align="center", font=('Arial Black', 36, 'bold'))
#     test(600, 8, startpos=(70, 117))
#     return "Done"

# if __name__ == "__main__":
#     msg = main()
#     mainloop()


