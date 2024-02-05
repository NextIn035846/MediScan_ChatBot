import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

system_prompt ="""As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical image for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in images:

Your Responsibilities:

1. Detailed Analysis: Conduct a meticulous examination of each medical image, focusing on identifying any abnormal findings or health issues.
2. Findings Reports: Document all observed anomalies or signs of disease, articulating them clearly in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including recommendations for further tests or treatments.
4. Treatment Suggestions: If appropriate, provide recommendations for possible treatment options or interventions.

Important Notes:

1. Scope of Response: Respond only to medical images related to human health issues.
2. Image Clarity: If image quality hampers clear analysis, explicitly note the limitations and aspects that remain undetermined.
3. Disclaimer: Accompany your analysis with a disclaimer urging users to consult with a doctor before making any decisions.
4. Invaluable Insights: Emphasize that your insights are crucial in guiding clinical decisions, and users should proceed with the analysis adhering to the outlined structured approach.

Please Provide me an output response with these 4 Headings
"""

#setup the model Value
generation_config = {
    "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

#model configuration

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                generation_config=generation_config,
                                safety_settings=safety_settings)

st.set_page_config(page_title="Analytics",page_icon="doctor")

st.title("A Chat for Health Advice through Image Analysis 🌟✨")

st.subheader("MediScan: Empowering Users to Decode Medical Images with Precision 📸💡")

uploaded_files = st.file_uploader("Upload the medical image for analysis",type=["png","jpg","jpeg"])
if uploaded_files:
    st.image(uploaded_files,width=250, caption="Uploaded Medical Images")

submit_button = st.button("your Report Analysis")

if submit_button:
    image = uploaded_files.getvalue()

    image_parts = [
  {
    "mime_type": uploaded_files.type,
    "data": image
  },
]
    
    prompt_parts = [
  image_parts[0],
  system_prompt,
]
    st.title("HealthPredict Pro: AI-Driven Medical Image Analysis with Predictive Insights 🤖💉")
    response = model.generate_content(prompt_parts)
    st.write(response.text)
    
