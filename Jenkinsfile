pipeline {
    agent any
    
    stages{
        stage('Clone')
        {
            steps{
             git branch: 'main', credentialsId: 'newtoken', url: 'https://github.com/Rupali1520/ProjectKUP.git'
            }
        }
        stage('Build'){
            steps{
                sh 'pip install Django==3.2'
            }
        }
//         stage('test'){
//             steps{
//                 script{
//                     sh 'python manage.py test'
//                 }
//             }
//         }
        
//         stage('create docker image')
//         {
//             steps{
//                 script{
//                     // sh 'cat Dockerfile'
//                     // sh 'pwd'
//                     // sh 'ls'
//                     // sh 'docker image'
//                     // sh 'sudo usermod -aG docker jenkins'
//                     sh 'sudo docker build -t rupali1520/image:${BUILD_NUMBER} .'
//                     // sh 'sudo docker run -dp 8000:8000 image:env=${env.BUILD_NUMBER}'
//                     // sh 'sudo docker ps'
//                 }
//             }
//         }
//         stage('push image on docker hub'){
//             steps{
//                 script{
//                   withCredentials([string(credentialsId: 'dockerhubpwd', variable: 'dockerhubpwd')]) {
//     //some block

//                       sh 'sudo docker login -u rupali1520 -p ${dockerhubpwd}'
//                       sh 'sudo docker push rupali1520/image:${BUILD_NUMBER}'
//                   }
//                 }
//             }
//         }
//         stage('deploy'){
//             steps{
//                 sh 'chmod u+x changeTag.sh'
//                 sh './changeTag.sh ${BUILD_NUMBER}'
//                 withCredentials([file(credentialsId: 'k82', variable: 'kubernetesvar')]) {
//     // some block  yyy
//               sh 'kubectl --kubeconfig=$kubernetesvar --validate=false apply -f service.yaml'
//               sh 'kubectl --kubeconfig=$kubernetesvar --validate=false apply -f node-app-pod.yaml'
             
//               sh 'kubectl --kubeconfig=$kubernetesvar get all -o wide'
//              // sh 'kubectl --kubeconfig=$kubernetesvar describe pod/mydeploy-5fdc9df568-l9ng5' 
            
// }
//             }
//         }
        //jii
       
        
    }
}
