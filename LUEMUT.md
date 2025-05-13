# Projekti: Suomalaisen onnellisuuden tekijöiden jäljillä

**Tehtävä:** Rohkeasti mennä sinne, missä monet analyytikot ovat jo käyneet, mutta tällä kertaa tekoälypariohjelmoijien kanssa!

## 1. Johdanto: Tyytyväisyyden arvoitus

Suomi, huolimatta maineestaan pidättyväisten ihmisten, haastavan ilmaston ja kieliopin, joka hämmentää kielitieteilijöitä, maana, sijoittuu jatkuvasti maailman onnellisimmaksi maaksi World Happiness Report -raportin mukaan.

Vastaperustettu (ja hieman hämmentynyt) **Iloisuuden ja Hilpeyden Ministeriö (IHM)** pitää tätä ilahduttavana, mutta tarvitsee konkreettista dataa. Onko kyseessä saunat? Yllättävän suuri kahvin kulutus? Tehokkaat sosiaaliset järjestelmät? Raskaiden metallibändien suuri määrä asukasta kohden? Vai jotain aivan muuta?

Tiiminne tavoitteena on kehittää sovellus, joka hakee, analysoi ja visualisoi dataa auttaakseen IHM:ää ymmärtämään mahdollisia syitä Suomen korkeaan onnellisuussijoitukseen. Tarvitsemme datalähtöisiä hypoteseja selkeästi esitettynä!

## 2. Liiketoimintavaatimukset

Tiiminne kehittämän sovelluksen tulee täyttää seuraavat keskeiset vaatimukset:

1. **Datan haku ja sisäänluku:**
    * Sovelluksen tulee pystyä hakemaan tai lukemaan dataa vähintään kahdesta eri ulkoisesta lähteestä (katso ehdotetut lähteet alla).
    * Prosessin tulee olla toistettavissa (eli sovelluksen uudelleen ajaminen hakee tuoreen datan, jos saatavilla, tai käyttää välimuistissa olevaa dataa asianmukaisesti).

2. **Data-analyysi:**
    * Sovelluksen tulee analysoida kerättyä dataa tunnistaakseen mahdollisia korrelaatioita eri yhteiskunnallisten, taloudellisten, ympäristöllisten tai kulttuuristen tekijöiden ja Suomen (sekä mahdollisesti vertailumaiden) onnellisuusindikaattorien välillä.
    * Tiimin tulee määritellä, mitä tekijöitä tutkitaan saatavilla olevan datan perusteella.

3. **Datan visualisointi:**
    * Sovelluksen tulee tuottaa selkeitä ja merkityksellisiä visualisointeja (esim. kaavioita, graafeja, dashboardeja), jotka esittävät analyysin tulokset.
    * Näiden visualisointien tulee auttaa IHM:ää nopeasti ymmärtämään mahdolliset yhteydet, jotka tiiminne on löytänyt. Mitkä tekijät näyttävät korreloivan vahvasti Suomen onnellisuuspisteiden kanssa?

4. **Käyttöliittymä / Tuloste:**
    * Tulokset (keskeiset löydökset, visualisoinnit) tulee esittää helposti saavutettavassa muodossa. Tämä voi olla esimerkiksi:
        * Yksinkertainen verkkokäyttöliittymä/dashboard.
        * Generoidut raporttitiedostot (esim. HTML, PDF), jotka sisältävät tekstiä ja kaavioita.
        * Hyvin muotoiltu konsolituloste ja tallennetut kuvakaaviotiedostot.
    * Käyttöliittymän/tulosteen valinta on tiimin päätettävissä.

5. **Teknologiariippumattomuus:**
    * Toteutusteknologia (ohjelmointikieli, frameworkit, tietokannat, visualisointikirjastot) on täysin **tiimin päätettävissä**. Käyttäkää sitä, minkä tunnette, tai hyödyntäkää tätä mahdollisuutena oppia jotain uutta Copilotin avulla!

## 3. Odotettu lopputulos ja toimitettavat asiat

Työpajan lopussa jokaisen tiimin odotetaan:

