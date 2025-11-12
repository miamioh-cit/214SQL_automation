pipeline {
  agent any
  environment {
    MYSQL_HOST = "10.3.48.245"
    WORK_DIR = "/opt/db_class"
  }
  stages {
    stage('Checkout code') {
      steps {
        git branch: 'main', url: 'https://github.com/miamioh-cit/214SQL_automation.git'
      }
    }
    stage('Run student creation script') {
      steps {
        withCredentials([
          sshUserPrivateKey(credentialsId: 'SQL VM Creation', keyFileVariable: 'SSH_KEY', usernameVariable: 'SSH_USER'),
          usernamePassword(credentialsId: '214SQL Login', usernameVariable: 'MYSQL_USER', passwordVariable: 'MYSQL_PASS')
        ]) {
          sh """
            ssh -i ${SSH_KEY} -o StrictHostKeyChecking=no ${SSH_USER}@${MYSQL_HOST} '
              cd ${WORK_DIR} &&
              git pull &&
              python3 create_students_mysql.py ${MYSQL_USER} ${MYSQL_PASS}
            '
          """
        }
      }
    }
  }
  post {
    success {
      echo "✅ Student databases and accounts created successfully!"
    }
    failure {
      echo "❌ Pipeline failed — check MySQL connection or permissions."
    }
  }
}
