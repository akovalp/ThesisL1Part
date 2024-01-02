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
    st.session_state.user_tone = st.selectbox(
        "**5) Dalle seguenti opzioni, qual era il tono del testo?**", ("formale", "informale", "neutrale"))
    st.session_state.content = st.radio("**6) Does the text have enough relevant information?**",
                                        ("The text has very few ideas, and they don't relate to each other.",
                                         "The text has just a few ideas, and they aren't very consistent.",
                                         "The text has a fair amount of ideas, but they aren't always consistent.",
                                         "The text has a good amount of ideas, and they are fairly consistent.",
                                         "The text has plenty of ideas, and they are very consistent with each other.",
                                         "The text has an excellent amount of ideas, and they are extremely consistent with each other."
                                         ))
    st.session_state.task_requirements = st.radio("**7) Have the task requirements been fulfilled successfully (e.g. genre, speech acts, register)?**", (
        "None of the questions and the requirements of the task have been answered.",
        "Some (less than half) of the questions and the requirements of the task have been answered.",
        "Approximately half of the questions and requirements of the task have been answered.",
        "Most (morethan half) of the questions and the requirements of the task have been answered",
        "Almost all the questions and the requirements of the task have been answered.",
        "All the questions and the requirements of the task have been answered."
    ))
    st.session_state.comprehensibility = st.radio("**8) How easy is it to understand the purpose and ideas of the text?**", (
        "The text is completely unclear. Its ideas and purpose are not understandable, and trying to understand it is futile.",
        "The text is barely understandable. The purpose isn't clear and the reader has to guess most of the ideas",
        "The text is somewhat understandable. Some parts are hard to get on the first try, but a second read helps clarify things, though some doubts remain.",
        "The text is understandable. A few parts might be unclear, but they can be understood after a second read without much effort.",
        "The text is easy to understand and flows well. There are no issues with comprehensibility.",
        "The text is very easy to understand and highly engaging. The ideas and purpose are stated clearly"
    ))
    st.session_state.coherence_and_cohesion = st.radio("**9) How well does the text stick together and make sense as a whole (using things like linking words and strategies)?**", (
        "The text makes no sense at all. It jumps around a lot with no clear connection between ideas. There's no use of linking words or phrases",
        "The text barely makes sense. It often jumps to unrelated topics, sometimes using repetition to connect ideas. Very few linking words are used and ideas don't connect well.",
        "The text makes some sense, but there are frequent unrelated topics or repetitions. It uses some basic linking words, but the ideas aren't always connected smoothly",
        "The text is mostly coherent. Unrelated topics are rare, but there's some reliance on repetition. It uses a good amount of linking words, including more than just basic conjunctions.",
        "The text is very coherent. New topics are introduced smoothly with linking words or phrases, and repetition is rare. It uses a variety of linking words effectively, making ideas connect well.",
        "The text is extremely coherent and cohesive. New ideas are integrated seamlessly with a variety of linking words and phrases. There's no jumping around or repetition, and the text flows very smoothly.",
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
