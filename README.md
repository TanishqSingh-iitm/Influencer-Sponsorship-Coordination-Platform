# Influencer Engagement and Sponsorship Coordination Platform

A comprehensive, multi-user platform for seamless influencer marketing campaign management. This application facilitates campaign discovery, ad requests, negotiations, and payment between influencers and sponsors, with robust admin oversight and reporting.

## Features

- **Multi-User Roles**
    - **Influencers:**
        - View and search public campaigns
        - Request to participate in campaigns, negotiate, and complete ads for payment
        - Edit profile, review received ratings, view campaign-specific statistics
        - Chat with sponsors, report campaigns/sponsors
    - **Sponsors:**
        - Manage (CRUD) campaigns and ads
        - View and search influencers, rate and review influencers
        - Approve/reject ad requests, message influencers, run private/industry campaigns
        - View campaign/ad-specific statistics
    - **Admin (Superuser):**
        - View all users, campaigns, ads, reports, and platform-wide statistics
        - Read user reviews and reports, flag content/users, deactivate accounts if necessary
- **Authentication:** Secure, token-based login via Flask-Security
- **Real-Time Communication:** Messaging and negotiation between sponsors and influencers
- **Statistics \& Visualization:** Role-specific dashboards with charts (Chart.js)
- **Automated PDF Reports:** Generated using ReportLab
- **Background Jobs:** Reminders, exports, and reporting handled via Celery
- **Caching:** Fast API performance with Redis


## Tech Stack

- **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Security, Celery, Redis
- **Frontend:** Vue.js, Chart.js
- **Database:** SQLite (SQLAlchemy ORM)
- **Visualization \& Reporting:** Chart.js, ReportLab (PDF)
- **Utilities:** python-dotenv (env vars), HTML/CSS


## System Architecture

- **models.py:** Database schema and ORM models
- **config.py:** Environment-specific configuration
- **routes/**: All Flask API endpoints and route controllers
- **app.py:** App initialization and module imports
- **frontend/**: Vue.js modules and UI components
- **celery/** and **mailer/**: Asynchronous task/job handling
- **instance/**: Database storage
- **images/**: Profile image storage


## Database Schema

- **User:** Stores user info and authentication
- **Campaigns:** Marketing campaigns (with Ads as one-to-many)
- **Ad:** Ad listings, linked to Campaigns
- **Ad Request:** Links users to Ad invitations/requests
- **User Ratings:** Ratings and reviews (one-to-many)
- **Reports:** Campaign and User reports (one-to-many)
- **Transactions:** Payment or completion events
- **Messages:** User-to-user messaging
- **RolesUser/Roles:** Role-based access management

**View the complete ER diagram:**


## API Design

- RESTful endpoints supporting CRUD operations for Campaigns, Ads, Users, Reports, etc.
- Secure token-based authentication for all user actions
- Efficient database queries with SQLAlchemy ORM



