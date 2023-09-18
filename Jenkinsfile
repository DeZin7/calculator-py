pipeline {
  agent any
  triggers {
    pollSCM ('* * * * *')
  }
  stages {
    stage('Checkout') {
      parallel {
        stage('Checkout') {
          steps {
            git(url: 'https://github.com/DeZin7/calculator-py.git', branch: 'master')
          }
        }

        stage('Unit test') {
          steps {
            sh 'python3 test_calculator.py -v'
          }
        }
      }
    }
  }
}