#!/usr/bin/env groovy
pipeline {
    agent {
      label 'slave_'
    }
    
    parameters {
        string(name: 'auto_test_path', defaultValue: 'D:\\jiangqin\\SVN\\27-auto_test', description: 'auto_test路径')
        string(name: 'compile_ret', defaultValue: '1', description: '返回结果变量定义')
        string(name: 'test_ret', defaultValue: '1', description: '返回结果变量定义')
        string(name: 'cmd', defaultValue: ' ', description: '命令变量定义')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                params.cmd = "python ${params.auto_test_path}\\python_project\\compile_and_load.py"
                params.compile_ret = bat script: params.cmd, returnStatus: true
                println "exec ${params.cmd} result: ${params.compile_ret}"
            }
        }
        
        stage('Test') {
            steps {
                if (compile_ret != 0) {
                    echo 'compile error, exit test...'
                }
                else {
                    echo 'Testing...'
                    params.cmd = '${params.auto_test_path}\\python_project\\testcase\\run_all.py'
                    params.test_ret = bat script: params.cmd, returnStatus: true
                    println "exec ${params.cmd} result: ${params.test_ret}"
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
