from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import Contact,EventBooking
from .models import *
import re
import uuid
from django.core.exceptions import ValidationError


def validate_no_special_chars(value):
    if re.match("^[a-zA-Z0-9]*$", value):
        return value
    else:
        raise ValidationError("Special characters are not allowed.")
    

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            login(request,user)
            return redirect('home')
        else:
            error_message = 'Invalid login credentials...... Please enter again.'
            return render(request, 'Apps/Login.html', {'error_message': error_message})
    return render(request, "Apps/Login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        usertype = request.POST.get('usertype')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')


        if not re.match("^[a-zA-Z0-9_]*$", username):
            error_message = 'Username should only contain alphanumeric characters'
            return render(request, 'Apps/signup.html', {'error_message': error_message})
        
        if len(username) < 3:
            error_message = 'Username must be at least 3 characters long'
            return render(request, 'Apps/signup.html', {'error_message': error_message})
        
        if User.objects.filter(username=username).first():
            error_message = 'Username already exist.. Use some other username'
            return render(request, 'Apps/signup.html', {'error_message': error_message})
            

        if "@gmail.com" not in email:
            error_message = 'Invalid email address. Only Gmail accounts are allowed.'
            return render(request, 'Apps/signup.html', {'error_message': error_message})

        
        if User.objects.filter(email = email).first():
                error_message = 'Email already exist.. Use some other email.'
                return render(request, 'Apps/signup.html', {'error_message': error_message})
        
        if not email:
            error_message = 'Email is required'
        elif not re.match('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            error_message = 'Invalid email address'


        if not re.match("^[a-zA-Z0-9_]*$", pass1):
            error_message = 'Password should only contain alphanumeric characters'
            return render(request, 'Apps/signup.html', {'error_message': error_message})

        if pass1 != pass2:
            error_message = 'Passwords didnt match.'
            return render(request, 'Apps/signup.html', {'error_message': error_message})
        try:
            my_user = User.objects.create_user(username,email,pass1)
            my_user.save()
            admin = Admin(username = username, email = email,pass1 = pass1, pass2 = pass2)
            admin.save()


            return redirect('Login')
        except:
            error_message = 'Error creating an account'

    return render(request, "Apps/signup.html")


def forgotpass(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():
                error_message = 'User not found with this Email'
                return render(request, 'Apps/forgotpass.html', {'error_message': error_message})
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            error_message = 'An email is sent.'
            return render(request, 'Apps/forgotpass.html', {'error_message': error_message})



    except Exception as e:
        print(e)
    return render(request, "Apps/forgotpass.html")


def changepass(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.get(forgot_password_token = token)

        print(profile_obj)



    except Exception as e:
        print(e)

    return render(request, "Apps/changepass.html")

def home(request):
    return render(request, "Apps/home.html")


@login_required(login_url='Login')
def explore(request):
    return render(request, "Apps/Explore.html")


@login_required(login_url='Login')
def aboutus(request):
    return render(request, "Apps/Aboutus.html")


@login_required(login_url='Login')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        problem = request.POST.get('problem')
        contact = Contact(name=name, email=email, problem=problem)
        contact.save()
        subject = 'Contact Form Submission Received'
        message = 'Thank you for contacting us! We will get back to you soon.'
        from_email = '2100031677cseh@gmail.com'  # replace with your email address
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return redirect('thanks', email=email)
    else:
        return render(request, 'Apps/contact.html')


def thanks(request, email):
    return render(request, 'Apps/thanks.html', {'email': email})


@login_required(login_url='Login')
def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        event = request.POST.get('event')
        date = request.POST.get('date')
        time = request.POST.get('time')
        duration = request.POST.get('duration')
        venue = request.POST.get('venue')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        guests = request.POST.get('guests')
        budget = request.POST.get('budget')
        catering = request.POST.get('catering')
        audioVisual = request.POST.get('audioVisual')
        Photography = request.POST.get('Photography')
        videography = request.POST.get('videography')
        decorations = request.POST.get('decorations')
        other = request.POST.get('other')
        booking = EventBooking(name=name, email=email, phone=phone, event=event, 
                               date=date, time=time, duration=duration, venue=venue, address=address
                               , city=city, state=state, zipcode=zipcode, guests=guests, 
                               budget=budget, catering=catering, audioVisual=audioVisual,
                               Photography=Photography, videography=videography, decorations=decorations
                               , other=other)
        booking.save()
    bookings = EventBooking.objects.all() 
    return render(request, "Apps/Booking.html", {'bookings': bookings})



def contact_list(request):
    contacts = Contact.objects.all().order_by('-id')

    if request.method == 'POST':
        contact_id = request.POST.get('contact_id')
        contact = Contact.objects.get(id=contact_id)
        contact.is_read = True
        contact.save()

    context = {
        'contacts': contacts
    }
    return render(request, 'Apps/contact_list.html', context)

def delete_read_contacts(request):
    Contact.objects.filter(is_read=True).delete()
    return redirect('contact_list')



def booking_list(request):
    bookings = EventBooking.objects.all().order_by('-id')

    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        booking = EventBooking.objects.get(id=booking_id)
        booking.is_reads = True
        booking.save()

    context = {
        'bookings': bookings
    }
    return render(request, 'Apps/booking_list.html', context)

def delete_read_bookings(request):
    EventBooking.objects.filter(is_reads=True).delete()
    return redirect('booking_list')


def Logout(request):
    logout(request)
    return redirect('home')

def Profile(request):
    return render(request,"Apps/Profile.html")


def customer1(request):
    return render(request, "Apps/customer1.html" )


def producer1(request):
    return render(request, "Apps/producer1.html")


def jobBooking(request):
    if request.method == 'POST':
        name = request.Post.get('name')
        email = request.Post.get('email')
        phone = request.Post.get('phone')
        servicetype = request.Post.get('servicetype')
        if servicetype == 'catering':
            cateringtype = request.Post.get('cateringtype')
            menuitems = request.Post.get('menuitems')
            dietres = request.Post.get('dietres')
            catering = Catering(name = name, email = email,
                                phone = phone, cateringtype=cateringtype,
                                menuitems=menuitems,dietres=dietres)
            catering.save()
            caterings = Catering.objects.all()
            return render(request, "Apps/thanks.html", {'caterings': caterings})
        return render(request , 'Apps/thanks.html')
    return render(request, "Apps/jobBooking.html")


def hostre(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = 'Service Provider request received'
        message = 'Thank you for contacting us! . Login back to your account after 24 hours to host your job.'
        from_email = '2100031677cseh@gmail.com'  # replace with your email address
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        subject = 'Service Provider request'
        message = 'A person wants to be a service provider. Allow him to get the access'
        from_email =  '2100031677cseh@gmail.com' # replace with your email address
        recipient_list = ['2100031677cseh@gmail.com']
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        # Render a success page
        return render(request, 'Apps/thanks.html')
    
    # Render the form page for GET requests
    return render(request, 'Apps/hostre.html')


