import mysql.connector as mysql
mydb=mysql.connect(host="localhost", user="root", password="kvafs123")

#CREATING DATABASE AND TABLE
mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")

while True:
    print("""1:Signup
             2:Login""")

    ch=int(input("SIGNUP/LOGIN(1,2):"))

#SIGNUP
    if ch==1:

        username=input("ENTER USERNAME:")
        pw=input("ENTER PASSWORD:")

        mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
        mydb.commit()

#LOGIN
    elif ch==2:

        username=input("YOUR USERNAME PLEASE:")

        mycursor.execute("select username from signup where username='"+username+"'")
        pot=mycursor.fetchone()

        if pot is not None:
            print("VALID USERNAME!!!!!!")

            pw=input("ENTER YOUR PASSWORD PLEASE :")

            mycursor.execute("select password from signup where password='"+pw+"'")
            a=mycursor.fetchone()

            if a is not None:
                print("""+++++++++++++++++++++++
+++LOGIN SUCCESSFULL+++
+++++++++++++++++++++++""")

                print("""======================================================================
++++++++++++++++++++++++++    MY BOOK STORE     +++++++++++++++++++++++++
==========================================================================""")

                mycursor.execute("create table if not exists Available_Books(BookName varchar(30) primary key,Genre varchar(20),\
Quantity int(3),Author varchar(20),Publication varchar(30),Price int(4))")
                mycursor.execute("create table if not exists Sell_rec(CustomerName varchar(20),PhoneNumber char(10) unique key, \
BookName varchar(30),Quantity int(100),Price int(4),foreign key (BookName) references Available_Books(BookName))")
                mycursor.execute("create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber char(10) unique key , Address varchar(40))") 
                mydb.commit()

                while(True):
                    print("""1:Add Books
2:Delete Books
3:Search Books
4:Staff Details
5:Sell Record
6:Available Books
7:Total Income after the Latest Reset 
8:Exit""")

                    a=int(input("ENTER YOUR CHOICE PLEASE FROM ABOVE CHOICE:"))

    #ADD BOOKS
                    if a==1:

                        print("All information prompted are mandatory to be filled")
                    
                        book=str(input("Enter Book Name:"))
                        genre=str(input("Genre(BOOK TYPE):"))
                        quantity=int(input("Enter quantity:"))        
                        author=str(input("Enter author name:"))
                        publication=str(input("Enter publication house:"))
                        price=int(input("Enter the price:"))

                        mycursor.execute("select * from Available_Books where bookname='"+book+"'")
                        row=mycursor.fetchone()

                        if row is not None:
                            mycursor.execute("update Available_Books set quantity=quantity+'"+str(quantity)+"' where bookname='"+book+"'")
                            mydb.commit()

                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")
                        
                        
                        else:
                            mycursor.execute("insert into Available_Books(bookname,genre,quantity,author,publication,price) values('"+book+"\
','"+genre+"','"+str(quantity)+"','"+author+"','"+publication+"','"+str(price)+"')")
                            mydb.commit()

                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""") 
                   

    #DELETE BOOKS
                    elif a==2:                

                        print("AVAILABLE BOOKS...")

                        mycursor.execute("select * from Available_Books ")
                        for x in mycursor:
                            print(x)
                      
                        cusname=str(input("Enter customer name:"))
                        phno=int(input("Enter phone number:"))
                        book=str(input("Enter Book Name:"))
                        price=int(input("Enter the price:"))
                        n=int(input("Enter quantity:"))

                        mycursor.execute("select quantity from available_books where bookname='"+book+"'")
                        lk=mycursor.fetchone()

                        if max(lk)<n:
                            print(n,"Books are not available!!!!")

                        else:
                            mycursor.execute("select bookname from available_books where bookname='"+book+"'")
                            log=mycursor.fetchone()

                            if log is not None:
                                mycursor.execute("insert into Sell_rec values('"+cusname+"','"+str(phno)+"','"+book+"','"+str(n)+"','"+str(price)+"')")
                                mycursor.execute("update Available_Books set quantity=quantity-'"+str(n)+"' where BookName='"+book+"'")
                                mydb.commit()

                                print("""++++++++++++++++++++++
++BOOK HAS BEEN SOLD++
++++++++++++++++++++++""")

                            else:
                                print("BOOK IS NOT AVAILABLE!!!!!!!")

    #SEARCH BOOKS ON THE BASIS OF GIVEN OPTIONS
                    elif a==3:

                        print("""1:Search by name
