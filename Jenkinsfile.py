pipeline {
    agent any

    stages {
        // Stage 1: Checkout
        stage('Checkout') {
            steps {
                echo 'Stage: Checkout - Pulling source code...'
                // Code is automatically checked out if using a Pipeline from SCM
            }
        }

        // Stage 2: Parallel Checks
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
        }

        // Stage 3: Summary
        stage('Summary') {
            steps {
                echo 'Stage: Summary - Compiling results...'
            }
        }
    }

    // Post-execution blocks
    post {
        success {
            echo 'POST: Pipeline completed successfully!'
        }
        failure {
            echo 'POST: Pipeline execution failed!'
        }
    }
}
