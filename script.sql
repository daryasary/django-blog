DROP DATABASE IF EXISTS `dj_home_blog`;
CREATE DATABASE `dj_home_blog`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;

USE 'dj_home_blog';
GRANT ALL PRIVILEGES ON dj_home_blog.* TO 'hosein'@'localhost' IDENTIFIED BY 'hosein'

WITH GRANT OPTION;
FLUSH PRIVILEGES;