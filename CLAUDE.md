# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Jobbie-Clothes is an AI-powered Python application that helps users tailor their resumes and generate cover letters for specific job postings. The application uses OpenAI's GPT models to optimize resumes for ATS (Applicant Tracking Systems) and create compelling, personalized cover letters.

## Development Commands

### Setup and Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
# or manually:
streamlit run main.py
```

### Dependencies
- Python 3.8+
- Streamlit (web framework)
- Anthropic Claude API (for AI processing)
- python-docx (Word document handling)
- PyPDF2 (PDF processing)

## Architecture

### Core Components

1. **main.py**: Primary Streamlit application with:
   - `ResumeEnhancer` class: Core functionality for resume processing
   - File upload handling (PDF, DOCX, TXT)
   - Claude API integration
   - Text extraction and processing methods

2. **run.py**: Application launcher script for easy startup

3. **setup.py**: Package configuration for distribution

### Key Features

- **Resume Enhancement**: AI-powered resume tailoring using job description analysis
- **ATS Optimization**: Keyword matching and formatting for applicant tracking systems
- **Cover Letter Generation**: Personalized cover letters based on resume and job requirements
- **Multi-format Support**: Handles PDF, DOCX, and TXT file uploads
- **Keyword Analysis**: Extracts key terms from job descriptions

### AI Integration

The application uses Anthropic's Claude models for:
- Job description analysis and keyword extraction (Claude-3-Haiku for speed)
- Resume content enhancement and optimization (Claude-3-Sonnet for quality)
- Cover letter generation with role-specific customization (Claude-3-Sonnet)

### Security Considerations

- Users provide their own Claude API keys
- No permanent data storage
- Local processing with API calls only for AI enhancement
- Documents processed temporarily during session only