from django.shortcuts import render
from django.http import JsonResponse
from .google_linkedin import generate_linkedin_search_url
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST



@csrf_exempt
def process_search(request):
    if request.method == 'POST':
        # Get form data
        country = request.POST.get('country')
        job_title = request.POST.get('job_title')
        show_similar = request.POST.get('show_similar', 'off') == 'on'
        include_keywords = request.POST.get('include_keywords')
        exclude_keywords = request.POST.get('exclude_keywords')
        education = request.POST.get('education')
        current_employer = request.POST.get('current_employer')
        years_exp = request.POST.get('years_exp')

        search_url = generate_linkedin_search_url(job_title, additional_keyword=include_keywords, exclude_keyword=exclude_keywords, country_name=country,similar_job=show_similar,current_position=current_employer,degree=education,years_of_experience=years_exp) 
        
      
        return JsonResponse({'search_url': search_url})
    
    else:
        # Handle GET request
        return render(request, 'index.html')

