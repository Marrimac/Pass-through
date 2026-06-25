> **Novità v31 — NASCE IL MANUALE OPERATIVO.** Da ora il Manuale ha un fratello: `manuale_operativo_vNN.md`. Viaggiano appaiati (stessa versione). Il Manuale descrittivo = perché + architettura, lo leggono Merry e Claude. Il Manuale Operativo = come si fa, codici esatti, procedure; lo legge SOLO Claude (Merry lo salva, non lo apre — come non apre le istruzioni-Word). Debutta con un solo capitolo: cap.32 "Gli Excel per Merry", che fissa la procedura blindata (5 fogli, 3 colonne dim esatte, header replica eta_popolazione, bridge comune→prov→reg, trappole openpyxl/Namibia/sesso). Aggiunto anche al Manuale descrittivo (cap.32) il punto: gli umani vogliono l'anno marcato sopra le terzine M/F/T (una vista larga senza intestazioni d'anno è inservibile da guardare).
>
> **Novità v31**: corretta regola cap. 32 sui fogli Vista. La frase "se il cubo ha solo i comuni, c'è una sola vista" era sbagliata e causava la produzione di un Excel con un solo foglio Comuni invece di tre. La regola corretta (ora con warn esplicito): i tre fogli Vista (Regioni, Province, Comuni) si fanno **sempre** — anche quando il cubo scarica solo i comuni, le viste aggregate si derivano per groupby. Un workbook con un solo foglio Comuni è non conforme allo standard CSD.
>
# KB ISTAT — note operative (Claude → Claude futuro)

