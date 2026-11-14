# Testing and demonstration guide

## Automated checks
Run:
```bat
python manage.py check
python manage.py test
```
The included tests cover the public home page, registration page, login protection for the dashboard, authenticated dashboard access, farm creation, and ownership-based access control.

## Manual test plan
1. Register a new farmer account.
2. Sign in and verify the dashboard loads.
3. Add a farm with location, acreage and soil type.
4. Open My farms and view the farm detail page.
5. Add a crop and confirm it appears under the farm.
6. Create a farm task and toggle its completion from the dashboard.
7. Add a soil test with pH and N-P-K readings.
8. Open Soil insights and verify the basic pH note.
9. Publish a produce listing.
10. Open Marketplace, search by crop name and verify the listing.
11. Sign out and verify dashboard redirects to login.
12. Sign in as another user and verify the first user's farm is not accessible.

## Demo narration
Explain the problem (farm information scattered across notebooks and messages), demonstrate registration, farm creation, crop planning, tasks, soil record entry, marketplace listing, and finish with security/testing and future scope.
