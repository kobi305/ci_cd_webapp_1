pipeline {
    agent {
        docker {
            image 'python:3.11'
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo "🔄 מושך קוד מ-GitHub..."
                cleanWs() // ניקוי ה-Workspace לפני ה-checkout
                checkout scm // שימוש ב-checkout scm לביצוע ה-checkout
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "📦 מתקין תלויות..."
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Flask App (Smoke Test)') {
            steps {
                echo "🚀 מריץ את אפליקציית ה-Flask..."
                sh 'nohup python app/main.py &'
                sh 'sleep 5'
                sh 'curl http://localhost:5000'
            }
        }
    }
}
