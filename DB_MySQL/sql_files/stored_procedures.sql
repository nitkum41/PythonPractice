create database classicmodels;
use classicmodels;

-- show tables;

-- describe information_schema.columns;

-- select count(*) totalcolumns from information_schema.columns where table_name="customers";

-- select COLUMN_NAME , DATA_TYPE  from information_schema.columns where table_name="customers";

-- select COLUMN_NAME , COLUMN_TYPE  from information_schema.columns where table_name="customers";

-- select COLUMN_NAME , IS_NUllable from information_schema.columns where table_name="customers";

-- select COLUMN_NAME , COLUMN_KEY from information_schema.columns where table_name="customers";

delimiter //
create procedure SelectAllCustomers()
begin
	select * from customers;
End //

delimiter ;

call SelectAllCustomers();


delimiter //

create procedure SelectCustomersByCity(IN mycity varchar(50))
Begin
select * from customers where city=mycity;
End //

delimiter ; 


call SelectCustomersByCity('Singapore');


delimiter //

create procedure SelectCustomersByCityCode(IN mycity varchar(50) , IN pcode varchar(15))
Begin
select * from customers where city=mycity and postalcode=pcode;
End //

delimiter ; 


call SelectCustomersByCityCode('Singapore','079903');


select * from orders;

delimiter //
create procedure get_order_by_customer_no(
	IN custno int,
    OUT shipped int,
    OUT cancelled int,
    OUT resolved int,
    OUT disputed int,
    OUT hold int)
Begin

select count(*) into shipped from orders where customernumber=custno and status ='Shipped';
select count(*) into resolved from orders where customernumber=custno and status ='Resolved';
select count(*) into cancelled from orders where customernumber=custno and status ='Cancelled';
select count(*) into disputed from orders where customernumber=custno and status ='Disputed';
select count(*) into hold from orders where customernumber=custno and status IN ('On Hold','In Process');

End //
delimiter ;

call get_order_by_customer_no(144,@shipped,@resolved,@cancelled,@disputed,@hold);
select @shipped,@resolved,@cancelled,@disputed,@hold;

select 
    (select count(*) from orders where customernumber=144 and status ='Shipped') as shipped ,
    (select count(*) from orders where customernumber=144 and status ='Resolved') resolved,
    (select count(*) from orders where customernumber=144 and status ='Cancelled') cancelled,
    (select count(*)  from orders where customernumber=144 and status ='Disputed') disputed,
    (select count(*)  from orders where customernumber=144 and status IN ('On Hold','In Process')) hold;



select * from customers;

delimiter //
create procedure getStatusByCountry(
IN custno INT,
OUT shipStatus varchar(50))
begin
declare customerCountry varchar(50);
select country into customerCountry from customers where customerNumber=custno;

	case customerCountry
		when 'USA' then
			set shipStatus='2-Day-Shipping';
		when 'Canada' then
			set shipStatus='3-Day-Shipping';
		else
			set shipStatus='5-Day-Shipping';
	End case;
End //
delimiter ;


call getStatusByCountry(102,@shipstatus);
select @shipstatus;

select country ,
	case 
		when 'USA' then '2-Day-Shipping'
		when 'Canada' then '3-Day-Shipping'
		else '5-Day-Shipping'
	End as Ship
      from customers where customerNumber=112;
      
select country from customers where customerNumber=112;
select * from customers ;
customerNumber=102;

select * from payments;

insert into payments(customerNumber,checkNumber,paymentDate,amount) values(103,'ABCDEF12','2025-03-25',1000);

-- handle error --

delimiter //
create procedure handleDuplicatePaymentError(IN custno int,IN checkno varchar(50))
begin
	
    declare exit handler for 1062 select "duplicate keys error" ErrorMessage;
    declare exit handler for sqlexception select "SQL Exception error" ErrorMessage;
    declare exit handler for sqlstate '23000' select "state error error" ErrorCode;
    
	insert into payments(customerNumber,checkNumber,paymentDate,amount) values(custno,checkno,'2025-03-25',1000);
    select count(*) from payments where customerNumber=custno;
end //
delimiter ;

call handleDuplicatePaymentError(103,'ABCDEF12');

use classicmodels;
show procedure status where db='classicmodels';

show procedure status where name ='SelectCustomersByCityCode'

call SelectCustomersByCity('Singapore');






























