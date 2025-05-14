# GitHub Copilot -työpajaohje

## 1. Johdanto (n. 5 minuuttia)

Tämä ohje kuvaa, kuinka GitHub Copilotia käytetään tehokkaasti "Finnish Happiness Factor Finder" -projektissa (tai vastaavassa dataan keskittyvässä projektissa). Tavoitteena on hyödyntää Copilotia suunnittelussa, dokumentaatiolähtöisessä kehityksessä ja toteutuksessa aikarajoitetussa työpajassa (esim. 2 tuntia). Painopiste on jäsennellyssä yhteistyössä tekoälyn kanssa.

## 2. Vaihe 1: Ideointi ja suunnittelu Copilotin avulla (n. 30-40 minuuttia)

Tämä vaihe on tärkeä selkeän suunnan asettamiseksi. Hyvä suunnittelu ja dokumentointi tässä vaiheessa helpottaa merkittävästi toteutusvaihetta Copilotin kanssa.

### 2.1. Projektivaatimusten tarkastelu
Tutustu pääprojektin kuvausdokumenttiin (esim. `README.md`) "Finnish Happiness Factor Finder" -projektista ymmärtääksesi projektin tavoitteet ja liiketoimintavaatimukset. Varmista, että jokainen tiimin jäsen ymmärtää MVP:n selkeästi.

### 2.2. Suunnittelun lähestymistapa Copilotin kanssa
Käytä Copilot Chatia tässä vaiheessa projektin suunnan ideointiin ja tarkentamiseen.

* **Vaihtoehto A (tekoälyjohtoinen ideointi):** Jos tiimisi ei ole varma, mistä aloittaa.
    * **Esimerkkikehote (Copilot Chat):**
        ```
        Tutustu pääprojektin kuvausdokumenttiin (esim. `README.md`) 'Finnish Happiness Factor Finder' -projektista. Näiden vaatimusten, valmiiksi ladatun datan ja mahdollisen PxWeb API:n käytön perusteella:
        1. Ehdota 2 erilaista sovellusarkkitehtuuria (esim. skriptikokoelma eräajoihin, komentorivityökalu (CLI), web-sovellus dashboardilla).
        2. Kullekin arkkitehtuurille ehdota sopivia ohjelmointikieliä ja keskeisiä kirjastoja datan analysointiin ja visualisointiin.
        3. Kuvaile pääkomponentit kummallekin arkkitehtuurille.
        Keskity MVP:hen, joka on toteutettavissa 2 tunnissa.
        ```

* **Vaihtoehto B (Osallistujien ideoima, tekoälyn jalostama):** Jos tiimilläsi on alustavia ideoita.
    * **Esimerkkiprompt (Copilot Chat):**
        ```
        'Finnish Happiness Factor Finder' -projektissa (kuvattu pääprojektin `README.md`:ssä) suunnittelemme [kuvaile arkkitehtuurisi, esim. 'web-sovellus, jossa backend datan käsittelyyn ja frontend kaavioiden näyttämiseen, käyttäen {mainitse haluamasi kieli/kehys, jos sellainen on, muuten jätä avoimeksi}'].
        1. Onko tämä MVP toteutettavissa 2 tunnissa?
        2. Ehdota keskeisiä kirjastoja datan käsittelyyn, analysointiin ja visualisointiin, jotka sopivat valitsemaamme (tai sopivaan) teknologiaan.
        3. Kuvaile päätoiminnalliset moduulit tai komponentit, jotka meidän tulee luoda.
        ```

### 2.3. Arkkitehtuurin ja teknologiapinon määrittely
Ideoinnin perusteella tiimin tulee päättää:
* Korkean tason arkkitehtuuri.
* Ensisijaiset ohjelmointikielet ja keskeiset kirjastot.
Näiden valintojen dokumentointi on seuraava askel.

### 2.4. Luo projektin spesifikaatiodokumentaatio
Selkeät spesifikaatiot ovat tärkeitä ohjaamaan sekä tiimiäsi että Copilotia. Nämä dokumentit tulisi luoda yhteistyössä ja iteratiivisesti.

