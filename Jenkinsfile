def auto_test_path = "D:\\jiangqin\\SVN\\27-auto_test"
def cmd = " "
def compile_ret = '1'
def test_ret = '1'

node {
    stage('Build') {
        println "Building...."
        cmd = "python ${auto_test_path}\\python_project\\compile_and_load.py"
        compile_ret = bat script: cmd, returnStatus: true
        println "exec ${cmd} result: ${compile_ret}"
    }
    stage('Test') {
        if (compile_ret != 0) {
        println "compile error, exit test..."
        }
        else {
            println "Testing...."
            cmd = "python ${auto_test_path}\\python_project\\testcase\\run_all.py"
            test_ret = bat script: cmd, returnStatus: true
            println "exec ${cmd} result: ${test_ret}"
        }
    }
    stage('Deploy') {
        if (compile_ret != 0 || test_ret != 0) {
            println "compile or test error, exit deploy..."
        }
        else {
            println "Deploying...."
        }
    }
}
