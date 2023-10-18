-- Create database an user with read permissions
-- Execute: cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
create database if not exists hbtn_0d_2;
create user if not exists user_0d_2@localhost identified by 'user_0d_2_pwd';
grant select on hbtn_0d_2 . * to user_0d_2@localhost;
