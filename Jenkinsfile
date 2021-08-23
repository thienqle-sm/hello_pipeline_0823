pipeline {
 agent any
  
  stages {
    stage("build"){
      steps {
        echo 'building the application...'
        bat """
            python -m venv env
            cmd /c "env\\Scripts\\activate.bat"
            python -m pip install -r requirement.txt
            python manage.py collectstatic --noinput
            cmd /c "env\\Scripts\\deactivate.bat"
        """
      }
    }
    
    stage("test"){
      steps {
        echo 'testing the application...'
        bat """
            cmd /c "env\\Scripts\\activate.bat"
            python manage.py test
            cmd /c "env\\Scripts\\deactivate.bat"
        """
      }
    }
    
    stage("deploy"){
      steps {
        echo 'deploying the application...'
        bat """
            copy * G:\\Demo\\SERVER_HOSTING
            xcopy hello_project G:\\Demo\\SERVER_HOSTING\\hello_project\\ /y /S /E
            xcopy static G:\\Demo\\SERVER_HOSTING\\static\\ /y /S /E
        """
      }
    }
    
  }
}
