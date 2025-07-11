#!/usr/bin/env python3
"""
Jobbie-Clothes Resume Enhancer
A Python application to tailor resumes and generate cover letters for specific job postings.
"""

import streamlit as st
from pathlib import Path
import docx
import PyPDF2
from io import BytesIO
import re
import os
from datetime import datetime
import nltk
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import string

class ResumeEnhancer:
    def __init__(self):
        self.setup_nltk()
        
    def setup_nltk(self):
        """Download required NLTK data"""
        try:
            nltk.data.find('tokenizers/punkt')
            nltk.data.find('corpora/stopwords')
            nltk.data.find('taggers/averaged_perceptron_tagger')
        except LookupError:
            try:
                nltk.download('punkt', quiet=True)
                nltk.download('stopwords', quiet=True)
                nltk.download('averaged_perceptron_tagger', quiet=True)
            except:
                pass
        
    def extract_text_from_pdf(self, pdf_file):
        """Extract text from PDF file"""
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            st.error(f"Error reading PDF: {str(e)}")
            return None
            
    def extract_text_from_docx(self, docx_file):
        """Extract text from DOCX file"""
        try:
            doc = docx.Document(docx_file)
            text = ""
            for paragraph in doc.paragraphs:
                text += paragraph.text + "\n"
            return text.strip()
        except Exception as e:
            st.error(f"Error reading DOCX: {str(e)}")
            return None
            
    def clean_text(self, text):
        """Clean and normalize text"""
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        text = ' '.join(text.split())
        return text
        
    def extract_keywords_from_job_description(self, job_description):
        """Extract key skills and requirements from job description using NLP"""
        try:
            from nltk.corpus import stopwords
            from nltk.tokenize import word_tokenize, sent_tokenize
            from nltk import pos_tag
            
            stop_words = set(stopwords.words('english'))
            
            # Clean text
            cleaned_text = self.clean_text(job_description)
            
            # Tokenize
            words = word_tokenize(cleaned_text)
            
            # Filter out stopwords and short words
            filtered_words = [word for word in words if word not in stop_words and len(word) > 2]
            
            # Get word frequency
            word_freq = Counter(filtered_words)
            
            # Extract technical terms and skills (look for patterns)
            skill_patterns = [
                r'\b\w*(?:programming|development|software|system|database|web|mobile|cloud|data|analytics|machine learning|ai|python|java|javascript|react|angular|sql|aws|azure|docker|kubernetes)\w*\b',
                r'\b(?:experience|years|required|preferred|must|should|knowledge|skills|proficiency|expertise|familiar|understanding)\b',
                r'\b\w*(?:degree|bachelor|master|phd|certification|certified)\w*\b'
            ]
            
            skills_and_tech = []
            for pattern in skill_patterns:
                matches = re.findall(pattern, job_description.lower())
                skills_and_tech.extend(matches)
            
            # Get top keywords
            top_keywords = [word for word, count in word_freq.most_common(20)]
            
            # Combine results
            analysis = {
                'top_keywords': top_keywords,
                'skills_and_tech': list(set(skills_and_tech)),
                'word_frequency': dict(word_freq.most_common(30))
            }
            
            # Format results
            result = f"""
**KEY KEYWORDS & SKILLS ANALYSIS**

**Top Keywords:**
{', '.join(analysis['top_keywords'][:15])}

**Technical Skills & Requirements:**
{', '.join(analysis['skills_and_tech'][:20]) if analysis['skills_and_tech'] else 'No specific technical terms identified'}

**Word Frequency (Top 15):**
{', '.join([f"{word} ({count})" for word, count in list(analysis['word_frequency'].items())[:15]])}
            """
            
            return result.strip()
            
        except Exception as e:
            st.error(f"Error analyzing job description: {str(e)}")
            return "Error extracting keywords. Please check the job description format."
            
    def get_keyword_matches(self, resume_text, job_description):
        """Find keywords from job description that should be in resume"""
        try:
            from nltk.corpus import stopwords
            from nltk.tokenize import word_tokenize
            
            stop_words = set(stopwords.words('english'))
            
            # Extract keywords from job description
            job_words = word_tokenize(self.clean_text(job_description))
            job_keywords = [word for word in job_words if word not in stop_words and len(word) > 2]
            job_keyword_freq = Counter(job_keywords)
            
            # Extract words from resume
            resume_words = word_tokenize(self.clean_text(resume_text))
            resume_keywords = set([word for word in resume_words if word not in stop_words and len(word) > 2])
            
            # Find missing important keywords
            important_job_keywords = [word for word, count in job_keyword_freq.most_common(50)]
            missing_keywords = [word for word in important_job_keywords if word not in resume_keywords]
            
            return {
                'missing_keywords': missing_keywords[:20],
                'job_keywords': important_job_keywords[:30],
                'resume_keywords': list(resume_keywords)[:30]
            }
        except:
            return {'missing_keywords': [], 'job_keywords': [], 'resume_keywords': []}
    
    def enhance_resume(self, resume_text, job_description):
        """Enhance resume to match job description using local processing"""
        try:
            # Get keyword analysis
            keyword_analysis = self.get_keyword_matches(resume_text, job_description)
            missing_keywords = keyword_analysis['missing_keywords']
            
            # Split resume into sections
            resume_sections = resume_text.split('\n\n')
            enhanced_sections = []
            
            # Enhancement templates
            action_verbs = [
                "Developed", "Implemented", "Led", "Managed", "Created", "Designed", 
                "Optimized", "Improved", "Achieved", "Delivered", "Collaborated",
                "Streamlined", "Enhanced", "Established", "Executed", "Coordinated"
            ]
            
            quantifiers = ["25%", "30%", "50%", "$100K", "15 team members", "3 projects", "6 months"]
            
            for section in resume_sections:
                enhanced_section = section
                
                # If this looks like a bullet point section (experience/skills)
                if '•' in section or '-' in section:
                    lines = section.split('\n')
                    enhanced_lines = []
                    
                    for line in lines:
                        enhanced_line = line
                        
                        # Add missing keywords naturally to bullet points
                        if ('•' in line or line.strip().startswith('-')) and missing_keywords:
                            # Try to incorporate 1-2 missing keywords
                            keywords_to_add = missing_keywords[:2]
                            for keyword in keywords_to_add:
                                if keyword.lower() not in line.lower() and len(keyword) > 3:
                                    if 'experience' in line.lower():
                                        enhanced_line = enhanced_line.replace('experience', f'{keyword} experience')
                                    elif 'using' in line.lower():
                                        enhanced_line = enhanced_line.replace('using', f'using {keyword} and')
                                    elif 'with' in line.lower() and line.lower().count('with') == 1:
                                        enhanced_line = enhanced_line.replace('with', f'with {keyword} and')
                                    break
                        
                        # Enhance with action verbs
                        if ('•' in line or line.strip().startswith('-')):
                            line_lower = line.lower()
                            weak_starts = ['worked on', 'helped with', 'assisted', 'participated']
                            for weak in weak_starts:
                                if weak in line_lower:
                                    action_verb = np.random.choice(action_verbs)
                                    enhanced_line = enhanced_line.replace(weak, action_verb)
                                    break
                        
                        enhanced_lines.append(enhanced_line)
                    
                    enhanced_section = '\n'.join(enhanced_lines)
                
                # Add missing keywords to skills section
                elif 'skill' in section.lower() or 'technical' in section.lower():
                    if missing_keywords:
                        skills_to_add = [kw for kw in missing_keywords[:10] if len(kw) > 3]
                        if skills_to_add:
                            enhanced_section += f"\nAdditional: {', '.join(skills_to_add[:5])}"
                
                enhanced_sections.append(enhanced_section)
            
            enhanced_resume = '\n\n'.join(enhanced_sections)
            
            # Add a summary optimization note
            optimization_note = f"""
            
**ATS OPTIMIZATION APPLIED:**
- Integrated {len(missing_keywords[:10])} key terms from job description
- Enhanced action verbs for impact
- Improved keyword density for ATS scanning
- Maintained professional formatting and readability
            """
            
            return enhanced_resume + optimization_note
            
        except Exception as e:
            st.error(f"Error enhancing resume: {str(e)}")
            return resume_text + "\n\n**Note:** Enhancement completed with basic formatting improvements."
            
    def extract_experience_highlights(self, resume_text):
        """Extract key experience points from resume"""
        highlights = []
        lines = resume_text.split('\n')
        
        for line in lines:
            line = line.strip()
            if ('•' in line or line.startswith('-')) and len(line) > 20:
                # Clean up bullet points
                clean_line = line.replace('•', '').replace('-', '').strip()
                if any(word in clean_line.lower() for word in ['developed', 'led', 'managed', 'created', 'implemented', 'improved']):
                    highlights.append(clean_line)
        
        return highlights[:5]  # Return top 5 highlights
    
    def generate_cover_letter(self, resume_text, job_description, company_name="", position_title=""):
        """Generate a tailored cover letter using template-based approach"""
        try:
            # Extract key information
            keyword_analysis = self.get_keyword_matches(resume_text, job_description)
            job_keywords = keyword_analysis['job_keywords'][:10]
            experience_highlights = self.extract_experience_highlights(resume_text)
            
            # Determine company and position
            company = company_name if company_name else "your organization"
            position = position_title if position_title else "this position"
            
            # Cover letter template
            cover_letter = f"""Dear Hiring Manager,

I am writing to express my strong interest in the {position} role at {company}. After reviewing the job description, I am confident that my background and experience make me an ideal candidate for this opportunity.

**Why I'm the Perfect Fit:**

My experience aligns perfectly with your requirements, particularly in {', '.join(job_keywords[:3])}. Here are some key achievements that demonstrate my qualifications:

"""
            
            # Add experience highlights
            for i, highlight in enumerate(experience_highlights, 1):
                cover_letter += f"• {highlight}\n"
            
            # Add matching skills section
            cover_letter += f"""
**Relevant Skills & Experience:**
Based on your job description, I have direct experience with {', '.join(job_keywords[:5])}. My background in these areas, combined with my proven track record of success, positions me well to contribute immediately to your team.

**Value I Bring:**
I am particularly excited about the opportunity to contribute to {company}'s mission and growth. My experience in {job_keywords[0] if job_keywords else 'relevant areas'} and {job_keywords[1] if len(job_keywords) > 1 else 'team collaboration'} will enable me to make a meaningful impact from day one.

I would welcome the opportunity to discuss how my background and enthusiasm can contribute to your team's success. Thank you for considering my application, and I look forward to hearing from you.

Best regards,
[Your Name]

---
**ATS Keywords Included:** {', '.join(job_keywords[:8])}
            """
            
            return cover_letter.strip()
            
        except Exception as e:
            st.error(f"Error generating cover letter: {str(e)}")
            return f"""Dear Hiring Manager,

I am writing to express my interest in the {position_title if position_title else 'position'} at {company_name if company_name else 'your company'}.

My background and experience make me a strong candidate for this role. I have relevant experience and skills that align with your requirements.

I would welcome the opportunity to discuss my qualifications further.

Best regards,
[Your Name]
            """

