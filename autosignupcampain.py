import pickle
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == '__main__':
	email = "Pimoni94@gmail.com"
	password = "Thaothao090311@"

	options = webdriver.ChromeOptions()
	#options.add_argument('proxy-server=106.122.8.54:3128')
	#options.add_argument(r'--user-data-dir=C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Default')

	browser = uc.Chrome(
			options=options,
	)
	browser.get('https://sellercenter.lazada.vn/apps/seller/login')

	browser.find_element(By.ID, 'account').send_keys(email)
	browser.find_element(By.ID, 'password').send_keys(password)

	time.sleep(2)

	browser.find_element(by=By.XPATH, value="//button[@type='submit']").click()

	time.sleep(3)

	cookies = browser.get_cookies()

	pickle.dump(cookies, open("cookies.pkl", "wb"))
	
	time.sleep(1)
	
	browser.get('https://sellercenter.lazada.vn/apps/campaign/master/list?spm=a1zawf.26399937.campaigns_list.1.5a3e4edf6Bknuk')
	time.sleep(1)
	
	# Find the whole campaigns array 
	whole_campaigns = browser.find_elements(By.CSS_SELECTOR, "div.aplus-module-auto-exp > div")

	# Loop through the main campaign array
	for find_each_campaign in whole_campaigns:

		# Find list the campaign voucher in the array
		campaigns = find_each_campaign.find_elements(By.XPATH, '//div[@data-spm="master_card"]')
		
			# Loop through the list campaign voucher array & click the first campaign
	for campaign in campaigns:
		try:
			campaign.click()
		except:
			pass
		time.sleep(2)
		# find "Cổng voucher" element is present then click
		find_gate_voucher_tab = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//div/ul/li/div[text()="Cổng voucher"]')))
		find_gate_voucher_tab.click()

		# in "Cổng voucher" Find the whole campaigns array
		gate_voucher_whole_campaigns = browser.find_elements(By.CSS_SELECTOR, "div.aplus-module-auto-exp > div")

		# Loop through the "Cổng voucher" campaign array
		for find_each_campaign_in_gate in gate_voucher_whole_campaigns:

			# Find list the campaign voucher in the array
			campaigns = find_each_campaign_in_gate.find_elements(By.XPATH, '//div[@data-spm="scene_card"]')
			
				# Loop through the list campaign voucher array & click the first campaign
			for campaign in campaigns:




				try:
					campaign.click()
				except:
					pass
				time.sleep(2)
		
