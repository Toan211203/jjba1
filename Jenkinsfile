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
                sh 'python3 hello.py'  // Sử dụng python3
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                script {
                    if (fileExists('hello.py')) {
                        echo 'File hello.py found. Running the script...'
                        def output = sh(script: 'python3 hello.py', returnStdout: true).trim()
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
                // Thêm lệnh deploy ở đây
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
            // Thêm lệnh dọn dẹp nếu cần
        }
    }
}
