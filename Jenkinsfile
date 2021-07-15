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
                bat script: 'call D:\jiangqin\SVN\27-auto_test\run.bat', returnStatus: true
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
    
}
