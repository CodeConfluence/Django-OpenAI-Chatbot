# 🤖 SocialBrain 💬

## 🌟 Introduction
Welcome to the SocialBrain.ai Chatbot Platform repository! 🚀 This project allows users to create custom AI-powered chatbots that interact with users based on pre-defined instructions and knowledge bases. The platform offers a seamless and intuitive interface for managing chatbots, enabling both personal and public usage scenarios.

## 💡 Project Features
- **Custom AI Agents:** 🧠 Create and configure AI chatbots with user-defined instructions and knowledge base files.
- **User Authentication:** 🔑 Secure login functionality for creating and managing personal agents.
- **File Upload for Resources:** 📂 Upload custom files to train agents with specific knowledge.
- **Interactive Chat Interface:** 💬 Engage with chatbots in a dynamic user interface.
- **Agent Selection:** 🕹️ Choose between personal and public agents for different use cases.
- **AI Content Generation:** ⚙️ Use Google Vertex AI for generating intelligent responses based on knowledge base files.
  
## 🛠️ Technologies
- **Django:** 🖥️ Backend framework powering the platform’s core functionality and authentication system.
- **Google Vertex AI:** 🤖 Leverages Google’s AI capabilities to enable intelligent content generation for agents.
- **HTML/CSS/JavaScript:** 🌐 Frontend stack for building interactive pages and chat interfaces.
- **Bootstrap:** 🎨 Provides responsive and sleek design components.
- **SQLite/PostgreSQL:** 🛢️ Database for managing users, agents, and their resources.

## 🚀 Quick Start
**Clone the repository and navigate to the project folder**
```
git clone https://github.com/yourusername/Django-OpenAI-Chatbot.git
cd my_chatbot
```
**Install Python**
```
brew install python
```
**Install pip**
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```
**Create a Virtual Environment**
```
python3 -m venv venv
```
**Activate Virtual Environment**
```
source venv/bin/activate
```
**Install Django**
```
pip install django
```
**Install `python-decouple`**
```
pip install python-decouple
```
**Install `google-generativeai` Library**
```
pip install google-generativeai
```
**Install Pillow**
```
pip install Pillow
```
**Generate the `requirements.txt` File**
```
pip freeze > requirements.txt
```
**Install dependencies**
```
pip install -r requirements.txt
```
**Run migrations**
```
python manage.py migrate
```
**Start the development server**
```
python manage.py runserver
```
**Open** http://localhost:8000 in your web browser to view the platform.**

## 📁 Directory Structure
- `views.py` - Contains all views for managing agents, user authentication, and chatbot interactions.
- `models.py` - Defines the database models for agents, resources, and user profiles.
- `forms.py` - Handles the forms for creating and updating agents and uploading resources.
- `templates/` - Contains all HTML templates for rendering the frontend pages.
- `static/` - Holds the static files, including CSS, JavaScript, and images for the platform.

## 📝 Usage
- Create an account to start managing your custom AI agents.
- Upload knowledge base files in PDF format to enhance your chatbot’s responses.
- Configure chatbot instructions for guiding how the chatbot interacts with users.
- Generate intelligent responses by interacting with your chatbots in real-time.

## 📬 Contact
Have any questions or suggestions? Feel free to reach out via email at [zhangbri@umich.edu](mailto:zhangbri@umich.edu) and [snrkis@umich.edu](mailto:snrkis@umich.edu) or connect with us on [LinkedIn](https://www.linkedin.com/in/zhangbri/), [LinkedIn](https://www.linkedin.com/in/kristan-seenath-nagassar-922720290?), and [LinkedIn](https://www.linkedin.com/in/jesus-garcia-b57261310/). I'm open to discussions, collaborations, and feedback.
