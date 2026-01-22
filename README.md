# Smart Road Pothole Reporting System

A web-based system enabling citizens to report road issues (potholes) and authorities to manage and track repairs.

## Features

### For Citizens 🇮🇳
- **Report Issues**: Submit detailed reports including specific location, district, panchayat, and description.
- **Track Status**: Monitor the status of a report using a unique Report ID.

### For Authorities 👮
- **Secure Dashboard**: Login-protected area for officials.
- **Manage Reports**: View all submitted reports in a tabular format.
- **Update Status**: Change report status (Pending, In Progress, Completed).

## Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3 (Dark Theme)

## Installation & Running

1. **Clone/Open the project directory**.

2. **Install Flask** (if not already installed):
   ```bash
   pip install flask
   ```

3. **Run the Application**:
   ```bash
   python3 app.py
   ```

4. **Access the App**:
   - Open your browser and go to: `http://127.0.0.1:5000/`

## Authority Access

To access the Authority Dashboard:
1. Click on the "Authority Login / Dashboard" link at the bottom of the home page (or go to `/dashboard`).
2. Login with the following credentials:
   - **Username**: `admin`
   - **Password**: `admin123`

### Admin Dashboard Capabilities
Once logged in, administrators can:
- **View All Reports**: Access a centralized table showing every reported issue.
- **Detailed Insights**: See the exact location, Gram Panchayat, District, and reporter details for each issue.
- **Workflow Management**:
  1.  **Pending**: Initial state when a report is submitted.
  2.  **In Progress**: Mark reports as being worked on.
  3.  **Completed**: Close the report once the road is fixed.
- **Real-time Updates**: Status changes are immediately reflected for citizens tracking their reports.

## Project Structure
- `app.py`: Main Flask application handling routes and logic.
- `templates/`: HTML templates (`index.html`, `dashboard.html`, `login.html`).
- `static/`: CSS stylesheets (`style.css`).
