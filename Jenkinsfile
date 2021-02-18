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
        sh 'docker build -t my_image .'
      }
    }

    stage('Run') {
      steps {
        sh 'docker-compose up'
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
        sh 'docker image rm my_image'
      }
    }

  }
}
