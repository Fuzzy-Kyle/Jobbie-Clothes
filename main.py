#!/usr/bin/env python3
"""
Jobbie-Clothes Resume Enhancer
A Python application to tailor resumes and generate cover letters for specific job postings.
"""

import streamlit as st
import anthropic
from pathlib import Path
import docx
import PyPDF2
from io import BytesIO
import re
import os
from datetime import datetime

class ResumeEnhancer:
    def __init__(self):
        self.anthropic_api_key = None
        self.client = None
        
    def setup_claude(self, api_key):
        """Setup Claude API client"""
        self.anthropic_api_key = api_key
        self.client = anthropic.Anthropic(api_key=api_key)
        
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
            
    def extract_keywords_from_job_description(self, job_description):
        """Extract key skills and requirements from job description"""
        prompt = f"""
        Analyze this job description and extract:
        1. Required skills and technologies
        2. Key qualifications
        3. Important buzzwords that ATS systems would scan for
        4. Industry-specific terminology
        
        Job Description:
        {job_description}
        
        Return the results in a structured format with categories.
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=1000,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            st.error(f"Error analyzing job description: {str(e)}")
            return None
            
    def enhance_resume(self, resume_text, job_description):
        """Enhance resume to match job description"""
        prompt = f"""
        You are an expert resume writer and ATS optimization specialist. Your task is to enhance the following resume to be perfectly tailored for the job description provided. 

        CRITICAL REQUIREMENTS:
        1. Optimize for ATS (Applicant Tracking Systems) by including exact keyword matches from the job description
        2. Rewrite bullet points to emphasize relevant experience and achievements
        3. Quantify achievements wherever possible
        4. Use action verbs that match the job requirements
        5. Include industry-specific terminology from the job description
        6. Ensure the resume will trigger AI scanning tools to flag this candidate as a perfect match
        7. Maintain honesty - enhance and reframe existing experience, don't fabricate
        8. Use keywords naturally throughout the resume
        
        Job Description:
        {job_description}
        
        Current Resume:
        {resume_text}
        
        Return an enhanced resume that will score highly with ATS systems and make hiring managers see this candidate as the perfect fit. Focus on keyword optimization while maintaining readability and professionalism.
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=2000,
                temperature=0.4,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            st.error(f"Error enhancing resume: {str(e)}")
            return None
            
    def generate_cover_letter(self, resume_text, job_description, company_name="", position_title=""):
        """Generate a tailored cover letter"""
        prompt = f"""
        Write a compelling cover letter that perfectly matches the candidate's background to the job requirements. 

        REQUIREMENTS:
        1. Make it clear why this candidate is the perfect fit
        2. Use specific examples from the resume that align with job requirements
        3. Include keywords from the job description naturally
        4. Show enthusiasm and knowledge about the role
        5. Keep it professional but engaging
        6. Highlight unique value proposition
        7. Make it ATS-friendly with relevant keywords
        
        Company: {company_name if company_name else "the company"}
        Position: {position_title if position_title else "this position"}
        
        Job Description:
        {job_description}
        
        Candidate's Resume:
        {resume_text}
        
        Write a cover letter that will make the hiring manager excited to interview this candidate.
        """
        
        try:
            response = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1500,
                temperature=0.5,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            st.error(f"Error generating cover letter: {str(e)}")
            return None

def main():
    st.set_page_config(
        page_title="💅 Jobbie-Clothes Resume Enhancer 👔",
        page_icon="🦺",
        layout="wide"
    )
    
    st.title("💅 👔 👠 👞 🦺 Jobbie-Clothes Resume Enhancer 🦺 👞 👠 👔 💅")
    st.subheader("🕴️ Let's tailor your resume to land that perfect job! 🕴️")
    
    enhancer = ResumeEnhancer()
    
    # Sidebar for API key
    with st.sidebar:
        st.header("⚙️ Configuration")
        api_key = st.text_input("Claude API Key", type="password", help="Enter your Anthropic Claude API key")
        if api_key:
            enhancer.setup_claude(api_key)
            st.success("✅ Claude API Key configured!")
        else:
            st.warning("⚠️ Please enter your Claude API key to continue")
    
    if not api_key:
        st.error("🔑 Please enter your Claude API key in the sidebar to use this application.")
        st.info("💡 You can get an API key from: https://console.anthropic.com/")
        return
    
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
            
        with st.spinner("🔄 Analyzing job description and enhancing your resume..."):
            # Extract keywords
            keywords = enhancer.extract_keywords_from_job_description(job_description)
            
            # Enhance resume
            enhanced_resume = enhancer.enhance_resume(resume_text, job_description)
            
            # Generate cover letter
            cover_letter = enhancer.generate_cover_letter(
                resume_text, job_description, company_name, position_title
            )
        
        # Display results
        if enhanced_resume and cover_letter:
            st.success("✅ Documents generated successfully!")
            
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
                if keywords:
                    st.text_area("Keywords and Requirements", keywords, height=300)
                else:
                    st.error("Could not analyze keywords from job description.")
        else:
            st.error("❌ Failed to generate enhanced documents. Please check your API key and try again.")

if __name__ == "__main__":
    main()