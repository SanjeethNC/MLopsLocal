
import gradio as gr
from transformers import pipeline

# Initialize the translation pipeline with T5-base model
translator = pipeline("translation", model="google-t5/t5-base")

print('hi')

# Define available languages
AVAILABLE_LANGUAGES = ["French", "German", "Romanian"]

def translate(input_text, target_language):
    target_language = target_language.lower()
    
    # Set the task prefix based on the chosen language
    if target_language == "french":
        task_prefix = "translate English to French: "
    elif target_language == "german":
        task_prefix = "translate English to German: "
    elif target_language == "romanian":
        task_prefix = "translate English to Romanian: "
    else:
        return "Sorry, this language is not supported."

    # Perform translation
    full_input = task_prefix + input_text
    translated = translator(full_input, max_length=128)
    return translated[0]['translation_text']

def show_available_languages():
    return ", ".join(AVAILABLE_LANGUAGES)

def run_tests():
    test_cases = [
        ("Hello", "French"),
        ("How are you?", "German"),
        ("Good morning", "Romanian"),
        ("Hello", "Spanish")
    ]
    
    results = []
    for input_text, target_lang in test_cases:
        try:
            result = translate(input_text, target_lang)
            status = "Passed" if result != "Sorry, this language is not supported." else "Failed"
            results.append(f"Test '{input_text}' to {target_lang}: {status}\nResult: {result}")
        except Exception as e:
            results.append(f"Test '{input_text}' to {target_lang}: Failed - {str(e)}")
    
    return "\n".join(results)

# Create Gradio interface
with gr.Blocks() as iface:
    gr.Markdown("# Speech Translation using T5-base")
    gr.Markdown("Translate English text to French, German, or Romanian using the T5-base model.")
    
    with gr.Row():
        input_text = gr.Textbox(label="Enter English text", placeholder="Hi, how are you?")
        output_text = gr.Textbox(label="Translation")
    
    target_lang = gr.Dropdown(AVAILABLE_LANGUAGES, label="Target Language")
    translate_btn = gr.Button("Translate")
    
    with gr.Row():
        show_langs_btn = gr.Button("Show Available Languages")
        available_langs = gr.Textbox(label="Available Languages")
    
    test_btn = gr.Button("Run Tests")
    test_output = gr.Textbox(label="Test Results")
    
    translate_btn.click(translate, inputs=[input_text, target_lang], outputs=output_text)
    show_langs_btn.click(show_available_languages, inputs=None, outputs=available_langs)
    test_btn.click(run_tests, inputs=None, outputs=test_output)

# Launch the app
iface.launch()
