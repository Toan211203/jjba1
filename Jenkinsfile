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
                sh 'python hello.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                script {
                    // Kiểm tra xem file hello.py có tồn tại không
                    if (fileExists('hello.py')) {
                        echo 'File hello.py found. Running the script...'
                        def output = sh(script: 'python hello.py', returnStdout: true).trim()
                        echo "Output: ${output}"
                    } else {
                        error 'File hello.py does not exist!'
                    }
                }
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
