pipeline {
    agent any
    environment {
        PROJEC_NAME = 'yavbot-backend'
        TAGS = 'sistemaagil'
        HOME = '.'
    }
    stages {
        stage('analisis sonar') {
            agent {
                docker {
                    label 'principal'
                    image 'sonar-client-4.5-py3:1.0.2'
                    args '--network=service_net'
                //registryUrl 'https://sonarqube.sistemaagil.net:5000'
                //registryCredentialsId 'admin-registry-pass'
                }
            }
            steps {
                //sh 'python3 -m xmlrunner unit-tests/test_*.py -o ./junit-reports'
                //sh 'coverage run --source=./yavbot -m unittest unit-tests/test_*.py'
                //sh 'coverage xml'
                sh 'pwd'
                sh 'ls'
                //sh '/root/sonar-scanner-4.5.0.2216-linux/bin/sonar-scanner'
            }
        }
    }
}
