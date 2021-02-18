pipeline {
  agent any
  stages {
    stage('Checkout_pull') {
      steps {
        git(url: 'https://github.com/dev2function/PyGame-World-of-Games.git', branch: 'master')
      }
    }

    stage('Build') {
      steps {
        sh 'docker build -t pygame_1 .'
      }
    }

    stage('Run') {
      steps {
        sh 'docker run --rm -it -v .:/code -p 8777:8777 py.game:latest'
      }
    }

    stage('Test') {
      steps {
        sh 'pip3 install selenium'
        sh 'python3 e2e.py'
      }
    }

    stage('Finalize') {
      steps {
        sh 'docker image rm pygame'
      }
    }

  }
}
