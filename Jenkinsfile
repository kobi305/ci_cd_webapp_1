pipeline {
    agent any

    environment {
        IMAGE_NAME = "yourdockerhubusername/my-flask-app"
        DOCKER_CREDENTIALS_ID = "docker-hub-creds"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/yourname/yourrepo.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                pip install -r requirements.txt
                pip install pytest selenium
                '''
            }
        }

        stage('Run Flask App (Background)') {
            steps {
                sh 'nohup python app/main.py &'
                // נותן זמן לשרת לעלות
                sh 'sleep 5'
            }
        }

        stage('Run API Tests') {
            steps {
                sh 'pytest tests/test_api.py'
            }
        }

        stage('Run UI Tests (Selenium)') {
            steps {
                sh 'pytest tests/test_ui.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry(credentialsId: "${DOCKER_CREDENTIALS_ID}") {
                    script {
                        docker.image("${IMAGE_NAME}:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                sshagent(['your-ssh-key-id']) {
                    sh '''
                    ssh user@your-server "
                        docker pull yourdockerhubusername/my-flask-app:${BUILD_NUMBER} &&
                        docker stop flask-app || true &&
                        docker rm flask-app || true &&
                        docker run -d --name flask-app -p 80:5000 yourdockerhubusername/my-flask-app:${BUILD_NUMBER}
                    "
                    '''
                }
            }
        }
    }
}
