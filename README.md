## Project for Cryptocurrency Price Monitoring and Email Notifications

### Requirements

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### How to Deploy the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/ZalinaMag/my-crypto-app.git
   cd my-crypto-app
   ```

2. Start the project using Docker Compose:
   
   ```bash
   docker-compose up --build
   ```

   This command will:
   - Build the image for your application.
   - Start PostgreSQL, MailCatcher, and CloudBeaver.

3. Open MailCatcher to view the sent emails.

4. Open CloudBeaver for managing the PostgreSQL database.

5. To stop the containers, run:
   
   ```bash
   docker-compose down
   ```

### Database Management through CloudBeaver

1. Open CloudBeaver and register as an administrator.
2. Configure the connection to PostgreSQL:
   - **Host**: The IP address of the Postgres container inside Docker. You can find it with the command: 

     ```bash
     docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' postgres
     ```

   - **Port**: 5432
   - **User**: postgres
   - **Password**: your_password

6. The `my_crypto_container` script will regularly access resources listed in the job and perform queries to the database and mail server according to the algorithm.
