pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install selenium pytest pytest-html fastapi uvicorn'
            }
        }
        stage('Run FastAPI App') {
            steps {
                sh 'nohup uvicorn main:app --reload &'
                sleep 5  // Wait for the server to start
            }
        }
        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest'
            }
        }
    }
}
