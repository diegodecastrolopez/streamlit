import streamlit as st

# st.title accepts a subset of Markdown, including the :rainbow[...] colour directive.
st.title('🔴⚪️ Welcome to my :rainbow[Pokémon] - Streamlit Demo!')

# The same heading written as raw HTML. It needs unsafe_allow_html=True and is
# kept here only to show the alternative: prefer the Markdown version.
# st.markdown(
#     "<h1 style='font-size: 33px;'><p style='color:red;'>Welcome to my Pokémon - Streamlit Demo!</h1></p>",
#     unsafe_allow_html=True,
# )

# Paths are resolved against the folder you run streamlit from, which is the
# repository root, so the image path does not need a solutions/ prefix.
st.image('images/pokemon.png')

st.subheader('What are we going to do?')
st.write("")
st.markdown(
    '- EDA visualisations / dataset exploration \n'
    ' - **Prediction:** Is my Pokémon legendary? \n'
    ' - Find our Pokémon on the map'
)
