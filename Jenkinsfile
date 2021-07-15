#!/usr/bin/env groovy
pipeline {
    agent {
      label 'slave_001'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                bat script: 'start mspaint.exe', returnStatus: true
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    
}
