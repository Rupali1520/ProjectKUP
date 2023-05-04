pipeline {
    agent any
    
    stages{
        stage('Clone')
        {
            steps{
                git branch: 'main', credentialsId: '4d2afe5d-f0d8-486e-bd33-f537b15a34a0', url: 'https://github.com/Rupali1520/ProjectKUP.git'
            }
        }
        stage('Build'){
            steps{
                sh 'pip install Django==3.2'
            }
        }
        stage('test'){
            steps{
                script{
                    sh 'python manage.py test'
                }
            }
        }
        stage('create artifact'){
            steps{
                script{
                    sh 'tar -cvzf artifact.tar.gz ParkTicketManagement'}
            }
        }
        
        
    }
}
