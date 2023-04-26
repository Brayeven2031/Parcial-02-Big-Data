
from bs4 import BeautifulSoup
from job_processing_news_info import get_link_eltiempo, get_link_elespectador

html = '''
<article class="simple" data-autor="Alejandra lopez plazas" data-bloqueo="Abierto" data-board="Hs : Salud" data-category="salud" data-clasecontenido="Estandar" data-editorial="Editorial" data-id="762667" data-name="Invima admite tener más de 3.900 solicitudes de registros sanitarios represadas" data-publicacion="2023-04-25" data-seccion="Salud" data-subseccion="" data-tipocontenido="Articulo" dtm-name="Contenido7" id="m2625-9-2626" itemscope="" itemtype="https://schema.org/NewsArticle"><div class="category-published">
<a class="category page-link salud" href="/salud" id="m2630-2629-2631">Salud</a><span class="published-at" id="m2636-1-2637">6:00 pm</span></div>
<h2 class="title-container" itemprop="headline">
<a class="multimediatag page-link" href="/salud/invima-admite-tener-3-906-solicitudes-de-registros-sanitarios-represadas-762667">
<span id="m2642-2-2643">Video</span></a>
<a class="title page-link" href="/salud/invima-admite-tener-3-906-solicitudes-de-registros-sanitarios-represadas-762667" id="m2648-3-2649">Invima admite tener más de 3.900 solicitudes de registros sanitarios represadas</a></h2>
<meta content="2023-04-25" itemprop="datePublished"/><meta content="2023-04-25" itemprop="dateModified"/><meta itemid="https://www.eltiempo.com/salud/invima-admite-tener-3-906-solicitudes-de-registros-sanitarios-represadas-762667" itemprop="mainEntityOfPage" itemscope="" itemtype="https://schema.org/WebPage"/><span class="oculto" itemprop="author" itemscope="" itemtype="https://schema.org/Person">
<span itemprop="name">Alejandra López Plazas</span>
</span>
<div class="oculto" itemprop="publisher" itemscope="" itemtype="https://schema.org/Organization">
<div itemprop="logo" itemscope="" itemtype="https://schema.org/ImageObject">
<meta content="https://www.eltiempo.com/bundles/eltiempocms/images/el-tiempo/logo-el-tiempo-azul.jpg" itemprop="url"/><meta content="600" itemprop="width"/><meta content="60" itemprop="height"/></div>
<meta content="EL TIEMPO" itemprop="name"/><meta content="https://www.eltiempo.com" itemprop="url"/></div>
<div class="oculto" itemprop="image" itemscope="" itemtype="https://schema.org/ImageObject"><meta content="570" itemprop="width"/><meta content="380" itemprop="height"/><meta content="https://www.eltiempo.com/bundles/eltiempocms/images/default.jpg" itemprop="url"/></div></article>
'''

text_response = '"Invima admite tener más de 3.900 solicitudes de registros sanitarios represadas","salud","/salud/invima-admite-tener-3-906-solicitudes-de-registros-sanitarios-represadas-762667"\n'

def test_get_link_eltiempo():

    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a')[2]

    assert get_link_eltiempo(links) == text_response

    