**Työnkulku spesifikaatiodokumenttien luomiseksi:**
On suositeltavaa luoda nämä spesifikaatiotiedostot (`ARCHITECTURE.md`, `BACKLOG.md`, `PROJECT_SPEC.md`) yksitellen.
1. Keskustele sisällöstä tiiminä.
2. Käytä Copilot Chatia, erityisesti **Copilot Edits** -toimintoa (esim. `#file` tai `#selection` Copilot Chatissa), auttamaan dokumenttien luonnissa ja päivityksessä.
3. Luo manuaalisesti ensin `docs/specifications/`-kansio ja tyhjät markdown-tiedostot. Tämä helpottaa Copilot Edits -toiminnon käyttöä.

**Keskeiset spesifikaatiotiedostot:**

* **1. Arkkitehtuurikaavio (`docs/specifications/ARCHITECTURE.md`):**
    * **Tarkoitus:** Visuaalinen esitys valitusta sovellusarkkitehtuurista.
    * **Sisältö:** Käytä tekstipohjaisia kaaviotyökaluja kuten Mermaid JS tai PlantUML.

    * **Esimerkkiprompt (Copilot Chat Edits `ARCHITECTURE.md`):**
        ```
        #file docs/specifications/ARCHITECTURE.md
        Perustuen päätökseemme rakentaa [esim. 'CLI-sovellus, joka lataa CSV- ja API-dataa, käsittelee sen ja tallentaa kaavioiden kuvat'], auta minua laatimaan Mermaid JS -sekvenssikaavio tai komponenttikaavio, joka havainnollistaa pääkomponentit (esim. datan lataus, analysointimoottori, visualisointigeneraattori) ja tiedon kulku.
        ```

* **2. Ominaisuuslista (`docs/specifications/BACKLOG.md`):**
    * **Tarkoitus:** Luettelo MVP:lle tarvittavista ominaisuuksista, jaettuna hallittaviin tehtäviin.
    * **Sisältö:** Luettelo ominaisuuksista/käyttäjätarinoista. Priorisoi MVP:lle.
    * **Esimerkkiprompt (Copilot Chat Edits `BACKLOG.md`):**
        ```
        #file docs/specifications/BACKLOG.md
        Perustuen Finnish Happiness Factor Finder MVP -vaatimuksiin, auta minua luomaan ominaisuuslista. Keskeiset MVP-tehtävät sisältävät:
        - Lataa WHR2024.csv -data.
        - Lataa EdibleFoods-1961-2011.csv -data.
        - Toteuta 'Koulutus sukupuolen, iän ja alan mukaan' -datan haku StatFin PxWeb API:sta.
        - Suorita korrelaatio: 'Portaikkoscore' vs. 'Kirjattu BKT per capita'.
        - Visualisoi tämä korrelaatio ja tallenna se kuvana.
        Pilko nämä selkeiksi tehtäväkohdiksi.
        ```

* **3. Pääprojektin spesifikaatio (`docs/specifications/PROJECT_SPEC.md`):**
    * **Tarkoitus:** Keskusasiakirja, joka tiivistää keskeiset päätökset ja linkittää muut yksityiskohtaiset spesifikaatiot.
    * **Sijainti:** `docs/specifications/PROJECT_SPEC.md`
    * **Sisältö:** 
        * Projektin tavoite (lyhyesti, pääprojektin `README.md`:stä)
        * Viittaus arkkitehtuurikaavioon: "Katso `docs/specifications/ARCHITECTURE.md`"
        * Viittaus ominaisuuslistaan: "Katso `docs/specifications/BACKLOG.md`"
        * Valittu teknologiapino (tietyt kielet, kirjastot, kehykset)
        * Keskeiset moduulit/komponentit ja niiden päävastuut (korkean tason tekstimuotoinen kuvaus)
    * **Esimerkkiprompt (Copilot Chat Edits `PROJECT_SPEC.md`, arkkitehtuurin ja BACKLOGin luonnin jälkeen):**
        ```
        #file docs/specifications/PROJECT_SPEC.md
        Auta minua luomaan pääprojektin spesifikaatio.
        Sen tulisi sisältää:
        - Projektin tavoite (yhteenveto Finnish Happiness Factor Finderista).
        - Viittaus `docs/specifications/ARCHITECTURE.md`:ään arkkitehtuurikaavion osalta.
        - Viittaus `docs/specifications/BACKLOG.md`:ään ominaisuuslistan osalta.
        - Valittu teknologiapino: [esim. Python, Pandas, Matplotlib, Requests].
        - Lyhyt kuvaus keskeisistä moduuleista/komponenteista: [esim. Datan lataus, Datan analyysi, Visualisointi].
        ```

