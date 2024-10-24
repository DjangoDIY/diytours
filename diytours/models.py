from django.db import models

# Create your models here.


# Category class for models, admin can manage category like fixed tours, flexible tours and so on......
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank= True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name



# Location class, admin can manage locations for the trips, this can also be used to filter the data based on location
class Location(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank= True)
    state = models.CharField(max_length=100)
    ## add image handling here
    class Meta:
        verbose_name_plural = "Locations"
    
    def __str__(self):
        return self.name


# Feature class, tours can be assigned feature list to display the features for tours and also can be used to filter the data based on the features
class Feature(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank= True)
    feature_icon = models.CharField(max_length= 100, default="") # add a default icon here
    class Meta:
        verbose_name_plural = "Features"
    
    def __str__(self):
        return self.name

# Tag  class, admin can manage trips and select who is the organizer for that particular destination or tour
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank= True)
    class Meta:
        verbose_name_plural = "Tags"
    
    def __str__(self):
        return self.name

# Activity  class, admin can manage trips and select which activity is included for that particular destination or tour
class Activity(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank= True)
    class Meta:
        verbose_name_plural = "Activities"
    
    def __str__(self):
        return self.name

# Places class, this class will store information about places travellers visit in a tour.
class Place(models.Model):
    name = models.CharField(max_length=50)
    ## add a featured image for the place
    description = models.TextField(blank= True)
    class Meta:
        verbose_name_plural = "Places"
    
    def __str__(self):
        return self.name
 
# FAQ model, admins can manage FAQs for tours
class FAQ(models.Model):
    question = models.CharField(max_length= 255)
    answer = models.TextField()
    class Meta:
        verbose_name_plural = "FAQs"
    
    def __str__(self):
        return self.question


# media model, it handles the image uploading and can be used by tours, and places

class Media(models.Model):
    image = models.ImageField(upload_to='media/images/')
    caption = models.CharField(max_length=255, blank= True)

    class Meta:
        verbose_name_plural = "Media"

    def __str__(self):
        return f"Media {self.id}"



# Tour class, this model will contain all the information about a tour.
class Tour(models.Model):
    title = models.CharField(max_length=255, unique= True)
    featured_image = models.ImageField(upload_to="media/images")
    description = models.TextField()
    duration_days = models.PositiveIntegerField()
    duration_night = models.PositiveIntegerField()
    regular_price = models.PositiveIntegerField()
    max_people = models.PositiveIntegerField( null= True)
    category = models.ManyToManyField(Category, blank= True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    inclusions = models.ManyToManyField(Feature, related_name="inclusions")
    exclusions = models.ManyToManyField(Feature, related_name="exclusions")
    tag = models.ManyToManyField(Tag, blank= True)
    activities = models.ManyToManyField(Activity, blank= True)
    places = models.ManyToManyField(Place, related_name="tour_places")
    tour_ques = models.ManyToManyField(FAQ, related_name="tour_ques")
    published = models.BooleanField(default= False)
    featured = models.BooleanField(default=False)
    images = models.ManyToManyField(Media, related_name="images")
    
    class Meta:
        verbose_name_plural = "Tours"
    
    def __str__(self):
        return self.title


# date class, handling dates for the tours
class Date(models.Model):
    FIXED = "fixed"
    PARTICULAR = "particular"
    REPEATED = "repeated"

    DATE_TYPE_CHOICE = [
        (FIXED, "Fixed Dates"),
        (PARTICULAR,"Particular Dates"),
        (REPEATED, "Repeated Dates")
    ]
    tour = models.ForeignKey(Tour, on_delete= models.CASCADE, related_name="tours_date")
    date_type = models.CharField(max_length= 10, choices= DATE_TYPE_CHOICE)
    start_date = models.DateField(null= True, blank= True)
    end_date = models.DateField(null= True, blank= True)
    repeat_interval = models.IntegerField(null= True, blank= True, help_text="Interval in days for repeated tour dates")
    def __str__(self):
        return f"{self.tour.title} ({self.get_date_type_display()})"

    def is_repeated(self):
        return self.date_type == self.REPEATED






# Promo model, admins can display discounted prices for the tours

class Promo(models.Model):
    tour = models.ForeignKey(Tour, on_delete= models.PROTECT, related_name="promos")
    date = models.DateField()
    discounted_price = models.DecimalField(max_digits=10, decimal_places= 2)
    is_active = models.BooleanField(default= False)

    class Meta:
        verbose_name_plural = "Promos"

    def __str__(self):
        return f"Promo for {self.tour.title} on {self.date} - {self.discounted_price}"








    
