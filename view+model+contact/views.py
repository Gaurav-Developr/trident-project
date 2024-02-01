from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import contact_file
from django.contrib import messages 
import re



def agile_scrum_foundation_training_course(Request):
    return render(Request,'agile-scrum-foundation-training-course.html')

def agile_scrum_master_training_course(Request):
    return render(Request,'agile-scrum-master-training-course.html')

def azure_aI_engineer_associate_training_course(Request):
    return render(Request,'azure-aI-engineer-associate-training-course.html')

def become_trainer(Request):
    return render(Request,'become-trainer.html')

def business_analyst_training(Request):
    return render(Request,'business-analyst-training.html')

def business_intelligence_training_course(Request):
    return render(Request,'business-intelligence-training-course.html')

def ccna_training_course(Request):
    return render(Request,'ccna-training-course.html')

def ccnp_training_course(Request):
    return render(Request,'ccnp-training-course.html') 

def certified_ethical_hacking_training(Request):
    return render(Request,'certified-ethical-hacking-training.html')

def certified_scrum_master_training_course(Request):
    return render(Request,'certified-scrum-master-training-course.html')

def certified_scrum_product_owner_certification_training(Request):
    return render(Request,'certified-scrum-product-owner-certification-training.html')

def checkpoint_certified_security_expert_certification_training(Request):
    return render(Request,'checkpoint-certified-security-expert-certification-training.html')

def check_point_security_administration_certification_training(Request):
    return render(Request,'check-point-security-administration-certification-training.html')

def cisa_certification_training_course(Request):
    return render(Request,'cisa-certification-training-course.html')

def cism_certification_training(Request):
    return render(Request,'cism-certification-training.html')

def cloud_computing_essentials_course(Request):
    return render(Request,'cloud-computing-essentials-course.html')

def cobit_training_course(Request):
    return render(Request,'cobit-training-course.html')


def contact(Request):
    if Request.method == 'POST':
        name = Request.POST.get("name")
        lastname = Request.POST.get("lastname")
        email = Request.POST.get("email")
        
        # Validate email/name/lastname format using a regular expression
        
        email_regex = r'^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
        name_regex= r'^[a-zA-Z]{0,15}$'
        lastname_regex= r'^[a-zA-Z]{0,20}$'
        if not re.match(email_regex, email):
            messages.error(Request, 'Please enter a valid email address.')
            return render(Request, 'contact.html')
        elif not re.match(name_regex,name):
            messages.error(Request,'Please enter valid name..Not allowed digits,symbols and others')
            return render(Request,'contact.html')
        elif not re.match(lastname_regex,name):
            messages.error(Request,'Please enter valid lastname..Not allowed digits,symbols and others ')
            return render(Request,'contact.html')
        # check on database (fields are exists or not)
        try:
            if contact_file.objects.filter(name=name).exists() and contact_file.objects.filter(email=email).exists() or contact_file.objects.filter(lastname=lastname).exists():
                messages.error('Name or Email will be exists..Please enter another name or email...')
                return render(Request,'contact.html',{'name':name,'email':email,'lastname':lastname})
    
            contact = contact_file()
            contact.name = name
            contact.lastname = lastname
            contact.email = email
            contact.phone = Request.POST.get("Phone Number")
            contact.subject = Request.POST.get("subject")
            contact.message = Request.POST.get("message")
            print(contact.name,contact.lastname,contact.email,contact.phone,contact.subject,contact.message)
            contact.save()
            messages.success(Request,'Thanks to Share Your Query with us!!!!... Our Team will contact you soon...')
            return redirect("thankyou") 
        except:
            messages.error(Request,'Name or Email will be exists..Please enter another name or email...')

    elif Request.method == 'GET' and 'name' in Request.GET:
        # If there are errors, retrieve the form data and display them
        name = Request.GET.get("name")
        email = Request.GET.get("email")
        lastname = Request.GET.get("lastname")
        return render(Request, 'contact.html', {'name': name, 'email': email, 'lastname': lastname})
    
    return render(Request,'contact.html')

def thankyou(Request):
    return render(Request,'thankyou.html')

def data_science(Request):
    return render(Request,'data-science.html')

def digital_marketing(Request):
    return render(Request,'digital-marketing.html')

def disclaimer(Request):
    return render(Request,'disclaimer.html')


def index(Request):
    return render(Request,'index.html')

def index__2(Request):
    return render(Request,'index--2.html')

def itil_intermediate_training_course(Request):
    return render(Request,'itil-intermediate-training-course.html')

def itil_v4_foundation_training_course(Request):
    return render(Request,'itil-v4-foundation-training-course.html')

def lean_six_sigma_black_belt(Request):
    return render(Request,'lean-six-sigma-black-belt.html')

def lean_six_sigma_green_belt(Request):
    return render(Request,'lean-six-sigma-green-belt.html')

def machine_learning_training_course(Request):
    return render(Request,'machine-learning-training-course.html')

def managing_across_training_course(Request):
    return render(Request,'managing-across-training-course.html')

def microsoft_azure_administrator_training_course(Request):
    return render(Request,'microsoft-azure-administrator-training-course.html')

def microsoft_azure_architect_technologies_training_course(Request):
    return render(Request,'microsoft-azure-architect-technologies-training-course.html')

def microsoft_azure_data_scientist_associate_training_course(Request):
    return render(Request,'microsoft-azure-data-scientist-associate-training-course.html')

def microsoft_azure_training_course(Request):
    return render(Request,'microsoft-azure-training-course.html')

def pmp_certification_training_course(Request):
    return render(Request,'pmp-certification-training-course.html')

def prince2_practitioner_training_course(Request):
    return render(Request,'prince2-practitioner-training-course.html')

def prince_foundation_training_course(Request):
    return render(Request,'prince-foundation-training-course.html')

def privacy_policy(Request):
    return render(Request,'privacy-policy.html')

def python_and_django_certification(Request):
    return render(Request,'python-and-django-certification.html')

def salesforce_platform_app_builder_certification_training(Request):
    return render(Request,'salesforce-platform-app-builder-certification-training.html')

def terms_conditions(Request):
    return render(Request,'terms-conditions.html')

def togaf_training_course(Request):
    return render(Request,'togaf_training_course.html')







