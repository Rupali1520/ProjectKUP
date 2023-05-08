pipeline {
    agent any
    
    stages{
        stage('Clone')
        {
            steps{
              git branch: '', credentialsId: '009dc801-8b4a-4aac-92d4-2401d42d76c4', url: 'https://github.com/Rupali1520/ProjectKUP.git'
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
