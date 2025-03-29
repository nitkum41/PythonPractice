select * from customers;

delimiter //
create function CustomerLevel(credit decimal(10,2)) returns varchar(20)
deterministic
begin

	declare custlevel varchar(20);
    if credit > 50000 then
		set custlevel="PLATINUM";
	elseif (credit >= 10000) and (credit <= 50000) then
		set custlevel="GOLD";
	elseif credit < 10000 then
		set custlevel="SILVER";
	end if;
	return custlevel;
end //

delimiter ;


show function status where db="classicmodels";
show function status where name="CustomerLevel";

select customerName, CustomerLevel(creditLimit) custLevel from customers;

select customerName,
case 
	when creditLimit > 50000 then "PLATINUM"
	when (creditLimit >= 10000) and (creditLimit <= 50000) then "GOLD"
	when creditLimit < 10000 then "SILVER"
end as custLevel from customers;


delimiter //
create procedure GetCustomerLevel(
	IN customerNo INT,
    OUT customerLevel varchar(20)
)

begin
	declare credit dec(10,2) default 0;
    
    select creditLimit into credit
    from customers 
    where customerNumber=customerNo;
    
    set customerLevel = CustomerLevel(credit);
    
end //

delimiter ;

call GetCustomerLevel(103,@customerLevel);
select  @customerLevel;
select * from customers;