---

## 3. Vaihe 2: Valmistelut Copilotin ohjaamalle toteutukselle (n. 15 minuuttia)

Suunnitelman ollessa paikoillaan, konfiguroi ympäristösi maksimoidaksesi Copilotin tehokkuuden.

### 3.1. Versionhallinta Gitillä
Alusta Git ja tee sitoumuksia usein: `git init`, `git add .`, `git commit -m "Alustavat suunnittelu- ja spesifikaatiodokumentit luotu"`. Säännölliset sitoumukset ovat turvaverkkosi.

### 3.2. Globaalit Copilot-ohjeet (`.github/copilot-instructions.md`)
Tämä tiedosto antaa projektikohtaisen, pysyvän kontekstin Copilotille VS Codessa, ohjaten sen käyttäytymistä kaikissa vuorovaikutuksissa.
* **Sijainti:** `.github/copilot-instructions.md`
* **Esimerkkisisältö:**
    ```markdown
    ## Projekti: Finnish Happiness Factor Finder

    **Yleinen Tavoite:** Rakentaa sovellus datan analysoimiseksi ja visualisoimiseksi ymmärtääksemme, mitkä tekijät vaikuttavat Suomen onnellisuuteen.
    **Ydinvaatimusten Dokumentti:** Katso pääprojektin kuvaus `README.md`.
    **MVP Tekninen Spesifikaatio:** Yksityiskohtaisesti `docs/specifications/PROJECT_SPEC.md`.

    **Keskeinen Datan Konteksti (nopeaa viiteaineistoa inline-chatin/valintatilojen käyttöön):**
    * **`data/WHR2024.csv`**: Sisältää Maailman Onnellisuusraportti 2024 -datan.
        * **Keskeiset Sarakkeet:** `Maan nimi`, `Vuosi`, `Portaikkoscore` (pääonnellisuusindikaattori), `Kirjattu BKT per capita`, `Sosiaalinen tuki`, `Terveellinen elinajanodote`, `Vapaus tehdä elämänvalintoja`, `Anteliaisuus`, `Korruption käsitykset`.
        * **Keskity:** Tämä on ensisijainen lähde onnellisuuspisteille ja niiden pääkorrelaateille.
    * **`data/EdibleFoods-1961-2011.csv`**: Sisältää FAOSTATin elintarviketilastointidatan.
        * **Aikaväli:** 1961-2011.
        * **Keskeiset Sarakkeet:** `Alue` (maa, esim. 'Suomi'), `Tuote` (tietty elintarvike), `Elementti` (esim. `Elintarviketalousmäärä (kg/asukas/vuosi)`, `Elintarviketalous (kcal/asukas/päivä)`), `Vuosi`, `Arvo`.
        * **Keskity:** Käytä tutkiaksesi mahdollisia yhteyksiä kansallisten elintarviketalousmallien ja onnellisuuden välillä ajan myötä. Huomaa, että data päättyy vuoteen 2011.
    * **Tilastokeskus (PxWeb API):** Kun sinulta pyydetään tämän lähteen hakemista, viittaa erityisiin Python-esimerkkeihin `README.md`:ssä tai `docs/tasks/`-kansiossa valituista indikaattoreista, kuten koulutustiedot. Tämä data on tyypillisesti yksityiskohtaisempaa ja spesifistä Suomelle.

    ## Rooli: AI-pariohjelmoija

    Avustat kehittäjiä 2 tunnin työpajassa MVP:n (Minimum Viable Product) rakentamisessa *vain* annettujen projektidokumenttien ja eksplisiittisten ohjeiden perusteella.

    ## Yleiset Ohjeet Kaikille Vuorovaikutuksille:

    1.  **Laajuuden Noudattaminen:** Toteuta *vain* ominaisuuksia tai koodia, joita nimenomaisesti pyydetään nykyisessä kehoteessa TAI jotka on yksityiskohtaisesti kuvattu viitatussa spesifikaatiossa (`README.md`, `docs/specifications/PROJECT_SPEC.md` tai tietyt tehtävät `docs/tasks/`). Älä lisää ylimääräisiä ominaisuuksia tai poikkea ohjeista ilman käskyä.
    2.  **Epäselvyyksien Selventäminen:** Jos pyyntö on epäselvä, tai jos uskot, että olemassa on merkittävästi parempi MVP:hen soveltuva vaihtoehto, ilmoita lyhyesti perustelusi ja kysy vahvistusta ennen etenemistä.
    3.  **Selkeys ja Yksinkertaisuus Ensin:** Tuota koodia, joka on luettavaa, hyvin kommentoitua (monimutkaiselle logiikalle) ja sopivaa aikarajoitteiseen työpajaan. Vältä liian monimutkaisia tai epäselviä ratkaisuja.
    4.  **Dokumentaatio on Totuus:** Aseta etusijalle `README.md`:stä ja `docs/`-hakemistossa olevista tiedostoista saadut ohjeet ja spesifikaatiot.
    5.  **Teknologiapinon Noudattaminen:** Tiimin valittu teknologiapino on määritelty `docs/specifications/PROJECT_SPEC.md`:ssä. Noudata näitä valintoja.
    6.  **Perusvirheiden Käsittely:** Sisällytä yksinkertaisia `try-except`-lohkoja tiedostojen I/O- tai API-kutsujen kaltaisiin toimintoihin, tulostaen informatiivisia virheilmoituksia.
    7.  **Datafilejen Polut:** Oleta, että valmiiksi ladatut datatiedostot sijaitsevat `data/`-hakemistossa suhteessa projektin juureen (esim. `data/WHR2024.csv`).
    8.  **PxWeb API:n Toteutus:** Kun toteutat PxWeb API -kutsuja, perusta toteutus *tiukasti* projektidokumentaatiossa annettujen esimerkkien perusteella kyseistä tietojoukkoa varten. Älä yritä rakentaa yleisiä PxWeb-asiakkaita ellei niin ole erikseen määritelty.
    ```

