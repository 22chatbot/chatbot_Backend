pipeline {
    agent any
    environment {
        PROJEC_NAME = "yavbot-backend"
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
                sh 'python3 -m xmlrunner unit-tests/test_*.py -o ./junit-reports'
                sh 'coverage run --source=./yavbot -m unittest unit-tests/test_*.py'
                sh 'coverage xml'
                sh '/root/sonar-scanner-4.5.0.2216-linux/bin/sonar-scanner'
            }
        }

        stage("Respuesta Sonar"){
            agent {
                docker {
                    label 'integracion'
                    image 'jq:latest'
                    args '--network=service_net'
                }
            }
            environment {
                SONAR_CREDENTIALS = credentials('sonar-admin')
            }
            steps{
                script {
                    estatus = sh(
                        script: 'curl -u $SONAR_CREDENTIALS_USR:$SONAR_CREDENTIALS_PSW -s http://sonarqube:9000/api/qualitygates/project_status?projectKey=${PROJEC_NAME} | jq .projectStatus.status',
                        returnStdout: true
                    ).trim().toUpperCase().replaceAll("[\n\r]", "")
                    if (estatus == '"ERROR"'){
                        throw new Exception("No supera los estandares de calidad..")

                    }
                    if (estatus.isEmpty()){
                        throw new Exception("Not OK status isEmpty, please check sonarqube report")
                    }
                }
            }
        }

        stage("Despliegue"){
            agent {
                label 'integracion'
            }
            steps{
                sh 'docker build -f devops/Dockerfile -t yavbot-backend:latest .'
                sh 'docker stack rm yavbot'
                sh 'docker stack deploy -c devops/stack.yml yavbot'
            }
        }

    }
}