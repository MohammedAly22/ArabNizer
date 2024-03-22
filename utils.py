import re
from transformers import pipeline
from nltk import word_tokenize


pipe = pipeline('token-classification', 'mohammedaly22/arabnizer-xlmr-panx-ar')

class_mapper = {
    'PER': 'شخص',
    'ORG': 'مؤسسة',
    'LOC': 'عنوان',
    'X': ''
}



def get_all_words_and_entities(text, words, entities):
    word_entity_mapper = {word: entity for word, entity in zip(words, entities)}
    all_tokens = word_tokenize(text)

    all_words = [token for token in all_tokens]
    all_entities = ["X" if token not in words else word_entity_mapper[token] for token in all_tokens]

    return all_words, all_entities
    

def generate_highlighted_word(word, entity):
    highlight_word = f' <span class="highlight-{entity}"> ' + word + f' <span class="highlight-inner-{entity}"> ' + class_mapper[entity] + " </span> " + " </span> "
    
    return highlight_word    


def generate_highlighted_text(words, entities):
    rendered_text = '<div class="highlighted-text"> '
    
    for word, entity in zip(words, entities):
        highlight_word = generate_highlighted_word(word, entity)
        rendered_text += highlight_word

    rendered_text += ' </div>'

    return rendered_text
