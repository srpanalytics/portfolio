from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

projects = [
    {
        'id': 'pr1',
        'name': 'flyseer.ai',
        'short': 'ML-powered app to predict airline booking completion behavior.',
        'details': 'Built a full-stack Flask web application to predict booking completion based on user behavior inputs. Integrated trained machine learning models (Random Forest, Logistic Regression, Gradient Boosting) with a modular backend and a clean, responsive front-end UI. Includes preprocessing pipeline and form logic to match model input structure. Deployed using Render.',
        'img': 'images/project_bookease.png',
        'tags': ['Flask', 'Python', 'Machine Learning', 'Deployment', 'UI/UX'],
        'demo': 'https://flyseekerai.onrender.com/',
        'code': 'https://github.com/srpanalytics/bookingp'
    },
    {
        'id': 'pr2',
        'name': 'Plotly Dashboard',
        'short': 'Interactive dashboard to monitor and analyze SAP ticket performance.',
        'details': 'Developed a Dash-based web dashboard for IT Service Management at Shyam Metalics and Energy Ltd. Visualizes key SAP ticket metrics like TAT, ticket age, department-level trends, and status distribution. Integrated real-time filtering by department, date, and location. The app uses Plotly for interactive charts and a clean, dark-themed UI for stakeholder reporting and decision support.',
        'img': 'images/project_itsm.png',  
        'tags': ['Dash', 'Plotly', 'Python', 'Analytics', 'Dashboard'],
        'demo': 'https://your-itsm-app-link.com',  
        'code': 'https://github.com/yourusername/itsm-dashboard'
    },
    {
        'id': 'pr3',
        'name': 'SMART-PARCHI (Automated Logbook System)',
        'short': 'Designed with a user-friendly interface, it makes record-keeping faster, easier, and more reliable.', 
        'details': 'Smartparchi is a simple, secure, and cloud-based logbook automation tool. It lets you fill forms online with minimal input and access your data anytime, from anywhere. Designed with a user-friendly interface, it makes record-keeping faster, easier, and more reliable.',
        'img': 'images/smartparchi.png',
        'tags': ['Requirement gathering', 'Change management', 'Data analysis', 'Communication', 'BRD,FRD,PRD and SRS documentation', 'Stakeholder management'],
        'demo': 'https://smartparchi-qas.shyamgroup.com/home',
        'code': 'https://github.com/srpanalytics'
    },
    {
        'id': 'pr4',
        'name': 'Quality Inspection application for Manufacturing',
        'short': 'Streamline and centralize the management of quality inspection data for raw materials.',
        'details': 'QAINSP is a web-based application designed for Shyam Metalics & Energy Ltd. to streamline and centralize the management of quality inspection data for raw materials. The primary objective of this document is to define the business requirements of QAINSP, ensuring alignment with organizational goals and quality assurance standards. By integrating inspection results from different stages of the supply chain, the application enhances accuracy, efficiency, and accessibility of quality inspection data, ultimately improving decision-making and operational effectiveness. The purpose of this document is to outline the business requirements for the QAINSP application. It serves as a bridge between stakeholders and the development team, ensuring that all requirements align with business goals and user needs. ',
        'img': 'images/qainsp.png',
        'tags': ['Requirement gathering', 'Change management', 'Data analysis', 'Communication', 'BRD,FRD,PRD and SRS documentation'],
        'demo': 'http://192.168.96.19:3030/login',
        'code': 'https://github.com/srpanalytics'
    },
    {
        'id': 'pr5',
        'name': 'NutriGoAI',
        'short': 'AI-powered nutrition analysis for Indian foods.',
        'details': 'Built an AI-powered nutrition recommendation system trained on 500+ Indian foods from IFCT 2017 dataset. Implemented data preprocessing, exploratory data analysis, and machine learning models to provide nutritional insights and healthier food alternatives. Designed an interactive web app for real-time food analysis and visualization. ',
        'img': 'images/project_nutrigoai.png',
        'tags': ["Machine Learning", "Python", "EDA", "Nutrition Analysis", "Flask"],
        'demo': 'https://nutrigoai.onrender.com',
        'code': 'https://github.com/srpanalytics'
    },
    {
        
        "id": "pr6",
        "name": "Bhoomitales",
        "short": "Platform to explore hidden places, flavors, and cultures of India.",
        "details": "Built a storytelling and discovery platform showcasing India’s hidden destinations, local cuisines, and cultural experiences. Integrated background video animations, dynamic UI, and responsive design to create an immersive browsing experience for users.",
        "img": "images/project_bhoomitales.png",
        "tags": ["Travel", "Culture", "Web Development", "Frontend"],
        "demo": "https://bhoomitalesapp.onrender.com/",
        "code": "https://github.com/srpanalytics/bhoomitales"
        

    },
    # {
    #     'id': 'pr7',
    #     'name': 'Bank Transaction EDA',
    #     'short': 'Exploratory analysis of banking transaction data using Python.',
    #     'details': 'Used Pandas, NumPy, and Matplotlib to analyze transaction patterns, customer behavior, and fraud indicators. Provided descriptive and inferential insights to support financial decision-making.',
    #     'img': 'images/project_bankeda.png',
    #     'tags': ['Python', 'EDA', 'Finance', 'Data Cleaning', 'Matplotlib'],
    #     'demo': 'https://your-banking-eda-demo.com',
    #     'code': 'https://github.com/yourusername/bank-transaction-eda'
    # },
    # {
    #     'id': 'pr8',
    #     'name': 'Kaizen Suggestion Tracker',
    #     'short': 'Tool to track continuous improvement ideas in factory units.',
    #     'details': 'Developed a Kaizen tracker dashboard to analyze suggestion categories, implementation rate, and plant-wise performance. Automated data refresh using Excel + Power BI integration for plant leadership reviews.',
    #     'img': 'images/project_kaizen.png',
    #     'tags': ['Kaizen', 'Excel', 'Power BI', 'Lean', 'Improvement'],
    #     'demo': 'https://your-kaizen-tracker.com',
    #     'code': 'https://github.com/yourusername/kaizen-tracker'
    # },
    # {
    #     'id': 'pr9',
    #     'name': 'Vendor Onboarding Tracker',
    #     'short': 'Dashboard to streamline and monitor vendor onboarding process.',
    #     'details': 'Automated and visualized vendor onboarding steps using a dashboard integrated with Zoho CRM. Enabled weekly status reviews with metrics on onboarding speed, documentation, and compliance gaps.',
    #     'img': 'images/project_vendor.png',
    #     'tags': ['CRM', 'Zoho', 'Automation', 'Vendor Management'],
    #     'demo': 'https://your-vendor-dashboard-demo.com',
    #     'code': 'https://github.com/yourusername/vendor-onboarding'
    # },
    # {
    #     'id': 'pr10',
    #     'name': 'Marketing Analytics Report',
    #     'short': 'Social media engagement and campaign analytics.',
    #     'details': 'Collected and analyzed performance data of campaigns run for tribal artisans via SWA Odisha. Used engagement metrics and growth trends to optimize social content and build targeted outreach.',
    #     'img': 'images/project_marketing.png',
    #     'tags': ['Social Media', 'Marketing', 'Analytics', 'Campaigns'],
    #     'demo': 'https://your-marketing-analytics.com',
    #     'code': 'https://github.com/yourusername/social-marketing-report'
    # },
    # {
    #     'id': 'pr11',
    #     'name': 'Production KPI Dashboard',
    #     'short': 'Live dashboard for production performance tracking.',
    #     'details': 'Created live dashboards in Excel and Power BI for KPIs like output vs plan, delay causes, and equipment effectiveness. Used plant data to analyze furnace availability, TAT, and spillage trends.',
    #     'img': 'images/project_kpi.png',
    #     'tags': ['Production', 'OEE', 'Excel', 'Power BI', 'KPI'],
    #     'demo': 'https://your-production-kpi.com',
    #     'code': 'https://github.com/yourusername/production-kpi-dashboard'
    # },
    # {
    #     'id': 'pr12',
    #     'name': 'Regression Forecasting Model',
    #     'short': 'Forecasted production trends using regression models.',
    #     'details': 'Used past plant performance data to build regression models for output forecasting. Applied sklearn’s Linear and Ridge regression techniques and visualized results in Jupyter Notebook.',
    #     'img': 'images/project_regression.png',
    #     'tags': ['Regression', 'Sklearn', 'Python', 'Forecasting'],
    #     'demo': 'https://your-forecasting-model.com',
    #     'code': 'https://github.com/yourusername/regression-forecasting'
    # }
]


