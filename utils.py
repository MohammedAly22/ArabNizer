from transformers import pipeline


pipe = pipeline('token-classification', 'mohammedaly22/arabnizer-xlmr-panx-ar')

class_mapper = {
    'PER': 'شخص',
    'ORG': 'مؤسسة',
    'LOC': 'عنوان',
}


def generate_highlighted_word(word, entity):
    highlight_word = f' <span class="highlight-{entity}"> ' + word + f' <span class="highlight-inner-{entity}"> ' + class_mapper[entity] + " </span> " + " </span> "
    
    return highlight_word    


def generate_highlighted_text(words, entities):
    rendered_text = '<div class="highlighted-text"> '
    
    for word, entity in zip(words, entities):
        highlight_word = generate_highlighted_word(word, entity)
        rendered_text += highlight_word
        # rendered_text += ' <br> '

    rendered_text += ' </div>'

    return rendered_text