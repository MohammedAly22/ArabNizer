import streamlit as st
from utils import pipe, get_all_words_and_entities, generate_highlighted_text


# for custom CSS styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.title('التعرف على الكيانات المُسماة')

with st.form('submission_form'):
    text = st.text_area('من فضلك ادخل النص:', placeholder='ادخل النص المراد تصنيفه...', height=80)
    submitted = st.form_submit_button('تأكيد')

    if submitted:
        if text:
            with st.spinner('...جاري التحميل'):
                model_output = pipe(text, grouped_entities=True)

            words = [item['word'] for item in model_output if item['word']]
            entities = [item['entity_group'] for item in model_output if item['word']]  

            # all_words, all_entities = get_all_words_and_entities(text, words, entities)
            rendered_text = generate_highlighted_text(words, entities)
            
            st.write('<p class="bold-text"> الكيانات المُسماة: </p>', unsafe_allow_html=True)
            st.markdown(rendered_text, unsafe_allow_html=True)

        else:
            st.error('من فضلك ادخل النص المراد تصنيفه')
