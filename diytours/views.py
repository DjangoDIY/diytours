from django.shortcuts import render, HttpResponseRedirect
from django.db import DatabaseError
from django.http import HttpResponseForbidden, JsonResponse
from diytours.models import *
import logging
logger = logging.getLogger(__name__)

# Create your views here.

#tour_index will render all the tours created in the database
def tour_index(request):
    try:
        tours = Tour.objects.filter(published = True)
        if not tours.exists():
            raise ValueError("TourIndex(1): No published tours found.")
        context ={
            "tours": tours
        }
        return render(request, "tours/index.html", context)
    except ValueError as ve:
        context = {
            "error": str(ve)
        }
        return render(request, "tours/index.html", context)
    except DatabaseError as db_err:
        context = {
            "error": "TourIndex(2): Database error occured:" + str(db_err)
        }
        return render(request, "tours/index.html", context)
    except Exception as e:
        logger.error(f"Error occurred in tour_index: {e}")
        context = {
            "error": "TourIndex(3):An unexpected error occurred:" + str(e)
        }
        return render(request, "tours/index.html", context)



#tour_detail will render tour's full details based on title

def tour_detail(request, title):
    try:
        tour = Tour.objects.get(
            title = title,
            published = True
        )
        context = {
            "title": title,
            "tour": tour,
        }
        return render(request, "tours/detail.html", context)
    except Tour.DoesNotExist:
        context = {
            "error": "TourDetails(1): No tour found."
        }
        return render(request, "tours/detail.html", context)
    except DatabaseError as db_err:
        context = {
            "error": "TourDetails(2): Database error occured:" + str(db_err)
        }
        return render(request, "tours/detail.html", context)
    except Exception as e:
        logger.error(f"Error occurred in tour_detail: {e}")
        context = {
            "error": "TourDetails(3): An unexpected error occurred:" + str(e)
        }
        return render(request, "tours/detail.html", context)


# tour_category will render tours based on category
def tour_category(request, category):
    try:
        tour = Tour.objects.filter(
            category__name = category,
            published = True
        )
        if not tour.exists():
            raise ValueError("TourCategory(1): No valid category found.")
        context = {
            "category": category,
            "tour": tour
        }
        return render(request, "tours/category.html", context)
    except ValueError as ve:
        context = {
            "error": str(ve)
        }
        return render(request, "tours/category.html", context)
    except DatabaseError as db_err:
        context = {
            "error": "TourCategory(2): Database error occured:" + str(db_err)
        }
        return render(request, "tours/category.html", context)
    except Exception as e:
        logger.error(f"Error occurred in tour_category: {e}")
        context = {
            "error": "TourCategory(3): An unexpected error occurred:" + str(e)
        }
        return render(request, "tours/category.html", context)   



# tour_location will render tours based on location
def tour_location(request, location):
    try:
        tour = Tour.objects.filter(
            location__name = location,
            published = True
        )
        if not tour.exists():
            raise ValueError("TourLocation(1): Location not found.")
        context = {
            "location": location,
            "tour": tour
        }
        return render(request, "tours/location.html", context)
    except ValueError as ve:
        context = {
            "error": str(ve)
        }
        return render(request, "tours/location.html", context)
    except DatabaseError as db_err:
        context = {
            "error": "TourLocation(2): Database error occured:" + str(db_err)
        }
        return render(request, "tours/location.html", context)
    except Exception as e:
        logger.error(f"Error occurred in tour_location: {e}")
        context = {
            "error": "TourLocation(3): An unexpected error occurred:" + str(e)
        }
        return render(request, "tours/location.html", context)  

# tour_tag will render tours based on tags
def tour_tag(request, tag):
    try:
        tour = Tour.objects.filter(
            tag__name = tag,
            published = True
        )
        if not tour.exists():
            raise ValueError("TourTag(1): Tag not found.")
        context = {
            "tag": tag,
            "tour": tour
        }
        return render(request, "tours/tag.html", context)
    except ValueError as ve:
        context = {
            "error": str(ve)
        }
        return render(request, "tours/tag.html", context)
    except DatabaseError as db_err:
        context = {
            "error": "TourTag(2): Database error occured:" + str(db_err)
        }
        return render(request, "tours/tag.html", context)
    except Exception as e:
        logger.error(f"Error occurred in tour_tag: {e}")
        context = {
            "error": "TourTag(3): An unexpected error occurred:" + str(e)
        }
        return render(request, "tours/tag.html", context)

# tour_activity will render tours based on activities
def tour_activity(request, activity):
    try:
        tour = Tour.objects.filter(
            activities__name = activity,
            published = True
        )
        if not tour.exists():
            raise ValueError("TourActivity(1): Activity not found.")
        context = {
            "activity": activity,
            "tour": tour
        }
        return render(request, "tours/activity.html", context)
    except ValueError as ve:
        context = {
            "error": str(ve)
        }
        return render(request, "tours/activity.html", context)
    except DatabaseError as db_err:
        context = {
            "error": "TourActivity(2): Database error occured:" + str(db_err)
        }
        return render(request, "tours/activity.html", context)
    except Exception as e:
        logger.error(f"Error occurred in tour_activity: {e}")
        context = {
            "error": "TourActivity(3): An unexpected error occurred:" + str(e)
        }
        return render(request, "tours/activity.html", context)

# tour_promo will render tours on sale or with discount
def tour_promo(request):
    try:
        tour = Tour.objects.filter(
            promos__is_active = True,
            published = True
        )
        if not tour.exists():
            raise ValueError("TourPromo(1): Promo not found.")
        context = {
            "tour": tour
        }
        return render(request, "tours/promo.html", context)
    except ValueError as ve:
        context = {
            "error": str(ve)
        }
        return render(request, "tours/promo.html", context)
    except DatabaseError as db_err:
        context = {
            "error": "TourPromo(2): Database error occured:" + str(db_err)
        }
        return render(request, "tours/promo.html", context)
    except Exception as e:
        logger.error(f"Error occurred in tour_promo: {e}")
        context = {
            "error": "TourPromo(3): An unexpected error occurred:" + str(e)
        }
        return render(request, "tours/promo.html", context)

