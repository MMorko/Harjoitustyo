Ohjelman rakenne:
-

Ohjelma koostuu kolmesta eri tiedostosta: peli (game.py), tekoäly(AI.py) ja käyttöliittymä (play.py)

---

Peli (game.py):
game.py sisältää luokan Connect4 pelille, joka pitää sisällään kaikki metodit pelin toiminalle  
Peliä kutsuessa se luo tyhjän 6*7 kokoisen laudan  
<img width="614" height="79" alt="kuva" src="https://github.com/user-attachments/assets/fdcc0e1b-73cf-4d50-8f16-8df2be7df202" />

Nappulan lisääminen laudalle  
<img width="552" height="267" alt="kuva" src="https://github.com/user-attachments/assets/36fc499a-a8fc-4936-b08a-f081aa23eef7" />

Nappulan poistaminen laudalta  
<img width="362" height="137" alt="kuva" src="https://github.com/user-attachments/assets/cffcf382-f62c-45c6-bbe8-cc94d869e9e7" />

Laudan täytenäisyyden tarkistaminen  
<img width="328" height="190" alt="kuva" src="https://github.com/user-attachments/assets/a3226892-e918-49ca-a9c7-7131da5fefb7" />

Laudan tulostus  
<img width="329" height="118" alt="kuva" src="https://github.com/user-attachments/assets/9ad0c1eb-da5a-45f6-9d45-831c507d2810" />

Voiton tarkistus (viimeiselle liikkeelle ja koko laudalle)  
<img width="624" height="513" alt="kuva" src="https://github.com/user-attachments/assets/d67e37fe-7b63-4fdb-9709-7e3f76aded65" />  
<img width="666" height="418" alt="kuva" src="https://github.com/user-attachments/assets/06685479-a352-4c26-a981-d0d21d31dd74" />

Metodi, joka palauttaa laudan  
<img width="332" height="96" alt="kuva" src="https://github.com/user-attachments/assets/ede72658-b877-4ad6-ace4-7025b96557c4" />

Laillisten liikkeiden saanti  
<img width="498" height="212" alt="kuva" src="https://github.com/user-attachments/assets/c6924569-d971-4049-9cb3-90129fba2096" />


---

Tekoäly (AI.py):
AI.py on ohjelman pääkohta ja pitää sisällään minimax ja alpha-beta karsintaa hyödyntävän luokan tekoälylle  
Tekoälyä kutsuessa, sille määritellään tekoälyn nappula, syvyyshaku ja aikaraja  
<img width="426" height="132" alt="kuva" src="https://github.com/user-attachments/assets/8fb272d2-2e4b-456c-92c7-9ee845d37a5c" />  

Tekoälyn pää funktio on best_move, jolle annetaan pelin luokka, jota se käyttää hyväkseen  
Funktio samalla luo sanakirjan, johon tallenetaan pelilaudan liikkeitä ja tilanteita ja aloittaa aika laskennan  
<img width="446" height="191" alt="kuva" src="https://github.com/user-attachments/assets/f7b71fa5-30e9-4fd6-8628-c82ac1cdb62f" />


best_move käy ensiksi läpi onko mahdollista välitöntä voittavaa liikettää itselleen tai vastustajalle ja tekee siirron niiden perusteella (priorisoi voittoa),
jos voittavia siirtoja ei löydy siirtyy tekoäly iteratiiviseen syvenemiseen 
<img width="489" height="250" alt="kuva" src="https://github.com/user-attachments/assets/4d281b0a-7aa6-4b71-b0f2-56ad92cae88c" />


Iteratiivsessa syvenemisesä tehdään syvyyden mukaan iteraatioita, joissa kutsutaan minimaxia, joka palauttaa parhaimman siirron, kunnes päästeen tilanteeseen, jossa iteraatio loppuu
tai minimax palauttaa None  
<img width="483" height="212" alt="kuva" src="https://github.com/user-attachments/assets/b830e992-41a2-467e-980c-7f27c676a3cd" />

minimax, jota best_move() kutsuu, tarvitsee pelin luokan, hakusyvyyden, maksimoiko vai ei, sekä alphan ja betan  
<img width="536" height="242" alt="kuva" src="https://github.com/user-attachments/assets/ee639b3c-9b0e-4189-a131-778b31e70d45" />

minimax aloittaa toiminnan aikarajan ylittymisen testaamisesta ja lopettaa toiminnon, jos se ylittyy, tämän jälkeen minimax suorittaa 3 eri testiä riippuen maksimoiko se vai ei. Testis ovat voiton tarkistus, onko pelilauta täynnä ja jos 0 syvyys on saavutettu  
<img width="639" height="248" alt="kuva" src="https://github.com/user-attachments/assets/9d1d9c02-574d-4ae4-b1f0-b999db41a3c5" />

Tämän jälkeen minimax luo laudan tilanteelle avaimen ja tallentaa pelilaudan avaimen kanssa muistiin  
<img width="432" height="161" alt="kuva" src="https://github.com/user-attachments/assets/a354aae5-c9a6-4dd3-a833-3b2c636f7f92" />

