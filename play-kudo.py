
import unittest, time, os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = '192.168.232.2:5566'
        desired_caps['app'] = PATH(
            'kudo.apk'
        )

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()
    
    def test_main(self):
        sleep(2)
    	self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/btn_next_kudo_tutorial_kudo_new")').click()
    	self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/btn_next_kudo_tutorial_kudo_new")').click()
    	self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/btn_next_kudo_tutorial_kudo_new")').click()
    	self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/btn_next_kudo_tutorial_kudo_new")').click()
    	sleep(5)

    	self.driver.back()
        sleep(2)
    	self.driver.back()
    	sleep(1)
    	self.driver.back()

        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageButton[@class="android.widget.ImageButton"]'))).click()
    	wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@resource-id="kudo.mobile.app:id/bt_drawer_login"]'))).click()
        self.login_stage(wait)
        sleep(2)
        
        find = 0
        while find == 0:
            sleep(1)
            found = self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/category_item_title")')
            if found.is_displayed() and found.text == "Pesawat":
                found.click()
                find = 1
            self.driver.swipe(100, 700, 100, 150)
        self.search_ticket(wait)
        sleep(2)
        self.driver.back()
        sleep(1)
    	self.driver.back()
    	sleep(1)
    	self.driver.back()
        
        self.get_product(wait)
        sleep(10)

    def login_stage(self, wait):
    	self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/activity_login_et_username")').set_value('your@email.com')
    	self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/login_bt_next")').click()
    	wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.EditText[@resource-id="kudo.mobile.app:id/login_et_password"]'))).set_value('yourpassword123')
    	self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/login_button")').click()
        
    def search_ticket(self, wait):
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.TextView[@resource-id="kudo.mobile.app:id/ticket_tv_code_to"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.EditText[@resource-id="kudo.mobile.app:id/actionbar_et_search_box"]'))).set_value('Medan')
        sleep(1)
        self.driver.find_element_by_android_uiautomator('text("Kuala Namu (KNO)")').click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.TextView[@resource-id="kudo.mobile.app:id/ticket_tv_number_date_from"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.TextView[@class="android.widget.TextView"][@text="27"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@resource-id="kudo.mobile.app:id/btn_pick"]'))).click()
        self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/ticket_sw_round_trip")').click()
        self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/ticket_sw_round_trip")').click()
        self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/ticket_tv_passenger")').click()
        self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/iv_plus_adult")').click()
        self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/iv_plus_adult")').click()
        self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/btn_confirm")').click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@resource-id="kudo.mobile.app:id/flight_btn_search_ticket"]'))).click()
        sleep(8)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.TextView[@class="android.widget.TextView"][@text="LIHAT DETAIL TIKET"]'))).click()
        sleep(1)
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageButton[@class="android.widget.ImageButton"]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@resource-id="kudo.mobile.app:id/schedule_iv_icon_airline"]'))).click()
        

    def get_product(self,wait):
        self.driver.back()
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.ImageView[@resource-id="kudo.mobile.app:id/iv_topbar_search"]'))).click()
        wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.EditText[@resource-id="kudo.mobile.app:id/actionbar_et_search_box"]'))).set_value('tv')
        sleep(1)
        wait.until(EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@resource-id="kudo.mobile.app:id/autocomplete_tv_tag"][@text="Tv dalam "]'))).click()
        self.driver.back()
        sleep(1)
        self.driver.back()
        sleep(1)
        self.driver.back()

        find3 = 0
        while find3 == 0:
            sleep(1)
            found3 = self.driver.find_element_by_android_uiautomator('resourceId("kudo.mobile.app:id/item_list_product_name_tv")')
            if found3.is_displayed() and found3.text == "FUNIKA CLTV 1000C - Meja Rak TV":
                found3.click()
                find3 = 1
                break
            self.driver.swipe(100, 700, 100, 400)
        
        wait.until(EC.element_to_be_clickable((By.XPATH,'//android.widget.Button[@resource-id="kudo.mobile.app:id/product_detail_btn_buy"]'))).click()


if __name__=='__main__':
   	suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
   	unittest.TextTestRunner(verbosity=2).run(suite)
       
       