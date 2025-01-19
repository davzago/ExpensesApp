# Use the official PostgreSQL image as the base
FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER=exp_own
ENV POSTGRES_PASSWORD=dbpwtest
ENV POSTGRES_DB=exp_own

# Copy initialization scripts (optional)
# Any .sql or .sh file in this directory will be executed when the database initializes
# COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL default port
EXPOSE 5090
