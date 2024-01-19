"""
URL configuration for trident project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tridentApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index' ),
    path('agile-scrum-foundation/',views.agile_scrum_foundation_training_course,name='agile-scrum-foundation-training-course'),    
    path('alile-scrum-master/',views.agile_scrum_master_training_course,name='agile-scrum-master-training-course'),
    path('azure-aI-engineer-associate/',views.azure_aI_engineer_associate_training_course,name='azure-aI-engineer-associate-training-course'),
    path('become-trainer/',views.become_trainer,name='become-trainer'),
    path('business-analyst/',views.business_analyst_training,name='business-analyst-training'),
    path('business-intelligence/',views.business_intelligence_training_course,name='business-intelligence-training-course'),
    path('ccna/',views.ccna_training_course,name='ccna-training-course'),
    path('ccnp/',views.ccnp_training_course,name='ccnp-training-course'),
    path('certified-ethical-hacking/',views.certified_ethical_hacking_training,name='certified-ethical-hacking-training'),
    path('certified-scrum-master/',views.certified_scrum_master_training_course,name='certified-scrum-master-training-course'),
    path('certified-scrum-product-owner-certification/',views.certified_scrum_product_owner_certification_training,name='certified-scrum-product-owner-certification-training'),
    path('checkpoint-certified-security-expert-certification-training/',views.checkpoint_certified_security_expert_certification_training,name='checkpoint-certified-security-expert-certification-training'),
    path('check-point-security-administration-certification-training/',views.check_point_security_administration_certification_training,name='check-point-security-administration-certification-training'),
    path('cisa/',views.cisa_certification_training_course,name='cisa-certification-training-course'),
    path('cism/',views.cism_certification_training,name='cism-certification-training'),
    path('cloud-computing/',views.cloud_computing_essentials_course,name='cloud-computing-essentials-course'),
    path('cobit-training-course/',views.cobit_training_course,name='cobit-training-course'),
    path('contact/',views.contact,name='contact'),
    path('data-science/',views.data_science,name='data-science'),
    path('digital-marketing/',views.digital_marketing,name='digital-marketing'),
    path('disclaimer/',views.disclaimer,name='disclaimer'),
    path('index--2/',views.index__2,name='index__2'),
    path('itil-intermediate-training/',views.itil_intermediate_training_course,name='itil-intermediate-training-course'),
    path('itil-v4-foundation-training/',views.itil_v4_foundation_training_course,name='itil-v4-foundation-training-course'),
    path('lean-six-sigma-black-belt/',views.lean_six_sigma_black_belt,name='lean-six-sigma-black-belt'),
    path('lean-six-sigma-green-belt/',views.lean_six_sigma_green_belt,name='lean-six-sigma-green-belt'),
    path('machine-learning/',views.machine_learning_training_course,name='machine-learning-training-course'),
    path('managing-across/',views.managing_across_training_course,name='managing-across-training-course'),
    path('microsoft-azure-administrator/',views.microsoft_azure_administrator_training_course,name='microsoft-azure-administrator-training-course'),
    path('microsoft-azure-architect-technologies/',views.microsoft_azure_architect_technologies_training_course,name='microsoft-azure-architect-technologies-training-course'),
    path('microsoft-azure-data-scientist-associate/',views.microsoft_azure_data_scientist_associate_training_course,name='microsoft-azure-data-scientist-associate-training-course'),
    path('microsoft-azure/',views.microsoft_azure_training_course,name='microsoft-azure-training-course'),
    path('pmp-certification/',views.pmp_certification_training_course,name='pmp-certification-training-course'),
    path('prince2-practitioner/',views.prince2_practitioner_training_course,name='prince2-practitioner-training-course'),
    path('prince-foundation/',views.prince_foundation_training_course,name='prince-foundation-training-course'),
    path('privacy-policy/',views.privacy_policy,name='privacy-policy'),
    path('python-and-django/',views.python_and_django_certification,name='python-and-django-certification'),
    path('salesforce-platform-app/',views.salesforce_platform_app_builder_certification_training,name='salesforce-platform-app-builder-certification-training'),
    path('terms-conditions/',views.terms_conditions,name='terms-conditions'),
    path('togaf-training/',views.togaf_training_course,name='togaf-training-course'),
    path('example/',views.example,name='example')
    


]
