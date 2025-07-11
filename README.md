# 💅 👔 👠 👞 🦺 Welcome to your own personal "Job" Boutique! 🦺 👞 👠 👔 💅 	

🕴️🕴️🕴️ Let's shake out those Jobbies so the perfect "Job" will fall right into your lap 🫟. When it does, you 🫵 better have on your "Job" clothes! 🕴️🕴️🕴️

## 🚀 Jobbie-Clothes Resume Enhancer

A completely offline Python application that helps you tailor your resume and generate cover letters for specific job postings. This tool uses local natural language processing to optimize your resume for ATS (Applicant Tracking Systems) and create compelling cover letters that make you stand out as the perfect candidate.

### ✨ Features

- **📄 Resume Enhancement**: Automatically tailors your resume to match job descriptions
- **🎯 ATS Optimization**: Includes relevant keywords to trigger AI scanning tools
- **📝 Cover Letter Generation**: Creates personalized cover letters for each position
- **🔍 Keyword Analysis**: Extracts key terms and requirements from job descriptions
- **📁 Multiple File Formats**: Supports PDF, DOCX, and TXT resume uploads
- **💾 Easy Downloads**: Save your enhanced documents with one click
- **🔒 100% Offline**: No API keys required, complete privacy protection
- **⚡ Fast Processing**: Local NLP processing without internet dependency

### 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Jobbie-Clothes
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **First-time setup:**
   - Run the application
   - Click "Download Language Data" in the sidebar (one-time only)
   - You're ready to go - no API keys needed!

### 🎮 Usage

1. **Start the application:**
   ```bash
   python run.py
   ```
   Or manually:
   ```bash
   streamlit run main.py
   ```

2. **Using the app:**
   - Upload your current resume (PDF, DOCX, or TXT)
   - Paste the job description you're applying for
   - Optionally add company name and position title
   - Click "Enhance Resume & Generate Cover Letter"
   - Download your tailored documents

### 🔧 Requirements

- Python 3.8+
- Internet connection (only for initial NLTK data download)

### 📋 Dependencies

- `streamlit` - Web application framework
- `nltk` - Natural language processing
- `scikit-learn` - Machine learning for text analysis
- `numpy` - Numerical computing
- `python-docx` - Microsoft Word document handling
- `PyPDF2` - PDF file processing

### 🎯 How It Works

1. **Upload Analysis**: Extracts text from your resume file
2. **Job Parsing**: Analyzes the job description for key requirements using NLP
3. **Local Enhancement**: Uses machine learning and NLP to rewrite your resume with:
   - Relevant keywords from the job posting
   - Enhanced action verbs
   - Improved keyword density
   - ATS-optimized formatting
4. **Cover Letter Creation**: Generates a personalized cover letter using template-based approach that connects your experience to the job requirements

### 🔒 Privacy & Security

- **100% Offline Processing**: Your documents never leave your computer
- **No API Keys Required**: No external services or accounts needed
- **Complete Privacy**: No data is sent to any server or cloud service
- **Local Storage Only**: All generated content stays on your local machine
- **No Tracking**: No analytics, logging, or data collection

### 💡 Tips for Best Results

- Use a well-formatted, current resume as your base
- Provide complete job descriptions for better keyword matching
- Review and customize the generated content before submitting
- Keep your original resume - this tool creates enhanced versions for specific applications
- Download language data on first run for optimal performance
- Ensure your resume has bullet points for better enhancement

### 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome!

---

**Ready to land your dream job? Let's get you dressed for success - completely offline! 🕴️✨**