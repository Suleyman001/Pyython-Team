Project Documentation - Python TEM
Project Title:
Academic Data Extraction from Gradus
Group Members:
1. Jumaniyazov Suleyman - Neptun: eg6x6k
2. Dijanira Muachifi - Neptun: u2felp
3. Bermejo Magarín Alberto - Neptun: h64gog
Project Description
This project automates the process of collecting and analyzing article data available on the 
Gradus website. Using web scraping, PDF file processing, and data organization techniques, the 
application processes relevant article information and consolidates it into an Excel file.
Homework Description:
We did this homework with the following task:
On the webpage https://gradus.kefo.hu/archive/, one can find all the issues and articles of 
the scientific journal of the university called Gradus. The task was to create a Python program that 
gathers the following information about all the articles published in Gradus and stores the 
information in an Excel file. The Hungarian, German, and other special characters must be stored 
correctly.
The required data includes:
1. Year (e.g., 2015)
2. Volume (Vol, e.g., 2)
3. Number (No, e.g., 1)
4. Filename of the article (e.g., 2015_1_ART_001_Bardos.pdf)
5. First page (e.g., 1)
6. Last page (e.g., 13)
7. Authors (e.g., Bárdos Dóra)
8. Original title (e.g., Szobák, tárgyak, bútorok – Metaforikusság Petelei István 
elbeszéléseiben)
9. Title in English (e.g., Key symbols and metaphors of István Petelei’s sixth book) - extracted 
from the PDF file.
10. Section code (e.g., ART)
11. Abstract in original language - extracted from the PDF file.
12. Abstract in English - extracted from the PDF file.
13. Email address of the corresponding author - extracted from the PDF file.
14. MTA REPO URL (e.g., https://real.mtak.hu/110689/) - obtained from MTA Repository.
15. DOI (e.g., https://doi.org/10.47833/2020.1.AGR.001) - available only for articles starting 
with Vol 7, No 1 (2020).
16. MTMT Link (e.g., 
https://m2.mtmt.hu/gui2/?mode=browse&params=publication;30314490) - obtained from 
MTMT.
Objectives:
1. Data Collection: Scrape and download PDF files of articles available on the Gradus 
website.
2. Information Extraction: Process the PDFs to extract the aforementioned data points, 
including: 
o Titles (original and English).
o Authors and their emails.
o Abstracts (original and English).
o Metadata such as year, volume, number, and section code.
3. Result Storage: Export the data into an organized Excel file for easy access and analysis.
Technologies and Libraries Used:
• Language: Python 3.x
• Libraries:
o os - For file management on the operating system.
o requests - To make HTTP requests and download files.
o BeautifulSoup (from bs4) - For web scraping and HTML element extraction.
o PyPDF2 - To read and extract text from PDF files.
o pandas - For organizing and managing tabular data.
o openpyxl - To create and manipulate Excel spreadsheets.
o re - For pattern matching using regular expressions.
Code Architecture:
1. Constants:
o BASE_URL: Base URL of the Gradus site to access the 2020 articles.
2. Function process_pdf(pdf_url)
This function downloads a PDF file, processes its content, and returns:
o Extracted text.
o The first and last page numbers of the article.
3. Function scrape_gradus()
This function performs scraping on the Gradus webpage and:
o Searches for links to PDF files.
o Processes the PDFs using the process_pdf function.
o Extracts specific article details such as: 
▪ Titles (original and English).
▪ Abstracts (original and English).
▪ Authors.
▪ Contact emails.
o Organizes the data into a list of dictionaries.
4. Function main()
o Orchestrates the program execution.
o Calls scrape_gradus() to collect data.
o Converts the results into a pandas DataFrame.
o Saves the results into an Excel file (gradus_articles.xlsx).
How to Use:
1. Prerequisites:
o Python installed on the system.
o Install the necessary dependencies: 
o pip install requests beautifulsoup4 PyPDF2 pandas openpyxl
2. Execution:
o Download the code and save it as a Python file (script.py).
o Run the script in the terminal with the command: 
o python script.py
o The results will be saved in an Excel file named gradus_articles.xlsx.
Expected Results:
• An Excel file with the following columns: 
o Filename
o PDF URL
o Title (Original)
o Title (English)
o Authors
o Abstract (Original)
o Abstract (English)
o Email
o Year
o Vol
o No
o Section Code
o First Page
o Last Page
Contributions and Responsibilities:
Member Task Observations
Jumaniyazov 
Suleyman
Implementation of the process_pdf
function.
Focused on extracting simple metadata 
from PDFs.
Dijanira Muachifi
Development of the scrape_gradus
function.
Web scraping and HTML data 
collection.
Bermejo Magarín 
Alberto
Creation of Excel export and 
testing.
Final data organization.
Conclusion
This project demonstrates the power of automation in handling and processing large 
amounts of academic data from online sources. By leveraging Python libraries like BeautifulSoup
and PyPDF2, we were able to efficiently extract, process, and organize article metadata and 
content. The final product, an Excel file, provides a structured and user-friendly format for 
analyzing the gathered information. This project serves as a foundation for further improvements 
and expansions, showcasing the potential for future applications in academic research and data 
management.
