from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "https://myadress.com/"


def test_send_message_by_prepod():
	try:
		browser = webdriver.Chrome()
		browser.maximize_window()
		browser.implicitly_wait(5)
		browser.get(link)
		input1 = browser.find_element(By.CSS_SELECTOR, '[name="email"]') # старт авторизации администратором
		input1.send_keys("test1@test.ru")
		input2 = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
		input2.send_keys("123123")
		button = browser.find_element(By.CSS_SELECTOR, '.m-button.m-button_view_fill.m-button_size_big')
		button.click() # авторизация администратором завершена
		button_users = browser.find_element(By.XPATH, '//button[text()="Пользователи"]')
		button_users.click()
		button_student = browser.find_element(By.XPATH, '//div[text()="Преподаватели"]')
		button_student.click()
		input_student = browser.find_element(By.XPATH, '//div[@class="row align-center"]/div[2]//div[@class="v-text-field__slot"]/input')
		input_student.send_keys("Преподаватель Иванов") # поиск преподавателя в базе через веб интерфес приложения
		time.sleep(1)
		button_student_find = browser.find_element(By.CSS_SELECTOR, '.mr-2.v-btn.v-btn--contained.theme--light.v-size--default.primary')
		button_student_find.click() # кнопка входа администратором за преподавателя в рабочую зону приложения
		time.sleep(1)
		button_student_find2 = browser.find_element(By.CSS_SELECTOR, '.v-icon.notranslate.v-icon--link.mdi.mdi-account.theme--light.ml-1.mr-1')
		button_student_find2.click()
		time.sleep(1)		
		button_messages = browser.find_element(By.XPATH, '//div[contains(text(), "Повідомлення")]')
		button_messages.click()
		time.sleep(1)
		button_open_chat = browser.find_element(By.XPATH, '//button[text()="Створити чат"]')
		button_open_chat.click()
		time.sleep(1)
		button_open_chat_group = browser.find_element(By.XPATH, '//h4[contains(text(),"eng_ege_on_personal_god_101218_41m")]')
		button_open_chat_group.click()
		time.sleep(1)
		button_open_chat_student = browser.find_element(By.XPATH, '//a[contains(text(),"Учень 143640")]')
		button_open_chat_student.click()
		time.sleep(1)
		input_theme = browser.find_element(By.CSS_SELECTOR, '[name="theme"]')
		input_theme.send_keys("Тестовая тема")  # ввод темы сообщения
		time.sleep(1)
		input_message = browser.find_element(By.CSS_SELECTOR, '[data-placeholder="Твоє повідомлення"] > p')
		input_message.send_keys("Тестовое сообщение")  # ввод тела сообщения
		time.sleep(1)
		button_open_message = browser.find_element(By.CSS_SELECTOR, '.m-button.form__create-chat-btn.m-button_view_empty.m-button_size_normal')
		button_open_message.click()
		time.sleep(1)
		button_open_prepod_profile = browser.find_element(By.CSS_SELECTOR, '.user-block__arrow.svg-icon.svg-fill.svg-up')
		button_open_prepod_profile.click()
		time.sleep(1)
		button_prepod_signout = browser.find_element(By.CSS_SELECTOR, '[href="/signout"]')
		button_prepod_signout.click() # разлогин преподавателем
		input1 = browser.find_element(By.CSS_SELECTOR, '[name="email"]') # после разлогина нас возвращает на страницу авторизации
		input1.send_keys("test1@test.ru") 
		input2 = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
		input2.send_keys("123123")
		button = browser.find_element(By.CSS_SELECTOR, '.m-button.m-button_view_fill.m-button_size_big')
		button.click() # снова авторизуемся администратором и далее ищем ученика
		button_users = browser.find_element(By.XPATH, '//button[text()="Пользователи"]')
		button_users.click()
		button_student = browser.find_element(By.XPATH, '//div[text()="Студенты"]')
		button_student.click()
		input_student = browser.find_element(By.XPATH, '//div[@class="row align-center"]/div[4]//div[@class="v-text-field__slot"]/input')
		input_student.send_keys("Студент Петров") # поиск ученика
		button_student_find = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.mr-2.v-btn.v-btn--contained.theme--light.v-size--default.primary')))
		button_student_find.click() # кнопка входа администратором за ученика в рабочую зону приложения
		time.sleep(2) 
		button_student_find2 = browser.find_element(By.CSS_SELECTOR, '.v-icon.notranslate.v-icon--link.mdi.mdi-account.theme--light.ml-1.mr-1')
		button_student_find2.click()
		time.sleep(1)
		button_student_open_chat = browser.find_element(By.CSS_SELECTOR, '[href="/chat/"]')
		button_student_open_chat.click() # открытие чата
		prepod_name = browser.find_element(By.CSS_SELECTOR, '.dialog__name')
		assert "Преподаватель Иванов" in prepod_name.text   # проверка , то что в сообщении нужный преподаватель , по имени преподавателя
		prepod_message = browser.find_element(By.CSS_SELECTOR, '.dialog__message-body')
		assert "Тестовое сообщение" in prepod_message.text  # проверка тела сообщения 
		prepod_theme = browser.find_element(By.CSS_SELECTOR, '.dialog-preview__text')
		assert "Тестовая тема" in prepod_theme.text # проверка темы сообщения

	finally:
		browser.quit()
if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")	