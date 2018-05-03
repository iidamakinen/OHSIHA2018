# Lisäominaisuudet harjoitustyöhön - Github (Versionhallinta)

#### Lyhyesti harjoitustyöstä

Harjoitustyöni ideana oli siis toteuttaa käyttäjälle palvelu, josta voi selata tulevia musiikkitapahtumia Tampereella ja lisätä niistä kiinnostavimpia omaan listaan. Datan lähteenä käytin https://visittampere.fi/ -sivuston tarjoamaa API:a tulevista tapahtumista.
Harjoitustyön versionhallintaan päätin lopuksi ottaa avuksi Githubin, jonka käyttöönotto onnistui seuraavien vaiheiden kautta. Omaan harjoitustyöhöni liittyvät projektikansiot löytyvät osoitteesta: https://github.com/iidamakinen/OHSIHA2018.

#### Gitin asennus ja Github-käyttäjätunnukset
Ensimmäiseksi tuli ladata Git, jonka sai ladattua osoitteesta:	https://git-scm.com/downloads
Seuraavaksi loin käyttäjätunnukset Githubin sivuilla osoitteessa: https://github.com/.

#### Projektin tallentaminen repositorioon
Repositorion luominen onnistui helposti Github:n sivuilla. Oman projektin juuri luotuun repositorioon tallensin terminaalin kautta seuraavin komennoin:

```
$ cd [projetki]
$ mkdir .github
$ git ominaisuudet$ git remote add origin [repositorion_url]
$ git add -A
$ git commit -m "Commit message"
$ git push -u origin master
```
Kun tehdään muutoksia/lisäyksiä projektiin, tarpeeseen tulevat komennot `add`, `commit`, `push` ja `pull`.
