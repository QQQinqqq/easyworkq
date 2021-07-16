parameters {
        string(name: 'auto_test_path', defaultValue: 'D:\\jiangqin\\SVN\\27-auto_test', description: 'auto_test路径')
        }

node {
    stage('Build') {
        echo 'Building....'
    }
    stage('Test') {
        echo 'Testing....${params.auto_test_path}'
    }
    stage('Deploy') {
        echo 'Deploying....'
    }
}
