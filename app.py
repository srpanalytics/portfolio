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
    }
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
