# Web-Scraping-Following-Links-with-BeautifulSoup
Web Scraping with BeautifulSoup – Link Traversal Demo

This project demonstrates how to use Python’s urllib and BeautifulSoup to scrape web pages and follow links iteratively. The program starts from a user-provided URL, then repeatedly follows a link at a given position for a specified number of times.

Features

Uses urllib to fetch HTML content.

Parses web pages with BeautifulSoup.

Iteratively retrieves links by position.

Handles SSL certificate errors safely.

How It Works

Enter a starting URL.

Enter the count (how many times to repeat the process).

Enter the position of the link to follow on each page.

The program prints each retrieved URL step by step.

Example Run
Enter URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html  
Enter count: 4  
Enter position: 3  

Retrieving: http://py4e-data.dr-chuck.net/known_by_Kaiya.html  
Retrieving: http://py4e-data.dr-chuck.net/known_by_Danya.html  
Retrieving: http://py4e-data.dr-chuck.net/known_by_Anum.html  
Retrieving: http://py4e-data.dr-chuck.net/known_by_Arun.html  

Skills Demonstrated

Python Web Scraping

BeautifulSoup HTML Parsing

Iterative Web Navigation

Handling SSL Certificates
