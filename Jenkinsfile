#!/usr/bin/env groovy
pipeline {
    agent {
      label 'slave_'
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
