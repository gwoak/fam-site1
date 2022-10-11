from .models import Category, Post

def category_renderer(request):
    # category list in base template (navbar) and add category template
    # order by name here as the filter disctsort is not working in templates
    return {
        'all_cats': Category.objects.values_list("name", flat=True).order_by('name'),
        
    }

def author_renderer(request):    
    all_authors = {i.author_id: i.author.first_name for i in Post.objects.all()}
    return {
        'all_authors': all_authors
    }