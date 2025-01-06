def get_linkedin_country_codes():
    return {
        'af': 'Afghanistan', 'al': 'Albania', 'dz': 'Algeria', 'ar': 'Argentina', 
        'am': 'Armenia', 'au': 'Australia', 'at': 'Austria', 'az': 'Azerbaijan', 
        'bh': 'Bahrain', 'bd': 'Bangladesh', 'by': 'Belarus', 'be': 'Belgium', 
        'bo': 'Bolivia', 'ba': 'Bosnia and Herzegovina', 'br': 'Brazil', 
        'bg': 'Bulgaria', 'kh': 'Cambodia', 'cm': 'Cameroon', 'ca': 'Canada', 
        'cl': 'Chile', 'cn': 'China', 'co': 'Colombia', 'cr': 'Costa Rica', 
        'hr': 'Croatia', 'cy': 'Cyprus', 'cz': 'Czech Republic', 'dk': 'Denmark', 
        'do': 'Dominican Republic', 'ec': 'Ecuador', 'eg': 'Egypt', 'sv': 'El Salvador', 
        'ee': 'Estonia', 'et': 'Ethiopia', 'fi': 'Finland', 'fr': 'France', 
        'ge': 'Georgia', 'de': 'Germany', 'gh': 'Ghana', 'gr': 'Greece', 
        'gt': 'Guatemala', 'hn': 'Honduras', 'hk': 'Hong Kong', 'hu': 'Hungary', 
        'is': 'Iceland', 'in': 'India', 'id': 'Indonesia', 'ir': 'Iran', 
        'iq': 'Iraq', 'ie': 'Ireland', 'il': 'Israel', 'it': 'Italy', 
        'jm': 'Jamaica', 'jp': 'Japan', 'jo': 'Jordan', 'kz': 'Kazakhstan', 
        'ke': 'Kenya', 'kr': 'South Korea', 'kw': 'Kuwait', 'lv': 'Latvia', 
        'lb': 'Lebanon', 'ly': 'Libya', 'lt': 'Lithuania', 'lu': 'Luxembourg', 
        'mk': 'North Macedonia', 'my': 'Malaysia', 'mt': 'Malta', 'mx': 'Mexico', 
        'md': 'Moldova', 'mn': 'Mongolia', 'me': 'Montenegro', 'ma': 'Morocco', 
        'mm': 'Myanmar', 'np': 'Nepal', 'nl': 'Netherlands', 'nz': 'New Zealand', 
        'ni': 'Nicaragua', 'ng': 'Nigeria', 'no': 'Norway', 'om': 'Oman', 
        'pk': 'Pakistan', 'pa': 'Panama', 'py': 'Paraguay', 'pe': 'Peru', 
        'ph': 'Philippines', 'pl': 'Poland', 'pt': 'Portugal', 'pr': 'Puerto Rico', 
        'qa': 'Qatar', 'ro': 'Romania', 'ru': 'Russia', 'sa': 'Saudi Arabia', 
        'sn': 'Senegal', 'rs': 'Serbia', 'sg': 'Singapore', 'sk': 'Slovakia', 
        'si': 'Slovenia', 'za': 'South Africa', 'es': 'Spain', 'lk': 'Sri Lanka', 
        'se': 'Sweden', 'ch': 'Switzerland', 'tw': 'Taiwan', 'tz': 'Tanzania', 
        'th': 'Thailand', 'tn': 'Tunisia', 'tr': 'Turkey', 'ug': 'Uganda', 
        'ua': 'Ukraine', 'ae': 'United Arab Emirates', 'uk': 'United Kingdom', 
        'www': 'United States', 'uy': 'Uruguay', 'uz': 'Uzbekistan', 've': 'Venezuela', 
        'vn': 'Vietnam', 'ye': 'Yemen', 'zm': 'Zambia', 'zw': 'Zimbabwe'
    }

def country_name_to_code(country_name):
    country_codes = get_linkedin_country_codes()
    for code, name in country_codes.items():
        if name.lower() == country_name.lower():
            return code
    return None


def generate_linkedin_search_url(main_keyword, additional_keyword=None, exclude_keyword=None, country_name=None, similar_job=False, current_position=None, degree=None, years_of_experience=None):
    country_codes = get_linkedin_country_codes()
    
    # Handle country code
    if country_name:
        country_code = country_name_to_code(country_name)
        country_code = country_code.lower() if country_code else None
        if country_code and country_code.lower() not in country_codes:
            print(f"Warning: '{country_name}' is not a known LinkedIn country. Using 'www' instead.")
            country_code = None
    else:
        country_code = None
    
    # Base URL
    base_url = "https://www.google.com/search?q="
    
    # Format keywords without escape characters
    main_part = f'+"{main_keyword.replace(" ", "+")}"' if main_keyword else ""
    additional_part = f'+"{additional_keyword.replace(" ", "+")}"' if additional_keyword else ""
    exclude_part = f' -"{exclude_keyword.replace(" ", "+")}"' if exclude_keyword else ""
    
    # Standard exclusions
    exclusions = ' -intitle:"profiles" -inurl:"dir/+"'
    
    # LinkedIn domain construction
    linkedin_domain = f"{country_code}.linkedin.com" if country_code else "www.linkedin.com"
    site_search = f"+site:{linkedin_domain}/in/+OR+site:{linkedin_domain}/pub/"
    
    # Current position handling
    position_part = f'+"{current_position.replace(" ", "+")}"' if current_position else ""


    #similar jobs
    if similar_job:
        main_part = f'~+"{main_keyword.replace(" ", "+")}"' if main_keyword else ""

    
    # Experience handling
    experience_part = ""
    if years_of_experience:
        try:
            years = int(years_of_experience)
            if years > 0:
                experience_terms = [f'"{i}+ years"' for i in range(years, years + 5)]
                experience_part = f'+({"+OR+".join(experience_terms)})'
        except ValueError:
            print(f"Warning: Invalid years of experience value. Skipping experience filter.")
    
    # Degree handling
    degree_part = ""
    if degree:
        degree = degree.lower()
        if degree == "masters":
            degree_part = '+"{masters+mba+master+diploma+msc+magister}"'
        elif degree == "bachelor":
            degree_part = '+"{bachelor+degree+licence}"'
        elif degree == "doctorate":
            degree_part = '+"{dr+Ph.D.+PhD+doctor+doctorate}"'
    
    # Combine all parts
    return base_url + main_part + additional_part + exclude_part + exclusions + site_search + position_part + experience_part + degree_part
