def auto_test_path = "D:\\jiangqin\\SVN\\27-auto_test"
def cmd = " "
def compile_ret = '1'
def test_ret = '1'

node {
    stage('Build') {
        println "Building...."
        def cmd = "python ${auto_test_path}\\python_project\\compile_and_load.py"
        def compile_ret = bat script: cmd, returnStatus: true
        println "exec ${cmd} result: ${compile_ret}"
    }
    stage('Test') {
        if (compile_ret != '0') {
        println "compile error, exit test..."
        }
        else {
            println "Testing...."
        }
    }
    stage('Deploy') {
        println "Deploying...."
    }
}