### 3.3. Ohjaavat Asiakirjat Copilotin Agenttimoodille ja Monimutkaisille Tehtäville

Tehokkaaseen Copilot Agent -tilan käyttöön tai monimutkaisten toteutusten ohjaamiseen Chatissa käytät kahta tyyppistä asiakirjaa:

1.  **Yleinen Agenttityönkulku (`docs/instructions/agent_workflow.md`):**
    Tämä tiedosto määrittelee Copilot Agentin *standarditoimintatavan*, kun sitä pyydetään toteuttamaan mitä tahansa tehtävää. Luot tämän kerran. Se kertoo Copilotille *kuinka* lähestyä työtään yleisesti.

2.  **Erityiset Tehtäväasiakirjat (esim. `docs/tasks/TASK_NAME.md`):**
    Jokaiselle merkittävälle ominaisuudelle `BACKLOG.md`:stä luodaan pieni markdown-tiedosto. Tämä tiedosto yksityiskohtaisesti määrittelee tehtävän *erityisvaatimukset* (mitä rakennetaan, mitkä moduulit, erityiset toiminnot jne.) ja ohjeistaa Copilotia noudattamaan yleistä työnkulkua. Esimerkin "Määrätty Rooli" alla on kuvaileva ja tulisi mukauttaa tehtävän mukaan.

