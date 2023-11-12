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
st.header("Questions about the text")
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
    st.session_state.content = st.radio("**6) Is the number of information units provided in the text adequate and relevant?**",
                                        ("None of the questions and the requirements of the task have been answered.",
                                         "Some (less than half) of the questions and the requirements of the task have been answered.",
                                         "Approximately half of the questions and requirements of the task have been answered.",
                                         "Most (morethan half) of the questions and the requirements of the task have been answered",
                                         "Almost all the questions and the requirements of the task have been answered.",
                                         "All the questions and the requirements of the task have been answered."
                                         ))
    st.session_state.task_requirements = st.radio("**7) Have the task requirements been fulfilled successfully (e.g. genre, speech acts, register)?**", (
        "None of the questions and the requirements of the task have been answered.",
        "Some (less than half) of the questions and the requirements of the task have been answered.",
        "Approximately half of the questions and requirements of the task have been answered.",
        "Most (morethan half) of the questions and the requirements of the task have been answered",
        "Almost all the questions and the requirements of the task have been answered.",
        "All the questions and the requirements of the task have been answered."
    ))
    st.session_state.comprehensibility = st.radio("**8) How much effort is required to understand text purpose and ideas?**", (
        "The text is not at all comprehensible. Ideas and purposes are unclearly stated and the efforts of the reader to understand the text are ineffective.",
        "The text is scarcely comprehensible. Its purposes are not clearly stated and the reader struggles to understand the ideas of the writer. The reader has to guess most of the ideas and purposes.",
        "The text is somewhat comprehensible. Some sentences are hard to understand at a first reading. A second reading helps to clarify the purposes of the text and the ideas conveyed, but some doubts persist.",
        "The text is comprehensible. Only a few sentences are unclear but are understood, without too much effort, after a second reading.",
        "The text is easily comprehensible and reads smoothly. Comprehensibility is not an issue.",
        "The text is very easily comprehensible and highly readable. The ideas and the purpose are clearly stated."
    ))
    st.session_state.coherence_and_cohesion = st.radio("**9) Is the text coherent and cohesive (e.g. cohesive devices, strategies)?**", (
        "The text is not at all coherent. Unrelated progressions and coherence breaks are very common. The writer does not use any anaphoric device. The text is not atall cohesive. Connectives are hardly ever used and ideas are unrelated.",
        "The text is scarcely coherent. The writer often uses unrelated progressions; when coherence is achieved, it is often done through repetitions. Only a few anaphoric devices are used. There are some coherence breaks. The text is not very cohesive. Ideas are not well linked by connectives, which are rarely used.",
        "The text is somewhat coherent. Unrelated progressions and/or repetitions are frequent. More than two sentences in a row can have the same subject (even when the subject is understood). Some anaphoric devices are used. There can be a few coherence breaks. The text is somewhat cohesive. Some connectives are used, but they are mostly conjunctions.",
        "The text is coherent. Unrelated progressions are somewhat rare, but the writer sometimes relies on repetitions to achieve coherence. A sufficient number of anaphoric devices is used. There may be some coherence breaks. The text is cohesive. The writer makes good use of connectives, sometimes not limiting this to conjunctions.",
        "The text is very coherent: when the writer introduces a new topic, it is usually done by using connectives or connective phrases. Repetitions are very infrequent. Anaphoric devices are numerous. There are no coherence breaks. The text is very cohesive and ideas are well linked by adverbial and/or verbal connectives.",
        "The writer ensures extreme coherence by integrating new ideas in the text with connectives or connective phrases. Anaphoric devices are used regularly. There are few incidences of unrelated progressions and no coherence breaks. The structure of the text is extremely cohesive, thanks to a skillful use of connectives (especially linking chunks, verbal constructions and adverbials), often used to describe relationships between ideas.",
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
