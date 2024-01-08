pipeline {
    agent any
    
    environment {
        // Define the Python tool name as configured in Jenkins
        pythonTool = 'Python3'
    }
    stages {
        stage('Install Python') {
            steps {
                script {
                    // Install Python using the 'tool' step
                    def pythonHome = tool name: "${pythonTool}", type: 'hudson.plugins.python.PythonInstallation'

                    // Add the Python executable to the PATH
                    env.PATH = "${pythonHome}/bin:${env.PATH}"
                }
            }
        }
        stage('Check Python Version') {
            steps {
                script {
                    // Verify that Python is installed
                    sh 'python --version'
                }
            }
        }
        stage('hello') {
            steps {
                script {
                    def logFilePath = "${WORKSPACE}/output1.txt"

                    // Define the combined command with PowerShell redirection for each command
                    // def combinedCommand = """python test.py 
                    // """

                    // echo "Running command: \n${combinedCommand}"

                    def pythonVersion = sh(script: 'python --version', returnStdout: true, returnStatus: true)

                    if (pythonVersion == 0) {
                        echo "Python is installed. Version: ${sh(script: 'python --version', returnStdout: true).trim()}"
                    } else {
                        error "Python is not installed on this machine."
                    }
                    
                    // Print the list of files in the workspace
                    def filesList = sh(script: 'ls -l', returnStdout: true).trim()
                    echo "List of files: \n${filesList}"

                    // Run the combined command
                    sh(script: 'python test.py')
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
