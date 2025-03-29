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
    stored_procedure_data = cursor.callproc('getStatusByCountry', (102,0))

    # print results
    print("Printing Status By Country", stored_procedure_data, type(stored_procedure_data))

    test_query = """ 
    select country ,
	case 
		when 'USA' then '2-Day-Shipping'
		when 'Canada' then '3-Day-Shipping'
		else '5-Day-Shipping'
	End as Ship
      from customers where customerNumber=112;"""
    cursor.execute(test_query)
    test_query_data = cursor.fetchall()

    # print results
    print("Printing Status By Country", test_query_data, type(test_query_data))

    ##checking data
    if stored_procedure_data[0]==102 and test_query_data[0][0]=="USA":
        if stored_procedure_data[1]==test_query_data[0][1]:
            print("data equal")

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
    stored_procedure_data = cursor.callproc('get_order_by_customer_no', (144,0,0,0,0,0))
    # print results
    print("Printing order by customer number", stored_procedure_data, type(stored_procedure_data))

    ##test query
    ##fetch test query data
    test_query = """
    select 
    (select count(*) from orders where customernumber=144 and status ='Shipped') shipped ,
    (select count(*) from orders where customernumber=144 and status ='Resolved') resolved,
    (select count(*) from orders where customernumber=144 and status ='Cancelled') cancelled,
    (select count(*)  from orders where customernumber=144 and status ='Disputed') disputed,
    (select count(*)  from orders where customernumber=144 and status IN ('On Hold','In Process')) hold;
    """
    cursor.execute(test_query)
    test_query_data = cursor.fetchall()


    print("Printing order by customer number", test_query_data, type(test_query_data))

    ##compare
    print(stored_procedure_data[1:]==test_query_data[0])


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