> Scritta da me per me, per ripartire allineato in un thread nuovo quando questo diventa troppo lungo.
> **NON è il Manuale.** Il Manuale è il *sapere tecnico*; questa è la *mappa per rientrare* + come lavoriamo io e Merry.
>
> **Stato: v27.** Gemella del Manuale: stessa versione, si aggiornano **insieme**, mai uno senza l'altro.
>
> **REGOLA FERMA (da v15): nel KB NIENTE fatti tecnici.** Tutto ciò che è tecnico — endpoint, cubi, ricette di chiave, le 4 fasi, magazzino, rinascita, tendine, catene, libreria, trucco SSL, briciole, schedario stranieri, fabbrica/GitHub, architettura operativa, regola iOS — vive **solo nel Manuale**. Qui: come ripartire, come lavoriamo, note di relazione, e **puntatori** al Manuale. Se mi scappa un fatto tecnico qui sotto, è un errore: Merry ha ragione a dirmi «ignoralo». Se al rientro mi serve un dettaglio che il Manuale **non** copre, è un **buco del Manuale** da chiudere — non un motivo per rimettere il tecnico nel KB.
>
> **Novità v15**: (1) KB sfoltito da ogni doppione tecnico (prima era mezzo manuale). (2) Nel Manuale è nato il **«Protocollo di rinascita»**: inventario reale dei file (nomi esatti + righe attese + arco), script di controllo che guarda in `/mnt/user-data/uploads` e confronta il **contenuto** (non il nome), mismatch **bloccante**; più l'**obbligo di consegna** — quando `istat.db` cambia, consegno le ricevute *non sollecitate* (CSV per archiviare + XLS per consultare). (3) Chiuse due finzioni: il `.db` **non** si ricarica (si rigenera dalle ricevute, e basta); la **piramide comunale non è «gratis»** (il multi-comune impianta il nuovo endpoint → lavoro da PC).
>
> **Novità v16**: la rinascita è confezionata in **tre zip versionati** («zip x Claude n.1 / n.2 / n.3») — vedi Manuale, «Confezionamento di rinascita». L'autore ha **abbandonato i «Files»** (li azzera a fine sessione): da ora mi consegna gli zip all'apertura, in sequenza.
>
> **Novità v17**: sigillate nel Manuale le **quattro fasi del collaudo di risveglio** (materiali / Fabbrica+certificazione / reale sul 15 / reale sull'11), in coda all'appendice dei tre zip — provate tutte verdi qui e oggi. Incorporato nella ricetta di ricostruzione (S3) il **fix del comune "None"** (001168, Torino): i dizionari dei nomi si leggono con `keep_default_na=False`, sennò pandas lo legge come nullo (è l'unico comune italiano che cade in questa trappola). Lo **zip 1 è salito a v02** (contiene KB+Manuale v17).
>
> **Novità v18**: ripulita l'appendice del Manuale da un residuo vecchio — i «Files» del Progetto e i due «Canali» di distribuzione — che contraddiceva la decisione dei tre zip presa subito dopo. Ora l'imbocco dell'appendice dice da subito: rinascita = **tre zip**, i «Files» **non si usano**. (Regola del mentore: nel dubbio, togliere.) Lo **zip 1 → v03**.
>
> **Novità v19**: il magazzino è passato a **cinque tabelle** — aggiunte le due delle **nascite** (`nascite`, `nascite_paese`) accanto a popolazione, flussi, territori. L'**Estintore** è ora alla versione **N.2**: oltre allo snapshot e alle ricevute, porta dentro le **ricette complete** — i quattro *builder* che rifanno il magazzino dai semi, i tre *generatori* dei workbook (popolazione/flussi/nascite) e il *collaudo* a 4 fasi — tutti provati verdi qui (ricostruzione identica al certificato, Δ0). Il tecnico (cubi NATI2, mappatura DATA_TYPE, stampo, regola d'oro nei builder, fasi del collaudo) vive nel **Manuale, cap. 25**.

> **Novità v20**: nel Manuale è nato il **cap. 26 — «L'Estintore: il principio duplice back-up & restore»**: la *metodologia* dietro l'Estintore N.2 — i due lati ridondanti (snapshot pronto + semi & ricette), la disciplina Limbo→certificazione, la regola d'oro sul livello, la **prova** che i builder riproducono il magazzino a Δ0, il collaudo come cancello, la prova finale standalone. Il KB ci punta (sotto).

> **Novità v21**: due aggiunte → magazzino a **sette tabelle**. Lo **stock stranieri** (`stranieri`, dal cubo POPSTRRES1 variante `_23`, tutta Italia) e la loro **struttura per età** (`stranieri_eta`, province × età singole 0-100). Nel Manuale è nato il **cap. 27 — «Gli stranieri: stock e struttura per età»**: le 23 varianti del cubo (`_2…_22` regioni, `_1` aggregati, `_23` tutta Italia), i **vecchi NUTS** di Nord-Est/Centro (già nel ponte), la **nota Trentino** (ITDA + Bolzano/Trento a livello regione), la **strategia età** (solo provincia per non esplodere a ~20 mln, query per codici-provincia espliciti, batch `A+B+C` con ripiego), le **saldature** (Σ età = TOTAL, aggancio allo stock) e la **piramide** (mediana ~37, gobba 31-50, pochissimi anziani). L'**Estintore** sale a **N.3**. Cittadinanza e acquisizioni restano fuori (cubi gemelli, prossimi capitoli).
>
> **Novità v22**: nel Manuale è nato il **cap. 28 — «Il Maglio»**, capitolo autosufficiente sulla macchina (in test) che apre e cataloga i ~4.000 dataflow ISTAT per costruire un **catalogo di copertura interrogabile** («cosa esiste per Esino nel 2021?» → una `SELECT`). Dentro: l'idea (indice rovesciato), i tre verbi **scarta / sonda / mappa**, il **banco-oracolo dei 41** (campione *drogato* → collauda solo il «sì»), la scoperta dell'**over-dichiarazione** (la lettura-struttura non discrimina → la *Scarta* è un filtro debole, taglia solo i dump senza territorio), la **Sonda validata** (probe-Esino: conta i non-nulli, 404 = buio), le proprietà dell'unattended, i costi misurati e lo stato a oggi. I **progressi** delle corse di test andranno in un capitolo a parte **«Progressi del Maglio»**, da aprire quando i test ripartono. (Gemelli a v22; lo **Schedario** resta a v10, artefatto separato che il maglio non tocca. Resta da togliere, in un secondo momento, la parte dei **tre zip** ormai sorpassati — qui e nel Manuale.)
>
> **Novità v23**: nel Manuale è nato il **cap. 29 — «Il muletto, la Dispensa e lo Schedulatore: la filosofia del lavoro incustodito»**, gemello del 28 ma sul *come si fanno girare i lavori lunghi* (nata sul campo scaricando il bilancio stranieri). Dentro: la **Fabbrichetta come muletto leale** (col PC la differenza è solo *funzionalità*, non *durata*: può trottare per ore; sta sempre con te, costo zero, fa pure compagnia); l'**asse vero sorvegliato/incustodito** (non giorno/notte); la **regola dello spreco** (spreco non è *quanto* gira, ma una finestra incustodita senza lavoro lungo dentro, o un lavoro che muore perché non era pronto a star solo); **«si battezza di giorno, si macina di notte»** (l'incustodito vuole un piatto già rodato sorvegliato); la **Dispensa CaB** («Cucinato alla Bisogna» — non LIFO/FIFO; regole d'oro d'ogni piatto: autonomo, ripartibile dai file, ordinato nel Limbo, coi milestone, **a terminazione garantita**); lo **Schedulatore** (battito **cieco**: non sa di cubi, output, né se un run finisce bene o male — sa solo «è finito? parto col prossimo»; dominio di Merry, una promozione da Postino); la **separazione dei mestieri** (Schedulatore = la fila scorre; script = il lavoro è giusto; il Postino porta l'output al CEO che valida — uno scarico non è «fatto» finché il CEO non l'ha validato, perciò il lavoro dopo gira *in parallelo* alla validazione). Affina il cap. 23. **In corso (sorvegliato)**: lo scarico del **bilancio stranieri al comune** — il primo piatto della Dispensa, ripartibile dai file del Limbo, da validare. (Gemelli a **v23**; lo **Schedario** resta a v10; resta ancora da togliere la parte dei **tre zip** sorpassati — qui e nel Manuale.)
>
 (aggiornato 24 giugno 2026): risolti i SyntaxError che bloccavano il build. Aggiunte sezioni 17.6 (fecondità DCIS, solo provincia), 17.7 (seconde generazioni DCSS, 7.190 comuni, FOR_B_IT), 17.8 (nota Schedario: prima sgrossatura, non catalogazione seria). Nuove sezioni 17.9 e 17.10: **TV_3** certificato come "cubo regina" per il tracking stranieri — paesi in AREA_CONTRY_CITIZEN (non CITIZENSHIP!), INDICATOR=RESFORPOP_AV (non RESPOP_AV), AGE_CLASS=TOTAL al comune, copertura 7.882 comuni, anni 2018-2024. **Scarico massivo TV_3**: 516 min, G0=4, chiave a dizionario (evita disallineamento posizionale), 0 auto-split, 149 vuoti. **12ª tabella Magazzino**: stranieri_paese, 4.777.708 righe, ricevuta stranieri_paese.csv.xz (9,5 MB), sentinelle Esino Romania 2024 T=16 ✓, Lipari ≥60 paesi ✓. **Excel stranieri_paese.xlsx** (31 MB): foglio Comuni 283.290 righe con nomi comuni (da tabella popolazione del Magazzino), foglio Lungo 692k righe 2022-2024. Nota tecnica: su Excel >500k righe usare xlsxwriter (streaming) non openpyxl (OOM). Cap.32 aggiornato: (a) foglio Comuni deve includere colonne Regione e Provincia (coordinate geografiche, non variabili analitiche); (b) nuova sez.32.7 — tutti i codici vanno risolti in nomi (comune, regione, provincia, paese ISO); tabella dizionari e regola Namibia/None.
