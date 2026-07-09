## Study:

- Why deployment is important
- What is Render?
- What is WSGI?
- Difference between Local Development and Production
- What are Build Commands and Start Commands?
- Importance of "requirements.txt" and "Procfile" (optional)

## Answer the following in your notes:

- What was the biggest challenge during deployment?
- Why should every backend developer know deployment?
- What would happen if environment variables were missing?
- How does deployment improve your portfolio?

## "notes.md" should contain:

- What is Render?
- What is Gunicorn?
- What is WhiteNoise?
- Development vs Production.
- Importance of deploying backend applications.

1. Why deployment is important
   Deployment is the process of making an application available on the internet so users can access it. It allows developers to share their projects, test them in real-world conditions, and use them in production.

2. What is Render?
   Render is a cloud hosting platform that allows developers to deploy web applications, APIs, databases, and static websites. It automates deployment from GitHub and provides SSL, custom domains, and continuous deployment.

3. What is WSGI? (Web Server Gateway Interface)
   WSGI (Web Server Gateway Interface) is a standard interface between Python web applications (such as Django) and web servers. It enables servers like Gunicorn to communicate with Django applications in production.

4. Difference between Local Development and Production
##    Local Development  	              Production
      Runs on a personal computer	      Runs on a cloud server
      Used for testing and development	  Used by real users
      Debug mode enabled	              Debug mode disabled
      Local database	                  Production database
      Less secure	                      Highly secure and optimized

5. What are Build Commands and Start Commands?
   Build Command: Installs dependencies and prepares the application for deployment.
   Example:
    pip install -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py migrate

   Start Command: Starts the application server.
   Example:
    gunicorn backend_journey.wsgi

6. Importance of requirements.txt and Procfile
##  requirements.txt
   - Lists all Python packages required by the project.
   - Ensures the server installs the correct dependencies.
   - Makes the project reproducible on any machine.

##  Procfile
   - Tells the hosting platform how to start the application.
   - Defines the command used to launch the web server.
   - Common example:
      web: gunicorn backend_journey.wsgi

7. What was the biggest challenge during deployment?
   The biggest challenge is usually configuring the production environment correctly, including environment variables, static files, dependencies, database settings, and fixing deployment errors from logs.

8. Why should every backend developer know deployment?
   Every backend developer should understand deployment because writing code is only part of the job. Knowing deployment helps developers publish APIs, troubleshoot production issues, collaborate effectively, and deliver complete, usable applications.

9. What would happen if environment variables were missing?
   If environment variables are missing:
  - The application may fail to start.
  - Secret keys and database credentials won't be available.
  - API keys cannot be accessed.
  - The application may produce runtime errors or become insecure if sensitive information is hardcoded.

## 10. How does deployment improve your portfolio?
    Deploying projects demonstrates that you can build, configure, and publish real-world applications. Recruiters can access your live API, making your portfolio more professional and showcasing practical backend development skills.

## 11. Importance of deploying backend applications
    Deploying backend applications is important because it:
    - Makes APIs accessible over the internet.
    - Enables real users and frontend applications to interact with the backend.
    - Helps identify production-specific issues.
    - Demonstrates end-to-end development skills.
    - Supports continuous integration and continuous deployment (CI/CD).
    - Improves collaboration by providing a live environment for testing.
    - Enhances credibility and employability through live, working projects.
