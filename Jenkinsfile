

def containsSubstringWithoutBOM(content, substring) {
    return content.replaceAll("\\uFEFF", "").contains(substring)
}

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
                    echo "Log File Path: ${logFilePath}"
                    def fullOutput = readFile(file: logFilePath)
                    echo "Full Output:\n${fullOutput}"
                    def fullOutput1 = readFile(file: logFilePath, encoding: 'UTF-16').trim()
                    echo "Full Output 1:\n${fullOutput1}"
                    if(fullOutput1.contains("KeyError:"))
                    {
                      echo "passed"
                    }
                    else
                    {
                      echo "failes"
                    }
                    echo "Full Output 2:\n${fullOutput2}"
                    if (containsSubstringWithoutBOM(fullOutput2, "printing extra step"))
                    {
                      echo "full output 2 passed"
                    }
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
