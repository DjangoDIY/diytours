For full documentation, please visit: https://djangodiy.github.io/docs/

## Requirements

Ensure the following are installed on your system before starting:

	•	Python 3.7+
	•	Django 5.0+
	•	Pillow (for handling images)
	•	Git


## Features


1. Tour Management

	•	Add, Edit, and Delete Tours: Manage tours with options to create new ones, update existing ones, or remove them as needed.
	•	Tour Attributes:
	•	Title
	•	Description
	•	Duration (Days & Nights)
	•	Price (Regular Price)
	•	Maximum Number of People
	•	Published Status (Control visibility of the tour on the website)

2. Categories and Tags

	•	Categories: Organize tours under different categories for better user navigation.
	•	Tags: Add relevant tags to tours to improve filtering and categorization.

3. Tour Dates

	•	Date Model: Attach multiple available dates to a tour, allowing customers to see when the tour is available.
	•	Booking Based on Date: Users can book a tour for a specific available date.

4. Promo and Discounts

	•	Promo Model: Create promotional offers by applying discounted prices to tours.
	•	Non-Destructive Deletion: When promos are deleted, the associated tour remains intact without any data loss.

5. Image Gallery

	•	Featured Image: Each tour can have a featured image that appears prominently on the tour details page.
	•	Gallery Images: Upload multiple images to form a gallery for each tour, giving potential customers a visual preview.
	•	Navigation: Users can navigate through the gallery images on the tour detail page with previous and next buttons.
	•	Lightbox: View gallery images in a lightbox for an enlarged view.

6. Front-end Display

	•	Tour Details Page: A well-structured front-end template to display all the tour information, including gallery, description, price, and other attributes.
	•	Dynamic Template Support: The app uses extendable templates that can be customized according to user needs.

7. Admin Panel Features

	•	Admin Interface: Manage tours, categories, tags, images, and promotions easily from the Django admin panel.
	•	Customizable Forms: Add and update information for tours, promos, and categories from the admin interface.

8. Content Control

	•	Published Status: Easily enable or disable a tour’s visibility on the website with a simple toggle for the published field.

9. Bookings & Payments (Planned/Extendable)

	•	Booking Integration: While not implemented by default, the app is designed to work with booking systems and payment gateways in future iterations or with separate plugins.

10. Modular and Reusable

	•	Pluggable Design: The app can be easily integrated into existing Django projects or used as a standalone.
	•	Reusable Components: Developers can reuse components like the gallery, promo system, and tour models in other projects.

11. Customization Support

	•	Extensible Templates: Developers can override default templates to suit the design of their main project.
	•	Customizable Models: Easily extend models like Tour, Category, and Promo to add more fields and features.

TEMPLATE IS CREATED USING CHATGPT


## Contribute
If you would like to contribute to the project:

1.	Fork the repository.
2.	Create a new branch for your feature:
   	.. code:: bash
        	git checkout -b feature-branch
3.	Make your changes and commit:
	.. code:: bash
        	git commit -m "Added a new feature"
4.	Push to your branch:
	 .. code:: bash
        	git push origin feature-branch
5.	Submit a pull request for review.

