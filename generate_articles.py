import google.generativeai as genai
from datetime import datetime

# Configure API
genai.configure(api_key="AIzaSyBWaEcJEisnuFfuch5WN_tJbea_UpUTuvk")
model = genai.GenerativeModel('gemini-2.0-flash')

prompts = {
    "ibs": """Write a comprehensive, SEO-optimized article about "Best Diet for IBS (Irritable Bowel Syndrome)" for Healthy Gut AI app.

Requirements:
- Title (H1) with IBS diet keyword
- Meta description (150-160 chars)
- Introduction (100 words with keyword)
- Main sections with H2/H3 headers (question-based)
- Include: symptoms, foods to eat, foods to avoid, meal plan table
- Add "When to see a doctor" section
- Add "How Healthy Gut AI Helps" section with app features
- Include 5-8 FAQ in Q&A format
- Add 2-3 credible citations (NIH, NHS, CDC)
- Medical disclaimer at end
- Reading level: Grade 7-9, clear and scannable
- Word count: 1500-2000 words

Output: Well-structured article with clear headers, bullet points, and tables.""",

    "ibd": """Write a comprehensive, SEO-optimized article about "Managing IBD (Inflammatory Bowel Disease) Symptoms" for Healthy Gut AI app.

Requirements:
- Title (H1) with IBD symptoms keyword
- Meta description (150-160 chars)
- Introduction (100 words with keyword)
- Sections: What is IBD, Early symptoms, Difference from IBS, Treatment options, Diet management
- Include comparison table: IBD vs IBS
- Add "When to see a doctor" section
- Add "How Healthy Gut AI Helps" section
- Include 5-8 FAQ
- Add 2-3 credible citations (NIH, Mayo Clinic, CDC)
- Medical disclaimer
- Reading level: Grade 7-9
- Word count: 1500-2000 words

Output: Structured article with headers, lists, comparison table.""",

    "sibo": """Write a comprehensive, SEO-optimized article about "Early Symptoms of SIBO (Small Intestinal Bacterial Overgrowth)" for Healthy Gut AI app.

Requirements:
- Title (H1): "Early Symptoms of SIBO and How to Recognize Them"
- Meta description (150-160 chars)
- Introduction (100 words with keyword)
- Sections: What is SIBO, Common symptoms, Risk factors, Diagnosis, Treatment, Diet recommendations
- Include symptom checklist (bulleted)
- Include foods table (safe vs. avoid)
- Add "When to see a doctor" section
- Add "How Healthy Gut AI Helps" section
- Include 5-8 FAQ
- Add 2-3 medical citations
- Medical disclaimer
- Reading level: Grade 7-9
- Word count: 1500-2000 words

Output: Well-organized article with clear structure."""
}

print("\n" + "="*60)
print("HEALTHY GUT AI - SEO ARTICLE GENERATOR")
print("Powered by Google Gemini 2.0 Flash")
print("="*60)

total_words = 0
success_count = 0

for topic, prompt in prompts.items():
    print(f"\n{'='*60}")
    print(f"Generating {topic.upper()} article...")
    print(f"{'='*60}")
    
    try:
        response = model.generate_content(prompt)
        article = response.text
        
        filename = f"{topic}_article.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Topic: {topic.upper()}\n")
            f.write("="*60 + "\n\n")
            f.write(article)
        
        word_count = len(article.split())
        print(f"✅ SUCCESS! {topic.upper()} article generated")
        print(f"   Word count: {word_count}")
        print(f"   Saved to: {filename}")
        
        total_words += word_count
        success_count += 1
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")

print("\n" + "="*60)
print("GENERATION SUMMARY")
print("="*60)
print(f"✅ Articles generated: {success_count}/3")
print(f"✅ Total words: {total_words}")
print("="*60)
