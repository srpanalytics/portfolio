from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

projects = [
    {
        'id': 'pr1',
        'name': 'ML SaaS Dashboard',
        'short': 'End-to-end SaaS for business metric prediction, embed AI in workflow.',
        'details': 'Built a cloud-native dashboard for business metric forecasting using Python/Flask backend, React frontend, and deployed ML models for live predictions. Enabled role-based analytics and report scheduling.',
        'img': 'images/project1.png',
        'tags': ['AI', 'ML', 'Analytics', 'Python', 'Flask'],
        'demo': 'https://example.com/demo1',
        'code': 'https://github.com/example/ml-saas'
    },
    {
        'id': 'pr2',
        'name': 'Churn Prediction API',
        'short': 'Deployable Python API for real-time customer churn prediction.',
        'details': 'Created and containerized predictive ML model pipeline and Flask REST API, integrated with business CRM to automate retention campaigns and A/B testing.',
        'img': 'images/project2.png',
        'tags': ['ML', 'API', 'Python', 'Flask'],
        'demo': '',
        'code': 'https://github.com/example/churn-api'
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
