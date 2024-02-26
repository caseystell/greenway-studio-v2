from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

def index(request):
  screenname = 'Home'
  return render(request, 'index.html', {
    'screenname':screenname
  })

def contact(request):
  screenname = 'Contact Us'
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    company = request.POST['company']
    message = request.POST['message']
    
    # send_mail() variables
    subject = "You have a new message - Greenway Studio"
    compiled_message = f'''
      You have a new message that was submitted through Greenway
      Studio website:\n
      Contact Name: {name}
      Contact Email: {email}
      Contact Phone: {phone}
      Contact Company: {company}
      Message: {message}
    '''
    print(compiled_message)
    from_email = settings.EMAIL_HOST_USER
    # recipient_list = ['david@greenway-studio.com', 'luis@greenway-studio.com']
    recipient_list = ['cleigh14@hotmail.com']
    # send_mail(subject, compiled_message, from_email, recipient_list)
    
  return render(request, 'contact.html', {
    'screenname':screenname
  })

def portfolio(request):
  screenname = 'Our Work'
  return render(request, 'portfolio.html', {
    'screenname':screenname
  })

def clients(request):
  screenname = 'Who We Serve'
  return render(request, 'about/clients.html', {
    'screenname':screenname
  })

def mission(request):
  screenname = 'Our Mission'
  return render(request, 'about/mission.html', {
    'screenname':screenname
  })

def our_story(request):
  screenname = 'Our Story'
  return render(request, 'about/our-story.html', {
    'screenname':screenname
  })