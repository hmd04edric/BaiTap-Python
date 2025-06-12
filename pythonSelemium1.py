from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

def get_driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    return driver

def crawl_saucedemo(driver, output_file="saucedemo_products.xlsx"):
    driver.get("https://www.saucedemo.com")

    usernames = [
        "standard_user", "locked_out_user", "problem_user",
        "performance_glitch_user", "error_user", "visual_user"
    ]
    password = "secret_sauce"
    product_data = []

    for username in usernames:
        driver.get("https://www.saucedemo.com")
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "password").clear()

        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        time.sleep(2)

        if "inventory" in driver.current_url:
            print(f"[Saucedemo] Đăng nhập thành công với user: {username}")
            products = driver.find_elements(By.CLASS_NAME, "inventory_item")
            for p in products:
                name = p.find_element(By.CLASS_NAME, "inventory_item_name").text
                price = p.find_element(By.CLASS_NAME, "inventory_item_price").text
                product_data.append({"Username": username, "Product": name, "Price": price})

            # Mở menu và click Logout
            try:
                menu_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
                )
                menu_button.click()

                logout_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
                )
                logout_button.click()

            except Exception as e:
                print(f"[Saucedemo] Lỗi khi logout: {e}")

        else:
            print(f"[Saucedemo] Đăng nhập thất bại với user: {username}")

    pd.DataFrame(product_data).to_excel(output_file, index=False)
    print(f"[Saucedemo] Đã lưu vào file: {output_file}")

def crawl_masothue(driver, output_file="masothue.xlsx"):
    url = "https://thuvienphapluat.vn/ma-so-thue/tra-cuu-ma-so-thue-doanh-nghiep"
    driver.get(url)

    dfs = []
    page = 1

    while True:
        try:
            # Chờ phần tử danh sách xuất hiện
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".tax-code-list .tax-code-item"))
            )
            print(f"[MST] Đang xử lý trang {page}...")
        except:
            print(f"[MST] Không tìm thấy danh sách trên trang {page} hoặc lỗi tải trang.")
            break

        companies = driver.find_elements(By.CSS_SELECTOR, ".tax-code-list .tax-code-item")
        if not companies:
            print(f"[MST] Trang {page} không có dữ liệu.")
            break

        data = []
        for c in companies:
            try:
                name = c.find_element(By.CLASS_NAME, "name").text.strip()
                mst = c.find_element(By.CLASS_NAME, "tax-code").text.strip()
                ngay_cap = c.find_element(By.CLASS_NAME, "reg-date").text.strip()
                data.append({"Tên doanh nghiệp": name, "Mã số thuế": mst, "Ngày cấp": ngay_cap})
            except Exception as e:
                print(f"[MST] Lỗi khi đọc dữ liệu 1 doanh nghiệp: {e}")

        df = pd.DataFrame(data)
        dfs.append((f"Trang_{page}", df))

        # Tìm và click nút Next
        try:
            next_btn = driver.find_element(By.XPATH, "//a[contains(@class, 'next-page') and not(contains(@class, 'disabled'))]")
            next_btn.click()
            page += 1
            time.sleep(2)  # Đợi trang mới load
        except:
            print("[MST] Đã đến trang cuối hoặc không tìm thấy nút Next.")
            break

    # Lưu Excel nếu có dữ liệu
    if dfs:
        with pd.ExcelWriter(output_file) as writer:
            for sheet_name, df in dfs:
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"[MST] Đã lưu vào file: {output_file}")
    else:
        print("[MST] Không có dữ liệu để lưu!")


driver = get_driver()
    
crawl_saucedemo(driver, output_file="D:/Download/saucedemo.xlsx")
crawl_masothue(driver, output_file="D:/Download/masothue.xlsx")