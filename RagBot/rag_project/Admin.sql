CREATE USER 'healthorbit'@'localhost' IDENTIFIED BY 'Admin@123';
GRANT ALL PRIVILEGES ON healthorbit.* TO 'healthorbit'@'localhost';
FLUSH PRIVILEGES;