skills = [
    {'category': 'Data & Analysis', 'skills': ['Pandas', 'NumPy', 'OpenPyXL', 'Matplotlib', 'Seaborn', 'Plotly', 'Scikit-learn', 'Sweetviz']},
    {'category': 'AI/ML', 'skills': ['Python', 'scikit-learn', 'TensorFlow', 'NLP' ,'PyTorch', 'pandas', 'NumPy','Hugging Face Transformers']},
    {'category': 'Dev & APIs', 'skills': ['Flask', 'REST', 'Docker', 'Postman', 'HTML5', 'CSS3']},
    {'category': 'Soft Skills', 'skills': ['Agile/Scrum', 'Stakeholder Management', 'Process Mapping', 'Requirement Gathering', 'Data-Driven Decision Making', 'Root Cause Analysis', 'Cross-Functional Collaboration', 'Change Management']
}
]

@app.route('/')
def index():
    return render_template("index.html",
                           name="SOUMYA RANJAN PATRA",
                           title="Business Analyst & AI/ML Developer",
                           description="Building data-driven, intelligent business solutions.",
                           projects=projects,
                           skills=skills)

@app.route('/contact', methods=['POST'])
def contact():
    # This simply redirects for this demo; implement email sending as needed.
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)







# if __name__ == '__main__':
#     app.run(debug=True)
