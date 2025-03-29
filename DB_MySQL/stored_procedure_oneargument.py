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
    cursor.execute("show procedure status where name ='SelectCustomersByCity'")
    result = cursor.fetchone()
    if result[1] == "SelectCustomersByCity":
        print("stored procedure exists")
    else:
        print("stored procedure does not exists")

    ## call the stored procedure
    ## argument must be a sequence
    cursor.callproc('SelectCustomersByCity',('Singapore',))

    # print results
    print("Printing Customers by city")
    stored_procedure_result_rows = []

    # print(len(list(cursor.stored_results())))
    for result in cursor.stored_results():
        # print(result.description)
        columns = [col_data[0] for col_data in result.description]  ###get columns
        print(columns)
        stored_procedure_result_rows = result.fetchall()  ##get all rows
    for r in stored_procedure_result_rows:
        print(r)
        # print(result.fetchmany())

    ##fetch test query data
    cursor.execute("select * from customers where city='Singapore'")
    test_query_data = cursor.fetchall()



    ##check if two result sets are equal
    print(stored_procedure_result_rows==test_query_data)
except mysql.connector.Error as error:
    print("Failed to execute stored procedure: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
    else:
        print("connection already closed")