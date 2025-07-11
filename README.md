# 💅 👔 👠 👞 🦺 Welcome to your own personal "Job" Boutique! 🦺 👞 👠 👔 💅 	

🕴️🕴️🕴️ Let's shake out those Jobbies so the perfect "Job" will fall right into your lap 🫟. When it does, you 🫵 better have on your "Job" clothes! 🕴️🕴️🕴️

## 🚀 Jobbie-Clothes Resume Enhancer

An AI-powered Python application that helps you tailor your resume and generate cover letters for specific job postings. This tool uses advanced AI to optimize your resume for ATS (Applicant Tracking Systems) and create compelling cover letters that make you stand out as the perfect candidate.

### ✨ Features

- **📄 Resume Enhancement**: Automatically tailors your resume to match job descriptions
- **🎯 ATS Optimization**: Includes relevant keywords to trigger AI scanning tools
- **📝 Cover Letter Generation**: Creates personalized cover letters for each position
- **🔍 Keyword Analysis**: Extracts key terms and requirements from job descriptions
- **📁 Multiple File Formats**: Supports PDF, DOCX, and TXT resume uploads
- **💾 Easy Downloads**: Save your enhanced documents with one click

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

3. **Get a Claude API key:**
   - Visit https://console.anthropic.com/
   - Create a new API key
   - Keep it secure - you'll enter it in the app

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
   - Enter your Claude API key in the sidebar
   - Upload your current resume (PDF, DOCX, or TXT)
   - Paste the job description you're applying for
   - Optionally add company name and position title
   - Click "Enhance Resume & Generate Cover Letter"
   - Download your tailored documents

### 🔧 Requirements

- Python 3.8+
- Claude API key (Anthropic account with credits)
- Internet connection

### 📋 Dependencies

- `streamlit` - Web application framework
- `anthropic` - Claude API client
- `python-docx` - Microsoft Word document handling
- `PyPDF2` - PDF file processing

### 🎯 How It Works

1. **Upload Analysis**: Extracts text from your resume file
2. **Job Parsing**: Analyzes the job description for key requirements
3. **AI Enhancement**: Uses Claude to rewrite your resume with:
   - Relevant keywords from the job posting
   - Quantified achievements
   - Industry-specific terminology
   - ATS-optimized formatting
4. **Cover Letter Creation**: Generates a personalized cover letter that connects your experience to the job requirements

### 🔒 Privacy & Security

- Your documents are processed locally and sent only to Anthropic's Claude API
- No data is stored permanently by the application
- Use your own Claude API key for complete control
- All generated content is downloaded to your local machine

### 💡 Tips for Best Results

- Use a well-formatted, current resume as your base
- Provide complete job descriptions for better matching
- Review and customize the generated content before submitting
- Keep your original resume - this tool creates enhanced versions for specific applications

### 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome!

---

**Ready to land your dream job? Let's get you dressed for success! 🕴️✨**