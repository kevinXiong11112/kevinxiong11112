import speech_recognition as sr
from gtts import gTTS

# Function to transcribe audio using SpeechRecognition
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        transcription = recognizer.recognize_google(audio)  # Using Google Web Speech API
        return transcription
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None

# Function to synthesize Chinese text to speech using gTTS
def synthesize_chinese(text, output_file):
    tts = gTTS(text=text, lang='zh')  # Set lang to 'zh' for Chinese
    tts.save(output_file)

# Example Usage:
english_audio_path = r"C:\Users\engik\.vscode\kys.mp3"

# Transcribe English Audio
transcription = transcribe_audio(english_audio_path)
if transcription:
    print(f"Transcription: {transcription}")

    # Synthesize Chinese Text
    chinese_text = "你好, 这是一个测试"  # Example Chinese text
    output_speech_path = "output_cloned_voice.mp3"  # gTTS saves files as MP3
    synthesize_chinese(chinese_text, output_speech_path)
    print(f"Synthesized speech saved to {output_speech_path}")
else:
    print("Failed to transcribe audio.")
