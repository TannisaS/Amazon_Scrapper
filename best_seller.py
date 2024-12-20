from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# Setup Selenium WebDriver
def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    service = Service("C:/Users/KIIT/Downloads/chromedriver-win64/chromedriver.exe")  # Update the path
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Login to Amazon
def amazon_login(driver, email, password):
    driver.get("https://na.account.amazon.com/ap/signin?_encoding=UTF8&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.pape.max_auth_age=0&ie=UTF8&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=lwa&openid.assoc_handle=amzn_lwa_na&marketPlaceId=ATVPDKIKX0DER&arb=b02b98c6-cadf-4cc5-aa42-fb8bb037935a&language=en_US&openid.return_to=https%3A%2F%2Fna.account.amazon.com%2Fap%2Foa%3FmarketPlaceId%3DATVPDKIKX0DER%26arb%3Db02b98c6-cadf-4cc5-aa42-fb8bb037935a%26language%3Den_US&enableGlobalAccountCreation=1&metricIdentifier=amzn1.application.e3b40bcf8dae40e6bf8b197b9b3dec8d&signedMetricIdentifier=b1rnnUP4iinb%2B%2BwjCOWA1f5Y%2B6DlINB%2BDQCz1Q54AtU%3D")
    time.sleep(3)  # Allow page to load

    try:
        # Enter email
        email_input = driver.find_element(By.ID, "ap_email")
        email_input.send_keys(email)
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        # Enter password
        password_input = driver.find_element(By.ID, "ap_password")
        password_input.send_keys(password)

        # Submit login form
        sign_in_button = driver.find_element(By.ID, "signInSubmit")
        sign_in_button.click()
        time.sleep(5)  # Wait for login to process

        # Check for login success
        if "youraccount" not in driver.page_source.lower():
            print("Login failed. Please check your credentials or solve any CAPTCHA.")
            driver.quit()
            exit()
        else:
            print("Login successful!")
    except Exception as e:
        print(f"Error during login: {e}")
        driver.quit()
        exit()

# Scrape Best Sellers
def scrape_best_sellers(driver, category_url, category_name):
    print(f"Scraping category: {category_name}")
    driver.get(category_url)
    time.sleep(3)

    products = []
    try:
        for product_card in driver.find_elements(By.CSS_SELECTOR, ".zg-item-immersion"):
            try:
                product_name = product_card.find_element(By.CSS_SELECTOR, "a div").text
                price = product_card.find_element(By.CSS_SELECTOR, ".p13n-sc-price").text
                discount = None  # Placeholder: Adjust if discount info is available
                rating = product_card.find_element(By.CSS_SELECTOR, ".a-icon-alt").text
                seller = None  # Placeholder: Needs to be extracted from product page
                description = None  # Placeholder: Needs to be extracted from product page

                products.append({
                    "Product Name": product_name,
                    "Price": price,
                    "Discount": discount,
                    "Rating": rating,
                    "Category": category_name,
                    "Seller": seller,
                    "Description": description
                })
            except Exception as e:
                print(f"Error scraping product: {e}")
    except Exception as e:
        print(f"Error loading category page: {e}")

    return products

# Save data to CSV
def save_to_csv(data, filename):
    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Main function
def main():
    email = input("Enter your Amazon email: ")
    password = input("Enter your Amazon password: ")

    driver = setup_driver()
    amazon_login(driver, email, password)

    # Example categories: Add your own
    categories = [
        {"name": "Books", "url": "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books"},
        {"name": "Electronics", "url": "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics"},
        # Add more categories here
    ]

    all_products = []
    for category in categories:
        products = scrape_best_sellers(driver, category["url"], category["name"])
        all_products.extend(products)

    # Save data to CSV
    if all_products:
        save_to_csv(all_products, "amazon_best_sellers.csv")
        print("Data saved to amazon_best_sellers.csv")
    else:
        print("No products found.")

    driver.quit()

if __name__ == "__main__":
    main()
