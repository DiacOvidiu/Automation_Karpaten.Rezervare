# Automation_Karpaten.Rezervare
Automatizarea unei rezervari pe platforma Karpaten.ro si verificarea acesteia prin afisarea ID-ului de rezervare la finalul acesteia


Exemplu de utilizare a Selenium pentru automatizarea rezervărilor de hotel
În acest exemplu, vom utiliza Selenium pentru a deschide un browser Chrome și a interacționa cu diferite elemente de pe site-ul karpaten.ro în scopul realizării unei rezervări de hotel.

Descrierea pas cu pas a codului:

1.Importarea modulelor necesare din pachetul Selenium: webdriver, Service, By, WebDriverWait, EC și Select.
2. Specificarea căii către driverul Chrome (chromedriver).
3. Configurarea opțiunilor pentru Selenium și crearea unui obiect driver de tipul webdriver.Chrome, care reprezintă browserul Chrome.
4. Maximizarea ferestrei browserului.
5. Deschiderea paginii principale a site-ului karpaten.ro.
6. Așteptarea până când butonul de acceptare a cookie-urilor devine vizibil și apoi se face clic pe el.
7. Accesarea paginii de căutare a hotelului.
8. Accesarea paginii hotelului specificat.
9. Alegerea unei camere și realizarea rezervării.
10. Completarea detaliilor rezervării, cum ar fi numele, adresa de e-mail, adresa etc.
11. Realizarea unor acțiuni suplimentare, cum ar fi bifarea unor opțiuni, completarea datelor personale etc.
12. Finalizarea rezervării prin acceptarea termenilor și condițiilor.

Pot fi adăugate și alte acțiuni sau verificări specifice, în funcție de nevoile tale. 
Selenium oferă o multitudine de funcționalități și metode pentru a automatiza diferite acțiuni într-un browser web. 

În exemplul de mai sus, se utilizează metodele de localizare a elementelor (de exemplu, By.CSS_SELECTOR, By.ID) și metodele de așteptare (de exemplu, WebDriverWait) pentru a interacționa cu elementele de pe pagină.
Observație: Pentru a utiliza Selenium în acest exemplu, trebuie să ai instalat driverul Chrome (chromedriver) și pachetul Selenium în mediul tău de lucru.
