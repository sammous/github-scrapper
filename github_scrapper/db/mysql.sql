DROP DATABASE IF EXISTS github3;
CREATE DATABASE github3;
USE github3;
CREATE TABLE users_javascript(
username VARCHAR(100),
link_profile VARCHAR(100),
email  VARCHAR(100),
image VARCHAR(200),
PRIMARY KEY (username)
) ENGINE = InnoDB, DEFAULT CHARSET=utf8;
CREATE TABLE users_python(
username VARCHAR(100),
link_profile VARCHAR(100),
email  VARCHAR(100),
image VARCHAR(200),
PRIMARY KEY (username)
) ENGINE = InnoDB, DEFAULT CHARSET=utf8;
CREATE TABLE users_ruby(
username VARCHAR(100),
link_profile VARCHAR(100),
email  VARCHAR(100),
image VARCHAR(200),
PRIMARY KEY (username)
) ENGINE = InnoDB, DEFAULT CHARSET=utf8;
CREATE TABLE users_java(
username VARCHAR(100),
link_profile VARCHAR(100),
email  VARCHAR(100),
image VARCHAR(200),
PRIMARY KEY (username)
) ENGINE = InnoDB, DEFAULT CHARSET=utf8;
