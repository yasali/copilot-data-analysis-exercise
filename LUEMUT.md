# Projekti: Suomalaisen onnellisuuden tekijöiden jäljittäjä

**Tehtävä:** Rohkeasti mennä sinne, minne monet analyytikot ovat menneet aiemminkin, mutta tällä kertaa tekoälypariohjelmoijien kanssa!

## 1. Johdanto: Onnellisuuden arvoitus

Suomi, huolimatta maineestaan pidättyväisten ihmisten maana, haastavasta ilmastostaan ja kielirakenteestaan, joka hämmentää kielitieteilijöitäkin, sijoittuu jatkuvasti maailman onnellisimmaksi maaksi World Happiness Report -raportin mukaan.

Vastaperustettu (ja hieman hämmentynyt) **Iloisuuden ja hilpeyden ministeriö (MMM)** pitää tätä ilahduttavana, mutta tarvitsee käyttökelpoista dataa. Johtuuko onnellisuus saunoista? Yllättävän suuresta kahvin kulutuksesta? Tehokkaista sosiaalijärjestelmistä? Raskaiden metallibändien suuresta määrästä asukasta kohden? Vai jostain aivan muusta?

Tiiminne tavoitteena on kehittää sovellus, joka hakee, analysoi ja visualisoi dataa auttaakseen MMM:ää ymmärtämään mahdollisia syitä Suomen korkeaan onnellisuussijoitukseen. Tarvitsemme datalähtöisiä hypoteseja selkeästi esitettynä!

## 2. Liiketoimintavaatimukset

Tiiminne kehittämän sovelluksen tulee täyttää seuraavat ydinkriteerit:

1. **Datan haku ja sisäänluku:**
    * Sovelluksen tulee kyetä hakemaan tai vastaanottamaan dataa **vähintään kahdesta** eri ulkoisesta lähteestä (katso ehdotetut lähteet alla).
    * Prosessin tulee olla toistettavissa (eli sovelluksen uudelleenajo hakee tuoreen datan, jos saatavilla, tai käyttää välimuistia asianmukaisesti).

2. **Data-analyysi:**
    * Sovelluksen tulee analysoida kerättyä dataa tunnistaakseen mahdollisia korrelaatioita eri yhteiskunnallisten, taloudellisten, ympäristöön liittyvien tai kulttuuristen tekijöiden ja Suomen (sekä mahdollisesti vertailumaiden) onnellisuusindikaattorien välillä.
    * Tiimin tulee määritellä tutkittavat tekijät saatavilla olevan datan perusteella.

3. **Datavisualisointi:**
    * Sovelluksen tulee tuottaa selkeitä ja merkityksellisiä visualisointeja (esim. kaavioita, graafeja, dashboardeja), jotka esittävät analyysin tulokset.
    * Näiden visualisointien tulee auttaa MMM:ää nopeasti ymmärtämään mahdolliset yhteydet, jotka tiiminne on löytänyt. Mitkä tekijät näyttävät korreloivan vahvasti Suomen onnellisuuspisteiden kanssa?

4. **Käyttöliittymä / Tulokset:**
    * Tulokset (keskeiset löydökset, visualisoinnit) tulee esittää helposti saavutettavassa muodossa. Tämä voi olla esimerkiksi:
        * Yksinkertainen web-käyttöliittymä/dashboard.
        * Generoidut raporttitiedostot (esim. HTML, PDF), jotka sisältävät tekstiä ja kaavioita.
        * Hyvin muotoiltu konsolituloste ja tallennetut kuvakaaviot.
    * Käyttöliittymän/tulosteen valinta on tiimin päätettävissä.

5. **Teknologiariippumattomuus:**
    * Toteutusteknologia (ohjelmointikieli, frameworkit, tietokannat, visualisointikirjastot) on täysin **tiimin päätettävissä**. Käyttäkää tuttua teknologiaa tai hyödyntäkää tilaisuus oppia jotain uutta Copilotin avulla!

## 3. Odotettu lopputulos ja toimitettavat asiat

Työpajan lopussa jokaisen tiimin odotetaan:

