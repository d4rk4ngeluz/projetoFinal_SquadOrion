from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

class Navegador:
    def __init__(self, url):
        self.navegador = Firefox()
        self.navegador.maximize_window()
        self.url = url

    def acessar_site(self):
        self.navegador.get(self.url)

    def preencher_formulario(self, email, password):
        form_email = self.navegador.find_element(By.NAME, "email")
        form_email.send_keys(email)
        form_password = self.navegador.find_element(By.NAME, "password")
        form_password.send_keys(password)
        self.navegador.find_element(By.XPATH, "/html/body/div/main/form/button").click()
        sleep(5)

    def adicionar_item(self, nome, descricao, preco, desconto, imagem):
        self.navegador.find_element(By.XPATH, "//*[contains(text(), ' Adicionar')]").click()
        sleep(5)
        self.navegador.find_element(By.ID, "mui-2").send_keys(nome)
        sleep(0.5)
        self.navegador.find_element(By.ID, "mui-3").send_keys(descricao)
        sleep(0.5)
        self.navegador.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/div[3]/div/label[3]").click()
        sleep(0.5)
        self.navegador.find_element(By.ID, "mui-4").send_keys(preco)
        sleep(0.5)
        self.navegador.find_element(By.ID, "mui-6").send_keys(desconto)
        sleep(0.5)
        self.navegador.find_element(By.XPATH, "//*[@id='mui-5']").send_keys(imagem)

    def cadastrar_item(self):
        self.navegador.find_element(By.XPATH, "/html/body/div/header/section[2]/div/div[1]/div/form/button").submit()
        sleep(5)

    def fechar_navegador(self):
        self.navegador.quit()

# Uso da classe
navegador = Navegador("https://projetofinal.jogajuntoinstituto.org/")
navegador.acessar_site()
navegador.preencher_formulario("orion@squadorion.org", "orion1234")
navegador.adicionar_item("Bolsa Clássica Jessica Sun", "Bolsa Clássica Jessica Sun - Branca", "205,50", "20,00", 'f:\IJJ\Itensdesafio\jessica.jpg')
navegador.cadastrar_item()
navegador.fechar_navegador()