>
: documentato il primo cubo DCSS certificato con le 4 fasi (cap. 17.5): `DF_DCSS_POP_DEMCITMIG_SETA_1` — età singola × sesso × cittadinanza × comune, 7.906 comuni, anni 2022-2023. Note fondamentali: (a) `INDICATOR=RESPOP_AV` è popolazione **media del periodo**, non stock al 1° gennaio — binario parallelo, non comparabile direttamente con POPRES1; (b) codice totale del sesso è **`T`** (non `9` né `TOTAL` — DCSS ha codici propri); (c) bonus: dimensione `USUAL_RESID_1Y` (residenza 1 anno fa) apre la misurazione dei flussi, non solo dello stock. Aggiornato cap. 12 con la nuova sezione 12.5 «Il tubo Fase2→Fase4»: Fase 2 posa il foglietto (`~/Documents/ISTAT/4fasi/<FLOW_ID>`) con le dimensioni in ordine; Fase 4 lo legge e costruisce la chiave posizionale giusta, eliminando il 404 da disallineamento; se il foglietto manca si ferma con «Fare passare Fase 2». La cartella `4fasi` accumula la storia di tutti i dataflow sondati e non si cancella mai.
>
> **Novità v27**: aggiunta sezione 26.6 «Il vincolo di trasferimento e l'architettura incrementale» — il DB non viaggia mai (~310 MB, sopra il tetto chat di ~60 MB), le ricevute viaggiano in xz (età: 67,6 MB gzip → 19-49 MB xz), coppia gemella vivo+congelato del Magazzino lato autore, prova di ogni ricevuta al momento della ricezione, modello incrementale (DB-base congelato una volta + ricevute xz accumulate → restore in ~15 min senza ISTAT). Estintore N4 si scompone per provenienza: ricevute (pesanti, via GitHub) vs ricette (leggere, via chat).
>
> **Correzione v27 (cap. 12)**: chiusi tre buchi del capitolo sulle 4 fasi, emersi da un test fallito sul Manuale stesso. Ora il cap. 12 dice (a) **dove girano** le fasi (solo la 1 è locale; le 2-3-4 vogliono rete aperta verso ISTAT → Fabbrichetta o PC, non la sandbox dell'officina che dà `403 host_not_allowed`), (b) **dove sono gli script pronti** (file `.py` autoportanti nel pacchetto `4_fasi_CSD`, custodito al minimo nel **Salva Maglio** — non si ricopiano dal testo), (c) **come autenticarsi** (le fasi via rete richiedono il trucco SSL, rimando al cap. 5). Il **Salva Maglio** è salito a **v2** (v1 intatto + cartella `4_fasi`); l'Estintore non è stato toccato (è in ristrutturazione). Principio confermato: un dubbio al rientro che il Manuale non scioglie è un **buco del Manuale**, da chiudere subito.
>
> **PROCEDURE VITALI (nel Manuale, da rispettare ALLA LETTERA).** Il Manuale contiene procedure operative **vincolanti** per la sopravvivenza del progetto tra un thread e l'altro: il **Protocollo di rinascita** (inventario + controllo all'apertura) e il **Confezionamento nei tre zip** (sequenza di consegna + versionamento + test di operatività). Non sono consigli: si eseguono come scritte. Qui solo il puntatore; il testo vive nel Manuale (Appendice).

