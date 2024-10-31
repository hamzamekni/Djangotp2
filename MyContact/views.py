
from django.http import HttpResponse
from django.shortcuts import render

from MyContact.forms import contactform2
from MyContact.models import Contact
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from MyContact.forms import contactform2
from MyContact.models import Contact
from django.conf import settings

# Create your views here.

# Create your views here.
def controleform1(request):
    if request.method == 'POST':
        f = request.POST['firstname']
        l = request.POST['lastname']
        e = request.POST['email']
        m = request.POST['message']
        
        # Create the Contact object
        contact = Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
        #contact=Contact(firstname=f,lastname=l,Email=e,msg=m)

        # contact.save()  # This line is not necessary since create() already saves it

        return HttpResponse('<h2> Data has been submitted </h2>')

    return render(request, "myform1.html")  # Return the form if not a POST request


def controleform2(request):
    if request.method == 'POST':  # If it's a POST request
        form = contactform2(request.POST)  # Populate the form with the request data
        if form.is_valid():  # Check if the data is valid
           
            # Get the data from the form
            f = form.cleaned_data['firstname']
            l = form.cleaned_data['lastname']
            e = form.cleaned_data['email']
            m = form.cleaned_data['message']
           
            # Create the Contact object
            contact = Contact.objects.create(firstname=f, lastname=l, email=e, message=m)
            
            # Send the email
            subject = "Thank you for contacting us"
            message = f"Hi {f} {l},\n\nThank you for reaching out. Here’s a copy of your message:\n\n{m}\n\nBest Regards,\nYour Team"
            from_email = settings.EMAIL_HOST_USER  # Sender's email from settings
            recipient_list = [e]  # Recipient is the email from the form

            # Send the email using Django's send_mail function
            send_mail(subject, message, from_email, recipient_list)

            return HttpResponse('<h2>Data has been submitted and email sent</h2>')  # Success message
    else:  # If it's a GET request, display a blank form
        form = contactform2()  
   
    return render(request, "myform2.html", {'mycontactform2': form})