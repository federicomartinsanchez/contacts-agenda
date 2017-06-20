from django.views import generic
from django.views.generic import CreateView,UpdateView, DeleteView,ListView
from .models import Contacto
from django.core.urlresolvers import reverse_lazy
from django.http import request

class IndexView(generic.ListView):
    context_object_name= 'all_contacts'
    template_name = 'contacts/index.html'
    model = Contacto

    def get_queryset(self):
        query = self.request.GET.get('q')
        sfield = self.request.GET.get('select')
        qs = super(IndexView, self).get_queryset()
        if query and sfield:
            if sfield == "Nombre":
                return qs.filter(nombre__icontains=query) or qs.filter(apellidos__icontains=query)
            if sfield == "Correo":
                return qs.filter(email__icontains=query)
            if sfield == "Codigo Postal":
                return qs.filter(codigo_postal__icontains=query)
            if sfield == "Pais":
                return qs.filter(pais__icontains=query)
        else:
            return Contacto.objects.all()


class DetailView(generic.DetailView):
    model = Contacto
    template_name = 'contacts/detail.html'

class ContactoCreate (CreateView):
    model= Contacto
    fields = ['nombre','apellidos', 'telefono', 'email', 'pagina_web','calle', 'provincia','pais','codigo_postal']

class ContactoUpdate (UpdateView):
    model= Contacto
    fields = ['nombre','apellidos', 'telefono', 'email', 'pagina_web','calle', 'provincia','pais','codigo_postal']

class ContactoDelete (DeleteView):
    model= Contacto
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    success_url = reverse_lazy('contacts:index')