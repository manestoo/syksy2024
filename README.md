# Suunnantunnistus projekti

### Laitteisto ja teknologia:
- nRF5340 Development Kit
- Raspberry Pi
- GY-61 ADXL335 kiihtyvyysanturi
- Linux-palvelin tietokantaa varten
- MySQL-tietokanta
- Python-ohjelmat Rasberrylle sensoridatan lähetystä sekä vastaanottoa varten

![Komponentit](https://github.com/user-attachments/assets/56c4bbcd-2feb-4b4c-8b8e-515688ba0762)


### Projektin tavoite:
Tavoitteena oli lähettää kiihtyvyysanturilta dataa tietokantaan. Sensoridataa voidaan tutkia sitten selaimella, ja tätä varten asennettiin Linux-palvelimet. Tietokantaan tallennettua kiihtyvyysanturin dataa käytetään K-means-algoritmin luomiseksi, jonka tarkoituksena on tunnistaa missä suunnassa kiihtyvyysanturi on.
Eli päämääränä on saavuttaa tulos, jossa kehitysalustan nappia painamalla saadaan kiihtyvyysanturin senhetkinen asento.

![Datan_kulku](https://github.com/user-attachments/assets/91382a94-d39f-4224-85d5-0451f590b7eb)


### Haasteita ja opetuksia:

25.11.2024:
Suurin haaste tähän asti oli saada Raspberrylle dataa vastaanottava ja lähettävä koodi. Datan vastaanottaminen oli helppoa nRF:ltä, mutta datan lähettämisessä tietokantaan tuli ongelmia. X-, y- ja z-akselin sensoridata tallentui aluksi tietokantaan kummallisen suurina arvoina, sekä sinne tallentui virheellisesti samoja arvoja useita kertoja. Pitkän pähkäilyn jälkeen asia korjaantuikin, kun kiihtyvyysanturiin menevä pin nRF-laitteesta vaihdettiin 5V -> VCC.

30.11.2024
Saimme luotua K-means algoritmin, johon syötetään sensoridataa. Malli oppi datan x-, y- ja z -suunnista tunnistamaan millaisessa asennossa laite on fyysisesti. Tämä oli varsin helppo tehdä.
![K-means](https://github.com/user-attachments/assets/298eddae-4990-499b-814c-541c94dade5f)

Projekti oli hyvin moniulotteinen, sillä se sisälsi laitteiden kanssa työskentelyä, palvelimien käsittelyä sekä koneoppimista. Voin sanoa että Linux-komennot tulivat projektin aikana tutuksi. Oli myös oppimisen kannalta palkitsevaa saada kokonaiskuvaa ja ymmärrystä siitä mitä tällaisen IoT-laitteen tai tuotteen takana todella saattaa tapahtua.