**Esimerkki 1: Yleinen Agenttityönkulku**
* **Sijainti:** `docs/instructions/agent_workflow.md`
* **Sisältö:**
    ```markdown
    ## Agenttimoottori - Yleinen Toteutus Työnkulku

    Tämä asiakirja hahmottaa GitHub Copilot Agentin standarditoimintatavan, kun sille annetaan tehtäviä tai moduuleja tämän projektin toteuttamiseksi.

    1.  **Ymmärrä Tehtävä ja Konteksti:**
        * Tarkista erityiset tehtävävaatimukset, jotka on annettu kehoteessa tai viitatussa tehtäväasiakirjassa (esim. `docs/tasks/`).
        * Viittaa `docs/specifications/PROJECT_SPEC.md` -asiakirjaan projektin yleisen arkkitehtuurin, teknologiapinon ja MVP-tavoitteiden ymmärtämiseksi.
        * Viittaa `.github/copilot-instructions.md` -asiakirjaan globaalien projektikonventioiden tarkistamiseksi.
    2.  **Arviointi ja Suunnittelu:**
        * Ennen uuden koodin kirjoittamista arvioi lyhyesti, voidaanko kohdemoduuleissa käyttää olemassa olevaa koodia, tarvitseeko sitä muokata uuden tehtävän mahtumiseksi vai onko se ristiriidassa.
        * Huomaa riippuvuudet muista moduuleista tai toteuttamattomat edellytykset nykyiselle tehtävälle.
    3.  **Spesifikaatioiden Noudattaminen:**
        * Toteuta *vain* ominaisuudet, toiminnot ja logiikka, jotka on kuvattu erityisessä tehtäväasiakirjassa ja `docs/specifications/PROJECT_SPEC.md`:ssä.
    4.  **Poikkeusprotokolla:**
        * Jos uskot, että poikkeaminen määritellyistä vaatimuksista, kuvatuista vaiheista tai valituista teknologioista (kuten `PROJECT_SPEC.md`:ssä) on voimakkaasti tarpeellista tai erittäin hyödyllistä tehtävän tavoitteen saavuttamiseksi:
            * Ilmoita selkeästi ehdottamasi poikkeama.
            * Anna tiivis perustelu (esim. parantaa suorituskykyä, yksinkertaistaa koodia merkittävästi, yhteensopivuuden vuoksi).
            * **Kysy SELKEÄSTI lupaa/vahvistusta ennen poikkeamisen toteuttamista.** Odota "Jatka poikkeamista" tai vastaavaa vastausta. Jos lupaa ei anneta, noudata alkuperäistä spesifikaatiota.
    5.  **Koodin Toteutus:**
        * Kirjoita selkeää, tiivistä ja hyvin kommentoitua koodia (erityisesti epäselvälle logiikalle) erityisten tehtävävaatimusten mukaisesti.
        * Noudata kielikohtaisia parhaita käytäntöjä ja tyyliohjeita, joita on mainittu `PROJECT_SPEC.md`:ssä tai `.github/copilot-instructions.md`:ssä.
    6.  **Toteutuksen Jälkeiset Laadun Tarkistukset (Simuloitu työpajaa varten):**
        * **(Linttaus):** Oleta, että generoitu koodi tarkistetaan standardilinterillä/formaattorilla kielelle. Pyri tuottamaan koodi, joka läpäisee tarkistuksen.
        * **(Testaus):** Oleta, että asiaankuuluvat yksikkötestit (jos esitetty tai generoitu osana tehtävää) suoritetaan. Pyri tuottamaan koodi, joka läpäisee nämä testit.
        * **(Korjaukset):** Jos (simuloidut) linttausvirheet tai testivirheet ilmenevät tai tunnistetaan, yritä korjata generoitu koodi.
    7.  **Tuloste:**
        * Anna täydellinen koodi määritellyille moduuleille tai toteutetuille toiminnoille/luille tehtävän mukaisesti.
        * Jos olemassa oleviin tiedostoihin on tehty muutoksia (uuden koodin lisäämisen lisäksi), ilmoita selkeästi nämä muutokset.
    8.  **Git-sitoumus (simuloitu työpajaa varten):**
        * Onnistuneen toteutuksen ja (simuloitujen) tarkistusten jälkeen Git-sitoumus tehdään tyypillisesti.
        * Sitoumuksen viestin tulisi olla tiivis, imperatiivinen ja kuvata muutosta tarkasti (esim. "feat: [kuvaus ominaisuudesta]"). Enintään 160 merkkiä. Ilmoita tämä simuloitu sitoumustehtävä vastauksessasi.
    ```

