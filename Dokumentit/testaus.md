Testaus dokumentti
-

---

Viimeisin coverage report:  
<img width="722" height="364" alt="kuva" src="https://github.com/user-attachments/assets/8fe8de52-d830-43db-94b2-a00b5cddc95e" />


---

Pelin testit:
game_test.py testaa, että pelin logiikka toimii oikein eri tapauksissa.  
Testeihin kuuluu:  
-Lauta aloituksessa tyhjä varmistus  
-Liikken teko toimii oikein  
-Täyteen sarakkeeseen nappulan tiputtaminen ei onnistu  
-Onko pelilauta tyhjä vai ei palauttaa True tai False oikein  
-Pelilaudan tulostus onnistuu  
-Joka suuntaan voiton tarkistus toimii (pysty, vaaka, molemmat vinot)  
-Voiton tarkistus palauttaa False, jos ei voittoa  
-Peli palauttaa vain lailliset liikkeet, niitä kutsuessa  
-Viime siirron voiton tarkistus joka suuntaan toimii (pysty, vaaka, molemmat vinot)

Tämän hetkinen coverage on: 100%

---

Minimax tekoälyn testit:  
Connect4AI_test.py testaa, että minimax ja sen käyttäminen metodien logiikka on oikeaa ja toimivaa  
Testeihin kuuluu:  
-Tekoäly löytää välittömät voitot (1 siirto depth=0) itselleen ja vastustajalle ja suosii omaa voittoa  
-Evaluate window toimii oikein ja antaa oikean arvon 4 nappulan ikkunoille (kaikki yhdistelmät)  
-Neljä eri tapausta, jotka testaavat evaluate_board toimivan oikein ja palauttavan oikean heuristisen arvon  
-Kaksi testiä minimaxille, toinen testaa löytääkö minimax syvyydellä 5 taatun voiton ja toinen samaan tapaukseen, kun voittoon 3 siirtoa  
-Kolme erillistä testiä parhaan liikkeen tekemiseen, jotka varmistavat, että tekoäly tekee parhaan liikkeen (Liikkeet tarkastettu Connect4 solver avulla)  
-Testi tasapeli tilanteeseen

Tämän hetkinen coverage on: 100%
