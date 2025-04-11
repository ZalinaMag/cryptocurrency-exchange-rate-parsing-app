## Project for Cryptocurrency Price Monitoring and Email Notifications written in Python & Dockerfile
This is headless backend application that continuously monitors price changes and reacts in near real-time in a resource-efficient, asynchronous manner.

### Features
The app:
- automatically scrapes cryptocurrency exchange rates from online sources every 2 minutes 
- stores data in a database
- compares rate changes between entries
- if a currency’s value increases by ≥0.03% generates email reports with total savings value in the user’s preferred currency and with calculated difference (profit/loss) from the rate change.
  
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
