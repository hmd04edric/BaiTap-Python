from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import os

# 1. Mở trình duyệt và truy cập meinvoice.vn
def open_chrome():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    folder_download = os.path.join(os.getcwd(), "download")
    os.makedirs(folder_download, exist_ok=True)
    options.add_experimental_option("prefs", {
        "download.default_directory": folder_download
    })
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.meinvoice.vn/tra-cuu")
    time.sleep(2)
    print("Đã mở trang meinvoice.vn")
    return driver

# 2. Nhập mã tra cứu
def nhap_ma_tra_cuu(driver, ma_hoa_don):
    try:
        xpath_input = '//*[@id="txtCode"]'
        element_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xpath_input))
        )
        element_input.clear()
        element_input.send_keys(ma_hoa_don)
        print("Đã nhập mã:", ma_hoa_don)
        return True
    except Exception as e:
        print("Lỗi nhập mã:", e)
        ghi_nhat_ky(ma_hoa_don, "Lỗi nhập mã", str(e))
        return False

# 3. Bấm nút tra cứu
def bam_nut_tra_cuu(driver, ma_hoa_don):
    try:
        xpath_button = '//*[@id="btnSearchInvoice"]'
        element_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_button))
        )
        element_button.click()
        print("Đã bấm nút tra cứu")
        return True
    except Exception as e:
        print("Lỗi bấm nút:", e)
        ghi_nhat_ky(ma_hoa_don, "Lỗi bấm nút", str(e))
        return False

# 4. Xử lý kết quả
def xu_ly_ket_qua(driver, ma_hoa_don):
    time.sleep(3)
    try:
        xpath_not_exist = '//*[@id="showPopupInvoicNotExist"]'
        element_not_exist = driver.find_elements(By.XPATH, xpath_not_exist)
        if element_not_exist and element_not_exist[0].is_displayed():
            print("Không tìm thấy hóa đơn")

            # Đóng popup "Không tìm thấy"
            xpath_close = '//*[@id="showPopupInvoicNotExist"]/div[1]'
            element_close = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath_close))
            )
            element_close.click()
            time.sleep(2)
            return False

        # Nếu không có lỗi, kiểm tra thông tin hóa đơn
        xpath_invoice_info = '//*[@id="popup-content-container"]/div[1]/div[2]'
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath_invoice_info))
        )
        print("Tìm thấy hóa đơn")
        return True
    except Exception as e:
        print("Lỗi xử lý kết quả:", e)
        ghi_nhat_ky(ma_hoa_don, "Lỗi xử lý kết quả", str(e))
        return False

# 5. Tải hóa đơn
def tai_hoa_don(driver, ma_hoa_don):
    try:
        xpath_download = '//*[@id="popup-content-container"]/div[1]/div[2]/div[12]/div'
        nut_tai = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_download))
        )
        nut_tai.click()

        xpath_pdf = '//*[@id="popup-content-container"]/div[1]/div[2]/div[12]/div/div/div[1]'
        nut_pdf = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_pdf))
        )
        nut_pdf.click()

        print("Đã tải hóa đơn thành công")

        # Đóng popup sau khi tải
        xpath_close_popup = '//*[@id="pnResult"]/div[1]/div[2]/div[2]'
        nut_dong = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_close_popup))
        )
        nut_dong.click()
        time.sleep(2)
        return True
    except Exception as e:
        print("Lỗi tải hóa đơn:", e)
        ghi_nhat_ky(ma_hoa_don, "Lỗi tải hóa đơn", str(e))
        return False

# 6. Ghi nhật ký
def ghi_nhat_ky(ma, ket_qua, loi=None):
    folder = os.path.join(os.getcwd(), "download")
    file_path = os.path.join(folder, "nhat_ky.txt")
    thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    dong = f"[{thoi_gian}] Mã tra cứu: {ma} | Trạng thái: {ket_qua}"
    if loi:
        dong += f" | Lỗi: {loi}"
    dong += "\n"
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(dong)
        print("Đã ghi nhật ký.")
    except Exception as e:
        print("Lỗi ghi nhật ký:", e)

# chay bot
def run_rpa(driver, ma_hoa_don):
    if not nhap_ma_tra_cuu(driver, ma_hoa_don): return
    if not bam_nut_tra_cuu(driver, ma_hoa_don): return

    if xu_ly_ket_qua(driver, ma_hoa_don):
        if tai_hoa_don(driver, ma_hoa_don):
            ghi_nhat_ky(ma_hoa_don, "Thành công")
    else:
        ghi_nhat_ky(ma_hoa_don, "Không tìm thấy hóa đơn")

# Đọc danh sách mã hd từ file
def doc_list_ma(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print("Không đọc được file mã:", e)
        return []


path_file_mahoadon = r"D:\mahoadon.txt"
ds_ma = doc_list_ma(path_file_mahoadon)
driver = open_chrome()

for ma in ds_ma:
    run_rpa(driver, ma)

driver.quit()