2:Search by genre
3:Search by author""")

                        l=int(input("Search by?:"))

        #BY BOOKNAME
                        if l==1:
                            o=input("Enter Book to search:")

                            mycursor.execute("select bookname from available_books where bookname='"+o+"'")
                            tree=mycursor.fetchone()

                            if tree!=None:
                                print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")

                            else:
                                print("BOOK IS NOT IN STOCK!!!!!!!")

        #BY GENRE
                        elif l==2:
                            g=input("Enter genre to search:")

                            mycursor.execute("select genre from available_books where genre='"+g+"'")
                            poll=mycursor.fetchall()

                            if poll is not None:
                                print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")

                                mycursor.execute("select * from available_books where genre='"+g+"'")

                                for y in mycursor:
                                    print(y)

                            else:
                                print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!!!!!")


        #BY AUTHOR NAME
                        elif l==3:
                            au=input("Enter author to search:")

                            mycursor.execute("select author from available_books where author='"+au+"'")
                            home=mycursor.fetchall()

                            if home is not None:
                                print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")

                                mycursor.execute("select * from available_books where author='"+au+"'")

                                for z in mycursor:
                                    print(z)

                            else:
                                print("BOOKS OF THIS AUTHOR ARE NOT AVAILABLE!!!!!!!")
                        mydb.commit()

    #STAFF DETAILS
                    elif a==4:
                        print("1:New staff entry")
                        print("2:Remove staff")
                        print("3:Existing staff details")

                        ch=int(input("Enter your choice:"))

        #NEW STAFF ENTRY
                        if ch==1:
                            fname=str(input("Enter Fullname:"))
                            gender=str(input("Gender(M/F/O):"))
                            age=int(input("Age:"))
                            phno=int(input("Staff phone no.:"))
                            add=str(input("Address:"))

                            mycursor.execute("insert into Staff_details(name,gender,age,phonenumber,address)\
values('"+fname+"','"+gender+"','"+str(age)+"','"+str(phno)+"','"+add+"')")
                            print("""+++++++++++++++++++++++++++++
+STAFF IS SUCCESSFULLY ADDED+
+++++++++++++++++++++++++++++""")
                            mydb.commit()

        #REMOVE STAFF
                        elif ch==2:
                            nm=str(input("Enter staff name to remove:"))
                            mycursor.execute("select name from staff_details where name='"+nm+"'")
                            toy=mycursor.fetchone()

                            if toy is not None:
                                mycursor.execute("delete from staff_details where name='"+nm+"'")
                                print("""+++++++++++++++++++++++++++++++++
++STAFF IS SUCCESSFULLY REMOVED++
+++++++++++++++++++++++++++++++++""")
                                mydb.commit()

                            else:
                                print("STAFF DOESNOT EXIST!!!!!!")

        #EXISTING STAFF DETAILS
                        elif ch==3:
                            mycursor.execute("select * from Staff_details")
                            run=mycursor.fetchone()
                            for t in mycursor:
                                print(t)
                            if run is not None:
                                print("EXISTING STAFF DETAILS...")                        
                                for t in mycursor:
                                    print(t)

                            else:
                                print("NO STAFF EXISTS!!!!!!!")
                            mydb.commit()

    #SELL HISTORY                                
                    elif a==5:
                        print("1:Sell history details")
                        print("2:Reset Sell history")

                        ty=int(input("Enter your choice:"))

                        if ty==1:
                            mycursor.execute("select * from sell_rec")
                            for u in mycursor:
                                print(u)

                        if ty==2:
                            bb=input("Are you sure(Y/N):")

                            if bb=="Y":
                                mycursor.execute("delete from sell_rec")
                                mydb.commit()

                            elif bb=="N":
                                pass

    #AVAILABLE BOOKS
                    elif a==6:
                        mycursor.execute("select * from available_books order by bookname")
                        for v in mycursor:
                            print(v)

    #TOTAL INCOME AFTER LATEST UPDATE
                    elif a==7:
                        mycursor.execute("select sum(price) from sell_rec")
                        for x in mycursor:
                            print(x)
    #EXIT                    
                    elif a==8:
                        break

#LOGIN ELSE PART
            else:
                print("""++++++++++++++++++++++
++INCORRECT PASSWORD++
++++++++++++++++++++++""")


        else:
            print("""++++++++++++++++++++
++INVALID USERNAME++
++++++++++++++++++++""")

    else:
        break
