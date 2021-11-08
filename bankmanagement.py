import mysql.connector
mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '*******' , database = 'bank_system')

def openacc():
    n = input("enter your name : ")
    ac = input("enter the account no : ")
    db = input("enter the date of birth : ")
    add = input("enter the addres : ")
    cn = int(input("enter contact number : "))
    ob = int(input("enter the opening balance : "))
    details1 = (n , ac , db , add , cn , ob)
    details2 = (n , ac , ob)

    sql1 = ('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into amount values (%s,%s,%s)')

    var1 = mydb.cursor()
    var1.execute(sql1 , details1)
    var1.execute(sql2 , details2)
    mydb.commit()
    print("Data entered successfully .")
    main()

def depositamount():
    amount = int(input("enter the amount to deposit : "))
    ac = input("enter the account no : ")
    a = 'select balance from amount where account_no = %s'
    data1 = (ac, )

    var1 = mydb.cursor()
    var1.execute(a , data1)
    result = var1.fetchone()
    t = result[0] + amount

    k = ('update amount set balance = %s WHERE account_no = %s')
    data1 = (t , ac)
    var1.execute(k , data1)
    mydb.commit()
    main()


def  withdrawamount():
    amount = int(input("enter the amount to withdraw : "))
    ac = input("enter the account no : ")
    a = 'select balance from amount where account_no = %s'
    data1 = (ac,)

    var1 = mydb.cursor()
    var1.execute(a, data1)
    result = var1.fetchone()
    t = result[0] - amount

    sql = ('update amount set balance = %s where account_no = %s')
    d = (t, ac)
    var1.execute(sql, d)
    mydb.commit()
    main()

def balenq():
    ac = input("enter the account number : ")
    a =  'select * from amount where account_no = %s'

    data = (ac , )
    x = mydb.cursor()
    x.execute(a , data)
    result = x.fetchone()
    print("balance for account no : " , ac , "is" , result[-1])
    mydb.commit()
    main()

def discusdet():
    ac = input("enter the account number : ")
    a = 'select * from account where account_no = %s'

    data = (ac,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()

def closeacc():
    ac = input("enter the account number : ")
    sql1 = 'delete from account where account_no = %s'
    sql2 = 'delete from amount where account_no = %s'
    data = (ac, )
    x = mydb.cursor()
    x.execute(sql1 , data)
    x.execute(sql2 , data)
    mydb.commit()
    main()

def main():
    print("1: OPEN NEW ACCOUNT, 2: DEPOSIT ACCOUNT, 3: WITHDRAWW ACCOUNT ,4: BALANCE ENQUIRY, 5: DISPLAY CUSTOMERS DETAILS , 6: CLOSE AN ACCOUNT")

    task = int(input("enter the number of the task you want to perform : "))

    if task == 1:
        openacc()
    elif task == 2:
        depositamount()
    elif task == 3:
        withdrawamount()
    elif task == 4:
        balenq()
    elif task == 5:
        discusdet()
    elif task == 6:
        closeacc()
    else:
        print("invalid input ")
        main()

main()
