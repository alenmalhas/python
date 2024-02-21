#python -m unittest transformer1.py
#ref: Quick tour: Pipeline  https://huggingface.co/docs/transformers/quicktour#pipeline
#ref: The pipeline function https://www.youtube.com/watch?v=tiZFewofSLM&t=38s
import unittest
from transformers import pipeline

def Run1_SentimentAnalysis():
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    input_array = [
        "We are very happy to show you the 🤗 Transformers library.",
        "I've been waiting for a Huggingface course my whole life",
        "I can't wait for the next Hugging Face tutorial.",
        "I hate waiting in my car in a traffic jam.",
        "I am not a big fan of waiting in my car in a traffic jam."
        ]
    predictions = classifier(input_array)
    for i in range(len(predictions)):
        result = predictions[i]
        print(f"label: {result['label']}, with score: {round(result['score'], 4)} input: {input_array[i]}")

def Run2_ZeroShot():
    classifier = pipeline("zero-shot-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    predictions = classifier([
        "We are very happy to show you the 🤗 Transformers library.",
        "I can't wait for the next Hugging Face tutorial.",
        "I hate waiting in my car in a traffic jam.",
        "I am not a big fan of waiting in my car in a traffic jam."], 
        candidate_labels=["education", "politics", "travel", "business"],
        multi_label=False)
    
    for result in predictions:
        #print(f"label: {result['label']}, with score: {round(result['score'], 4)}")
        print(result)

def Run3_TextGeneration():
    generator = pipeline("text-generation", model="distilgpt2")
    predictions = generator("Once upon a time, there was a", max_length=30, num_return_sequences=2)
    for result in predictions:
        print(result)

def Run4_FillMask():
    fill_mask = pipeline("fill-mask", model="distilroberta-base")
    predictions = fill_mask(f"Once upon a time, there was a <mask> who wanted to do something incredible.", top_k=3)
    for result in predictions:
        print(result)

def Run5_NamedEntityRecognition():
    ner = pipeline("ner", model="distilgpt2", aggregation_strategy="simple")
    predictions = ner("I am superman, i work as a superhero at Marvel Studios, i came from a far away planet to save your species.")
    for result in predictions:
        print(result)

def Run6_QuestionAnswering():
    question_answering = pipeline("question-answering", model="distilgpt2")
    question_answering(
        question="Who is my employer?", 
        context="I am superman, i work as a superhero at Marvel Studios, i came from a far away planet to save your species."
        )


from transformers import BertTokenizerFast, EncoderDecoderModel
import torch
# ref: https://huggingface.co/mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization
def generate_summary(text, tokenizer, device, model):
    # cut off at BERT max length 512
    inputs = tokenizer([text], padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)

    output = model.generate(input_ids, attention_mask=attention_mask)

    return tokenizer.decode(output[0], skip_special_tokens=True)
  

def Run7_Summarization():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    tokenizer = BertTokenizerFast.from_pretrained('mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization')
    model = EncoderDecoderModel.from_pretrained('mrm8488/bert-small2bert-small-finetuned-cnn_daily_mail-summarization').to(device)
    input_text = '''
How do you cover nearly a century of sand, oil, and blood in less than four minutes? PIC Agency’s titles for The Kingdom do just that, 
giving viewers a geopolitical crash course in U.S.–Saudi Arabia relations that contextualizes the events depicted in the 2007 action thriller.
                  
Using a combination of infographics and news footage, this illustrated clash of cultures efficiently fills gaps missing in the viewer’s knowledge of the region, 
its people, and its relationship with the West. A less inspired approach would have been to deliver the facts through a dry, text-only prologue; instead, 
the sequence envelops viewers in a sandstorm of charts and details. Before you can fully register one fact, you’ve learned two more. Acting as a primer, 
a sort of CliffsNotes for Saudi Arabia, the sequence briefs us for entry into The Kingdom.
    '''
    from pathlib import Path
    input_text2 = Path('C:\WORK\workroom\python\pythonWorkroom\pgvector\lease-11-1958.txt').read_text()
    summary = generate_summary(input_text2, tokenizer, device, model)
    print(summary)

def Run8_Translation():
    translation = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-en-tr")
    predictions = translation("I know Tom didn't want to eat that.")
    for result in predictions:
        print(result)


def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(fun(3), 4)

    def test2(self):
        self.assertEqual(fun(5), 6)
        
def main():
    #unittest.main()
    '''
    Run1_SentimentAnalysis()
    Run2_ZeroShot()
    Run3_TextGeneration()
    Run4_FillMask()
    Run5_NamedEntityRecognition()
    '''
    #Run6_QuestionAnswering()
    Run7_Summarization()
    #Run8_Translation()
    

if __name__ == '__main__':
    main()