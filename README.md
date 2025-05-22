# streamlit-postgreSQL

A sample Streamlit app connected to PostgreSQL, ready for deployment with Coolify.

## Quick Start

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd streamlit-postgreSQL
   ```

2. **Deploy with Docker Compose:**
   ```sh
   docker-compose up --build
   ```
   The Streamlit app will be available at http://localhost:8501

3. **Environment Variables:**
   - All sensitive credentials are managed via environment variables in `docker-compose.yml`.
   - Update them as needed for your deployment.

## Files
- `app.py`: Main Streamlit application.
- `docker-compose.yml`: Multi-container setup for PostgreSQL and Streamlit.
- `Dockerfile.streamlit`: Build instructions for the Streamlit app.
- `requirements.txt`: Python dependencies.

## Notes
- The default database credentials are for local development. Change them for production.
- The custom `Dockerfile.postgreSQL` is not required; the official image is used in `docker-compose.yml`.
