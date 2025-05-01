# Lab-Tech---Appointment-Booking-System



LabTech is a Django-based platform designed to streamline operations for diagnostic labs, including admin management, branches, services, team members, appointments, media, and customer interaction features.

## 🚀 Features

- **Admin Management**: Superuser/admin can manage the entire platform.
- **Branches**: Each branch holds information such as location, contact, and timing.
- **Teams**: Each branch can have multiple team members (e.g., doctors, lab technicians).
- **Services**: Add lab services categorized and tagged for search and filtering.
- **Appointments**: Patients can book appointments for specific services and branches.
- **FAQs**: Frequently asked questions to help users understand lab processes.
- **Gallery**: Images showcasing lab infrastructure and events.
- **Banners & Popups**: Marketing banners and popups for promotions or important alerts.
- **Social Media Links**: Display lab’s social presence.
- **Notifications**: Notify users or admins about new appointments or updates.

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite / PostgreSQL (configurable)
- **Authentication**: Token-based (DRF Token Auth) (not added for now)
- **Permissions**: Role-based (Admin, User)

## 📁 App Structure

- `users/`: Handles user registration, login, and role management
- `tasks/`: Task management for assigning and tracking tasks (if extended)
- `branches/`: CRUD for branches
- `teams/`: Manage team members under branches
- `services/`: Services, tags, and categories
- `appointments/`: Booking and managing patient appointments
- `notifications/`: System and user notifications
- `media/`: Gallery, banners, and popups
- `faqs/`: FAQs management
- `socials/`: Social media links

## 🔐 Roles and Permissions

- **Admin**
  - Can manage all models
  - Can assign tasks and view all appointments
  - Can manage content (FAQs, Banners, Gallery, etc.)

- **User**
  - Can view available services, FAQs, gallery
  - Can book appointments
  - Can receive notifications

## 🧪 API Endpoints (Examples)

Here are a few example endpoints. For full details, refer to the Postman collection or API schema.

### Auth
- `POST /api/auth/register/`
- `POST /api/auth/login/`

### Branches
- `GET /api/branches/`
- `POST /api/branches/` (Admin only)

### Services
- `GET /api/services/`
- `GET /api/services/?category=Blood Test`

### Appointments
- `POST /api/appointments/` (User)
- `GET /api/appointments/` (Admin sees all, User sees their own)

## ▶️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/labtech-platform.git
cd labtech-platform
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Apply Migrations & Run Server

```bash
python manage.py migrate
python manage.py runserver
```

### 4. Create Superuser

```bash
python manage.py createsuperuser
```

## 📸 Media and Static Files

- Ensure `MEDIA_URL` and `MEDIA_ROOT` are configured in `settings.py`
- Use Django’s `ImageField` to upload media for banners, gallery, etc.

## ✅ To-Do (Optional Enhancements)

- Add user dashboard with analytics
- Appointment reminders via email/SMS
- Payment gateway integration
- Frontend (HTML templates)

## 📄 License

This project is licensed under the MIT License.

---

Developed with ❤️ using Django.
```

---
