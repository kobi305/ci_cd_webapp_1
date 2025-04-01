pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "🔄 Pulling code from GitHub..."
                git branch: 'main', url: 'https://github.com/kobi305/ci_cd_webapp_1.git'
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
