pipeline {
  agent any

  environment {
    MYSQL_HOST = "10.3.48.245"
    MYSQL_USER = "professor214"
    MYSQL_PASS = "profpass"
    WORK_DIR = "opt/db_class"

  }

  stages {
    stage ('checkout code') {
      steps {
        git branch: 'main', url: 'https://github.com/miamioh-cit/214SQL_automation.git'
      }
    }
    stage('Run student creation script') {
      steps { 
        // SSH into the MySQL server and run the python script
        sh"""
        ssh -o StrictHostKeyChecking=no ubuntu@${MYSQL_HOST} '
            cd ${WORK_DIR} &&
            git pull &&
            python3 create_students_mysql.py
          '
          """
      }
    }
  }
  post {
    sucess {
      echo"✅ Student databases and accounts created successfully!"
        }
        failure {
            echo "❌ Pipeline failed — check MySQL connection or permissions."
        }
    }
}
