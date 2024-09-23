#Selenium
# 1.Webdriver is interface , by using webdriver we can open or operate all browsers
# 8. There are 8 locators in selenium :- Id,name,classname,TagName,linktext, partial linktext,CSS Selector, Xpath

# 5. Stale Element means an old element or no longer available element.
#Assume there is an element that is found on a web page referenced as a WebElement in WebDriver.
#If the DOM changes then the WebElement goes stale.

# 2. How to handel selective dropdown, write a snippet for it?
# To handle a selective dropdown , we can use the Select class locater.
#         driver.find_elements
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# driver = webdriver.Chrome()
# driver.get("https:url.com")
# driver.find_element(by.id,"dropdown_id")
# select = Select(dropdown_element)
# select.select_by_visible_text("Option 1")

# 10. Write xpath
# import time
#
# from selenium import webdriver
# #from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# op=Options()
# op.add_experimental_option('detach',True)
# dr=webdriver.Chrome(options=op)
#
# dr.get('https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market')
# dr.maximize_window()
# dr.find_element(By.CLASS_NAME,('nav-item dropdown active')).click()


#Python
#Q1"
# What is decorator , write a decorator?
# DECORE
# def is_prim(is_prime):
#     def even_odd(num):
#         if num % 2 == 0:
#             return (num, "even")
#         else:
#             return is_prime(num)
#     return even_odd
# @is_prim
# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return (num, "not a prime number")
#         return (num, "its prime")
#     else:
#         return (num, "not a prime")
# print(is_prime(3))
# print(is_prime(10))

# Difference between List vs tuple vs set vs dictionary?
# Lists
#
# It is enclosed with Square Bracket
# Elements are stored in a specific order.
# Elements can be added, removed, or modified after creation.
# Elements can be accessed using their index.
# Example: my_list = [1, 2, 3, "treenetra"]
#
# Tuples
#
# It Enclosed with
# Similar to lists, but elements are stored in a specific order.
# Elements cannot be modified after creation.
# Elements can be accessed using their index.
# It is Immutable.
# Example: my_tuple = (1, 2, 3, "treenetra")
#
#
# Sets
#
# Elements are stored without a specific order.
# Elements can be added or removed, but not modified.
# Sets cannot contain duplicate elements.
# removing duplicates, and mathematical operations like union, intersection.
# Example: my_set = {7, 8, 9, "treenetra"}
#
#
# Dictionaries
#
# It is Collection of Key and value pair.
# It is enclosed with Curli Bracket {}.
# It is Mutable in nature.
# Key must be unic.
# Example: my_dict = {"name": "Atul", "age": 29,}
# Q1"
# "What is decorator , write a decorator?"
# """DECORE"""
# def is_prim(is_prime):
#     def even_odd(num):
#         if num % 2 == 0:
#             return (num, "even")
#         else:
#             return is_prime(num)
#     return even_odd
# @is_prim
# def is_prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 return (num, "not a prime number")
#         return (num, "its prime")
#     else:
#         return (num, "not a prime")
# print(is_prime(3))
# print(is_prime(10))
#
#
# "Q7"
# Li = [1,2,3,4], Li2 = [10,20,30]
# Result = {1:10,2:20,3:30}
#
# def dict_lists(list1, list2):
#     result = {}
#     length = len(list1) if len(list1)<len(list2) else len(list2)
#     for i in range(length):
#         result[list1[i]] = list2[i]
#     return result
# Li = [1, 2, 3, 4]
# Li2 = [10, 20, 30]
# result = dict_lists(Li, Li2)
# print(result)

# "Q8"
# Handel a csv file, write first_name , email, phn_no, insert 5 data in this csv, then read
# the csv and print in console bar
#
# import  csv
# data_col=["first_name" , "email", "phn_no"]
# data_cols=[["atul","atul@mail.com",2287887677],["tapan","zyx@mail.com",993375],["subha","abc@mail.com",2287887677],["ashok","bac@mail.com",2287887677],["sanju","ccb@mail.com",2287887677]]
# with open("output.csv",mode="w") as file:
#     csv_writer=csv.writer(file)
#     csv_writer.writerow(data_col)
#     csv_writer.writerows(data_cols)
# with open("output.csv",mode="r") as file:
#     csv_reader=csv.reader(file)
#     for i in csv_reader:
#         print(i)

