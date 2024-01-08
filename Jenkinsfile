

def dsau() {
  try {
    command = """python test.py
                  python extraStep.py
    """
    
    // Print the command (optional)
    echo "Running command: ${command}"

    // Execute the command and capture the return value
    try{
      // def combinedCommand = "${command} 2>&1"
      def returnValue = sh(returnStderr: true, script: command)
      echo "returnValue: ${returnValue}"
      //def stderr = sh(script: combinedCommand, returnStatus: true)
      // return returnValue
      
   } catch (Exception e) {
      echo "Cause: ${e}"
      return e
    }

    // def returnValue1 = sh(script: 'python test.py', returnStatus: true, returnStdout: true)
    // if(returnValue1 != 0){
    //   echo "Return Value: ${returnValue1}"
    //   return returnValue1
    // }
    // else{
    //   def returnValue2 = sh(script: 'python extraStep.py', returnStatus: true, returnStdout: true)
    // }

    // Print the return value
   // echo "Return Value: ${returnValue}"

    // Return the value
  }
  catch (e)
    {
        // println("Failed in running DSAU", e)
        error("Exceptions with ${e}")
        return e
    }
}

def containsSubstringWithoutBOM(content, substring) {
    return content.replaceAll("\\uFEFF", "").contains(substring)
}

pipeline {
  agent any
  stages {
    stage('hello') {
      steps {
                script {
                    // Define log file paths
                    def logFilePath1 = "${WORKSPACE}/output1.txt"
                    def logFilePath2 = "${WORKSPACE}/output2.txt"
                    def pythonExecutable = "C:\\Program Files\\Python310\\python.exe"

                    // Define the combined command with PowerShell redirection for each command
                    def combinedCommand = """
                         & '${pythonExecutable}' test.py > ${logFilePath1} 2>&1
                         & '${pythonExecutable}' extraStep.py > ${logFilePath2} 2>&1
                    """

                    // Run the combined command and capture the output using PowerShell
                    powershell(script: combinedCommand)

                    // Print the log file paths
                    echo "Log File Path 1: ${logFilePath1}"
                    echo "Log File Path 2: ${logFilePath2}"

                    // Read the full content of the log files
                    def fullOutput1 = readFile(file: logFilePath1, encoding: 'UTF-8')
                    // def content = readFile(file: 'logFilePath1')
                    // echo "content: ${content}"
                    def fullOutput2 = readFile(file: logFilePath2)

                    // Print the full output
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
