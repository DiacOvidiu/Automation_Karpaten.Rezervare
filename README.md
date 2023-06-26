# Automation_Karpaten.Rezervare
Automatizarea unei rezervari pe platforma Karpaten.ro si verificarea acesteia prin afisarea ID-ului de rezervare la finalul acesteia

În acest exemplu, se utilizează Selenium pentru a deschide un browser Chrome și a interacționa cu diferite elemente de pe site-ul karpaten.ro pentru a realiza o rezervare de hotel.

Iată o descriere pas cu pas a ceea ce face acest cod:

1. Se importă modulele necesare din pachetul Selenium: webdriver, Service, By, WebDriverWait, EC și Select.
2. Se specifică calea către driverul Chrome (chromedriver).
3. Se configurează opțiunile pentru Selenium și se creează un obiect driver de tipul webdriver.Chrome, care reprezintă browserul Chrome.
4. Se maximizează fereastra browserului.
5. Se deschide pagina principală a site-ului karpaten.ro.
6. Se așteaptă până când butonul de acceptare a cookie-urilor devine vizibil și se face clic pe el.
7. Se accesează pagina de căutare a hotelului.
8. Se accesează pagina hotelului specificat.
9. Se alege o cameră și se face rezervarea.
10. Se completează detaliile rezervării, cum ar fi numele, adresa de e-mail, adresa etc.
11. Se fac acțiuni suplimentare, cum ar fi bifarea unor opțiuni, completarea datelor personale etc.
12. Se finalizează rezervarea prin acceptarea termenilor și condițiilor.

Se pot adăuga și alte acțiuni sau verificări specifice, în funcție de nevoile tale.
Selenium oferă o multitudine de funcționalități și metode pentru a automatiza diferite acțiuni într-un browser web. 
În exemplul de mai sus, se utilizează metodele de localizare a elementelor (de exemplu, By.CSS_SELECTOR, By.ID) și metodele de așteptare (de exemplu, WebDriverWait) pentru a interacționa cu elementele de pe pagină.
