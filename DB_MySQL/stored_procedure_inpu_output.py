import mysql.connector
from mysql.connector import Error,MySQLConnection


##single input single output
def test_proc1(cursor):
    ##check procedure exists
    cursor.execute("show procedure status where name ='getStatusByCountry'")
    result = cursor.fetchone()
    if result[1] == "getStatusByCountry":
        print("stored procedure exists")
    else:
        print("stored procedure does not exists")

    ## call the stored procedure
    ## argument must be a sequence
    ## 0 is placeholder for output
    data = cursor.callproc('getStatusByCountry', (102, 0))

    # print results
    print("Printing Status By Country", data, type(data))

#single input multiple output
def test_proc2(cursor):
    ##check procedure exists
    cursor.execute("show procedure status where name ='get_order_by_customer_no'")
    result = cursor.fetchone()
    if result[1] == "get_order_by_customer_no":
        print("stored procedure exists")
    else:
        print("stored procedure does not exists")

    ## call the stored procedure
    ## argument must be a sequence
    ## 0 is placeholder for output
    data = cursor.callproc('get_order_by_customer_no', (144,0,0,0,0,0))

    # print results
    print("Printing order by customer number", data, type(data))

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='classicmodels',
                                         user='root',
                                         password='root')
    cursor = connection.cursor()

    ## call stored procedures
    # 'getStatusByCountry'
    # 'get_order_by_customer_no'
    # 'handleDuplicatePaymentError'
    # 'SelectAllCustomers'
    # 'SelectCustomersByCity'
    # 'SelectCustomersByCityCode'
    test_proc1(cursor)

    test_proc2(cursor)


except mysql.connector.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    else:
        print("connection already closed")