Jos minimax maksimoi suoritetaan maksimointi, jossa minimax käy läpi jokaisen laillisen liikkeen ja kutsuu itseään minimoimalla ja aina pienemällä syvyydellä ja arvioi parhaimman liikkeen pelilaudan arvon perusteella  
<img width="528" height="439" alt="kuva" src="https://github.com/user-attachments/assets/6c0c6d6c-4110-436e-9ca1-3d1d2bf16675" />

Jos minimax minimoi suoritetaan minimointi, joka on käytännössä täysin sama, kuin maksimointi, mutta vastustajalle  
<img width="521" height="439" alt="kuva" src="https://github.com/user-attachments/assets/0072d331-568e-4bb7-b8dc-1e17cef4beec" />

Kun minimax on päässyt syvyyteen 0 arvioidaan laudan tilanne evaluate_board avulla. Evaluate board tarvitsee pelin luokan, sekä nappulan, jolle se laskee pelin tilanteen. Ensimmäisenä evaluate_board luo kaikki tarvitsemansa tiedot sen toiminnalle    
<img width="348" height="256" alt="kuva" src="https://github.com/user-attachments/assets/a33efa89-2de9-4bc6-9b7f-2956553aedbc" />

Tämän jälkeen evaluate_board käy läpi kaikki 4 ruudun pituiset ikkunat vino, pysty ja vaakasuuntiin ja lisää pelilaudan arvoon pisteet mitä evalute_window palauttaa  
<img width="468" height="363" alt="kuva" src="https://github.com/user-attachments/assets/26426f80-8ad3-45dd-a3c8-694ab5b5c761" />

evaluate_window on heuristiikan pohja, joka palauttaa arvon perusteella, kuinka monta tyhjää ja omaa nappulaa tai monta tyhjää ja vastustajan nappulaa yhdessä 4 ruudun ikkunassa on.  
<img width="352" height="513" alt="kuva" src="https://github.com/user-attachments/assets/297fe47f-0181-4e3c-b969-8dd704e88aba" />

Tekoäly suorittaa toiminnot tässä järjestyksessä ja lopulta palautta parhaimman liikkeen, jota sen on ehtinyt laskea 

---

Käyttöliittymä (play.py):  
Tuodaan peli ja tekoäly  
<img width="196" height="42" alt="kuva" src="https://github.com/user-attachments/assets/cd375f66-6014-4985-86ea-f883f60f3e6f" />

Luodaan kutsuttava funktio ja määritellään pelaajat, tekoäly syvyys ja aikaraja käyttäjän syötteiden perusteella  
<img width="664" height="229" alt="kuva" src="https://github.com/user-attachments/assets/6959f791-dd5a-45cc-b04a-896df2e1f0d8" />

Silmukka, joka suoritta pelin pelaamisen. Silmukassa vaihdetaan siirron tekijää perustellaa, kuka teki siirron viimeksi. Voitto tarkistus on silmukan lopussa ja laudan tulostus alussa  
<img width="602" height="552" alt="kuva" src="https://github.com/user-attachments/assets/f87492e2-52b2-4ca6-9981-42dd32a6ee96" />




Saavutetut aika- ja tilavaativuudet, Suorituskyky- ja O-analyysivertailu:
-
b = Haarautumisluku (sarakkaiden määrä: 7)  
d = Hakusyvyys

Minimax:  
Aikavaativuus: O(b^d)  
Tilavaativuus: O(b)  

Alpha-beta karsinnan kanssa:  
Aikavaativuus: O(b^(d/2))  
Tilavaativuus: O(b)  

Iteratiivinen syveneminen:  
Aikavaativuus: O(b^d)  
Tilavaativuus: O(b)  

Koko tekoäly (ilman aikarajoitusta):  
Aikavaativuus: Pahimillaan O(b^d) ja parhaimillaan O(b^(d/2))  
Tilavaativuus: O(b)  

Työn mahdolliset puutteet ja parannusehdotukset:
-
Heuristiikka funktio on alkeellinen ja sitä voisi optimoida  
Tekoäly ei pelaa täydellisesti ja häviää täydellisesti pelaaville tekoälyille  
Testaus voisi aina olla kattavampaa  
Käyttöliittymä on rajoitteellinen ja sitä on välillä hankala lukea  

Laajojen kielimallien käyttö:
-
Käytetyt laajat kielimallit olivat ChatGPT ja Copilot.  
Kielimalleja käytettiin:  
-Koodin debugaamiseen  
-Koodin opitmisointi ehdotuksiin  
-Minimax funktion analysointiin pseudokoodilla  
-Vaatimusten täyttymisen analysointiin  
-Aika- ja tilavaatimusten analysointiin  

Merkitykselliset lähteet:
-
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning  
https://en.wikipedia.org/wiki/Minimax  
https://www.neverstopbuilding.com/blog/minimax  
https://www.youtube.com/watch?v=DV5d31z1xTI  
