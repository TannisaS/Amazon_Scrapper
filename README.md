# Amazon Best Sellers Web Scraper

This project is a Python-based web scraper designed to extract information from Amazon's Best Sellers section. It leverages the Selenium library to automate the browsing process and collects product details from specified categories.

## Features

- **Authentication**: Logs into Amazon using user-provided credentials.
- **Data Extraction**:
  - Product Name
  - Product Price
  - Sale Discount
  - Best Seller Rating
  - Ship From *(placeholder for future implementation)*
  - Sold By *(placeholder for future implementation)*
  - Rating
  - Product Description *(placeholder for future implementation)*
  - Category Name
  - All Available Images *(placeholder for future implementation)*
- **Multi-Category Support**: Scrapes data from any number of specified Best Sellers categories.
- **Data Storage**: Saves extracted data into a structured CSV file.
- **Error Handling**: Robust handling for login issues, CAPTCHA interruptions, and scraping errors.

## Prerequisites

### Python
- **Version**: 3.7 or higher.

### Selenium
- Install using pip:
  ```bash
  pip install selenium
  ```
## WebDriver

### ChromeDriver for Google Chrome
- **Download**: [ChromeDriver](https://chromedriver.chromium.org/downloads)
- **Ensure Compatibility**: Match the ChromeDriver version with your installed Google Chrome version.
- **Setup**: Place the driver in a known location and update its path in the script.

## Amazon Account
- **Requirement**: A valid Amazon account for login.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/amazon-best-sellers-scraper.git
   ```
2. **Navigate to the project directory:**:
   ```bash 
   cd amazon-best-sellers-scraper
   ```
3. **Install dependencies**:
   ```bash  
   pip install -r requirements.txt
   ```
4. **Update the ChromeDriver path in the script (setup_driver() function)**.

## Usage

1. **Run the Script**:
   ```bash
   python best_seller.py
   ```
## Configuration

### Categories
- Update the `categories` list in the script with the URLs and names of the Best Sellers categories you want to scrape.

### Example:
```python
categories = [
    {
        "name": "Books",
        "url": "https://www.amazon.com/Best-Sellers-Books/zgbs/books"
    },
    {
        "name": "Electronics",
        "url": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics"
    }
]
```
## Output

The script generates a CSV file (`amazon_best_sellers.csv`) with the following columns:

- **Product Name**
- **Price**
- **Discount**
- **Rating**
- **Category**
- **Seller**
- **Description**

## Limitations

- **CAPTCHAs**:  
  Manual intervention may be required to solve CAPTCHAs during login.

- **Dynamic Content**:  
  Some fields (e.g., "Ship From," "Sold By") require additional navigation to the product detail pages.

- **Compliance**:  
  Ensure that the scraping adheres to Amazon’s [Terms of Service](https://www.amazon.com/gp/help/customer/display.html).

## Future Enhancements

- **CAPTCHA Handling**:  
  Add support for CAPTCHA-solving tools.

- **Detailed Product Information**:  
  Navigate to product pages to scrape additional details such as "Ship From," "Sold By," and product images.

- **Multi-Browser Support**:  
  Add support for Firefox, Edge, or other browsers.
