# AgriTech – Smart Agriculture Management System
## MCA Project Report

### Abstract
AgriTech is a web-based farm management application developed with Python and Django. It gives farmers a single place to maintain farm profiles, plan crop cycles, track farm tasks, record soil test values and publish produce listings. The project demonstrates full-stack development, relational data modelling, authentication, access control, CRUD workflows, responsive UI design and automated testing.

### 1. Introduction
Farm operations involve multiple kinds of information: land details, crop seasons, daily tasks, soil test results and produce availability. When these records are fragmented, it becomes harder to review farm activity. AgriTech provides a centralized digital workspace for these records.

### 2. Problem statement
Small and medium farmers may rely on paper notes or disconnected applications. This can make it difficult to maintain a consistent history of farms, crop cycles and soil observations, and to communicate produce availability. The project addresses the record-management problem with a simple web platform.

### 3. Objectives
- Provide secure farmer registration and login.
- Maintain multiple farm records per farmer.
- Track crops, seasons, planting and expected harvest dates.
- Create and complete farm tasks.
- Store soil pH and N-P-K observations.
- Display cautious, basic pH-based educational notes.
- Publish and search produce listings.
- Provide an admin interface and automated tests.

### 4. Scope
The current version focuses on information management and marketplace listings. It does not claim to provide verified live weather forecasts, AI diagnosis, guaranteed crop yields, real-time commodity prices or direct payment processing.

### 5. Existing and proposed systems
Existing workflows can involve paper records, spreadsheets and separate communication channels. The proposed system centralizes farmer, farm, crop, task, soil and listing data through a browser-based interface.

### 6. Technology stack
Python, Django 5.2, SQLite for quick local setup, optional PostgreSQL, HTML, CSS and JavaScript. Django authentication and ORM are used for secure sessions and database operations.

### 7. System modules
1. Authentication and farmer profile
2. Farm management
3. Crop planning
4. Task management
5. Soil record management and basic insights
6. Produce marketplace
7. Dashboard and administration

### 8. Database design
- User: Django authentication identity.
- FarmerProfile: one-to-one extension of User.
- Farm: belongs to one User; contains location, acreage and soil type.
- Crop: belongs to one Farm; stores crop name, season, dates, area and status.
- FarmTask: belongs to one Farm; stores task, due date, priority and completion.
- SoilRecord: belongs to one Farm; stores date, pH and N-P-K values.
- ProduceListing: belongs to one User; stores crop, quantity, price, location and availability.

### 9. Security
The application uses Django's password hashing, authentication middleware, CSRF protection, login-required views and ownership-filtered farm queries. Production deployment must use a strong secret key, DEBUG=False, HTTPS, secure cookies, a production database and regular backups.

### 10. Testing
Automated tests cover public page access, registration page availability, authentication requirements, dashboard access, farm creation and ownership isolation. A manual test plan is supplied in `docs/TESTING_GUIDE.md`. Record actual test output and screenshots during final college validation.

### 11. Advantages
Centralized records, clear dashboard, multi-farm support, crop and task tracking, soil history, searchable produce listings, and a beginner-friendly interface.

### 12. Limitations
No external weather API, no sensor/IoT integration, no verified machine-learning model, no payment gateway and no live market feed. Recommendations are educational only and should not replace professional agricultural advice.

### 13. Future enhancements
Weather API integration, local-language UI, mobile/PWA support, verified crop advisory datasets, IoT soil sensors, buyer-seller messaging, order management, analytics and a validated ML model trained on a suitable dataset.

### 14. Conclusion
AgriTech demonstrates a practical full-stack application for organizing farm information. It provides a foundation that can be extended with verified agricultural data and services while keeping the current system transparent about its capabilities.

### References
- Django documentation: https://docs.djangoproject.com/
- Python documentation: https://docs.python.org/3/
- PostgreSQL documentation: https://www.postgresql.org/docs/
