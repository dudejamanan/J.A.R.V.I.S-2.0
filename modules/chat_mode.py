from core.imports import genai
from core.listener import listen
from core.speaker import speak 

client = genai.Client(api_key="")

def chat_mode(prompt,chat=None):
    try:
        # Send prompt to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        # Extract the text
        reply = response.text

        # Speak the response
        speak(reply)

        return reply

    except Exception as e:
        error_msg = f"Sorry, I couldn't get a response. Error: {e}"
        print(error_msg)
        return error_msg