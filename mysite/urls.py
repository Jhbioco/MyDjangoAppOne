from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'hospital.views.index', name='index'),
    url(r'^paciente/$', 'hospital.views.lista_pacientes', name='lista_pacientes'),
    #url(r'^medico/$','hospital.views.medico',name='medico'),
    url(r'^adicionar/$', 'hospital.views.home', name='home'),
    url(r'^pesquisa/$', 'hospital.views.pesquisa', name='pesquisa'),
    url(r'^show-consultas/$', 'hospital.views.show_consultas', name='show-consultas'),
    url(r"^hello.pdf$", 'hospital.views.some_view'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include('hospital.urls')),
]
