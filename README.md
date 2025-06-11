# Audio Transcription and LLM Project
### Overview
This project contains two Python scripts for distinct functionalities:

1. speech2text.py: An audio transcription application that converts uploaded audio files to text using the Whisper model.
2. simple_llm.py: A script that interacts with a large language model (LLM) to generate text responses, specifically using IBM WatsonxLLM with the Llama 3.2 model.

### Files
1. speech2text.py

- Purpose: Downloads an audio file from a specified URL and provides a Gradio-based interface to transcribe uploaded audio files to text.
- Dependencies:
```plain
gradio: For creating the web-based UI.
requests: For downloading the audio file.
transformers: For using the openai/whisper-tiny.en model for speech-to-text transcription.
```

- Functionality:
Downloads an audio file from a predefined URL and saves it locally as downloaded_audio.mp3.
Provides a Gradio interface where users can upload an audio file for transcription. Uses the Whisper model to transcribe audio with a chunk length of 30 seconds and a batch size of 8. Outputs the transcribed text in the Gradio interface.



2. simple_llm.py

- Purpose: Demonstrates interaction with a large language model (LLM) to generate text responses using IBM WatsonxLLM.
- Dependencies:
```plain
ibm_watson_machine_learning: For accessing the WatsonxLLM and Llama 3.2 model.
```

- Functionality:
Initializes a connection to IBM Watson Machine Learning with provided credentials. Configures the Llama 3.2 model with parameters for maximum tokens (700) and temperature (0.1 for deterministic output). Sends a sample query ("How to read a book effectively?") to the model and prints the response.



### Prerequisites

Python 3.8 or higher.
Install required packages:pip install gradio requests transformers ibm-watson-machine-learning


For simple_llm.py, you need valid IBM Watson Machine Learning credentials and access to the specified project_id.

### Usage

Running speech2text.py:

Execute the script:
```bash
python speech2text.py
```

A Gradio interface will launch in your browser.
Upload an audio file to transcribe it, and the transcribed text will appear in the interface.


Running simple_llm.py:

Ensure you have valid IBM Watson Machine Learning credentials and update the my_credentials dictionary in the script.
Run the script:
```bash
python simple_llm.py
```

The script will output the model's response to the query "How to read a book effectively?".

#### License
This project is licensed under the MIT License.