1. Omistavan toimivan sovelluksen, joka täyttää yllä kuvatut liiketoimintavaatimukset.
2. Esittävän lyhyen (5-10 minuutin) demon, joka sisältää:
    * Sovelluksen ominaisuuksien esittelyn (datan haku, analyysilogiikka, visualisoinnit).
    * Keskeiset visualisoinnit, jotka sovellus tuottaa.
    * Tiimin tärkeimmät hypoteesit Suomen onnellisuuteen vaikuttavista tekijöistä analyysin ja visualisointien perusteella. Muistakaa, että korrelaatio ei tarkoita kausaatiota, mutta se on erinomainen lähtökohta hypoteeseille!

## 4. Mahdolliset datalähteet (nopea alku!)

Analyysin nopeuttamiseksi tässä on suositeltuja lähteitä ja tarkkoja ehdotuksia relevanteista datapisteistä tai taulukoista. Keskittykää Suomen dataan ja mahdollisesti 1-2 vertailumaahan. **Aloittakaa 1-2 indikaattorilla kahdesta eri lähteestä.**

1.  **World Happiness Report Data:**
    * **Mitä:** Pääasiallinen lähde onnellisuusrankingille ja siihen liittyville tekijöille.
    * **Hae tämä:** Lataa päädatatiedosto (yleensä Excel tai CSV) **uusimmasta saatavilla olevasta vuodesta** viralliselta [World Happiness Report](https://worldhappiness.report/) -sivustolta (etsi datalisäyksiä/latauksia) tai luotettavalta lähteeltä kuten Kagglelta (Esimerkki: [https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2024](https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2024) - tarkista relevanssi).
    * **Avainsarjat käytettäväksi:**
        * `Maan nimi`
        * `Vuosi`
        * `Onnellisuusaste (Ladder score)` (tai vastaava pääonnellisuusindeksi)
        * `BKT asukasta kohden` (Logged GDP per capita)
        * `Sosiaalinen tuki`
        * `Terveellinen elinajanodote`
        * `Vapaus tehdä elämänvalintoja`
        * `Anteliaisuus`
        * `Korruption käsitykset`
    * **Muoto:** CSV tai Excel.
    * **Rekisteröinti/API-avain tarpeen?:** Yleensä **Ei** suoraan latauksille. Kaggle API:n asetukset tarvitaan, jos käytetään.
    * **Bootstrap:** Tämä antaa ydinnonellisuusindeksin ja siihen yleisesti liittyvät tekijät suoraan.

2.  **Tilastokeskus:**
    * **Mitä:** Viralliset suomalaiset tilastot. Rikkaita mutta monimutkaisia. Käytä PxWeb-käyttöliittymää.
    * **Hae tämä (Esimerkit - käytä avainsanoja/koodia StatFin PxWebissä):**
        * **BKT:** Siirry **Kansantalous** -> **Vuositason kansantalouden tilinpäätökset** -> **Bruttokansantuote (BKT) ja bruttokansantulo (GNI)**. Etsi vuosittaisia BKT per capita -taulukoita (esim. avainsana `BKT`, `asukasta kohden`. Taulukko `kans_v` on usein relevantti).
        * **Työttömyys:** Siirry **Työmarkkinat** -> **Työllisyys ja työttömyys** -> **Työvoimatutkimus**. Etsi työttömyysasteen taulukko (esim. avainsana `työttömyysaste`, taulukko `tyonv` tai `tyti` sarjat). Valitse vuosittaiset keskiarvot.
        * **Elinajanodote:** Siirry **Väestö** -> **Kuolemat** -> **Elinajanodote**. Etsi sukupuolen mukaan (esim. avainsana `elinajanodote`, taulukko `kuol_le`).
        * **Koulutus:** Siirry **Koulutus** -> **Väestön koulutustaso**. Etsi taulukoita väestöstä koulutustason mukaan (esim. avainsana `koulutustaso`, taulukko `vaerak_koul`).
    * **Kuinka:** Mene [StatFin Tietokannan käyttöliittymäsivulle](https://stat.fi/en/statistics-and-data/statfin-database) ja käytä PxWeb-käyttöliittymää. Selaa aiheittain tai hae avainsanoilla/taulukko-koodilla. Suodata data halutuille vuosille ja lataa CSV/Excel-muodossa.
    * **Rekisteröinti/API-avain tarpeen?:** Yleensä **Ei**.
    * **Bootstrap:** Valitse *yksi* tietty indikaattori (kuten työttömyysaste tai BKT per capita) aloittaaksesi.

3.  **Maailmanpankin avoin data:**
    * **Mitä:** Globaaleja indikaattoreita, hyviä perusvertailuihin.
    * **Hae tämä (Esimerkkindikaattorit - hae nimen tai koodin mukaan):**
        * `BKT per capita (nykyiset USD)`: Koodi `NY.GDP.PCAP.CD`
        * `Elinajanodote syntymähetkellä, yhteensä (vuosina)`: Koodi `SP.DYN.LE00.IN`
        * `Työttömyys, yhteensä (% koko työvoimasta) (mallinnettu ILO-arvio)`: Koodi `SL.UEM.TOTL.ZS`
        * `Internetin käyttäjät (% väestöstä)`: Koodi `IT.NET.USER.ZS`
    * **Kuinka:** Mene [https://data.worldbank.org/](https://data.worldbank.org/). Hae näitä indikaattoreita. Valitse Suomi (ja ehkä Ruotsi/Norja/Tanska vertailua varten). Näytä/lataa aikarividata CSV/Excel-muodossa.
    * **Rekisteröinti/API-avain tarpeen?:** Yleensä **Ei**.
    * **Bootstrap:** Hae aikarividata *yhdelle tai kahdelle* näistä indikaattoreista Suomelle.

4.  **OECD Data:**
    * **Mitä:** Tietoa OECD-maista, vahvoja hyvinvointimittareissa.
    * **Hae tämä (Esimerkkidata/indikaattorit):**
        * **Parempi elämän indeksi:** Tutki tätä datasettiä suoraan OECD-sivustolla vertailupisteiden saamiseksi ulottuvuuksilla kuten `Elämäntyytyväisyys`, `Työ- ja vapaa-ajan tasapaino`, `Yhteisö`, `Terveys`. ([https://www.oecdbetterlifeindex.org/](https://www.oecdbetterlifeindex.org/) sisältää usein interaktiivisia näkymiä ja taustadataa).
        * **Keskimääräiset palkat:** Hae `Keskimääräiset palkat` (esim. indikaattori `AV_AN_WAGE`) pääportaalista [https://data.oecd.org/](https://data.oecd.org/).
        * **Sosiaalimenot:** Hae `Sosiaalimenot`-datasettiä (usein `Sosiaalinen suoja ja hyvinvointi` -kohdassa). Etsi % BKT:sta.
    * **Kuinka:** Käytä OECD:n dataportaalin hakua tai selaa teemoja kuten `Hyvinvointi`. Keskity indikaattoreihin, jotka ovat saatavilla Suomelle. Lataa asiaankuuluvat taulukot/indikaattorit (CSV/Excel).
    * **Rekisteröinti/API-avain tarpeen?:** Yleensä **Ei**.
    * **Bootstrap:** Parempi elämän indeksin pisteet ovat loistava vertailun aloituspiste, jos saatavilla helposti. Muussa tapauksessa valitse yksi indikaattori, kuten keskimääräiset palkat.

5.  **Eurostat:**
    * **Mitä:** EU:n tilastotoimisto. Hyvä EU-vertailuille, mahdollisesti monimutkainen navigointi.
    * **Hae tämä (Esimerkkitaulukon koodit - käytä tietokannan haku-/navigointitoiminnossa):**
        * **Yleinen elämän tyytyväisyys:** Koodi `ilc_pw01` (väestö ja sosiaaliset olosuhteet -> Elinolosuhteet -> Elämänlaatu)
        * **BKT per capita (PPS):** Koodi `nama_10_pc` (talous ja rahoitus -> Kansantalous -> BKT ja pääkomponentit)
        * **Terveet elinvuodet syntymähetkellä:** Koodi `hlth_hlye` (väestö ja sosiaaliset olosuhteet -> Terveys -> Kuolleisuus ja elinajanodote)
        * **Puolet köyhyys- tai sosiaalisen syrjäytymisen vaarassa:** Koodi `ilc_peps01` (väestö ja sosiaaliset olosuhteet -> Elinolosuhteet -> Köyhyys ja sosiaalinen syrjäytyminen)
    * **Kuinka:** Mene [Eurostat Tietokantaan](https://ec.europa.eu/eurostat/web/main/data/database). Käytä hakua tai navigoi 'Tietokanta aiheittain'. Käytä taulukon koodeja löytääksesi dataa. Suodata maan (FI), ajan ja latauksen mukaan (CSV/Excel usein paras).
    * **Rekisteröinti/API-avain tarpeen?:** Yleensä **Ei**.
    * **Bootstrap:** Valitse *yksi* taulukko (kuten elämän tyytyväisyys tai terveet elinvuodet) ladattavaksi Suomelle ja ehkä naapureille.

6.  **Ruokahuollon data (Kaggle kautta - FAOSTAT-lähde):**
    * **Mitä:** Tietoa ruokahuollon määrästä (kg/asukas/vuosi) ja ravintoarvoista (kcal/asukas/päivä, proteiini, rasva) eri ruokatuotteille monissa maissa. Alun perin YK:n elintarvike- ja maatalousjärjestö FAOSTAT:ilta.
    * **Hae tämä:** Lataa CSV Kagglesta: [https://www.kaggle.com/datasets/aliesmaeilpoor/ediblefoods-1961-to-2011](https://www.kaggle.com/datasets/aliesmaeilpoor/ediblefoods-1961-to-2011)
    * **Avainsarjat/tiedot käytettäväksi:** Suodata `Alue` (esim. 'Suomi'). Valitse asiaankuuluvat `Tuote`(t) (esim. 'Kala, äyriäiset', 'Hedelmät - Ilman viiniä', 'Vihannekset', 'Eläinrasvat', 'Maito - Ilman voita') ja `Elementti`(t) (esim. `Ruokahuollon määrä (kg/asukas/vuosi)` tai `Ruokahuolto (kcal/asukas/päivä)`).
    * **Muoto:** CSV.
    * **Rekisteröinti/API-avain tarpeen?:** **Kyllä**, Kaggle-tili vaaditaan ladattaessa verkkosivuston käyttöliittymän kautta. Kaggle API:n asetukset tarvitaan ohjelmallista latausta varten.
    * **Bootstrap:** Huomaa, että data **päättyy vuoteen 2011**. Suodata 'Suomi' ja aloita analysoimalla trendiä *yhdelle tai kahdelle tietylle ruokatuotteelle* (kuten Kalalle tai Hedelmille) tai laajalle `Elementille` kuten koko `Ruokahuolto (kcal/asukas/päivä)`. Vertaa sen trendiä saatavilla oleville vuosille (1961-2011) onnellisuusdataan, jos mahdollista.

**Luovia / Humoristisia datan ideoita (Valinnainen bonus):**

* Nämä vaativat merkittävää datan metsästystä/puhdistusta (esim. Metal Archivesin bändien listaaminen, kahvin tuontitilastojen löytäminen, saunamäärien arvioiminen). **Vältä näitä aluksi**, jos tavoite on nopea aloitus analyysille. Haasta vain, jos valmistaudut aikaisemmin ja haluat haasteen. *Rekisteröinti/API-avaimia saatetaan tarvita tietyille erikoislähteille tai raaputtamiseen saatetaan tarvita (tarkista ehdot!)*.

Valitkaa lähteet, jotka vaikuttavat saavutettavilta ja relevantilta tekijöiltä, joita tiiminne haluaa tutkia! Onnea!

## 5. Kuinka käyttää tätä repositoriota (työpajaohjeet)

1.  Kloonaa tämä repositorio.
2.  Luo projektitiedostosi (koodi, notebookit jne.) kloonatun repositorion sisälle.
3.  Tee yhteistyötä tiimisi kanssa käyttäen standardeja Git-käytäntöjä.
4.  **Hyödynnä GitHub Copilotia!** Pyydä sitä auttamaan:
    * Kirjoittamaan boilerplate-koodia datan hakemiseen (esim. käyttäen `requests`, `pandas`).
    * Siivoamaan ja käsittelemään dataa.
    * Tekemään tilastollista analyysiä (esim. korrelaatiot käyttäen `pandas`, `numpy`, `scipy`).
    * Generoimaan visualisointikoodia (esim. käyttäen `matplotlib`, `seaborn`, `plotly`).
    * Rakentamaan yksinkertaisen web-käyttöliittymän (esim. käyttäen Flask, Streamlit, Dash).
    * Selittämään koodinpätkiä tai ehdottamaan vaihtoehtoisia lähestymistapoja.
5.  Tee commitit koodistasi ja valmistaudu esitykseen.