# 12.garbage collection
# it can help up for free space means which object we no need any longer it free that space ,it is a automatic memory managment.



#SQL

# SQL1. Explain about the DML, DDL, TCL, DQL commands?
# DML (Data Manipulation Language): Used for managing data within schema objects.Commands: INSERT, UPDATE, DELETE, MERGE.DDL (Data Definition Language): Used for defining and managing all database objects.Commands: CREATE, ALTER, DROP, TRUNCATE, COMMENT, RENAME.TCL (Transaction Control Language): Manages changes made by DML statements.Commands: COMMIT, ROLLBACK, SAVEPOINT, SET TRANSACTION.DQL (Data Query Language): Used to query data from the database.Commands: SELECT.

# 2. What is a join? Explain about all the joins.
# Join: A SQL operation that combines rows from two or more tables based on a related column between them.Inner Join: Returns records with matching values in both tables.sqlCopy codeSELECT * FROM table1
# INNER JOIN table2
# ON table1.common_column = table2.common_column;
# Left Join (Left Outer Join): Returns all records from the left table and matched records from the right table; returns NULL for unmatched rows in the right table.sqlCopy codeSELECT * FROM table1
# LEFT JOIN table2
# ON table1.common_column = table2.common_column;
# Right Join (Right Outer Join): Returns all records from the right table and matched records from the left table; returns NULL for unmatched rows in the left table.sqlCopy codeSELECT * FROM table1
# RIGHT JOIN table2
# ON table1.common_column = table2.common_column;
# Full Join (Full Outer Join): Returns records when there is a match in either left or right table records; returns NULL for unmatched rows in either table.sqlCopy codeSELECT * FROM table1
# FULL OUTER JOIN table2
# ON table1.common_column = table2.common_column;
# Cross Join: Returns the Cartesian product of the two tables.sqlCopy codeSELECT * FROM table1
# CROSS JOIN table2;
# Self Join: A table is joined with itself.sqlCopy codeSELECT a., b.
# FROM table a, table b
# WHERE a.common_column = b.common_column;

# 3. Difference between Joins vs Subquery?
# Joins combine data from multiple tables into a single result set by matching columns between them.Subqueries are nested queries executed separately before the outer query uses the result. Subqueries can be used for complex filtering and calculation.

# 4. Find 3rd Highest Salary Of employee table ?
# select * from emp where salary=>(select max(sal) from salary where salary =>(select max(sal) from salary))
# SELECT DISTINCT salary
# FROM employee
# ORDER BY salary DESC
# LIMIT 1 OFFSET 2;
#
#  5. Find the top seller in this month, according to date in customer table?
# SELECT seller_id, SUM(amount) AS total_sales
# FROM sales
# WHERE MONTH(sale_date) = MONTH(CURRENT_DATE)
# AND YEAR(sale_date) = YEAR(CURRENT_DATE)
# GROUP BY seller_id
# ORDER BY total_sales DESC;

# 1. Copy a file one directory to another directory?
#cp Existingdirectorypath  Newdirectorypathname

#2. How do you find the process IF(PID) of a running process.
# for finding the PID we use ps command for checking the the pid number after tha we can use
# ps -ef | grep process_name.

# 3. Difference between chown vs chmod?
# chown: Changes the ownership of files or directories.
# syntax:chown user:group filename
# chmod: Changes the file('s permissions (read, write, execute).'
# Syntax: chmod w/r/x filename
# chown: in this command used for changing the owner ship.
# chmod:in this command used for giving the permission who can access the file and modify.

# 4. In a directory a find a file name abc.txt?

# 5. Why we are using sed command?
# sed command basically used for find , replace ,search ,insert and delete word and lines in text file

# 6. How to list directories in Unix?
# ls  -ltr
# ls -la
# ls -al
