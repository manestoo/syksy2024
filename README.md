# Tietoliikenteen sovellusprojekti

### Laitteisto ja teknologia:
- nRF5340 Development Kit
- Raspberry Pi
- GY-61 ADXL335 kiihtyvyysanturi
- Linux-palvelin tietokantaa varten
- MySQL-tietokanta
- Python-ohjelmat Rasberrylle sensoridatan lähetystä sekä vastaanottoa varten

### Projektin tavoite:
Mitata kiihtyvyysanturilla dataa x-, y- ja z-akselilta. Data lähetetään sitten Bluetoothin kautta Raspberrylle Pille. Raspberry on yhdistettynä lähiverkkoon ethernet-kaapelilla, ja se vastaanottaa sensoridatan ja lähettää sen lähiverkossa sijaitsevaan tietokantaan. Tietokantaan tallennettua dataa käytetään sitten koneoppimisen parissa.


![Komponentit](https://github.com/user-attachments/assets/56c4bbcd-2feb-4b4c-8b8e-515688ba0762)

### Haasteita ja opetuksia:

25.11.2024:
Suurin haaste tähän asti oli saada Raspberrylle dataa vastaanottava ja lähettävä koodi. Datan vastaanottaminen oli helppoa nRF:ltä, mutta datan lähettämisessä tietokantaan tuli ongelmia. X-, y- ja z-akselin sensoridata tallentui aluksi tietokantaan kummallisen suurina arvoina, sekä sinne tallentui virheellisesti samoja arvoja useita kertoja. Pitkän pähkäilyn jälkeen asia korjaantuikin, kun kiihtyvyysanturiin menevä pin nRF-laitteesta vaihdettiin 5V -> VCC.

30.11.2024
Saimme luotua K-means algoritmin, johon syötetään sensoridataa. Malli oppi datan x-, y- ja z -suunnista tunnistamaan millaisessa asennossa laite on fyysisesti. Tämä oli varsin helppo tehdä.


![Datan_kulku](https://github.com/user-attachments/assets/91382a94-d39f-4224-85d5-0451f590b7eb)
