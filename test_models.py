import google.generativeai as genai

genai.configure(api_key="AIzaSyBWaEcJEisnuFfuch5WN_tJbea_UpUTuvk")

print("Available models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")
