# Awesome Reviews API

## Resumen

API para gestionar tiendas, usuarios y reseñas de productos. 

## Modelo conceptual

Una representación conceptual de la fuente de datos utilizando Modelo Entidad Relacionalidad Extendido (MERX) que muestre las entidades, interrelaciones y atributos.

## Modelo lógico

La representación lógico del modelo de datos

## Catálogo de datos

### Stores
Propósito: Listado paginado de tiendas.
id: Es de tipo entero, no null y único, y representa el id de las tiendas.
name: Es de tipo varchar, no null y representa el nombre de las tiendas.

### Users
Propósito: Listado paginado de usuarios.
id: Es de tipo entero, no null, y representa el id de los usuarios.
firstName: Es de tipo varchar, no null y representa el nombre.
lastName: Es de tipo varchar, no null y representa el apellido del usuario.
email:Es de tipo varchar y representa el correo de el usuario.
birthdate: Es de tipo varchar y representa la fecha de nacimiento de el usuario.

### Reviews
Propósito: Listado paginado de reseñas.
id: Es de tipo entero, no null y representa el id de las reseñas.
userid: Es de tipo entero, no null y representa el id de los usuarios. 
storeid: Es de tipo entero, no null y representa el id de las tiendas.
product: Es de tipo varchar y representa el producto. 
rating: Es de tipo entero y representa la clasificación.
date: Es de tipo varchar y representa la fecha de la reseña.