1. Saaneen aikaan toimivan sovelluksen, joka täyttää yllä kuvatut liiketoimintavaatimukset.
2. Esittävän lyhyen (5–10 minuutin) demon, joka sisältää:
    * Sovelluksen ominaisuuksien esittelyn (datan haku, analyysilogiikka, visualisoinnit).
    * Keskeiset sovelluksen tuottamat visualisoinnit.
    * Tiimin ensisijaiset hypoteesit Suomen onnellisuuteen vaikuttavista tekijöistä analyysin ja visualisointien perusteella. Muistakaa, että korrelaatio ei tarkoita kausaatiota, mutta se on erinomainen lähtökohta hypoteeseille!

## 4. Mahdolliset datalähteet (nopea aloitus!)

Päästäksenne nopeasti analysoimaan, tässä on suositeltuja lähteitä ja erityisiä ehdotuksia relevanteista datapisteistä tai taulukoista. Keskittykää Suomen dataan ja mahdollisesti 1–2 vertailumaan dataan. **Aloittakaa 1–2 indikaattorilla kahdesta eri lähteestä.**

---

### Valmiiksi ladattu data

Tämä repositorio sisältää kaksi keskeistä datasettiä valmiina `data/`-kansiossa:

- **World Happiness Report 2024:**
    - Tiedosto: `data/WHR2024.csv`
    - Sisältää uusimmat onnellisuussijoitukset ja niihin liittyvät tekijät monille maille, mukaan lukien Suomi.
    - Käyttäkää tätä ensisijaisena lähteenä onnellisuuspisteille ja niihin liittyville muuttujille.

- **Ruokatarjontadata (FAOSTAT, 1961–2011):**
    - Tiedosto: `data/EdibleFoods-1961-2011.csv`
    - Sisältää ruokatarjonta- ja ravitsemustietoja Suomelle ja muille maille ruoka-aineittain ja vuosittain.
    - Käyttäkää tätä tutkiaksenne ravitsemuksen/ruokatrendien ja onnellisuuden välistä suhdetta.

Näitä tiedostoja **ei tarvitse** ladata uudelleen – ne ovat valmiina analyysia ja koodiesimerkkejä varten.

---