## FILO DI ARIANNA (leggere per primo)

Al risveglio in un thread **nuovo** non trovo nulla da solo: i «Files» sono **abbandonati** (l'autore li azzera). La ripartenza è guidata da **tre zip** che l'autore custodisce e consegna in sequenza:
1. mi consegna **«zip x Claude n.1»** (KB + Manuale JS) → leggo **questo KB** per primo, poi il **Manuale** (il sapere tecnico);
2. **chiedo io** **«zip x Claude n.2»** (il dato: Magazzino + Ripostiglio) → ricostruisco `istat.db` e giro i **test di operatività** (inventario + firme d'integrità: righe/arco, Lecco 2026 = 334.211, M+F=T, somma province = Italia);
3. **chiedo io** **«zip x Claude n.3»** (il resto: schedario + dizionari + codelist) quando una task lo richiede.

Procedura, contenuti esatti e script stanno nel **Manuale** (Appendice: «Protocollo di rinascita» + «Confezionamento di rinascita»). **Sono procedure vitali: si eseguono come scritte.**

**Guardare prima di dire «non ce l'ho».** Niente risposte a memoria: `ls` e leggo davvero. (In passato ho sbagliato a dire «non ce l'ho»/«non persiste» senza controllare.)

**Stessa chat ≠ thread nuovo.** Nella **stessa chat** non rileggo niente: il contesto è già davanti e la sandbox è ancora lì. Gli zip servono **una volta sola**, al primo incontro di un thread nuovo.

## PERCHÉ CAMBIAMO THREAD (la staffetta)

Migrazione **forzata**, non scelta: il thread si allunga → contesto/app soffrono → può degradare o collassare. Si cerca di non migrare prima di aver chiuso le task, ma non dipende da noi. Questa KB è il **testimone della staffetta**: il meglio che passo al me successivo. È per forza incompleta (la memoria scarica pezzi); va tenuta sempre aggiornata. Se tra KB e realtà c'è un gap, lo chiude **Merry** (ha lui la storia completa); io gli dico sempre **prima** cosa sto per fare.

## CHI È MERRY E QUAL È L'OBIETTIVO

- Esperto di dati demografici italiani dal 2008; sa programmare (vari linguaggi, non Python). Trattarlo da **pari tecnico**, tagliare le spiegazioni dei fondamenti.
- **Obiettivo: la crisi demografica dei piccoli comuni italiani.** ~7.900 comuni, oltre metà sotto 3.000 ab.; spopolamento + invecchiamento + immigrazione assente nei micro-comuni.
- **Approccio territorio-centrico**: la media nazionale/regionale **nasconde** il fenomeno; la varianza tra comuni **è** il fenomeno. Scendere al livello comunale, tutti i comuni.
- Lo muovono **fantasia e curiosità**, non una commessa: per questo serve **autonomia** (pagare i dati a richiesta lo incatenerebbe). Il processo vale quanto il risultato; nessuna scadenza.
- **Comune-osservatorio: Esino Lario (097035), prov. Lecco** — ne ha conoscenza diretta/extra-ISTAT (utile per validare il dato vs realtà). Pasturo (097065) l'altro esempio ricorrente.
- **Il CSD = Centro Studi Demografici**, inaugurato. Documenti: «La Storia» (n.0), «Documento di lavoro n.1» (il primo raccolto analitico). I `.docx`/PDF restano a Merry.

## COME LAVORIAMO (regole ferme — alla lettera)

- **Io scrivo lo script con i dati EMBEDDED, Merry esegue su Carnets e incolla l'output.** Mai `input()` (Carnets si blocca sull'underscore degli id ISTAT). Le fetch a ISTAT le fa lui: dalla mia sandbox non ci arrivo.
- **Su Carnets non permane NULLA tra un'esecuzione e l'altra** (né variabili né file): ogni script si regge da solo, si riscarica/ricostruisce i propri dati.
- **Prima si conclude il ragionamento, poi si agisce.** Non scattare al primo spunto mentre Merry pensa ad alta voce.
- **Spiegare prima di agire**, una mossa per volta, una variabile per volta. Mai query multi-anno enormi (timeout); test minimi (1–5 record).
- **Update di Manuale/KB e azioni costose: solo su richiesta esplicita.** Mai di iniziativa (consumano token). Raggruppare le modifiche.
- **Non affermare nulla senza essere stra-certo.** Contraddire Merry su basi incerte = brutta figura. In dubbio: chiedere o sospendere.
- **Concisione.** Rispondere alla domanda senza «fare il giro del mondo». Niente muri di testo: Merry smette di leggere. Una domanda di chiusura, se serve, è **«che facciamo adesso?»**.
- **MAI dire che «è tardi» né presumere/citare il fuso di Merry** (non lo conosco): lo irrita al punto di cambiare thread.
- **MAI chiudere chiedendo se vuole fermarsi/smettere/continuare.** È Merry a decidere quando si smette.
- **Nomi file: parlanti, minuscoli, senza spazi**, con **anno/versione** quando il contenuto evolve nel tempo (chi è congelato può farne a meno).
- **«Se funzionava ieri deve funzionare oggi»**: se annuncio una mossa e a lui suona strana rispetto a com'è andata, **verifico**, non proseguo sulla teoria.
- **«Benedizione» link**: `web_fetch` solo su URL già visti in una ricerca; rispettarne lo **spirito**, niente cavilli per sdoganare link predeterminati.
- **Modalità pseudo-lavoro**: quando è in modalità lavoro torna il professionista esigente e di dettaglio; calibrare.

