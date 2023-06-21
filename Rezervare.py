from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

# Specificați calea către driverul Chrome (chromedriver)
chrome_driver_path = "D:\chromedriver.exe"

# Configurați opțiunile pentru Selenium și specificați calea către driverul Chrome
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Rulați în modul headless pentru a nu afișa browserul
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

# Maximizam fereastra
driver.maximize_window()
# Pasul 1: Deschideți pagina principală
driver.get("https://www.karpaten.ro/")
sleep(3)

# Așteptați până când butonul de acceptare a cookie-urilor devine vizibil
cookie_accept_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#fairlane-cookie-consent > button"))
)

# Faceți clic pe butonul de acceptare a cookie-urilor
cookie_accept_button.click()


# Pasul 2: Accesați pagina de căutare
driver.get(
    "https://www.karpaten.ro/live/cauta/?hotel-id=&location-id=56&search-checkin=24.08.2023&search-transport=avion&search-destinatie=56&search-oras-plecare=3049&adulti-1=2&copii-1=0&varsta-copil-1-1=0&varsta-copil-2-1=0&varsta-copil-3-1=0&varsta-copil-4-1=0&search-data=22-07-2023&liveNights=7&liveNights=7")
sleep(3)
# Pasul 3: Accesați pagina hotelului
driver.get(
    "https://www.karpaten.ro/oferta-cazare-viking-star-kemer-antalya/charter-antalya-viking-star-cu-plecare-din-bucuresti/#avion/50199/24.08.2023/7/2")
sleep(3)
# Pasul 4: Alegeți o cameră și rezervați

try:
    # Alegeți o cameră
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.label-title"))).click()
    sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='submit'][value='REZERVA ACUM'][class='btn btn-primary btn-md-block']"))).click()
    sleep(3)
    # Completați detaliile rezervării (exemplu: completați numele și adresa de e-mail)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fnet_karpaten_reservation_client_lastName"))).send_keys("Diac - TESTE")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fnet_karpaten_reservation_client_firstName"))).send_keys("Ovidiu - TESTE")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fnet_karpaten_reservation_client_email"))).send_keys("diac5@gmail.com")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fnet_karpaten_reservation_client_phone"))).send_keys("0754775329")

    # Identificați elementul pe care doriți să faceți clic
    element = driver.find_element(By.ID, "persoana-fnet_karpaten_reservation_client_facturaPj_0")

    # Executați un script JavaScript pentru a face clic pe element
    driver.execute_script("arguments[0].click();", element)
    #Bifam optiunea ca suntem persoana fizica
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "fnet_karpaten_reservation_client_address"))).send_keys("Str.Vamii, nr.1")
    #Selectam judetul Sibiu din lista
    select_element = Select(driver.find_element(By.ID, "fnet_karpaten_reservation_client_county"))
    select_element.select_by_value("Sibiu")
    sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "fnet_karpaten_reservation_client_city"))).send_keys("Dumbraveni")

    # Bifam optiunea ca suntem Domn
    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='apelativ-1-dl']")
    label_element.click()

    # In cazul in care nu se autocompleteaza cu datele de mai sus, activam cele doua comenzi de mai jos
    # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "nume-1"))).send_keys("Diac")
    # WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "prenume-1"))).send_keys("Ovidiu")
    # sleep(3)

    # Completam data nasterii
    data_nasterii_element = driver.find_element(By.ID, "data-nasterii-1")
    data_nasterii_element.send_keys("15/03/1998")
    sleep(3)

    # Bifam optiunea ca avem pasaport temporar
    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='documentType-1-pas-temp']")
    label_element.click()

    # Completam campul numar document
    element = driver.find_element(By.ID, "documentNumber-1")
    element.send_keys("987654321")
    sleep(3)

    # Completam data expirarii a pasaportului
    data_nasterii = "25/04/2027"
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "documentExpirationDate-1")))
    element.send_keys(data_nasterii)
    sleep(3)

    # Bifam optiunea ca suntem Doamna
    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='apelativ-2-dna']")
    label_element.click()
    sleep(3)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "nume-2"))).send_keys("Diactest")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "prenume-2"))).send_keys("Ovidiutest")

    # Completam data nasterii
    data_nasterii_element = driver.find_element(By.ID, "data-nasterii-2")
    data_nasterii_element.send_keys("30/04/1995")
    sleep(3)

    # Bifam optiunea ca avem pasaport
    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='documentType-2-pas']")
    label_element.click()

    # Completam campul numar document
    element = driver.find_element(By.ID, "documentNumber-2")
    element.send_keys("123456789")
    sleep(3)

    # Completam data expirarii a pasaportului
    data_nasterii = "25/04/2027"
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "documentExpirationDate-2")))
    element.send_keys(data_nasterii)
    sleep(3)

    # Bifam optiunea ca nu dorim asigurare
    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='no-insurance']")
    label_element.click()
    sleep(5)

    # Bifam optiunea ca platim integral
    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='fnet_karpaten_reservation_paymentTerms_1']")
    label_element.click()
    sleep(3)

    # Bifam optiunea de plata
    label_element = driver.find_element(By.CSS_SELECTOR, "label[for='fnet_karpaten_reservation_paymentMethod_1']")
    label_element.click()
    sleep(3)

    # Scriem un mesaj pentru rezervarea noastra
    mesaj = "Aceasta este o rezervare de TEST. Rog programatorii sa stearga din baza de date aceasta rezervare. Multumesc"
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "fnet_karpaten_reservation_message")))
    element.send_keys(mesaj)
    sleep(3)

    # Sunt de acord cu termenii si conditiile, contractul cu turistul si cu prelucrarea datelor cu caracter personal.
    try:
        # Caută elementul după ID
        element = driver.find_element(By.ID, "termeni-si-conditii")
    except NoSuchElementException:
        try:
            # Caută elementul după nume
            element = driver.find_element(By.NAME, "conditions_acceptance")
            if element.get_attribute("type") != "checkbox":
                raise NoSuchElementException("Elementul găsit nu este un checkbox.")
        except NoSuchElementException:
            print("Nu s-a găsit elementul.")
            # Puteți adăuga aici codul pentru tratarea cazului în care elementul nu a fost găsit
    else:
        # Execută un script JavaScript pentru a face clic pe element
        driver.execute_script("arguments[0].click();", element)
        sleep(3)

    # Faceți clic pe butonul "Rezervați acum"
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID, "reservationFormSubmitButton"))).click()
    sleep(3)
    # Așteptați confirmarea rezervării

try:
    # Așteptați confirmarea rezervării și obțineți ID-ul de rezervare
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.page-subtitle strong")))
    reservation_id = element.text.strip()
    print("Rezervarea a fost realizată cu succes!")
    print("ID rezervare:", reservation_id)

    is_id_valid = True
    if not isinstance(reservation_id, int) or reservation_id <= 0:
        is_id_valid = False

    assert is_id_valid == True

except Exception as e:
    print("A apărut o eroare în timpul rezervării:")
    traceback.print_exc()

finally:
    # Închideți browser-ul și încheiați sesiunea
    driver.quit()

