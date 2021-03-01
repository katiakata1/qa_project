pipeline {
    agent any 
    stages{
        stage('AppTesting'){
            steps{
                sh './scripts/apptesting.sh'
            }
        }
        stage('Ansible'){
            steps{
                sh './scripts/ansible.sh'
            }
        }
        stage('Build'){
            steps{
                sh './scripts/appbuild.sh'
            }
        }
        stage('Deploy'){
            steps{
                sh './scripts/appdeploy.sh'
            }
        }                   
        stage('NGINX'){
            steps{
                sh './scripts/nginx.sh'
            }
        }
    }
}