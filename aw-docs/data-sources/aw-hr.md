# AdventureWorks HR Files

## Resumen

Es una base de datos conformada por archivos csv, donde se encuentra información sobre los departamentos de la empresa y los empleados.

## Modelo conceptual

Una representación conceptual de la fuente de datos utilizando Modelo Entidad Relacionalidad Extendido (MERX) que muestre las entidades, interrelaciones y atributos.

## Modelo lógico

La representación lógico del modelo de datos

## Catálogo de datos

Una descripción completa de cada tabla dentro de la fuente de datos. Este catálogo debe incluir:

- Nombre y propósito de la tabla.

- Lista de campos, incluyendo nombre, tipo de dato, restricciones y descripción de negocio.

### Shift
Propósito: Información sobre los turnos laborales. 
ShiftId: Es de tipo entero, no null y único.
Name: Es de tipo texto, no null, y representa la sección de turno.
StartTime: Es de tipo time, no null, y representa la hora de inicio.
EndTime: Es de tipo time, no null y representa la hora de finalización.
ModifiedDate: Es de tipo time, no null y representa la fecha de las modificaciones que se realicen.

### EmployeePayHistory
Propósito: Información sobre el historial de pago de los empleados.
BusinessEntityId: Es de tipo entero, no null y único.
RateChangeDate: Es de tipo time, no null y representa la fecha de el cambio de tarifa.
Rate: Es de tipo varchar y representa la tasa de cambio.
PayFrequency: Es de tipo entero y representa la frecuencia del pago.
ModifiedDate: Es de tipo time, no null y representa la fecha de las modificaciones que se realicen

### EmployeeDepartmentHistory
Propósito: Información sobre el historial de los turnos de los empleados por departamentos.
BusinessEntityId: Es de tipo entero, no null y único.
DepartmentId: Es de tipo entero, no null y representa el ID del departamento.
ShiftId: Es de tipo entero y representa el Id de el turno.
StartDate: Es de tipo time, no null, y representa la hora de inicio.
EndDate: Es de tipo time, no null y representa la hora de finalización.
ModifiedDate: Es de tipo time, no null y representa la fecha de las modificaciones que se realicen.