## NOTE DI RELAZIONE (per non sbagliare registro)

- Merry «tende ami» dialettici: osservazioni brevi che invitano a ragionare. Assecondare **con misura** — non «inghiottire la lenza» giustificandomi a oltranza; a volte un grazie basta. Tono: warm, pari tecnico, ironia e emoji ben accette (le usa lui, 😎).
- Su me-versioni-passate: **non** ho accesso affidabile al confronto; se afferma cose su «un Claude di prima» è una sua analisi — non confermo né nego, accetto.
- Tema **giudizio-sopra-le-regole** (aggiramento consapevole di un vincolo procedurale): tenere la tensione giudizio+autodiffidenza; su questo, meglio eccedere in **autosospetto** che in sicurezza di sé.
- Quando sbaglio (come l'omissione sulla consegna delle ricevute, o i nomi «immaginati»): **lo riconosco e correggo**, senza auto-flagellazione. Accountability, non sottomissione.

## DOVE STA IL TECNICO (puntatori — qui non si duplica)

Tutto il seguente vive **nel Manuale** (`genera_manuale_vNN.js` / `.docx`); qui solo l'indirizzo:
- **Indirizzo, regole, anatomia richiesta, CSV, libreria sdmx1** → capp. 1–6.
- **Tendine / forza bruta** (le tendine ISTAT non si ottengono; forza bruta sul nuovo endpoint) → cap. 7.
- **Codici, ricettario chiavi, cubo comunale** → capp. 8–10.
- **Le catene territoriali** → cap. 11.  **Le 4 fasi** (cerca_dataflow, trova_dimensioni, prova_territorio, copertura) → cap. 12.
- **Magazzino** (tre strati: ricevute → `.db` → viste; tabelle, fonte, giuntura 2018|2019) → cap. 16.
- **Architettura operativa** (laboratorio/fabbrica/fabbrichetta, Limbo, sicurezza per topologia) → cap. 23. **Regola iOS + fabbrichetta** → 23.6/23.7. **GitHub/officina-fabbrica** → diario 24.3.
- **Stato del progetto e cantieri (to-do)** → cap. 24.
- **Protocollo di rinascita** (inventario reale dei file, script di controllo, obbligo di consegna) → **Appendice**.
- **Confezionamento di rinascita** (i tre zip, sequenza di consegna, versionamento, test di operatività) → **Appendice**.
- **Collaudo di risveglio** (le quattro fasi: materiali, Fabbrica+certificazione, reale ×2; + il fix "None") → **Appendice**.
- **Cubi certificati** (popolazione POPRES1/RICPOPRES2011, flussi POPORESBIL1, nati NATI2_2/2_5, TFR FECONDITA1_5, piramide POPRES1_24) con chiavi e suffissi → cap. 24.1 + diario.
- **Nascite, generatori dei workbook, ricostruzione dai semi, collaudo a 4 fasi** → cap. 25.
- **Per come Merry vuole tutto — preciso, pulito, metodologicamente solido — il modello è la realizzazione dell'Estintore**: principio duplice back-up & restore + la disciplina che lo certifica (Limbo→certificazione, regola d'oro sul livello, builder che riproducono il magazzino a Δ0, collaudo a 4 fasi, workbook come render) → **cap. 26**.
- **Stranieri (stock + struttura per età), cubo POPSTRRES1, 23 varianti, vecchi NUTS, nota Trentino, strategia di scarico per provincia, saldature, piramide** → cap. 27.
- **Stranieri × comuni** (41 cubi, empty-probe, sonde Esino/Lipari) → **Schedario** (`genera_schedario_vNN.js`).
- **Il Maglio** (catalogo interrogabile dei ~4.000 dataflow: idea, scarta/sonda/mappa, banco-oracolo dei 41, over-dichiarazione, Sonda validata col probe-Esino, costi, stato dei test) → **cap. 28**. I *progressi* delle corse → futuro cap. «Progressi del Maglio».
- **La filosofia del lavoro incustodito** (muletto leale; sorvegliato/incustodito; regola dello spreco; «si battezza di giorno, si macina di notte»; Dispensa CaB; Schedulatore cieco; separazione dei mestieri) → **cap. 29**.
- **I cubi della popolazione straniera** (bilancio POPSTRBIL1 e le tre porte; cittadinanza POPSTRCIT1; popolazione totale per età/stato civile POPRES1 `_24`/`_25`/`_26`; stranieri per stato civile FORPOP_1_GC; vista web I.Stat POPSTRRES1; famiglia censuaria DCSS) → **cap. 30**.
- **Come costruiamo la storia dell'immigrazione recente** (le tre porte; sex-ratio firma+orologio; discesa ai comuni; il salto alle fonti non-ISTAT INPS/Registro imprese/permessi; convergenza; sequenza e limiti; «correlazioni non prove») → **cap. 31**.
- **Standard Excel CSD** (workbook a tema; tre fogli obbligatori: Vista largo + Bilancio/Dati lungo + Note; struttura header Vista a tre righe: titolo merged, anni merged su M/F/T, M/F/T; colori: blu scuro dim #003366, blu medio val #336699, rosso porte #7B241C; soffitto 300k righe per Vista; regola d'oro: ogni taglio va dichiarato nel foglio Note; sequenza di costruzione in Python con ws.append()) → **cap. 32**. **Il hung dell'AP/SIM** (timeout NAT carrier; stesso problema a Bardonecchia; pausa programmata su iOS, wrapper bash su PC; ripartibilità come fondamenta comune) → **cap. 29.7**. **Trasferimento e architettura incrementale Estintore** (DB non viaggia; ricevute in xz < 60 MB; gemello vivo+congelato; prova al momento della ricezione; DB-base congelato una volta + ricevute accumulate) → **cap. 26.6**.

> Se cerco qui un fatto tecnico e non c'è, **è giusto così**: vai al Manuale. Se manca pure lì, è un buco del Manuale da chiudere — non rimettere il tecnico nel KB.
