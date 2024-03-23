# "ArabNizer" | An Arabic NER Tagger
in Natural Language Processing, **NER** stands for **Named Entity Recognition**. It is a subtask of information extraction that seeks to locate and classify named entities mentioned in unstructured text into predefined categories such as the **names of persons**, **organizations**, **locations**, etc. NER systems typically use machine learning techniques to automatically identify and categorize entities within a body of text. It's widely used in various natural language processing applications like **information retrieval**, **question answering**, **text summarization**, and more.

Here are some common named entity tags:

| Tag              | Arabic Tag | Description |
| :---------------- | ------: | :---- |
| PER        |   اسم شخص   | refers to named entities that represent individual people or characters, whether real or fictional, mentioned within a text. |
| LOC           |   اسم عنوان   | represents named entities that denote specific locations, such as countries, cities, landmarks, and geographical features.|
| ORG    |  اسم مؤسسة   | denotes named entities that refer to organizations, institutions, companies, agencies, or any group of people with a common purpose or affiliation.|

# Running Demo:
https://github.com/MohammedAly22/ArabNizer/assets/90681796/1d4a5f6a-c639-40b8-804c-a333b0d69642

# Usage:
Demo link: https://arabnizer.streamlit.app/

Hugging Face model card: https://huggingface.co/mohammedaly22/arabnizer-xlmr-panx-ar

## Downloading and Running Tasneef Locally:
1. Clone this repository
```git
git clone https://github.com/MohammedAly22/ArabNizer
```

2. Inside the project folder, run the demo using the following command
```
streamlit run main.py
```

## Use the Model as a Hugging Face pipeline:
```python
from transformers import pipeline

ner_tagger = pipeline("token-classification", "mohammedaly22/mohammedaly22/arabnizer-xlmr-panx-ar")
text = 'اسمي محمد، اعمل في شركة اورانج و اسكن في القاهرة.'
ner_tagger(text, grouped_entities=True)
```

**output**:
```
[{'entity_group': 'PER',
  'score': 0.9486102,
  'word': 'محمد',
  'start': 5,
  'end': 9},
 {'entity_group': 'ORG',
  'score': 0.8212871,
  'word': 'اورانج',
  'start': 24,
  'end': 30},
 {'entity_group': 'LOC',
  'score': 0.9967932,
  'word': 'القاهرة',
  'start': 41,
  'end': 48}]
```

# Dataset
The Cross-lingual Natural Language Inference (XNLI) corpus is a crowd-sourced collection of 5,000 test and 2,500 dev pairs for the MultiNLI corpus. The pairs are annotated with textual entailment and translated into 14 languages: French, Spanish, German, Greek, Bulgarian, Russian, Turkish, Arabic, Vietnamese, Thai, Chinese, Hindi, Swahili and Urdu. This results in 112.5k annotated pairs. Each premise can be associated with the corresponding hypothesis in the 15 languages, summing up to more than 1.5M combinations. The corpus is made to evaluate how to perform inference in any language (including low-resources ones like Swahili or Urdu) when only English NLI data is available at training time. One solution is cross-lingual sentence encoding, for which XNLI is an evaluation benchmark. The Cross-lingual TRansfer Evaluation of Multilingual Encoders (XTREME) benchmark is a benchmark for the evaluation of the cross-lingual generalization ability of pre-trained multilingual models. It covers 40 typologically diverse languages (spanning 12 language families) and includes nine tasks that collectively require reasoning about different levels of syntax and semantics. The languages in XTREME are selected to maximize language diversity, coverage in existing tasks, and availability of training data. Among these are many under-studied languages, such as the Dravidian languages Tamil (spoken in southern India, Sri Lanka, and Singapore), Telugu and Malayalam (spoken mainly in southern India), and the Niger-Congo languages Swahili and Yoruba, spoken in Africa.

| Column | Description |
| ------ | ------ |
| tokens | A list of tokens. |
| ner_tags | A list of the associated NER tags for each token. |
| langs | A list of the language of each token. |


# Results
Here is the table of results after fine-tuning for 3 epochs:
| Epoch              | Training Loss | Validation Loss | F1 | Accuracy |
| ---------------- | ------ | ---- |  ---- |  ---- |
| 1 | 0.203100 | 0.207782 | 0.859793 | 0.942558 |
| 2 | 0.155900 | 0.204332 | 0.873610 | 0.948951 |
| 3 | 0.099200 | 0.207264 | 0.888544 | 0.953322 |

confusion matrix:
![9f504a07-5ced-440e-9b9c-5f6a4037ef2a](https://github.com/MohammedAly22/ArabNizer/assets/90681796/496cf7a6-1b18-431c-af80-168dc32163de)
