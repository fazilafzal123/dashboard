# Product Specifications

Copyright (c) 2019 - present [AppSeed](http://appseed.us/)

<br />

## Requirements 

The product should provide all features listed below:

- **Status: DONE** - Updated dependencies (all [packages](https://github.com/app-generator/boilerplate-code-django-dashboard/blob/master/requirements.txt))
  - Django==3.2.6 (latest stable version)
- **Status: DONE** - Pythonic Footprint: 
  - Better Code formatting
  - Improved Files organization
  - Optimized imports
  - Docker Scripts Update
- **Status: DONE** - Improved Authentication: 
  - Extended user model 
  - Password reset 
  - Email confirmation on register
  - New user Fields: all information presented in the settings page:
    - First, Last Name
    - Birthday, Gender, Email, Phone   
    - Address, Number, City, ZIP
    - User Photo
- **Status: WIP** - API via DRF
- **Status: WIP** - Data Tables - manages paginated information 
- **Status: WIP** - Sample Charts
- **Status: WIP** - Social Login via Google and Github
- **Status: WIP** - Deployment: Docker, HEROKU, AWS Ec2, Google Cloud, Azure 
- **Status: WIP** - Payments: One-time payments via [Stripe Checkout](https://stripe.com/payments/checkout)

<br />

**1# - Dependencies**

> STATUS: **DONE**

The codebase should use the latest stable packages. 

<br />

**2# - Pythonic Footprint**

> STATUS: **DONE**

The codebase should implement the best practices adopted by the Python community. 

<br />

**3# - Improved Authentication**

> STATUS: **Work in progress**

On top of the default authentication the code will provide: 

- Optional email confirmation during the registration process
  - The feature becomes active as specified in the configuration
- Password reset mechanism 
- User Model extension
  - All Fiels of exposed by `settings.html` page
  
<br />

![User Model extension - New fields](https://user-images.githubusercontent.com/51070104/132366814-f8843ea2-19e0-46ae-a2ca-f477ab88d64d.png)

<br />

**4# - API via DRF**

> STATUS: **Work in progress**

Implemented in a separate application `api` - Features:

- `api/transactions/create` - create transaction
- `api/transactions/edit/id`- edit transaction
- `api/transactions/delete/id` - delete transaction
- `api/transactions/get/id` - get specific transaction 
- `api/transactions/get` - get all transactions 

> Existing sample project with similar features: [Django API Sample](https://github.com/app-generator/api-server-django-sample)

The information is saved using a `Transaction` model:

```python
class Transaction(models.Model):
    product = models.CharField(max_length=50)
    price = models.IntegerField()
    qty = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    info = models.CharField(max_length=250, null=True)
    created_at = models.DateTimeField(auto_now=True)
``` 

<br />

**5# - Data Tables**

> STATUS: **Work in progress**

Implemented in a separate application `datatables` - Features:

- Table `Transaction` saves the information (previously defined by the `API` feature).
- Load sample data using admin section
- Inline rows edit activated at double click
- Pagination and Search

> Existing sample project with similar features: [Django Datatables Sample](https://github.com/app-generator/django-datatables-sample)

<br />

**6# - Sample Charts**

> STATUS: **Work in progress**

Implemented in a separate application `charts` - Features:

- Manage orders and display the information visually using charts and widgets
- Table `Transaction` saves the information (previously defined by the `API` feature).
- `Charts`: Line and Bar Charts:
    - `Line Chart` shows the sales for a 12mo timeframe
    - `Bar Chart` shows the sales for a 12mo timeframe
- `Widget 1`: Total Sales (in value)
- `Widget 2`: Peek Sale - transaction with Biggest Value
- `Widget 3`: Total Orders (sum up of all transactions)
- `Widget 4`: Best Month - selected by the number of orders

<br />

**7# - Social Login**

> STATUS: **Work in progress**

Implemented in a separate application `socialauth`.
The application should provide multiple authentication options: 

- Default session-based authentication
- Social login: Google 
- Social login: Github

> Existing sample project with similar features: [Django Seed Project](https://github.com/app-generator/django-dashboard-eps)

<br />

**8# - Deployment Option**

> STATUS: **Work in progress**

Codebase should include dependencies and scripts to manage with ease following deployment options: 

- Docker
- HEROKU
- AWS EC2
- Google Cloud

<br />

**9# - Stripe Payments**

> STATUS: **Work in progress**

Implemented in a separate application `payments`. This feature implements `one-time` payments with [Stripe Checkout](https://stripe.com/payments/checkout)

> Related blog content: [Django Stripe Tutorial](https://testdriven.io/blog/django-stripe-tutorial/)

<br />

---
Django Dashboard Codebase Specifications - AppSeed [App Generator](https://appseed.us) 
