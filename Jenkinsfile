import groovy.json.JsonSlurperClassic
def jsonParse(def json) {
    new groovy.json.JsonSlurperClassic().parseText(json)
}
pipeline {
    agent any
    stages {
        stage("Paso 1: Probar JUnit"){
            steps {
                script {
                sh "echo 'Ejecutar pruebas de Junit'"
               // sh "mvn test"
                }
            }
        }    
        stage("Paso 2: Probar con Newman"){
            steps {
                script {
                sh "echo 'Ejecutar pruebas de Postman'"
                sh "newman run postman_collection.json"
                }
            }
        }    
    }
    post {
        always {
            sh "echo 'fase always executed post'"
        }
        success {
            sh "echo 'fase success'"
        }
        failure {
            sh "echo 'fase failure'"
        }
    }
}


