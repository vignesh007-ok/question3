pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Stage: Checkout - Pulling source code...'
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Unit Check') {
                    steps {
                        sh 'python3 unit_check.py'
                    }
                }
                stage('Integration Check') {
                    steps {
                        sh 'python3 integration_check.py'
                    }
                }
            }
        stage('Summary') {
            steps {
                echo 'Stage: Summary - Compiling results...'
            }
        }
    }

    post {
        success {
            echo 'POST: Pipeline completed successfully!'
        }
        failure {
            echo 'POST: Pipeline execution failed!'
        }
    }
}
