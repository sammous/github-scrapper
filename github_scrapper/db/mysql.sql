DROP DATABASE IF EXISTS github;
CREATE DATABASE github;
USE github;
CREATE TABLE users_javascript(
username VARCHAR(100),
language VARCHAR(100),
email  VARCHAR(100),
image VARCHAR(200),
joined VARCHAR(200),
location VARCHAR(100),
name VARCHAR(100),
PRIMARY KEY (username)
) ENGINE = InnoDB, DEFAULT CHARSET=utf8;
CREATE TABLE users_python(
username VARCHAR(100),
language VARCHAR(100),
email  VARCHAR(100),
image VARCHAR(200),
joined VARCHAR(200),
location VARCHAR(100),
name VARCHAR(100),
PRIMARY KEY (username)
) ENGINE = InnoDB, DEFAULT CHARSET=utf8;
CREATE TABLE users_ruby(
username VARCHAR(100),
language VARCHAR(100),
email  VARCHAR(100),
image VARCHAR(200),
joined VARCHAR(200),
location VARCHAR(100),
name VARCHAR(100),
PRIMARY KEY (username)
) ENGINE = InnoDB, DEFAULT CHARSET=utf8;
CREATE TABLE users_java(
username VARCHAR(100),
language VARCHAR(100),
email  VARCHAR(100),
image VARCHAR(200),
joined VARCHAR(200),
location VARCHAR(100),
name VARCHAR(100),
PRIMARY KEY (username)
) ENGINE = InnoDB, DEFAULT CHARSET=utf8;
