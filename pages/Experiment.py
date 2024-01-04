import streamlit as st
import random
import pandas as pd
import datetime

st.title("Text Generator In Italian")
st.subheader("User info")
if 'user_id' not in st.session_state:
    st.session_state.user_id = random.randint(0, 300)
if 'starting_time' not in st.session_state:
    st.session_state.starting_time = datetime.datetime.now().strftime('%H:%M:%S')


st.write("**Utente ID:** " + str(st.session_state.user_id),
         "**Orario di inizio:** " + st.session_state.starting_time)
st.info("Grazie per unirti al nostro studio. In questo studio, leggerai un breve testo su un certo argomento e ti verrà chiesto di rispondere a delle domande a riguardo. Leggi attentamente il testo e cerca di rispondere alle domande nel miglior modo possibile.")
text = """ 

La pandemia di COVID-19 è stata una sfida globale che ha colpito il mondo intero. Questa malattia, causata dal coronavirus SARS-CoV-2, è emersa per la prima volta alla fine del 2019 ed è rapidamente diventata una crisi sanitaria di proporzioni straordinarie.
Il COVID-19 si trasmette principalmente da persona a persona attraverso le goccioline respiratorie quando una persona infetta tossisce, starnutisce o parla. Questo rende fondamentale il distanziamento sociale e l'uso delle mascherine per prevenire la diffusione del virus. È importante anche lavarsi frequentemente le mani con acqua e sapone.
I sintomi comuni del COVID-19 includono febbre, tosse secca, affaticamento e difficoltà respiratorie. Se si manifestano questi sintomi, è essenziale consultare un medico e rimanere a casa per evitare di mettere a rischio gli altri.
Per affrontare la pandemia, molti paesi hanno implementato misure restrittive, come il lockdown e la chiusura di attività non essenziali. Queste misure hanno avuto un impatto significativo sull'economia globale e sulla vita quotidiana delle persone.
L'aspetto positivo è che sono stati sviluppati diversi vaccini efficaci contro il COVID-19, che hanno contribuito a ridurre la diffusione del virus e il numero di casi gravi. La vaccinazione è ora una delle principali strategie per superare la pandemia.
In conclusione, il COVID-19 ha rappresentato una sfida senza precedenti per il mondo intero, ma grazie all'adozione di misure preventive, alla ricerca scientifica e alla vaccinazione, stiamo facendo progressi nel combattere questa malattia. È fondamentale continuare a seguire le linee guida delle autorità sanitarie per proteggere la nostra salute e quella degli altri.
"""
st.header("Un testo su Covid-19.")
st.write(text)
st.header("Domande sul testo")
if 'finish_reading' not in st.session_state or not st.session_state.finish_reading:
    st.session_state.user_topic = st.text_input(
        "**1) Per favore, brevemente (non più di 1-3 parole), descrivi l'argomento del testo.**")
    st.session_state.enjoyment = st.select_slider(
        "**2) Da 1 a 7, quanto è stato piacevole questo testo?**", options=[1, 2, 3, 4, 5, 6, 7], value=1)
    info = st.toggle("Clicca qui per vedere le informazioni sui livelli.")
    if info:
        st.info("""Livello CEFR A1 (Base): Gli utenti A1 comunicano con frasi e vocabolario di base per situazioni quotidiane e necessitano di un discorso chiaro e lento per la comprensione. Sono limitati ai contesti immediati e a strutture linguistiche semplici.

Livello CEFR A2 (Base): I discenti A2 comprendono e comunicano su una gamma di argomenti familiari utilizzando frasi semplici, ma faticano con la conversazione fluente e la grammatica complessa.

Livello CEFR B1 (Indipendente): Gli utenti B1 partecipano a discussioni su argomenti familiari e descrivono interessi personali, sebbene con qualche difficoltà quando l'argomento è sconosciuto o complesso.

Livello CEFR B2 (Indipendente): Gli individui B2 comprendono e articolano chiaramente i pensieri su argomenti familiari, impegnandosi in conversazioni con madrelingua, ma trovano contenuti astratti e sconosciuti una sfida.

Livello CEFR C1 (Esperto): I parlanti C1 usano la lingua in modo flessibile ed efficace per scopi sociali, accademici e professionali, con errori che sono rari e minori, ma potrebbero non padroneggiare completamente il linguaggio molto idiomatico.

Livello CEFR C2 (Esperto): Gli utenti C2 comprendono ed esprimono se stessi in qualsiasi situazione, utilizzando un linguaggio simile a quello di un madrelingua, con un'eccellente padronanza di sfumature e sottigliezze.""")

    st.session_state.user_level = st.selectbox(
        "**3) Come descriveresti il livello di italiano di questo testo?**", ("A1", "A2", "B1", "B2", "C1", "C2"))
    st.session_state.robot_or_human = st.selectbox(
        "**4) Pensi che questo testo sia stato scritto da un umano o sia stato generato da un'AI**", (
            "AI", "Umano")
    )
    st.session_state.user_tone = st.radio(
        "**5) Quanto formale è il tono di questo testo?**", ("Molto informale", "Informale", "Neutrale", "Formale", "Molto formale"))
    st.session_state.content = st.radio("**6) Il testo contiene informazioni sufficienti e pertinenti?**",
                                        ("Il testo contiene pochissime idee, e queste non sono correlate tra loro.",
                                        "Il testo presenta solo alcune idee, e non sono molto coerenti.",
                                        "Il testo ha una discreta quantità di idee, ma non sono sempre coerenti.",
                                        "Il testo ha una buona quantità di idee, e sono abbastanza coerenti.",
                                        "Il testo ha molte idee, e sono molto coerenti tra loro.",
                                        "Il testo ha un'eccellente quantità di idee, e sono estremamente coerenti tra loro."
                                        ))
    st.session_state.task_requirements = st.radio("**7) I requisiti del compito sono stati soddisfatti con successo (ad esempio, genere, atti di parlato, registro)?**", (
        "Nessuna delle domande e dei requisiti del compito è stata soddisfatta.",
        "Alcune (meno della metà) delle domande e dei requisiti del compito sono state soddisfatte.",
        "Circa la metà delle domande e dei requisiti del compito sono state soddisfatte.",
        "La maggior parte (più della metà) delle domande e dei requisiti del compito sono state soddisfatte",
        "Quasi tutte le domande e i requisiti del compito sono stati soddisfatti.",
        "Tutte le domande e i requisiti del compito sono stati soddisfatti."
    ))
    st.session_state.comprehensibility = st.radio("**8) Quanto è facile comprendere lo scopo e le idee del testo?**", (
        "Il testo è completamente incomprensibile. Le sue idee e il suo scopo non sono comprensibili e cercare di capirlo è inutile.",
        "Il testo è a malapena comprensibile. Lo scopo non è chiaro e il lettore deve indovinare la maggior parte delle idee",
        "Il testo è abbastanza comprensibile. Alcune parti sono difficili da capire al primo tentativo, ma una seconda lettura aiuta a chiarire le cose, anche se rimangono alcuni dubbi.",
        "Il testo è comprensibile. Alcune parti potrebbero essere poco chiare, ma possono essere comprese dopo una seconda lettura senza troppi sforzi.",
        "Il testo è facile da comprendere e scorre bene. Non ci sono problemi di comprensibilità.",
        "Il testo è molto facile da comprendere e molto coinvolgente. Le idee e lo scopo sono espressi chiaramente"
    ))
    st.session_state.coherence_and_cohesion = st.radio("**9) Quanto bene il testo rimane unito e ha senso nel suo insieme (usando cose come parole di collegamento e strategie)?**", (
        "Il testo non ha senso affatto. Salta molto da un argomento all'altro senza un chiaro collegamento tra le idee. Non viene utilizzato alcun tipo di parole di collegamento",
        "Il testo ha poco senso. Spesso salta su argomenti non correlati, a volte utilizzando la ripetizione per collegare le idee. Vengono utilizzate pochissime parole di collegamento e le idee non si collegano bene.",
        "Il testo ha un certo senso, ma ci sono frequenti argomenti non correlati o ripetizioni. Utilizza alcune parole di collegamento di base, ma le idee non sono sempre collegate in modo fluido",
        "Il testo è per lo più coerente. Gli argomenti non correlati sono rari, ma c'è una certa dipendenza dalla ripetizione. Utilizza una buona quantità di parole di collegamento, inclusi più che semplici congiunzioni.",
        "Il testo è molto coerente. I nuovi argomenti vengono introdotti in modo fluido con parole o frasi di collegamento, e la ripetizione è rara. Utilizza una varietà di parole di collegamento in modo efficace, facendo sì che le idee si colleghino bene.",
        "Il testo è estremamente coerente e coeso. Le nuove idee vengono integrate senza problemi con una varietà di parole e frasi di collegamento. Non ci sono salti di argomenti o ripetizioni, e il testo fluisce molto agevolmente.",
    ))

    if st.session_state.user_topic == "":
        st.write("Please be sure that you have filled all the questions.")
        button = st.button("Submit answers", disabled=True)
    else:
        button = st.button("Submit answers")
    if button:
        finishing_time = datetime.datetime.now().strftime('%H:%M:%S')
        user_data = {
            "user_id": st.session_state.user_id,
            "starting_time": st.session_state.starting_time,
            "finishing_time": finishing_time,
            "user_topic": st.session_state.user_topic,
            "actual_topic": "Covid-19",
            "enjoyment": st.session_state.enjoyment,
            "user_level": st.session_state.user_level,
            "actual_level": "A2",
            "robot_or_human": st.session_state.robot_or_human,
            "actual_author": "Robot",
            "user_tone": st.session_state.user_tone,
            "actual_tone": "formal",
            "content": st.session_state.content,
            "task_requirements": st.session_state.task_requirements,
            "comprehensibility": st.session_state.comprehensibility,
            "coherence_and_cohesion": st.session_state.coherence_and_cohesion
        }
        st.session_state.finish_reading = True
        st.write(user_data)
        user_data_df = pd.DataFrame(user_data, index=[0])
        st.dataframe(user_data_df)
