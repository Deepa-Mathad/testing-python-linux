pipeline {
    agent any

    stages {
        stage('hello') {
            steps {
                script {
                    def logFilePath = "${WORKSPACE}/output1.txt"
                    command = 'python3 test.py > ${logFilePath} 2>&1 '

                    // Print the list of files in the workspace
                    def filesList = sh(script: 'ls -l', returnStdout: true).trim()
                    echo "List of files: \n${filesList}"

                    // Adjust the PATH environment variable
                    withEnv(["PATH=C:/Program Files/Python310/python.exe:${env.PATH}"]) {
                        // Now, the 'python' executable should be found in the modified PATH
                        sh(script: 'python3 --version')

                        // Specify the full path to the 'test.py' script
                        sh(script: command)
                    }
                    echo "Log File Path: ${logFilePath}"
                    def fullOutput = readFile(file: logFilePath)
                    echo "Full Output:\n${fullOutput}"
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


// pipeline {
//     agent any
//     stages {
//         stage('hello') {
//             steps {
//                 script {
//                     def logFilePath = "${WORKSPACE}/output1.txt"

//                     // Define the combined command with PowerShell redirection for each command
//                     // def combinedCommand = """python test.py 
//                     // """

//                     // echo "Running command: \n${combinedCommand}"

//                     def pythonVersion = sh(script: 'python --version', returnStdout: true, returnStatus: true)

//                     if (pythonVersion == 0) {
//                         echo "Python is installed. Version: ${sh(script: 'python --version', returnStdout: true).trim()}"
//                     } else {
//                         error "Python is not installed on this machine."
//                     }
                    
//                     // Print the list of files in the workspace
//                     def filesList = sh(script: 'ls -l', returnStdout: true).trim()
//                     echo "List of files: \n${filesList}"

//                     // Run the combined command
//                     sh(script: 'python test.py')
//                 }
//             }
//         }

//         stage('Upload database to artifactory') {
//             steps {
//                 echo "Uploaded DB to artifactory"
//             }
//         }
//     }

//     post {
//         // always cleanup
//         always {
//             deleteDir()
//         }
//     }
// }
