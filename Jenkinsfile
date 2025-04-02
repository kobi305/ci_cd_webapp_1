pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo "🔄 Pulling code from GitHub..."
                cleanWs() // Clean workspace before checkout.
                checkout scm // Use checkout scm for reliable checkout.
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 Installing dependencies..."
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App (Smoke Test)') {
            steps {
                echo "🚀 Running Flask app..."
                sh 'nohup python app/main.py &'
                sh 'sleep 5'
                sh 'curl http://localhost:5000'
            }
        }
    }
}