import streamlit as st
import time 
current_time = time.time()
st.set_page_config(page_title="MODULO INFORMATIVO E DI CONSENSO ALLA PARTECIPAZIONE E AL TRATTAMENTO DEI DATI",  )
st.title("**Research Title**: Some very creative and catchy title")


st.header("DESCRIZIONE E SCOPI DELLA RICERCA")
st.write(
    """
Gentile partecipante, \n
Lei è invitato a partecipare a uno studio di ricerca che mira a valutare certi aspetti di testi generati dall'intelligenza artificiale. Prima che Lei decida di partecipare, è importante che Lei comprenda la natura dello studio e cosa ci si aspetta da Lei. La preghiamo di leggere attentamente le seguenti informazioni e di porre qualsiasi domanda prima di dare il Suo consenso.
Lo scopo di questo studio è di valutare vari aspetti di testi generati dall'intelligenza artificiale e raccogliere approfondimenti sulla loro qualità, pertinenza e impatto. Questo studio è coordinato dalla prof.ssa Judit Gervain, Università di Padova
    """
)
st.divider()
st.subheader("METODOLOGIA DI RICERCA")
st.write(
    """
    Come partecipante, ti verranno presentati brevi testi di lettura generati da un modello di AI o da un umano, seguiti da una serie di domande relative al testo. Dopo aver risposto alle domande, ti verrà chiesto di fornire alcune informazioni demografiche su di te.
    """
)
st.divider()
st.subheader("LUOGO E DURATA DELLA RICERCA")
st.write(
    """
    La ricerca sarà svolta presso il Dipartimento di Psicologia dello Sviluppo e della Socializzazione
    dell’Università di Padova e avrà una durata complessiva di circa 30-45 minuti
    """
)
st.divider()
st.subheader("RECAPITI")
st.write(
    """
    Judit Gervain, professore ordinario, Dipartimento di Psicologia dello Sviluppo e della
    Socializzazione, Università degli studi di Padova (judit.gervain@unipd.it, +39 049 8276531, Via
    Venezia 8 - 35131, Padova) \n
    **Responsabile della raccolta dati:**
    Judit Gervain, professore ordinario, Dipartimento di Psicologia dello Sviluppo e della
    Socializzazione, Università degli studi di Padova
    Anna Martinez, assegnista, Università degli studi di Padova, anna.martinez.alv@gmail.com
    Jessica Germignani, assegnista, Università degli studi di Padova, jessicagemignani@gmail.com
    Caroline Nallet, dottoranda, Università degli studi di Padova, caroline.nallet94@gmail.com
    laureandi e tirocinanti lavorando sulla supervisione della responsabile della ricerca
    """
)
st.divider()
st.subheader("CONSENSO ALLA PARTECIPAZIONE E AL TRATTAMENTO DEI DATI")
st.write(
    """
    Il/La sottoscritto/a acconsente liberamente alla partecipazione allo studio: ** My beautiful study name ** \n
1. Di essere a conoscenza che lo studio è in linea con le vigenti leggi D. Lgs 196/2003 e UE
GDPR 679/2016 sulla protezione dei dati e di acconsentire al trattamento e alla comunicazione
dei dati personali, nei limiti, per le finalità e per la durata precisati dalle vigenti leggi (D. Lgs 196/2003 e UE GDPR 679/2016). Il/la responsabile della ricerca si impegna ad adempiere agli
obblighi previsti dalla normativa vigente in termini di raccolta, trattamento e conservazione di
dati sensibili.
2. Di sapere di potere ritirare la propria partecipazione in qualunque momento, senza fornire
spiegazioni, senza alcuna penalizzazione e ottenendo il non utilizzo dei Suoi dati.
3. Di essere a conoscenza che i dati saranno raccolti in forma confidenziale (nome/codice).
4. Di essere a conoscenza che propri i dati saranno utilizzati esclusivamente per scopi
scientifici e statistici e con il mantenimento delle regole relative alla riservatezza.
5. Di sapere che, qualora lo desiderassero, possono ottenere la restituzione dei dati grezzi.
Poiché il presente studio non ha finalità cliniche, siamo stati informati che dovremo
rivolgerci ad una/o specialista per l&#39;eventuale interpretazione dei dati.
6. Di sapere che, nonostante il presente studio non abbia finalità cliniche, i metodi utilizzati
potrebbero in rari casi rivelare anomalie, e che in tale eventualità gli sperimentatori gliene
daranno informazione.
7. Di sapere che una copia del presente modulo ci sarà consegnata dalla ricercatrice o dal
ricercatore.
8. Di sapere che la protezione dei suoi dati è designata con Decreto del Direttore Generale
4451 del 19 dicembre 2017, in cui è stato nominato un Responsabile della Protezione dati,
privacy@unipd.it.
    """
)
st.divider()
name = st.text_input("Nome")
surname = st.text_input("Cognome")
st.write(
    f"La/Il sottoscritt {name} {surname} presa visione del presente modulo esprime il proprio consenso alla partecipazione e al trattamento dei propri dati personali."
    )
if st.button("CONSENSO"):
    st.write("Grazie per il tuo consenso, per favore clicca sul pulsante situato sulla sinistra per iniziare lo studio. Per favore clicca sul pulsante della pagina sperimentale che puoi vedere sul lato sinistro dello schermo per cominciare lo studio.")


