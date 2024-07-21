from gtts import gTTS
import playsound
import os
from translate import Translator
from happytransformer import HappyTextToText, TTSettings

happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")

args = TTSettings(num_beams=5, min_length=1)

# Read the sentence from the text file
with open("sentence.txt", "r") as f:
    sentence = f.read()

if sentence.strip():  # Ensure there's content in the sentence
    sentence = "grammar:" + sentence
    result = happy_tt.generate_text(sentence, args=args)
    inter = result.text

    # Translate the sentence to Kannada
    translator = Translator(to_lang="kn")
    translated_sentence = translator.translate(inter)

    # Create a gTTS object with the translated Kannada sentence
    tts = gTTS(text=translated_sentence, lang='kn')

    # Save the speech to a file
    audio_file = "speech.mp3"
    tts.save(audio_file)

    # Play the speech
    playsound.playsound(audio_file)

    # Optional: Remove the audio file after playing
    os.remove(audio_file)
else:
    print("No sentence detected for processing.")
