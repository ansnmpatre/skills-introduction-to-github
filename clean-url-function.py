import re

def clean_url_for_log(string):
    url = string
    if url:
        # Extract the main domain
        domain = re.search(r'(https?://)?(www\.)?([\w-]+\.\w+)', url)
        if domain:
            main_domain = domain.group(3)
            print(f"Main Domain: {main_domain}")  # Debugging line
            return main_domain
    else:
        # Return the entire string if no URL or domain is found
        return string
    
print(clean_url_for_log("https://www.example.com"))