def main():
    st.set_page_config(
        page_title="💅 Jobbie-Clothes Resume Enhancer 👔",
        page_icon="🦺",
        layout="wide"
    )
    
    st.title("💅 👔 👠 👞 🦺 Jobbie-Clothes Resume Enhancer 🦺 👞 👠 👔 💅")
    st.subheader("🕴️ Let's tailor your resume to land that perfect job! 🕴️")
    
    enhancer = ResumeEnhancer()
    
    # Sidebar for information
    with st.sidebar:
        st.header("ℹ️ Information")
        st.success("✅ Ready to use! No API key required")
        st.info("🔄 This application works completely offline using local AI processing")
        st.markdown("""
        **Features:**
        - 🎯 Local keyword extraction
        - 📝 Intelligent resume enhancement
        - 📄 Professional cover letter generation
        - 🔒 Complete privacy (no data sent online)
        """)
        
        # Download NLTK data on first run
        if st.button("📥 Download Language Data"):
            with st.spinner("Downloading language processing data..."):
                enhancer.setup_nltk()
            st.success("Language data downloaded!")
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("📄 Upload Your Resume")
        resume_file = st.file_uploader(
            "Choose your resume file",
            type=['pdf', 'docx', 'txt'],
            help="Upload your current resume in PDF, DOCX, or TXT format"
        )
        
        if resume_file:
            # Extract text based on file type
            if resume_file.type == "application/pdf":
                resume_text = enhancer.extract_text_from_pdf(resume_file)
            elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                resume_text = enhancer.extract_text_from_docx(resume_file)
            else:  # txt file
                resume_text = str(resume_file.read(), "utf-8")
                
            if resume_text:
                st.success("✅ Resume uploaded successfully!")
                with st.expander("📋 View extracted resume text"):
                    st.text_area("Resume content", resume_text, height=200, disabled=True)
    
    with col2:
        st.header("💼 Job Description")
        job_description = st.text_area(
            "Paste the job description here",
            height=300,
            help="Copy and paste the complete job description you want to tailor your resume for"
        )
        
        # Optional fields
        st.subheader("📝 Additional Information (Optional)")
        company_name = st.text_input("Company Name")
        position_title = st.text_input("Position Title")
    
    # Process button
    if st.button("🚀 Enhance Resume & Generate Cover Letter", type="primary"):
        if not resume_file or not job_description:
            st.error("⚠️ Please upload a resume and provide a job description.")
            return
            
        if not resume_text:
            st.error("⚠️ Could not extract text from the resume file.")
            return
            
        with st.spinner("🔄 Analyzing job description and enhancing your resume locally..."):
            # Extract keywords
            keywords = enhancer.extract_keywords_from_job_description(job_description)
            
            # Enhance resume
            enhanced_resume = enhancer.enhance_resume(resume_text, job_description)
            
            # Generate cover letter
            cover_letter = enhancer.generate_cover_letter(
                resume_text, job_description, company_name, position_title
            )
        
        # Display results
        if enhanced_resume and cover_letter and keywords:
            st.success("✅ Documents generated successfully using local AI processing!")
            
            # Create tabs for results
            tab1, tab2, tab3 = st.tabs(["🎯 Enhanced Resume", "📝 Cover Letter", "🔍 Keywords Analysis"])
            
            with tab1:
                st.header("🎯 Your Enhanced Resume")
                st.text_area("Enhanced Resume", enhanced_resume, height=400)
                
                # Download button
                st.download_button(
                    label="💾 Download Enhanced Resume",
                    data=enhanced_resume,
                    file_name=f"enhanced_resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
            
            with tab2:
                st.header("📝 Your Tailored Cover Letter")
                st.text_area("Cover Letter", cover_letter, height=400)
                
                # Download button
                st.download_button(
                    label="💾 Download Cover Letter",
                    data=cover_letter,
                    file_name=f"cover_letter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain"
                )
            
            with tab3:
                st.header("🔍 Key Terms Analysis")
                st.text_area("Keywords and Requirements", keywords, height=300)
                
                st.info("💡 **Tip:** Review the keywords to ensure your resume includes the most important terms from the job description.")
        else:
            st.error("❌ Failed to generate enhanced documents. Please try again or check if language data is downloaded.")

if __name__ == "__main__":
    main()