1.  **World Happiness Report Data:**
    * **Mikä:** Pääasiallinen lähde onnellisuussijoituksille ja niihin liittyville tekijöille.
    * **Mistä löytää:** Tiedosto `data/WHR2024.csv` on jo mukana tässä repositoriossa.
    * **Hae tämä:** Lataa päädatatiedosto (yleensä Excel tai CSV) **uusimmasta saatavilla olevasta vuodesta** viralliselta [World Happiness Report](https://worldhappiness.report/) -sivustolta (etsi datalisäyksiä/latauksia) tai luotettavalta lähteeltä kuten Kagglelta (Esimerkki: [https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2024](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2024) - tarkista relevanssi).
    * **Avainsarjat käytettäväksi:**
        * `Maan nimi`
        * `Vuosi`
        * `Onnellisuusindeksi` (tai vastaava pääonnellisuuspiste)
        * `BKT per capita`
        * `Sosiaalinen tuki`
        * `Terveellinen elinajanodote`
        * `Vapaus tehdä elämänvalintoja`
        * `Anteliaisuus`
        * `Korruption käsitykset`
    * **Muoto:** CSV tai Excel.
    * **Rekisteröinti/API-avain tarvitaan?:** Yleensä **Ei** suoran latauksen osalta. Kaggle API:n asetukset tarvitaan, jos käytetään.
    * **Bootstrap:** Tämä antaa ytimen onnellisuuspisteelle ja sen yleisesti liitetyille tekijöille suoraan.

2.  **Ruokatarjontadata (Kaggle - FAOSTAT-lähde):**
    * **Mikä:** Dataa ruokatarjonnasta (kg/asukas/vuosi) ja ravitsemuksellisista arvoista (kcal/asukas/päivä, proteiini, rasva) eri ruoka-aineille monissa maissa. Alun perin YK:n elintarvike- ja maatalousjärjestö FAOSTAT:ilta.
    * **Mistä löytää:** Tiedosto `data/EdibleFoods-1961-2011.csv` on jo mukana tässä repositoriossa.
    * **Hae tämä:** Lataa CSV Kagglesta: [https://www.kaggle.com/datasets/aliesmaeilpoor/ediblefoods-1961-to-2011](https://www.kaggle.com/datasets/aliesmaeilpoor/ediblefoods-1961-to-2011)
    * **Avainsarjat/Tiedot käytettäväksi:** Suodata `Alue` (esim. 'Suomi'). Valitse asiaankuuluvat `Tuote`(t) (esim. 'Kala, merenelävät', 'Hedelmät - Ilman viiniä', 'Vihannekset', 'Eläinrasvat', 'Maito - Ilman voita') ja `Elementti`(t) (esim. `Ruokatarjonnan määrä (kg/asukas/vuosi)` tai `Ruokatarjonta (kcal/asukas/päivä)`).
    * **Muoto:** CSV.
    * **Rekisteröinti/API-avain tarvitaan?:** **Kyllä**, Kaggle-tili vaaditaan lataamiseen verkkosivuston käyttöliittymän kautta. Kaggle API:n asetukset tarvitaan ohjelmalliseen lataamiseen.
    * **Bootstrap:** Huomaa, että data **päättyy vuoteen 2011**. Suodata 'Suomi' ja aloita analysoimalla *yksi tai kaksi erityistä ruoka-ainetta* (kuten kala tai hedelmät) tai laajaa `Elementtiä` kuten kokonais `Ruokatarjonta (kcal/asukas/päivä)`. Vertaa sen kehitystä saatavilla olevien onnellisuustietojen kanssa päällekkäisille vuosille, jos mahdollista.

3.  **Tilastokeskus:**
    * **Mikä:** Viralliset suomalaiset tilastot. Rikkaita mutta monimutkaisia. Käytä PxWeb-käyttöliittymää tai API:a.
    * **Hae tämä:**
        * Kun vierailet [StatFin-tietokannan pääsivulla](https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/), voit selata ja valita laajasta valikoimasta tilastoja (esim. BKT, työttömyys, elinajanodote, koulutus jne.).
        * **Tärkeää:** Et voi yksinkertaisesti ladata dataa CSV/Excel-muodossa suoraan kaikista taulukoista. Sen sijaan sinun tulee noutaa data ohjelmallisesti PxWeb API:n avulla.
        * Jokainen taulukko tarjoaa "API-kysely" esimerkin (katso "Näytä API-kysely" tai vastaava painike). Sinun on käytettävä tätä valitsemiesi tietojen hakemiseen.
    * **Kuinka:**
        1. Siirry [StatFin-tietokannan pääsivulle](https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/).
        2. Selaa aiheittain tai hae avainsanoilla/taulukon koodeilla (esim. BKT, työttömyysaste, elinajanodote, koulutus).
        3. Valitse haluamasi taulukko ja suodata haluamasi vuodet, muuttujat ja erittelyt.
        4. Napsauta "Näytä API-kysely" -painiketta saadaksesi API-päätepisteen ja esimerkkijsonikyselyn valinnallesi.
        5. Hae dataa skriptin tai sovelluksesi avulla. Esimerkiksi voit käyttää Pythonia:

           ```python
           import requests
           import json
           import os

           url = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/eot/statfin_eot_pxt_11ty.px"
           query = {
               "query": [
                   {
                       "code": "Ikä",
                       "selection": {
                           "filter": "item",
                           "values": ["SSS", "16-24", "25-34", "35-49", "50-64", "65-74", "75-84", "85-"]
                       }
                   }
               ],
               "response": {"format": "json-stat2"}
           }

           response = requests.post(url, json=query)
           data = response.json()
           # Tallenna haettu data 'data' -kansioon johdonmukaisuuden vuoksi
           os.makedirs('data', exist_ok=True)
           with open('data/output.json', 'w') as f:
               json.dump(data, f)
           ```

        6. Voit sitten muuntaa JSON-stat datan CSV:ksi käyttäen Pythonia (katso pää-README esimerkkiä `pyjstat` ja `pandas` kanssa).
        7. **Suositus:** Tallenna aina haettu data omistettuun `data`-kansioon projektiisi. Tämä pitää raakatiedostot ja prosessoidut datasetit järjestyksessä ja tekee työnkulustasi toistettavan.
    * **Rekisteröinti/API-avain tarvitaan?:** Yleensä **Ei**.
    * **Bootstrap:** Valitse *yksi* erityinen indikaattori (kuten työttömyysaste tai BKT per capita) aloittaaksesi. Sinun on haettava data itse API:n avulla kuten yllä on kuvattu.

4.  **Tilastokeskus: Koulutus sukupuolen, iän ja koulutusalojen mukaan (PxWeb API)**
    * **Mikä:** Viralliset suomalaiset tilastot koulutuksesta, eriteltynä sukupuolen, iän ja koulutusalojen mukaan.
    * **Lähde (UI):** [https://pxdata.stat.fi/PxWeb/pxweb/fi/StatFin/StatFin__vkour/statfin_vkour_pxt_12br.px/](https://pxdata.stat.fi/PxWeb/pxweb/fi/StatFin/StatFin__vkour/statfin_vkour_pxt_12br.px/)
    * **Kuinka noutaa (Python-esimerkki):**

      ```python
      import requests
      import json
      import os

      url = "https://pxdata.stat.fi:443/PxWeb/api/v1/fi/StatFin/vkour/statfin_vkour_pxt_12br.px"
      query = {
          "query": [
              {"code": "Alue", "selection": {"filter": "item", "values": ["SSS"]}},
              {"code": "Ikä", "selection": {"filter": "item", "values": [
                  "SSS", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-"
              ]}},
              {"code": "Sukupuoli", "selection": {"filter": "item", "values": ["SSS", "1", "2"]}},
              {"code": "Koulutusala", "selection": {"filter": "item", "values": [
                  "SSS", "00T10", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "SSSX00T10", "X"
              ]}}
          ],
          "response": {"format": "json-stat2"}
      }

      response = requests.post(url, json=query)
      data = response.json()
      os.makedirs('data', exist_ok=True)
      with open('data/statfin_vkour_pxt_12br.json', 'w') as f:
          json.dump(data, f)
      print("Tallennettu data/statfin_vkour_pxt_12br.json")
      ```

    * **Rekisteröinti/API-avain tarvitaan?:** Ei
    * **Bootstrap:** Tämä noutaa koko koulutustiedot sukupuolen, iän ja koulutusalojen mukaan -datasetin Suomelle. Voit edelleen käsitellä tai muuntaa JSON-stat2 datan CSV:ksi analyysiä varten.
    * **Vianetsintä:** Jos koodi ei toimi, vieraile [lähteen UI:ssa](https://pxdata.stat.fi/PxWeb/pxweb/fi/StatFin/StatFin__vkour/statfin_vkour_pxt_12br.px/) tarkistaaksesi oikea API-päätepiste ja JSON-rakenne kyselyllesi.


5.  **OECD Data:**
    * **Mikä:** Dataa OECD-maista, vahvoja hyvinvointimittareita ja kansainvälisiä vertailuja varten.
    * **Mistä löytää:**
        * [OECD Data Portal](https://data.oecd.org/)
        * [OECD Better Life Index](https://www.oecdbetterlifeindex.org/)
    * **Kuinka:** Sinun tulee etsiä tai selata OECD:n dataportaalista ja Better Life Indexistä asiaankuuluvia indikaattoreita. Lataa taulukoita (CSV/Excel) Suomelle ja vertailumailla. Kokeile etsiä indikaattoreita kuten keskimääräiset palkat, sosiaalimenot tai elämän tyytyväisyys.
    * **Tärkeää:** Nämä lähteet vaativat sinua tekemään hieman etsimistä, suodattamista ja manuaalista lataamista. Oikean datan löytäminen ja erottaminen saattaa vaatia hieman vaivannäköä - tutki, suodata ja lataa mitä pidät mielenkiintoisena!

6.  **Maailmanpankin avoin data:**
    * **Mikä:** Globaaleja indikaattoreita taloudellisista, sosiaalisista ja kehitystekijöistä.
    * **Mistä löytää:** [https://data.worldbank.org/](https://data.worldbank.org/)
    * **Kuinka:** Sinun tulee etsiä indikaattoreita (esim. BKT per capita, elinajanodote, internetin käyttö, työttömyys) ja ladata aikarividata CSV/Excel-muodossa Suomelle ja muille maille. Rekisteröintiä ei tarvita.
    * **Tärkeää:** Maailmanpankilla on valtava määrä indikaattoreita - oikean datan löytäminen saattaa vaatia hieman etsimistä ja suodattamista. Sinun odotetaan tutkivan, etsivän ja yhdistävän löytämäsi onnellisuuteen!

7.  **Tilastokeskus PxWeb (Tilastokeskus PxWeb):**
    * **Mikä:** Viralliset suomalaiset tilastot laajasta aihepiiristä, saatavilla PxWeb API:n ja verkkokäyttöliittymän kautta.
    * **Mistä löytää:** [StatFin-tietokannan pääsivulla](https://pxdata.stat.fi/PxWeb/pxweb/en/StatFin/)
    * **Kuinka:** Sinun tulee selata tai etsiä taulukoita, käyttää "Näytä API-kysely" -painiketta ohjelmalliseen käyttöön tai ladata saatavilla olevia CSV/Excel-tiedostoja. Monet taulukot sallivat erittelyt valinnan mukaan vuosi, sukupuoli, alue jne.
    * **Tärkeää:** On olemassa monia rikkaita, monimutkaisia datasettiä - oikean datan löytäminen ja erottaminen saattaa vaatia hieman vaivannäköä. Sinua kannustetaan tutkimaan ja yrittämään löytää jotain mielenkiintoista ja relevanteista onnellisuuden analyysiisi!

**Luovia / Humoristisia datan ideoita (valinnainen bonus):**

* Nämä vaativat merkittävää datan metsästystä/puhdistusta (esim. Metal Archivesista bändien etsimistä, kahvintuontitilastojen löytämistä, saunamäärien arvioimista). **Vältä näitä aluksi**, jos tavoite on nopea aloitus analyysille. Käsittele vain, jos valmistaudut aikaisemmin ja haluat haasteen. *Rekisteröinti/API-avaimia saatetaan tarvita tietyille erikoislähteille tai raapimiseen saatetaan liittyä (tarkista ehdot!)*.

Tarjoamalla nämä suoremmat vihjeet osallistujat pystyvät hankkimaan alkuperäiset datasetit paljon nopeammin ja siirtymään ydintehtäväänsä analysoimiseen ja visualisoimiseen Copilotin avustuksella.

* **Saunatiheys:** Saattaa vaatia Tilastokeskuksen (rakennustyypit) yhdistämistä alueellisiin tietoihin tai luovaa arviointia. *Rekisteröintitarpeet:* Riippuu lähteestä; viralliset tilastot todennäköisesti avoimia, erikoislähteet voivat vaihdella.
* **Kahvin kulutus:** Etsi tietoja kauppajärjestöiltä (kuten Kansainväliseltä kahvijärjestöltä) tai markkinatutkimusraporteista. *Rekisteröintitarpeet:* Kauppajärjestöt *voivat* olla avoimia; markkinatutkimussivustot (esim. Statista) vaativat usein rekisteröintiä tai tilausta täydellisten tietojen saamiseksi.
* **Raskaiden metallibändien määrä asukasta kohden:** Saattaa edellyttää tietojen raapimista Wikipedian listoista tai omistetuista musiikkiensykleistä (esim. Metal Archives) ja yhdistämistä väestötietoihin. *Rekisteröintitarpeet:* Raapiminen ei yleensä vaadi avaimia (mutta **tarkista aina käyttöehdot ja `robots.txt`**). Jos musiikkitietokannan virallinen API on olemassa, se *voi* vaatia rekisteröintiä/avaimia.

Valitse lähteet, jotka vaikuttavat saavutettavilta ja relevanteilta tekijöiltä, joita tiimisi haluaa tutkia! Onnea!

## 5. Kuinka käyttää tätä repoa (työpajaohjeet)

1.  Kloonaa tämä repositorio.
2.  Luo projektitiedostosi (koodi, notebookit, jne.) kloonatun repositorion sisälle.
3.  Tee yhteistyötä tiimisi kanssa käyttäen standardeja Git-käytäntöjä.
4.  **Hyödynnä GitHub Copilotia!** Pyydä sitä auttamaan sinua:
    * Kirjoittamaan boilerplate-koodia datan hakemiseen (esim. käyttäen `requests`, `pandas`).
    * Siivoamaan ja käsittelemään dataa.
    * Suorittamaan tilastollista analyysiä (esim. korrelaatiot käyttäen `pandas`, `numpy`, `scipy`).
    * Tuottamaan visualisointikoodia (esim. käyttäen `matplotlib`, `seaborn`, `plotly`).
    * Rakentamaan yksinkertaisen verkkokäyttöliittymän (esim. käyttäen Flask, Streamlit, Dash).
    * Selittämään koodinpätkiä tai ehdottamaan vaihtoehtoisia lähestymistapoja.
5.  Tee commitit koodistasi ja valmistaudu esitykseesi.