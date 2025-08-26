# Bookstore Website
**Bookstore website** is a full-stack web application that functions as an online bookstore. Users can browse books by category, search with multiple parameters, and manage purchases through a dynamic shopping cart. The platform integrates essential e-commerce features into one cohesive system.

## Tech Stack
- Frontend: HTML5, CSS3, JavaScript, Bootstrap
- Backend: Python, Django  
- Database: SQLite  

## Features
- **Book Browsing & Search**  
  - Browse books by category (all, new, on sale, etc.)  
  - Advanced search by title, author, publisher and other parameters  
- **Shopping Cart**  
  - Add, update, and remove items  
  - Dynamic cart management  
- **User Accounts**  
  - Registration & login system  
  - Personalized shopping experience  
- **Customer Interaction**  
  - Post comments and reviews on books  
  - Contact form for direct inquiries  
- **Store Location**  
  - Embedded Google Map with store details  
- **Pagination** for browsing large book collections
- **Admin Panel**  
  - Manage books, categories, and users  
  - Monitor and process customer orders  

### Installation
A quick introduction of the minimal setup you need toinstall and run the bookstore-website project. This will start the server with an already populated database.
#### Python3 must be already installed!

```bash
git clone https://github.com/your-username/bookstore.git
cd bookstore-website
python -m venv venv 
source venv/scripts/activate
cd../..
pip install -r requirements.txt
cd bookstore
python manage.py runserver
```