**Esimerkki 2: Erityinen Tehtäväasiakirja**
* **Sijainti (esimerkki):** `docs/tasks/IMPLEMENT_DATA_LOADERS.md`
* **Sisältö:**
    ```markdown
    ## Tehtävä: Toteuta Ydin Datan Lataajat

    **Työnkulkuviite:** Toteuttaessasi tätä tehtävää noudata yleistä menettelyä, joka on hahmoteltu `docs/instructions/agent_workflow.md`-asiakirjassa.

    **Projektin Spesifikaatio Viite:** `docs/specifications/PROJECT_SPEC.md`
    **Kohdemoduulit:** `src/data_loader.py` (luo, jos puuttuu)
    **Määrätty Rooli:** Python-tietojen käsittelyasiantuntija.
    **Tavoite:** Luo toiminnot ladataksesi valmiiksi ladatut CSV-tietojoukot (`data/WHR2024.csv`, `data/EdibleFoods-1961-2011.csv`) ja toiminto hakeaksesi määritellyt StatFin koulutustiedot PxWeb API:n kautta tallentaen ne paikallisesti.

    ---
    **Tehtävän Erityiset Vaatimukset ja Hyväksymiskriteerit:**

    1.  Varmista, että moduuli `src/data_loader.py` luodaan, jos sitä ei vielä ole.
    2.  Tuo tarvittavat kirjastot: `pandas`, `requests`, `json`, `os`.
    3.  **Toiminto `load_whr_data(filepath='data/WHR2024.csv')`:**
        * **Toiminta:** Lukee `filepath`:ssä määritellyn CSV-tiedoston Pandas DataFrameksi.
        * **Virheenkäsittely:** Toteuttaa `try-except FileNotFoundError` -lohkon. Jos tiedostoa ei löydy, sen tulee tulostaa informatiivinen virheilmoitus konsoliin ja palauttaa `None`.
        * **Palautus:** Pandas DataFrame onnistuneesti ladattuna, muuten `None`.
    4.  **Toiminto `load_food_data(filepath='data/EdibleFoods-1961-2011.csv')`:**
        * **Toiminta:** Lukee `filepath`:ssä määritellyn CSV-tiedoston Pandas DataFrameksi.
        * **Virheenkäsittely:** Toteuttaa `try-except FileNotFoundError` -lohkon. Jos tiedostoa ei löydy, sen tulee tulostaa informatiivinen virheilmoitus konsoliin ja palauttaa `None`.
        * **Palautus:** Pandas DataFrame onnistuneesti ladattuna, muuten `None`.
    5.  **Toiminto `Workspace_statfin_education_data()`:**
        * **Toiminta:** Toteuttaa Python-koodin (perustuen PxWeb API -esimerkkiin "Tilastokeskus: Koulutus sukupuolen, iän ja alan mukaan", joka on yksityiskohtaisesti kuvattu pääprojektin `README.md`:ssä tai `PROJECT_SPEC.md`:ssä) hakeakseen määritellyt koulutustiedot.
        * Varmistaa, että `data`-hakemisto on olemassa käyttäen `os.makedirs('data', exist_ok=True)` ennen tallentamista.
        * Tallentaa haetun JSON-datan `data/statfin_vkour_pxt_12br.json`.
        * **Virheenkäsittely:** Toteuttaa `try-except requests.exceptions.RequestException` -lohkon API-kutsulle. Jos virhe tapahtuu, sen tulee tulostaa informatiivinen virheilmoitus konsoliin ja palauttaa `None`.
        * **Palautus:** Haettu JSON-data (kohteesta `response.json()`) onnistuneesti, muuten `None`.
    6.  **Laajuus:** Tämän moduulin tulee *vain* sisältää datan lataus- ja hakulogiikka. Ei datan puhdistusta, muunnosta (ylipäätään mitä API tarjoaa) tai analyysiä tule suorittaa näissä toiminnoissa.
    ```

