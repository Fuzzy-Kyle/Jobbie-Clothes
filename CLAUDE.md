# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Jobbie-Clothes is a completely offline Python application that helps users tailor their resumes and generate cover letters for specific job postings. The application uses local natural language processing and machine learning to optimize resumes for ATS (Applicant Tracking Systems) and create compelling, personalized cover letters.

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
- NLTK (natural language processing)
- scikit-learn (machine learning for text analysis)
- numpy (numerical computing)
- python-docx (Word document handling)
- PyPDF2 (PDF processing)

## Architecture

### Core Components

1. **main.py**: Primary Streamlit application with:
   - `ResumeEnhancer` class: Core functionality for resume processing
   - File upload handling (PDF, DOCX, TXT)
   - Local NLP processing methods
   - Text extraction and enhancement algorithms

2. **run.py**: Application launcher script for easy startup

3. **setup.py**: Package configuration for distribution

### Key Features

- **Resume Enhancement**: Local NLP-powered resume tailoring using job description analysis
- **ATS Optimization**: Keyword matching and formatting for applicant tracking systems
- **Cover Letter Generation**: Template-based personalized cover letters
- **Multi-format Support**: Handles PDF, DOCX, and TXT file uploads
- **Keyword Analysis**: Extracts key terms from job descriptions using NLTK
- **Complete Offline Operation**: No API keys or internet required after setup

### Local Processing Architecture

The application uses local machine learning and NLP libraries:
- **NLTK**: For tokenization, stopword removal, and text preprocessing
- **scikit-learn**: For TF-IDF vectorization and text similarity analysis
- **Custom algorithms**: For keyword matching and resume enhancement
- **Template-based generation**: For cover letter creation with dynamic content

### Security Considerations

- **100% Offline**: No external API calls after initial NLTK data download
- **Complete Privacy**: No data leaves the user's machine
- **No API Keys**: No external accounts or services required
- **Local Storage Only**: All processing and storage happens locally