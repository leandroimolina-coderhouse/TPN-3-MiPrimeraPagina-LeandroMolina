# Proyecto Concesionario Automotriz - Django

## Funcionalidades

1. Página de inicio
2. Alta de Marcas
3. Alta de Autos
4. Alta de Clientes
5. Búsqueda de Autos por modelo

## Orden recomendado de prueba

1. Ingresar al admin y crear algunas marcas (opcional)
2. Alta de Marca desde /crear-marca/
3. Alta de Auto desde /crear-auto/
4. Alta de Cliente desde /crear-cliente/
5. Buscar autos desde /buscar-auto/

## Estructura

- Models: Marca, Auto, Cliente
- Formularios: uno por cada modelo
- Búsqueda: Auto por modelo
- Templates con herencia usando base.html