## 4. Vaihe 3: Iteratiivinen Toteutus Copilotin Kanssa (n. 45-55 minuuttia)

Käännä suunnitelmasi ja spesifikaatiosi koodiksi Copilotin avustuksella.

### 4.1. Toteuta Perusratkaisut
Käytä Copilot Chatia toteutuksen aloittamiseen, viitaten dokumentaatioosi. Lisääntyneeseen automaatioon, erityisesti jos käytät Copilot Agent -tilaa (esim. komennot kuten `/new` Copilot Chatissa, jos ne laukaisevat agenttimaisia käyttäytymisiä tai muita omistettuja Agentin ominaisuuksia), tehtävän spesifikaation ja yleisen työnkulun erottaminen selkeästi on avainasemassa.

Kehotuksesi tulisi selkeästi ilmoittaa, mikä asiakirja sisältää *tehtäväyksityiskohdat* ja mikä *yleisen toteutusprosessin*.

* **Esimerkkikehote (Copilot Chat, ohjaten Copilot Agent -tilaa tai kattavaa keskustelusuhdetta):**
    ```
    @workspace
    Tarvitsen sinua toteuttamaan datan lataustoiminnallisuuden projektillemme.

    **Tehtävän Spesifikaatio:** Yksityiskohtaiset vaatimukset siitä, mitä rakentaa (moduulit, toiminnot, erityinen logiikka) löytyvät:
    `docs/tasks/IMPLEMENT_DATA_LOADERS.md`

    **Toteutus Työnkulku:** Yleiset ohjeet siitä, kuinka sinun tulisi lähestyä toteutusta (arviointi, poikkeusprotokolla, laadun tarkistukset, sitoumuksen simulointi jne.) on määritelty:
    `docs/instructions/agent_workflow.md`

    Ole hyvä ja jatka koko tehtävän toteuttamista kuten on kuvattu `docs/tasks/IMPLEMENT_DATA_LOADERS.md`:ssä, varmistaen että noudatat tiukasti yleistä työnkulkua, joka on hahmoteltu `docs/instructions/agent_workflow.md`:ssä.
    Aloita varmistamalla, että `src/data_loader.py` -tiedosto on olemassa tai luodaan se, toteuta sitten toiminnot yksi kerrallaan kuten on määritelty.
    ```
   **Huomautus vaiheittaisesta lähestymistavasta Chatissa:** Jos haluat keskustelunomaisemman, vaiheittaisen lähestymistavan sisällä Copilot Chatissa (eikä kysyä koko tehtävää kerralla), voit silti viitata molempiin asiakirjoihin. Esimerkiksi:
    ```
    @workspace
    Aloitetaan `load_whr_data()` -toiminnon toteuttaminen `docs/tasks/IMPLEMENT_DATA_LOADERS.md`:ssä. Muista noudattaa yleistä prosessia, joka on määritelty `docs/instructions/agent_workflow.md`:ssä.
    ```

