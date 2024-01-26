from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Pet
from .forms import FeedbackForm, PetForm

# Create your views here.
class PetDetails(DetailView):
    model = Pet
    template_name = 'pet.html'
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        review_form = FeedbackForm(data=self.request.POST)
        pet = self.get_object()
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.name = f'{request.user.first_name} {request.user.last_name}'
            new_review.pet = pet
            new_review.save()
        return self.get(request, *args, **kwargs)
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_feedback = self.object.feedbacks.all()
        review_form = FeedbackForm()
   
        context['reviews'] = all_feedback        
        context['review_form'] = review_form
        return context

def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PetForm()
    
    return render(request, 'pet_form.html', {'form': form})
