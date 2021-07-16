#!/usr/bin/env groovy
pipeline {
    agent {
      label 'slave_'
    }
    
    parameters {
        string(name: 'auto_test_path', defaultValue: 'D:\\jiangqin\\SVN\\27-auto_test', description: 'auto_test路径')
        string(name: 'auto_test_path', defaultValue: 'D:\\jiangqin\\SVN\\27-auto_test', description: 'auto_test路径')
    }
    
    def compile_ret = 0
    def test_ret = 0
    def cmd = ''

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                cmd = "python ${auto_test_path}\\python_project\\compile_and_load.py"
                compile_ret = bat script: cmd, returnStatus: true
                println "exec $cmd result: $compile_ret"
            }
        }
        
        stage('Test') {
            steps {
                if (compile_ret != 0) {
                    echo 'compile error, exit test...'
                }
                else {
                    echo 'Testing...'
                    cmd = '${auto_test_path}\\python_project\\testcase\\run_all.py'
                    test_ret = bat script: cmd, returnStatus: true
                    println "exec $cmd result: $test_ret"
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
