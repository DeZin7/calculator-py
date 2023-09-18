pipeline {
  agent any
  stages {
    stage('error') {
      parallel {
        stage('error') {
          steps {
            git(url: 'https://github.com/DeZin7/calculator-py.git', branch: 'master')
          }
        }

        stage('Unit test') {
          steps {
            sh 'python test_calculator.py -v'
          }
        }

      }
    }

  }
}