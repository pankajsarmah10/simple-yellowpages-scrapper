# Yellow Pages Search Results Scraper

A simple Python-based scraper to extract Yellow Pages search results into an Excel file. You can search for various products, services, brands, or companies from the Yellow Pages UAE website.

## Usage Guide

Clone the repo to your local machine using the following command:

```bash
git clone <repo_url>
```
Navigate to the project directory and install the required packages:
```bash
pip install -r requirements.txt
```
Create or edit the .env file in the root directory and update the search_text variable to specify the field you’d like to search for (e.g., products, services, brand, company).
Note: Do not change the base_url in the .env file.

From the root directory, run the Python script to start the scraper:
```bash
python main.py
```

The scraper will produce the extracted data in an Excel file, which will be saved in the extracts folder.

## Requirements
This project uses the following Python libraries:
* requests
* lxml
* pandas
* openpyxl
* python-dotenv

Install these by running the following command:
```bash
pip install -r requirements.txt
```

## License

[MIT](https://choosealicense.com/licenses/mit/)