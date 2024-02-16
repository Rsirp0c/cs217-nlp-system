import spacy
from spacy import displacy
import streamlit as st
import re

# nlp = spacy.load("en_core_web_sm")
# doc = nlp("This is a sentence.")

# # Create a dot string representation
# dot_string = displacy.render(doc, style="dep", options={"compact": True}, page=True, minify=True)

# # Remove surrounding <svg> tag
# dot_string = dot_string[dot_string.index("<svg") + 5 : dot_string.index("</svg>")]

# # Convert SVG paths to DOT edges
# edges = []
# for line in dot_string.split("\n"):
#     if "<path" in line:
#         # Extract edge information
#         start, end, label, direction = re.findall(r'id="([^"]+)"', line)
#         edges.append(f'{start} -> {end} [label="{label}"];')

# # Build DOT graph
# dot_graph = "digraph {\n" + "\n".join(edges) + "\n}"

# # Display the graph using streamlit
# st.graphviz_chart(dot_graph)

st.graphviz_chart('''
    digraph G {
    "Sebastian Thrun" [label="PERSON"]
    "Google" [label="ORG"]
    "2007" [label="DATE"]
    "American" [label="NORP"]
    "Thrun" [label="PERSON"]
    "Recode" [label="ORG"]
    "earlier this week" [label="DATE"]
    
    "Sebastian Thrun" -> "Google" [label="works at"]
    "Sebastian Thrun" -> "2007" [label="worked in"]
    "Sebastian Thrun" -> "American" [label="is"]
    "Sebastian Thrun" -> "Thrun" [label="also known as"]
    "Sebastian Thrun" -> "Recode" [label="interviewed by"]
    "Sebastian Thrun" -> "earlier this week" [label="interviewed on"]
    }
    ''')