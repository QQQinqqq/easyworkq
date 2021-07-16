#!/usr/bin/env groovy
def running_node = '1'
pipeline {
    agent {
      label 'slave_'
    }
    
    parameters {
        string(name: 'auto_test_path', defaultValue: 'D:\\jiangqin\\SVN\\27-auto_test', description: 'auto_test路径')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                def cmd = "python ${params.auto_test_path}\\python_project\\compile_and_load.py"
                def compile_ret = bat script: cmd, returnStatus: true
                println "exec ${cmd} result: ${compile_ret}"
                if (compile_ret != '0') {
                    running_node = '0'
                }
            }
        }
        
        stage('Test') {
            steps {
                if (running_node != '1') {
                    echo 'compile error, exit test...'
                }
                else {
                    echo 'Testing...'
                    def cmd = '${params.auto_test_path}\\python_project\\testcase\\run_all.py'
                    def test_ret = bat script: cmd, returnStatus: true
                    println "exec ${cmd} result: ${test_ret}"
                }
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
    
}
