pipeline {
    agent any

    stages {
        stage('hello') {
            steps {
                script {
                    def logFilePath = "${WORKSPACE}/output1.txt"

                    // Define the combined command with PowerShell redirection for each command
                    def combinedCommand = """python test.py
                    python extraStep.py > ${logFilePath} 2>&1
                    """

                    echo "Running command: \n${combinedCommand}"

                    // Print the list of files in the workspace
                    def filesList = sh(script: 'ls -l', returnStdout: true).trim()
                    echo "List of files: \n${filesList}"

                    // Run the combined command
                    sh(script: combinedCommand)
                }
            }
        }

        stage('Upload database to artifactory') {
            steps {
                echo "Uploaded DB to artifactory"
            }
        }
    }

    post {
        // always cleanup
        always {
            deleteDir()
        }
    }
}
