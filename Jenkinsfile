

pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
            script {
                def logFilePath = "${WORKSPACE}/output1.txt"

                // Define the combined command with PowerShell redirection for each command
                def combinedCommand = """test.py
                
                """
                combinedCommand = combinedCommand + "extraStep.py > ${logFilePath} 2>&1 " 
                echo combinedCommand
                def filesList = sh(script: 'ls -l', returnStdout: true).trim()
                echo "List of files: \n${filesList}"
                sh(script: combinedCommand)
            }
        }
    }
    stage('Upload database to artifactory'){
            steps{
                echo "Uploaded DB to artifactory"
            }
        }
  }
  post{
        // always cleanup
        always{
            deleteDir()
        }
    }
}
