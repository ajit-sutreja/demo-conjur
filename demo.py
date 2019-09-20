import os
print("----------------------------------------------------------------------")
print("proof of concept - don't echo or print secrets in real life :)")
print("Jenkins API Key: " + os.environ['JENKINS_API_KEY'])
print("----------------------------------------------------------------------")
