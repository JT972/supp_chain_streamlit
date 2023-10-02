import utils
import streamlit as st
st.title("DS DEC 2002 - Supply Chain")
text_input = st.text_area("Commentaire à évaluer")
if st.button("Evaluer"):
    if text_input.strip():
        prediction = utils.predict_review_best_xgb(text_input)
        if prediction == 0:
            st.write(":rage: NEGATIF :rage:")
        elif prediction == 1:
            st.write("NEUTRE")
        elif prediction == 2:
            st.write(":tada: POSITIF :tada:")
    else:
        st.write("")