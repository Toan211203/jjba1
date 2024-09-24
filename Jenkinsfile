pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                git 'https://github.com/Toan211203/emo2_jenkin.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                // Thêm lệnh build ở đây, ví dụ: sh 'make'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Thêm lệnh test ở đây, ví dụ: sh 'make test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Thêm lệnh deploy ở đây, ví dụ: sh 'make deploy'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
        always {
            echo 'Cleaning up...'
            // Thêm lệnh dọn dẹp nếu cần, ví dụ: cleanWs()
        }
    }
}
