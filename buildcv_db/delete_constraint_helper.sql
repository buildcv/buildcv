
USE resume;  
GO  
-- Return the name of primary key.  
SELECT name  
FROM sys.key_constraints  
WHERE type = 'PK' AND OBJECT_NAME(parent_object_id) = N'users';  
GO  
alter table users 
drop constraint PK__users__3214EC0725AB0578 ;
go 
alter table address 
drop constraint FK__address__user_id__4CA06362

alter table <tablename> 
add  id int identity(1,1) primary key 