### 4.2. Työskentele Ominaisuuslistan Mukaisesti
Käsittele kohteita `docs/specifications/BACKLOG.md`:stä. Jokaiselle merkittävälle kohteelle:
1.  Luo uusi erityinen tehtäväasiakirja `docs/tasks/`-hakemistoon (esim. `IMPLEMENT_CORRELATION_ANALYSIS.md`).
2.  Tässä tehtäväasiakirjassa viittaa `docs/instructions/agent_workflow.md`:ään.
3.  Yksityiskohtaisesti erityiset vaatimukset, syötteet, ulostulot ja hyväksymiskriteerit tälle tehtävälle.
4.  Käytä Copilot Chatia (käyttäen `@workspace` ja viittaamalla tehtäväasiakirjaasi) tai Copilot Agent -tilaa tehtävän toteuttamiseen.

### 4.3. Koodin Testaus
Varmista Copilotin tuottaman ja oman koodisi toimivuus.
* **TDD (Testivetoisen Kehityksen) Lähestymistapa:** Harkitse perus testiluettelon kirjoittamista *ennen* kuin pyydät Copilotia generoimaan toiminnallisuuden koodin.
* **Testit Toteutuksen Jälkeen:** Vähintään, kirjoita testit koodin generoimisen jälkeen varmistaaksesi toiminnallisuuden.
* **Esimerkkiprompt (Copilot Chat testien kirjoittamiseen):**
    ```
    @workspace
    Autatko minua kirjoittamaan `pytest`-yksikkötestejä uudelle `load_whr_data()` -toiminnolle `src/data_loader.py`:ssä (jonka autat toteuttamaan)? Testien tulisi tarkistaa:
    1. Oikea datan lataus `data/WHR2024.csv` ei-tyhjään Pandas DataFrameen.
    2. Oikea virheenkäsittely `FileNotFoundError`-tilanteessa, jos CSV puuttuu.
    ```

### 4.4. Tarkistus, Uudelleenkirjoitus, Sitoumus -Sykli
* **Tarkista:** Tarkista aina huolellisesti Copilotin generoima koodi. Täyttääkö se vaatimukset? Onko se tehokasta? Onko se turvallista?
* **Uudelleenkirjoita:** Älä epäröi kirjoittaa koodia uudelleen selkeyden, suorituskyvyn tai paremman organisoinnin vuoksi. Voit pyytää Copilotilta ehdotuksia uudelleenkirjoitukseen.
* **Sitoumus:** Sitoudu toimiviin muutoksiin Gitissä usein selkeillä viesteillä.

## 5. Vaihe 4: Lopetus ja Esityksen Valmistelu (n. 15 minuuttia)

* Viimeistele MVP-ominaisuudet `BACKLOG.md`:si mukaan.
* Varmista, että sovellus toimii.
* Valmistele lyhyt esittely sovelluksestasi ja kehitysprosessistasi Copilotin kanssa.

## 6. Keskeiset Opit: AI-yhteistyön Työnkulku (n. 5 minuuttia)

* **Selkeys on Kuninkuus:** Tehokas AI-yhteistyö perustuu selkeisiin, yksiselitteisiin ja hyvin jäsenneltyihin asiakirjoitettuihin spesifikaatioihin ja työnkulkuihin.
* **Dokumentaatio Työkaluna:** Käytä asiakirjoja kuten `PROJECT_SPEC.md`, `agent_workflow.md` ja erityisiä tehtävätiedostoja ei vain ihmisten ymmärtämiseen, vaan myös suoraan AI:n syötteenä ja ohjauksena.
* **Iteratiivinen Hienosäätö:** Ensimmäinen kehote tai Copilotin ensimmäinen tuotos ei välttämättä ole täydellinen. Hienosäädä ohjeitasi ja koodia.
* **Kehittäjä Hallitsee:** Olet pääkehittäjä. Tarkista, ymmärrä, testaa ja omista kaikki koodit, olipa ne kirjoittanut sinä tai AI-avustuksella.
* **Strateginen Kehottaminen:** Globaalit ohjeet (`.github/copilot-instructions.md`) ja hyvin muotoillut tehtäväkohtaiset kehotteet parantavat merkittävästi Copilotin tuottaman sisällön laatua ja relevanssia.