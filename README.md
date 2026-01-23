# Proyecto Concesionario Automotriz - Django

## Funcionalidades

1. Página de inicio
2. Conocer Servicios ofrecidos
3. Conocer Marcas Disponibles
4. Búsqueda de Autos por modelo
5- Story/Brief acerca del fundador

## Orden recomendado de prueba

1. Ingresar al admin y crear algunas marcas (opcional)
2. Alta de Marca desde /crear-marca/
3. Alta de Auto desde /crear-auto/
4. Alta de Cliente desde /crear-cliente/
5. Buscar autos desde /buscar-auto/

## Estructura

concesionario/
│
├── manage.py
│
├── concesionario/            # Proyecto principal
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   ├── core/                 # Home / inicio
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── core/
│   │   │       └── inicio.html
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── models.py
│   │
│   ├── autos/                # Marcas y modelos
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── autos/
│   │   │       ├── marca_form.html
│   │   │       ├── modelo_form.html
│   │   │       ├── modelo_list.html
│   │   │       └── buscar_auto.html
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── models.py
│   │
│   └── usuarios/             # Login, registro, perfil
│       ├── migrations/
│       ├── templates/
│       │   └── usuarios/
│       │       ├── login.html
│       │       ├── register.html
│       │       └── perfil_detail.html
│       ├── views.py
│       ├── urls.py
│       └── models.py
│
├── templates/                # Templates globales
│   └── base.html            
│
├── static/
│   ├── css/
│   ├── js/
│   └── img/
│
└── media/
