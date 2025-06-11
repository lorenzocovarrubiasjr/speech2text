import gradio as gr
import requests
from transformers import pipeline

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX04C6EN/Testing%20speech%20to%20text.mp3'
response = requests.get(url)
audio_file_path = 'media/downloaded_audio.mp3'
if response.status_code == 200:
    with open(audio_file_path, 'wb') as file:
        file.write(response.content)
    print('File downloaded successfully!')
else:
    print('Failed to download the file')


def transcript_audio(audio_file):
    pipe = pipeline(
        'automatic-speech-recognition',
        model='openai/whisper-tiny.en',
        chunk_length_s=30
    )

    prediction = pipe(audio_file, batch_size=8)['text']
    print(f'\nPrediction:\n {prediction}')
    return prediction

audio_input = gr.Audio(sources='upload', type='filepath')
output_text = gr.Textbox()
ui = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input, 
    outputs=output_text,
    title='Audio Transcription App',
    description='Upload the audio file'
)

ui.launch()