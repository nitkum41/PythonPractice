import mysql.connector
from mysql.connector import Error

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

    ##check procedure exists
    cursor.execute("show procedure status where name ='SelectAllCustomers'")
    result = cursor.fetchone()
    if result[1]=="SelectAllCustomers":
        print("stored procedure exists")
    else:
        print("stored procedure does not exists")


    ## call the stored procedure
    cursor.callproc('SelectAllCustomers')

    # print results
    print("Printing Customers")
    stored_procedure_result_rows=[]

    # print(len(list(cursor.stored_results())))
    for result in cursor.stored_results():
        # print(result.fetchall())
        stored_procedure_result_rows = result.fetchall()  ##get all rows
    # for r in stored_procedure_result_rows:
    #     print(r)
        # print(result.fetchmany())

    ##fetch test query data
    cursor.execute("select * from customers")
    test_query_data = cursor.fetchall()


    ##check data is same from both the result set
    print(test_query_data==stored_procedure_result_rows)

except mysql.connector.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    else:
        print("connection already closed")