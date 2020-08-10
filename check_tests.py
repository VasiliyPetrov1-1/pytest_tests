from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "https://myaddress.com/"


def test_check_test():
	try:
		browser = webdriver.Chrome()
		browser.maximize_window()
		browser.implicitly_wait(2)
		browser.get(link)
		input1 = browser.find_element(By.CSS_SELECTOR, '[name="email"]') #авторизация администратором
		input1.send_keys("user@test.ru")
		input2 = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
		input2.send_keys("123")
		button = browser.find_element(By.CSS_SELECTOR, '.m-button.m-button_view_fill.m-button_size_big')
		button.click()
		time.sleep(1) # авторизация администратором завершена
		browser.get('https://myaddress.com/student_page')  # переход к странице студента
		assert "adm-panel" in browser.current_url, "u a not on admin page now" # проверка , что мы на странице администратора, т.е. авторизация действительно прошла
		browser.execute_script("window.scrollTo(0, 0)")
		time.sleep(1)
		button_enter_by_student = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.mr-1.v-btn.v-btn--contained.theme--dark.v-size--default.error')))
		button_enter_by_student.click() # кнопка входа администратором за ученика в рабочую зону приложения
		button_choise_group = browser.find_element(By.CSS_SELECTOR, '.m-select__arrow.svg-icon.svg-fill') # далее идет последовательный переход к странице с вопросом теста
		button_choise_group.click()
		button_select_group = browser.find_element(By.XPATH, '//li[@class="m-list__item"][last()]//div')
		button_select_group.click()
		button_schedule = browser.find_element(By.XPATH, '//span[text()="Расписание"]')
		button_schedule.click()
		button_practice = browser.find_element(By.CSS_SELECTOR, '[href="/lesson/217301/subjects/10932/practice/kbs/1169"]')
		button_practice.click()
		button_practice2 = browser.find_element(By.CSS_SELECTOR, 'a[href="/lesson/217301/subjects/10932/practice/kbs/4066?type=offline"]')
		button_practice2.click()
		time.sleep(1)
		button_test_number_3 = browser.find_element(By.XPATH, '//a[text()=" 3 "]')
		button_test_number_3.click()
		input_answer = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Твой ответ"]')
		input_answer.send_keys("test")
		b_get_answer = browser.find_element(By.CSS_SELECTOR, '.m-button.practice-page-main-footer__send-anser-btn.m-button_view_fill.m-button_size_normal')
		b_get_answer.click()  # введен ответ на тест
		time.sleep(1)
		wrong_answer = browser.find_element(By.CSS_SELECTOR, 'div.practice-page-main-footer__top > div.practice-page-main-footer__left > div > strong')
		one_more_chance = browser.find_elements(By.XPATH,'//button[text()="Попробуй еще раз"]')
		know_answer = browser.find_elements(By.XPATH,'//button[text()=" Узнать ответ "]')
		go_to_next = browser.find_elements(By.XPATH,'//button[text()="Перейти к следующему"]')
		assert 'Неправильно' == wrong_answer.text, 'answer is not wrong' # проверка, что ответ неверный
		assert len(one_more_chance) >= 1, 'button one_more_chance doesnt exist' # проверка, что есть кнопка "попробовать еще раз"
		assert len(know_answer) >= 1, 'button know_answer doesnt exist' # проверка, что есть кнопка "узнать ответ"
		assert len(go_to_next) >= 1, 'button go_to_next doesnt exist' # проверка наличия кнопки - перехода к следующему вопросу
		browser.refresh()
		time.sleep(4)
		assert 'Неправильно' == wrong_answer.text, 'answer is not wrong' # те же проверки, что и выше после обновления страницы, некоторые элементы могли "слететь"
		assert len(one_more_chance) >= 1, 'button one_more_chance doesnt exist'
		assert len(know_answer) >= 1, 'button know_answer doesnt exist'
		assert len(go_to_next) >= 1, 'button go_to_next doesnt exist'
		
	finally:
		time.sleep(2)
		browser.quit()
		
if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")