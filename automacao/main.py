from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

#ABRIR NAVEGADOR
navegador = Firefox()
navegador.maximize_window()
url = "https://projetofinal.jogajuntoinstituto.org/"

#ACESSAR SITE
navegador.get(url)

form_name = navegador.find_element(By.NAME, "email")
form_name.send_keys("orion@squadorion.org")
form_name = navegador.find_element(By.NAME, "password")
form_name.send_keys("orion1234")
form_name = navegador.find_element(By.XPATH, "/html/body/div/main/form/button").click()
sleep(5)

#ADICIONAR ITEM
navegador.find_element(By.XPATH, "//*[contains(text(), ' Adicionar')]").click()
sleep(5)

navegador.find_element(By.ID, "mui-2").send_keys("Bolsa Clássica Jessica Sun")
sleep(0.5)
navegador.find_element(By.ID, "mui-3").send_keys("Bolsa Clássica Jessica Sun - Branca")
sleep(0.5)
navegador.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[3]").click()
sleep(0.5)
navegador.find_element(By.ID, "mui-4").send_keys("205,50")
sleep(0.5)
navegador.find_element(By.ID, "mui-6").send_keys("20,00")
sleep(0.5)
navegador.find_element(By.XPATH, "//*[@id='mui-5']").send_keys('D:\IJJ\Itensdesafio\jessica.jpg')

#CADASTRAR ITEM
navegador.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/button").submit()
sleep(5)

#FECHAR NAVEGADOR
navegador.quit()





# pyautogui.click(x=865, y=725)
# pyautogui.write("D:\IJJ\Itensdesafio\Tenis_infantil.jpg")
# pyautogui.press("Enter")
  


# @when("clicar em enviar novo produto")
# def form_text(context):
#     btn = context.browser.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/button")
#     btn.submit()


# # button = WebDriverWait(navegador, 5).until(EC.visibility_of_element_located((By.XPATH, 
# # "//*[contains(text(), ' Adicionar')]")))
# # ActionChains(navegador).move_to_element(button).perform()

# # form_email = navegador.find_element(By.NAME, "email").send_keys("mgeambastiane@gmail.com")
# # form_body = navegador.find_element(By.NAME, "body").send_keys("Automação com Selenium Web Driver")
# # form_select = navegador.find_element(By.NAME, "assunto")


# # select = Select(form_select)

# # select.select_by_visible_text("Contratar profissionais")

# # form_btn = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")

# # print(form_btn)

# # form_btn.submit()

# # # resultados.click()

