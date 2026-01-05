# AdventureWorks HR Files

## Resumen

Es una base de datos conformada por archivos csv, donde se encuentra información sobre los departamentos de la empresa y los empleados.

## Modelo conceptual

Una representación conceptual de la fuente de datos utilizando Modelo Entidad Relacionalidad Extendido (MERX) que muestre las entidades, interrelaciones y atributos.

## Modelo lógico

Shift(
    ShiftId (PK)
    Name
    StartTime
    EndTime
    ModifiedD)

EmployeePayHistory(
    BusinessEntityId
    RateChangeDate
    Rate
    PayFrequency
    ModifiedDate)

EmployeeDepartmentHistory(
    BusinessEntityId (PK)
    DepartmentId (PK, FK->Department.DepartmentId)
    ShiftId (PK, FK->Shift.ShiftId)
    StartDate
    EndDate
    ModifiedDate)

Department(
    DepartmentId (PK)
    Name
    GroupName
    ModifiedDate
)

## Catálogo de datos

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

### Department
Propósito: Información sobre los departamentos.
DepartmentId: Es de tipo entero, no null y representa el ID de los departamentos.
Name: Es de tipo varchar, no null y representa el nombre de los departamentos.
GroupName: Es de tipo varchar, nu null y representa el nombre del grupo al que pertenece el departamento.
ModifiedDate: Es de tipo time, no null y representa la fecha de las modificaciones que se realicen.
