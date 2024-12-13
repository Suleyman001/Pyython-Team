#Just for testing some new features


import os
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import pandas as pd
from openpyxl import Workbook
import re

# Base URL for Gradus
BASE_URL = "https://gradus.kefo.hu/archive/2020-1/"

# Function to download and process PDF
def process_pdf(pdf_url):
    response = requests.get(pdf_url)
    filename = pdf_url.split("/")[-1]
    with open(filename, "wb") as f:
        f.write(response.content)
    
    # Read PDF content
    reader = PdfReader(filename)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    os.remove(filename)  # Remove file after reading

    page_numbers = []

    for i, page in enumerate(reader.pages, start=1):
        text += page.extract_text()
        page_numbers.append(i)

    first_page = min(page_numbers) if page_numbers else "N/A"
    last_page = max(page_numbers) if page_numbers else "N/A"

    return text, first_page, last_page

# Function to get MTA REPO URL
def get_mta_repo_url(title):
    search_url = f"https://real.mtak.hu/search?query={'+'.join(title.split())}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Find the first MTA REPO link in search results
    repo_url = None
    for link in soup.find_all("a", href=True):
        if "real.mtak.hu" in link["href"]:
            repo_url = link["href"]
            break
    return repo_url

# Function to get MTMT link
def get_mtmt_link(authors):
    search_url = f"https://m2.mtmt.hu/gui2/?mode=browse&params=publication;{'+'.join(authors.split())}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Find the first MTMT link in search results
    mtmt_url = None
    for link in soup.find_all("a", href=True):
        if "m2.mtmt.hu" in link["href"]:
            mtmt_url = link["href"]
            break
    return mtmt_url

# Function to scrape data from Gradus site
def scrape_gradus():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    data = []

    # Example structure to find articles
    for link in soup.find_all("a", href=True):
        if ".pdf" in link["href"]:
            print(link["href"])
            article_data = {}
            pdf_url = BASE_URL + link["href"]

            article_data["Filename"] = link["href"]
            article_data["PDF URL"] = pdf_url

            # Process PDF information
            pdf_text, first_page, last_page = process_pdf(pdf_url)
            lines = pdf_text.split('\n')

            # Extract data from PDF based on structure and text position
            vol_num_year_pages = lines[0].strip()
            page_numbers = re.findall(r'\b\d+\b', vol_num_year_pages)

            # Find the original and English title
            title_original_lines = []
            title_english_lines = []
            authors_line = None
            accented_characters = re.compile(r'[áéíóúÁÉÍÓ]')
            is_english = False

            for i, line in enumerate(lines[3:], start=3):  # Start from line 3
                if re.search(r'[A-Z][a-z]', line.strip()):  # Check if the line contains uppercase and lowercase letters
                    authors_line = i
                    break
                if accented_characters.search(line.strip()):
                    title_original_lines.append(line.strip())
                else:
                    title_english_lines.append(line.strip())
                    is_english = True

            title_original = " ".join(title_original_lines).strip() if title_original_lines else "N/A"
            title_english = " ".join(title_english_lines).strip() if title_english_lines else "N/A"
            authors = lines[authors_line].strip() if authors_line and authors_line < len(lines) else "N/A"

            # Abstract
            if 'Összefoglalás' in pdf_text:
                abstract_start = pdf_text.find('Összefoglalás') + len('Összefoglalás')
                abstract_end = pdf_text.find('Abstract')
                abstract_original = pdf_text[abstract_start:abstract_end].strip()
            else:
                abstract_original = "N/A"

            if 'Abstract' in pdf_text:
                abstract_english_start = pdf_text.find('Abstract') + len('Abstract')
                abstract_english = pdf_text[abstract_english_start:].strip()
            else:
                abstract_english = "N/A"

            # Email
            email_match = re.search(r'[\w\.-]+@[\w\.-]+', pdf_text)

            article_data["Title (Original)"] = title_original
            article_data["Title (English)"] = title_english
            article_data["Authors"] = authors
            article_data["Abstract (Original)"] = abstract_original
            article_data["Abstract (English)"] = abstract_english
            article_data["Email"] = email_match.group(0) if email_match else "N/A"

            # Add extra information (year, volume, article number, and section code)
            filename_parts = link["href"].split("_")
            article_data["Year"] = filename_parts[0]
            article_data["Vol"] = filename_parts[1]
            article_data["No"] = filename_parts[2] if filename_parts[2].isdigit() else filename_parts[3]
            article_data["Section Code"] = filename_parts[2] if filename_parts[2].isalpha() else filename_parts[3]

            # Pages
            article_data["First Page"] = first_page
            article_data["Last Page"] = last_page

            # Add MTA REPO URL, DOI, MTMT link
            article_data["MTA REPO URL"] = get_mta_repo_url(title_original)
            article_data["DOI"] = "N/A"  # Only articles from Vol 7, No 1 (2020) have DOIs, handle this logic as needed.
            article_data["MTMT Link"] = get_mtmt_link(authors)

            data.append(article_data)

    return data

# Main function
def main():
    articles = scrape_gradus()

    # Save results to an Excel file
    df = pd.DataFrame(articles)
    df.to_excel("gradus_articles.xlsx", index=False, engine="openpyxl")
    print("Data saved to gradus_articles.xlsx")

if __name__ == "__main__":
    main()
