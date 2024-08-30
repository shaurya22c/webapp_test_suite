pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install selenium pytest pytest-html fastapi uvicorn'
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
                sh 'pytest --html=reports/report.html'
            }
        }
        stage('Publish Report') {
            steps {
                publishHTML([reportName: 'Test Report', reportDir: 'reports', reportFiles: 'report.html', keepAll: true])
            }
        }
    }
}
