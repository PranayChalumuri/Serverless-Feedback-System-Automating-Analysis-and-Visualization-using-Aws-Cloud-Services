# 📊 Health App Feedback & Sentiment Analysis Dashboard

A real-time feedback collection system for health applications with AI-powered sentiment analysis and interactive visualizations.

<p align="center">
  <a href="https://qqainv8x5m.execute-api.ap-south-1.amazonaws.com/dev/">
    <img src="https://img.shields.io/badge/LIVE-DEMO-brightgreen?style=for-the-badge&logo=aws" alt="Live Demo"/>
  </a>
</p>

---

## 🎯 **Project Overview**

A fully serverless web application that collects user feedback for health applications, performs real-time sentiment analysis using AWS AI services, and displays interactive visualizations through a dynamic dashboard.

---

## 🖼️ **Screenshots**

### 📝 User Feedback Interface
*Clean, modern form for collecting user feedback*

![User Interface](./screenshots/User_Interface.png)

### 📱 App Selection Page
*Select specific health apps for detailed analysis*

![App Selection](./screenshots/App_Selection.png)

### 📊 Real-Time Dashboard
*Interactive charts showing sentiment distribution*

![Real-Time Dashboard](./screenshots/Real_Time_Dashboard.png)

### ✅ Thank You Response
*Confirmation page after feedback submission*

![Thank You Response](./screenshots/Thankyou_response.png)

---

## 🚀 **Live Demo**

Experience the application in action:

👉 **[Launch Live Application](https://qqainv8x5m.execute-api.ap-south-1.amazonaws.com/dev/)**

| Step | Action |
|------|--------|
| 1️⃣ | Submit feedback for any health app |
| 2️⃣ | Click "Live Feedback Chart" button |
| 3️⃣ | Select an app from the list |
| 4️⃣ | Watch real-time sentiment visualizations |

---

## ✨ **Key Features**

### 📝 **Feedback Collection**
- User-friendly form with app selection dropdown
- Support for **12+ health applications**
- Email validation and required field checks
- Real-time submission processing

### 🤖 **AI Sentiment Analysis**
- **AWS Comprehend** analyzes feedback text
- Detects: `POSITIVE`, `NEGATIVE`, `MIXED`, `NEUTRAL`
- Instant processing upon form submission
- 95%+ accuracy in sentiment detection

### 📈 **Interactive Dashboard**

| Chart Type | Purpose |
|------------|---------|
| 📊 **Stacked Bar Chart** | Sentiment distribution by app |
| 🥧 **Pie Chart** | Overall sentiment ratio |
| 📋 **Grouped Bar Chart** | Side-by-side sentiment comparison |
| 🍩 **Donut Chart** | Sentiment percentage visualization |

### 🎨 **Modern UI/UX**
- Gradient backgrounds and smooth animations
- Mobile-responsive design
- Real-time updates every 5 seconds
- Professional typography with Inter font

---

## 🏗️ **Architecture**

```ascii
┌─────────┐                    ┌─────────┐                    ┌─────────┐
│ FEEDBACK│───────POST────────▶│   API   │────invoke─────────▶│ LAMBDA  │
│  FORM   │                    │ GATEWAY │                    │         │
└─────────┘                    └─────────┘                    └────┬────┘
                                                                    │
                                          ┌─────────────────────────┼─────────────────────────┐
                                          ▼                         ▼                         ▼
                                   ┌─────────────┐          ┌─────────────┐          ┌─────────────┐
                                   │ COMPREHEND  │          │  DYNAMODB   │          │   THANK YOU │
                                   │ Sentiment   │◄────────│   STORAGE   │─────────▶│    PAGE     │
                                   │  Analysis   │          │             │          │ lasting.html│
                                   └─────────────┘          └──────┬──────┘          └─────────────┘
                                                                    │
                                                                    ▼
                                                              ┌─────────────┐
                                                              │  APPSYNC    │
                                                              │  GraphQL    │
                                                              └──────┬──────┘
                                                                    │
                                                                    ▼
                                                              ┌─────────────┐
                                                              │  DASHBOARD  │
                                                              │   CHARTS    │
                                                              │ success.html│
                                                              └─────────────┘
```
🛠️ Technology Stack
Frontend
Technology	Purpose
HTML5/CSS3	Structure and styling
JavaScript	Client-side logic
Tailwind CSS	UI framework
Google Charts	Data visualization
Inter Font	Typography
Backend (AWS Serverless)
Service	Purpose
API Gateway	REST API endpoints
Lambda	Business logic (Python 3.9)
DynamoDB	NoSQL database
AppSync	GraphQL API for real-time data
Comprehend	AI sentiment analysis


📁 Project Structure
text
📦 health-app-feedback
├── 📄 lambda_function.py      # Main Lambda function (Python)
├── 📄 contactus.html          # Feedback submission form
├── 📄 app_selection.html      # App selector page
├── 📄 success.html            # Dashboard with charts
├── 📄 lasting.html            # Thank you page
├── 📁 screenshots/            # Project images
└── 📄 README.md               # Project documentation


🔄 Data Flow
User Submits Feedback

User fills form → API Gateway POST → Lambda
Lambda calls Comprehend for sentiment analysis
Data stored in DynamoDB
User redirected to thank you page
Dashboard Displays Data

User selects app → Dashboard loads
Dashboard calls AppSync directly every 5 seconds
AppSync queries DynamoDB for latest data
Google Charts render visualizations
KPI cards update in real-time

🌐 API Endpoints
Endpoint                  |	Method |	Purpose |	Response            |
/dev/	                    |GET	   |Serve     |feedback form	HTML
/dev/?page=app_selection	|GET	   |Serve     |app selector	HTML
/dev/dashboard?app={name}	|GET	   |Serve     |dashboard	HTML
/dev/	                    |POST	   |Submit    |feedback	Redirect

📈 Performance Metrics
Metric	       |          Value
API Response Time	  --->    ~100-200ms
Dashboard           --->  Updates	Every 5 seconds
Concurrent Users	  --->  Scales automatically
Data Storage	      --->  Unlimited (DynamoDB)
Cold Start	        ---> ~500ms (first request)

🔒 Security Features
✅ API Gateway as secure entry point

✅ AppSync API Key authentication

✅ Lambda IAM roles with least privilege

✅ CORS enabled for browser access

✅ Input validation on form submissions
---------------------------------
🚀 Future Enhancements
Cognito authentication for secure dashboard access

Email notifications for critical feedback

Export data to CSV/Excel

Date range filtering on dashboard

Word cloud visualization of common terms

Multi-language support

Mobile app integration

PDF report generation
----------------------------------
👏 Acknowledgments
AWS for serverless services

Google Charts for visualization library

Tailwind CSS for styling framework

All contributors who helped test and improve

📞 Contact
Phone: +91 7093274782

Email: chalumuripranaykumar@gmail.com

GitHub Issues: Open an issue in this repository


