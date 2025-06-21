from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image, ImageFilter, ImageOps
import re 
import time
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def open_chrome():
    # Mo trinh duyet Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
    return driver

def xu_ly_bien_kiem_soat(driver):
    # Nhap bien so xe
    xpath_input = '//*[@id="formBSX"]/div[2]/div[1]/input'
    element_input = driver.find_element(By.XPATH, xpath_input)
    str_bien_so = "73K109240"
    element_input.send_keys(str_bien_so)
    print("Da nhap bien so:", str_bien_so)

def xu_ly_loai_phuong_tien(driver):
    # Mo dropdown loai phuong tien
    xpath_option = '//*[@id="formBSX"]/div[2]/div[2]/select'
    element_input = driver.find_element(By.XPATH, xpath_option)
    element_input.click()

    # Duyet va chon "Xe may"
    xpath_options = '//*[@id="formBSX"]/div[2]/div[2]/select/option'
    option_elements = driver.find_elements(By.XPATH, xpath_options)
    for i_element in option_elements:
        str_option = str(i_element.text)
        if str_option == "Xe máy":
            i_element.click()
            break


def xu_ly_captcha(driver):
    # Chụp ảnh captcha
    element = driver.find_element(By.CSS_SELECTOR, "#imgCaptcha")
    element.screenshot("screen.png")

    # Mở ảnh và chuyển về trắng đen + nhị phân
    img = Image.open("screen.png").convert("L")  # grayscale
    bw = img.point(lambda x: 0 if x < 150 else 255, '1')  # binary threshold

    # Nhận diện
    captcha_text = pytesseract.image_to_string(bw, config='--psm 8 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789').strip().lower()
    print("Captcha nhận dạng:", captcha_text)

    # Điền captcha
    xpath_input_captcha = '//*[@id="formBSX"]/div[2]/div[3]/div/input'
    input_captcha = driver.find_element(By.XPATH, xpath_input_captcha)
    input_captcha.clear()
    input_captcha.send_keys(captcha_text)

    # Click nút tra cứu
    xpath_button = '//*[@id="formBSX"]/div[2]/input[1]'
    button = driver.find_element(By.XPATH, xpath_button)
    button.click()


def kiem_tra_ket_qua(driver):
    try:
        time.sleep(3)  # Doi trang tai xong

        # Kiem tra ket qua vi pham
        try:
            result_table = driver.find_element(By.XPATH, '//*[@id="bodyPrint123"]/div')
            if result_table.is_displayed():
                print("Da hien thi ket qua vi pham:")
                print(result_table.text)
                return
        except:
            pass

        # Kiem tra loi captcha
        try:
            error_element = driver.find_element(By.ID, "errorCaptcha")
            if error_element.is_displayed():
                print("Loi captcha:", error_element.text)
                return
        except:
            pass

        print("Khong co ket qua hoac khong co loi ro rang.")

    except Exception as e:
        print("Loi khi kiem tra ket qua:", str(e))


driver = open_chrome()
time.sleep(2)

xu_ly_bien_kiem_soat(driver)
time.sleep(1)

xu_ly_loai_phuong_tien(driver)
time.sleep(1)

xu_ly_captcha(driver)
time.sleep(3)

kiem_tra_ket_qua(driver)

# Giữ trình duyệt mở để xem kết quả
input("Nhan Enter de dong trinh duyet...")
driver.quit()
