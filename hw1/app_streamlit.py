from collections import Counter
import streamlit as st
import ner
import graphviz
from src import *


# set up session state
if "view" not in st.session_state:
    st.session_state.view = None


# title, text area, and sidebar 
# st.set_page_config(layout='wide')
st.markdown('## SpaCy Named Entity Recognition')

text = st.text_area('Text to process', value=example, height=100)
st.info(text)
st.sidebar.markdown('### Settings')
st.sidebar.radio('#### select views', ['Entities', 'Dependencies'], key = "view", index = None)


# set up the spaCy configuration
doc = ner.SpacyDocument(text)

entities = doc.get_entities()
tokens = doc.get_tokens()
counter = Counter(tokens)
words = list(sorted(counter.most_common(30)))
dependencies = doc.get_dependency() 


# display the results
tab1, tab2, = st.tabs(["Table", "Graph"])

with tab1:
    if st.session_state.view ==  None:
        st.error('Please select a **view** from the sidebar',icon="⚠️")
    else:
        if st.session_state.view == 'Entities':
            st.table(entities)
        elif st.session_state.view == 'Dependencies':
            st.table(dependencies)
        st.markdown(f'Total number of tokens: {len(tokens)}<br/>'
            f'Total number of types: {len(counter)}', unsafe_allow_html=True)
        
with tab2:
    if st.session_state.view ==  None:
        st.error('Please select a **view** from the sidebar',icon="⚠️")

    elif st.session_state.view == 'Entities':
        doc.get_entities_viz()
        
    elif st.session_state.view == 'Dependencies':
        graph = graphviz.Digraph()
        for token, dep, head in dependencies:
            graph.edge(head, token, label=dep)

        st.graphviz_chart(graph)

