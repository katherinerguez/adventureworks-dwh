# AdventureWorks Core

## Resumen

AdventureWorks es una base de datos de ejemplo gratuita creada por Microsoft para SQL Server.   Simula una empresa ficticia de bicicletas llamada "Adventure Works Cycles".   La base de datos está organizada en esquemas lógicos que agrupan tablas según áreas de negocio, lo que facilita la navegación y el aprendizaje.   La base de datos presenta una estructura desnormalizada (esquema estrella), optimizada para consultas complejas y grandes volúmenes de datos.   

## Modelo conceptual

Una representación conceptual de la fuente de datos utilizando Modelo Entidad Relacionalidad Extendido (MERX) que muestre las entidades, interrelaciones y atributos.  



## Modelo lógico

Address(AddressId (PK)
    AddressLine1    
    AddressLine2
    City    
    StateProvinceId (FK->StateProvince.StateProvinceId)  
    PostalCode  
    SpatialLocation  
    rowguid   
    ModifiedDate)

AddressType(
    AddressTypeId  (PK)  
    Name
    rowguid   
    ModifiedDate)    

BillOfMaterials(
    BillOfMaterialsId (PK)   
    ProductAssemblyId (FK->Product.ProductId)   
    ComponentId   (FK->Product.ProductId)
    StartDate   
    EndDate  
    UnitMeasureCode (FK->UnitMeasure.UnitMeasureCode)   
    BOMLevel     
    PerAssemblyQty     
    ModifiedDate)

BusinessEntity( 
    BusinessEntityId (PK)
    rowguid   
    ModifiedDate)

BusinessEntityAddress(
    BusinessEntityId  (PK, FK->BusinessEntity.BusinessEntityId)
    AddressId  (PK, FK->Addres.Address.Id)
    AddressTypeId  (PK, FK->AddressType.AddressTypeId)
    rowguid   
    ModifiedDate)

BusinessEntityContact(
    BusinessEntityId  (PK, FK->BusinessEntity.BusinessEntityId)
    PersonId    (PK, FK->Person.PersonId)
    ContactTypeId (PK, FK->ContactType.ContactTypeId)   
    rowguid    
    ModifiedDate)

ContactType(
    ContactTypeId  (PK)
    Name   
    ModifiedDate)

CountryRegion(
    CountryRegionCode (PK)   
    Name   
    ModifiedDate)

CountryRegionCurrency(
    CountryRegionCode  (PK, FK->CountryRegion.CountryRegionCode) 
    CurrencyCode  (PK, FK->Currency.CurrencyCode) 
    ModifiedDate)

CreditCard(
    CreditCardId  (PK)
    CardType     
    CardNumber   
    ExpMonth    
    ExpYear     
    ModifiedDate)

Culture(
    CultureId   (PK) 
    Name     
    ModifiedDate)

Currency(
    CurrencyCode  (PK)  
    Name    
    ModifiedDate)

CurrencyRate(
    CurrencyRateId   (PK)
    CurrencyRateDate     
    FromCurrencyCode  (FK->Currency.CurrencyCode) 
    AverageRate     
    EndOfDayRate   
    ModifiedDate)

Customer(
    CustomerId  (PK) 
    PersonId  (FK->Person.PersonId)
    StoreId    (FK->Store.StoreId)
    TerritoryId    (FK->SalesTerritory.TerritoryId)
    AccountNumber
    rowguid   
    ModifiedDate)

EmailAddress( 
    BusinessEntityId (PK, FK->Person.PersonId)  
    EmailAddressId
    EmailAddress  
    rowguid  
    ModifiedDate)

Employee( 
    BusinessEntityId  (PK, FK->Person.PersonId)
    NationalIdNumber 
    LoginId  
    OrganizationNode  
    OrganizationLevel
    JobTitle
    BirthDate
    MaritalStatus 
    Gender  
    HireDate   
    SalariedFlag  
    VacationHours 
    SickLeaveHours  
    CurrentFlag
    rowguid  
    ModifiedDate)  

Illustration(
    IllustrationId (PK)
    Diagram   
    ModifiedDate) 

JobCandidate(
    JobCandidateId  (PK)
    BusinessEntityId  (FK->Employee.EmployeeId)
    Resume  
    ModifiedDate) 

Location( 
    LocationId  (PK) 
    Name  
    CostRate  
    Availability   
    ModifiedDate)  

Password(
    BusinessEntityId  (PK, FK->Person.PersonId)
    PasswordHash   
    PasswordSalt
    rowguid  
    ModifiedDate)

Person( 
    BusinessEntityId  (PK, FK->BusinessEntity.BusinessEntityId)
    PersonType  
    NameStyle: 
    Title  
    FirstName  
    MiddleName  
    LastName   
    Suffix
    AdditionalContactInfo 
    Demographics 
    rowguid  
    ModifiedDate)  

PersonCreditCard(
    BusinessEntityId  (PK, FK->Person.PersonId)
    CreditCardId   (PK, FK->CreditCard.CreditCardId)
    ModifiedDate)  

PersonPhone(
    BusinessEntityId (PK, FK->Person.PersonId)
    PhoneNumber (PK)
    PhoneNumberTypeId (PK, FK->PhoneNumberType.PhoneNumberTypeId)
    ModifiedDate) 

PhoneNumberType( 
    PhoneNumberTypeId (PK)
    Name   
    ModifiedDate)

Produt( 
    ProductId  (PK)
    Name  
    ProductNumber   
    MakeFlag  
    Color  
    SafetyStockLevel   
    ReorderPoint
    StandardCost 
    ListPrice  
    Size 
    SizeUnitMeasureCode (FK->UnitMeasure.UnitMeasureCode)
    WeightUnitMeasureCode (FK->UnitMeasure.UnitMeasureCode)
    Weight
    DaysToManufacture 
    ProductLine
    Class  
    Style  
    ProductSubcategoryId (FK->ProductSubcategory.ProductSubcategoryId)
    ProductModelId (FK->ProductModel.ProductModelId)
    SellStartDate 
    SellEndDate  
    DiscontinuedDate
    rowguid  
    ModifiedDate)  

ProductCategory(  
    ProductCategoryId (PK)
    Name  
    rowguid 
    ModifiedDate)  

ProductCostHistory(
    ProductId  (PK, FK->Product.ProductId)
    StartDate (PK)
    EndDate  
    StandardCost  
    ModifiedDate) 

ProductDescription( 
    ProductDescriptionId (PK)
    Description 
    rowguid
    ModifiedDate)  

ProductInventory(
    ProductId (PK, FK->Prduct.ProductId)
    LocationId (PK, FK->Location.LocationId)
    Shelf   
    Bin
    Quantity  
    rowguid  
    ModifiedDate) 

ProductListPriceHistory(
    ProductId (PK, FK->Product.ProductId)
    StartDate  (PK)
    EndDate   
    ListPrice 
    ModifiedDate)  

ProductModel(
    ProductModelId (PK)
    Name
    CatalogDescription  
    Instructions  
    rowguid  
    ModifiedDate)

ProductModelIllustration(
    ProductModelId (PK, FK->ProductModel.ProductModelId)
    IllustrationId  (PK, FK->Illustration.IllustrationId)
    ModifiedDate) 

ProductModelProductDescriptionCulture(
    ProductModelId (PK, FK->ProductModel.ProductModelId)
    ProductDescriptionId (PK, FK->ProductDescription.ProductDescriptionId)
    CultureId  (PK, FK->Culture.CultureId)
    ModifiedDate) 

ProductPhoto(
    ProductPhotoId (PK)
    ThumbNailPhoto
    ThumbNailPhotoFileName
    LargePhoto
    LargePhotoFileName
    ModifiedDate) 

ProductProductPhoto(
    ProductId  (PK, FK->Prduct.ProductId)
    ProductPhotoId  (PK, FK->PrductPhoto.ProductPhotoId)
    Primary
    ModifiedDate) 

ProductSubcategory(
    ProductSubcategoryId  (PK)
    ProductCategoryId  (FK->ProductCategory.ProductCategoryId)
    Name  
    rowguid  
    ModifiedDate) 

ProductVendor(
    ProductId (PK, FK->Product.ProductId)
    BusinessEntityId (PK, FK->Vendor.VendorId)
    AverageLeadTime
    StandardPrice
    LastReceiptCost
    LastReceiptDate
    MinOrderQty
    MaxOrderQty
    OnOrderQty
    UnitMeasureCode (FK->UnitMeasure.UnitMeasureCode)
    ModifiedDate
    )
 

PurchaseOrderDetail 
    (PurchaseOrderId (PK, FK->PurchaseOrder.PurchaseOrderId)
    PurchaseOrderDetailId (PK)
    DueDate
    OrderQty
    ProductId (FK->Product.ProductId)
    UnitPrice
    LineTotal
    ReceivedQty
    RejectedQty
    StockedQty
    ModifiedDate ) 

PurchaseOrderHeader(
    PurchaseOrderId  (PK)
    RevisionNumber 
    Status  (PK)
    EmployeeId (FK->Employee.EmployeeId)
    VendorId (FK->Vendor.VendorId)
    ShipMethodId  (FK->ShipMethod.ShipMethodId)
    OrderDate
    ShipDate
    SubTotal
    TaxAmt
    Freight
    TotalDue
    ModifiedDate
)
  

SalesOrderDetail
(
    SalesOrderId (PK, FK->SalesOrderHeader.SalesOrderId)
    SalesOrderDetailId (PK)
    CarrierTrackingNumber
    OrderQty
    ProductId (FK->Product.ProductId)
    SpecialOfferId  (FK->SpecialOffer.SpecialOfferId)
    UnitPrice
    UnitPriceDiscount
    LineTotal
    rowguid
    ModifiedDate
    )  

SalesOrderHeader
    (
    SalesOrderId (PK)
    RevisionNumber
    OrderDate
    DueDate
    ShipDate
    Status
    OnlineOrderFlag
    SalesOrderNumber
    PurchaseOrderNumber
    AccountNumber
    CustomerId (FK->Customer.CustomerId)
    SalesPersonId  (FK->SalesPerson.SalesPersonId)
    TerritoryId (FK->SalesTerritory.TerritoryId)
    BillToAddressId (FK->Address.AddressId)
    ShipToAddressId (FK->Address.AddressId)
    ShipMethodId (FK->ShipMethod.ShipMethodId)
    CreditCardId (FK->CreditCard.CreditCardId)
    CreditCardApprovalCode
    CurrencyRateId (FK->CurrencyRate.CurrencyRateId)
    SubTotal
    TaxAmt
    Freight
    TotalDue
    Comment
    rowguid
    ModifiedDate
    )

SalesOrderHeaderSalesReason(
    SalesOrderId  (PK, FK->SalesOrderHeader.SalesOrderId )
    SalesReasonId (PK, FK->SalesReason.SalesReason) 
    ModifiedDate) 

SalesPerson: 
    (
    BusinessEntityId (PK, FK->Employee.EmployeeId)
    TerritoryId (FK->SalesTerritory.TerritoryId)
    SalesQuota
    Bonus
    CommissionPct
    SalesYTD
    SalesLastYear
    rowguid
    ModifiedDate
    ) 

SalesPersonQuotaHistory 
    (BusinessEntityId (PK, FK->SalesPerson.SalesPersonId)
    QuotaDate  (PK)
    SalesQuota  
    rowguid 
    ModifiedDate ) 

SalesReason(
    SalesReasonId (PK)
    Name   
    ReasonType  
    ModifiedDate )

SalesTaxRate(
    SalesTaxRateId (PK)
    StateProvinceId  (FK->StateProvince.StateProvinceId)
    TaxType  
    TaxRate
    Name   
    rowguid  
    ModifiedDate) 

SalesTerritory(
    TerritoryId (PK)
    Name   
    CountryRegionCode (FK->CountryRegion.CountryRegionCode)
    Group  
    SalesYTD  
    SalesLastYear  
    CostYTD 
    CostLastYear 
    rowguid 
    ModifiedDate)  

SalesTerritoryHistory( 
    BusinessEntityId (PK, FK->SalesPerson.SalesPersonId)
    TerritoryId  (PK, FK->SalesTerritory.TerritoryId)
    StartDate (PK)
    EndDate 
    rowguid
    ModifiedDate) 

ScrapReason( 
    ScrapReasonId (PK)
    Name   
    ModifiedDate)
ShipMethod(
    ShipMethodId (PK)
    Name   
    ShipBase  
    ShipRate   
    rowguid 
    ModifiedDate) 

ShoppingCartItem( 
    ShoppingCartItemId (PK)
    ShoppingCartId 
    Quantity
    ProductId  (FK->Product.ProductId)
    DateCreated 
    ModifiedDate)  

SpecialOffer( 
    SpecialOfferId (PK)  
    Description  
    DiscountPct
    Type 
    Category 
    StartDate
    EndDate
    MinQty
    MaxQty
    rowguid  
    ModifiedDate) 

SpecialOfferProduct( 
    SpecialOfferId (PK, FK->SpecialOffer.SpecialOfferId)
    ProductId (PK, FK->Product.ProductId)
    rowguid  
    ModifiedDate)  

StateProvince( 
    StateProvinceId  (PK)
    StateProvinceCode  
    CountryRegionCode  (FK->CountryRegion.CountryRegionCode)
    IsOnlyStateProvinceFlag  
    Name   
    TerritoryId  (FK->SalesTerritory.TerritoryId)
    rowguid 
    ModifiedDate)  

Store(  
    BusinessEntityId  (PK, FK->BusinessEntity.BusinessEntityId)
    Name  
    SalesPersonId (FK->SalesPerson.SalesPersonId)
    Demographics
    rowguid  
    ModifiedDate)  

TransactionHistory(
    TransactionId   (PK)
    ProductId   
    ReferenceOrderId 
    ReferenceOrderLineId  
    TransactionDate  
    TransactionType  
    Quantity  
    ActualCost  
    ModifiedDate) 

UnitMeasure(
    UnitMeasureCode  (PK)
    Name  
    ModifiedDate)  

Vendor(
    BusinessEntityId (PK, FK->BusinessEntity.BusinessEntityId)
    AccountNumber
    Name 
    CreditRating  
    PreferredVendorStatus
    ActiveFlag  
    PurchasingWebServiceURL 
    ModifiedDate )

WorkOrder(
    WorkOrderId  (PK)
    ProductId (FK->Product.ProductId)
    OrderQty
    ScrappedQty   
    StockedQty 
    StartDate
    EndDate
    DueDate 
    ScrapReasonId  (FK->ScrapReason.ScrapReasonId)
    ModifiedDate)  

WorkOrderRouting( 
    WorkOrderId  (PK, FK->WorkOrder.WorkOrderId)
    ProductId   (PK)
    OperationSequence (PK)
    LocationId   (FK->Location.LocationId)
    ScheduledStartDate  
    ScheduledEndDate
    ActualStartDate 
    ActualEndDate  
    ActualResourceHrs 
    PlannedCost  
    ActualCost   
    ModifiedDate) 

## Catálogo de datos

### Address: 
Propósito: Almacena todas las direcciones  
AddressId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las direcciones  
AddressLine1: Es de tipo varchar(60), donde se acepta cadenas de textos hasta 60 caracteres, es de valor no null y representa las direcciones.     
AddressLine2: Es de tipo varchar(60), donde se acepta cadenas de textos hasta 60 caracteres, acepta valores null.     
City: Es de tipo varchar(30), donde se acepta cadenas de textos hasta 30 caracteres, acepta valores null y representa la ciudad de la dirreción.    
StateProvinceId: Es de tipo entero, no acepta valores null, representa el código correspondiente al estado provincial y puede contener valores duplicados.    
PostalCode: Es de tipo varchar(15), solo acepta cadenas de textos y hasta 15 caracteres, no acepta valores null y representa el código postal correspondiente.    
SpatialLocation: Es de tipo varchar(200), donde acepta cadenas de textos de hasta 200 caracteres, acepta valores null y representa la ubicación espacial.    
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null.    
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.     

### AddressType:
Propósito: Almacena el tipo de las direcciones, el tipo de lugar desde donde se puede realizar.    
AddressTypeId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de el tipo de las direcciones.     
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de los tipos de direcciones.     
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.    
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.     

### BillOfMaterials: 
Propósito: Presenta la lista de materiales.    
BillOfMaterialsId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de la lista de materiales.    
ProductAssemblyId: Es de tipo entero, acepta valores null, representa el ID de ensamblaje del producto y puede contener valores duplicados.    
ComponentId: Es de tipo entero, no acepta valores null y representa el ID del componente y puede teneer valores duplicados.    
StartDate: Es de tipo datetime, no acepta valores null, maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual y representa la fecha de inicio (año-mes-día).    
EndDate: Es de tipo datetime, acepta valores null y representa la fecha de finalización.    
UnitMeasureCode: Es de tipo char(3), donde acepta cadenas de textos de solo 3 caracteres, no acepta valores null, puede tener valores duplicados y representa el código de medida de unidad.    
BOMLevel: Es de tipo smallint, donde acepta números hasta 16 bits, es de valor no null y representa el nivel de la lista de materiales.     
PerAssemblyQty: Es de tipo decimal(8,2), donde se acepta números que tengan hasta 8 dígitos en total de los cuales 2 pueden estar después del punto decimal, no acepta valores null y si no se proporciona un valor al insertar un nuevo registro en la base de datos el campo tomará automáticamente el valor 1.  00.     
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.     

### BusinessEntity: 
Propósito: Presenta las entidades comerciales.    
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las entidades.    
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.    
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.     

### BusinessEntityAddress: 
Propósito: Presenta las direcciones de las entidades comerciales.    
BusinessEntityId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades.    
AddressId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único, representa el ID de las direcciones.    
AddressTypeId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único, representa el ID de el tipo de las direcciones.    
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.    
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.     

### BusinessEntityContact: 
Propósito: Presenta lcontactos de las entidades comerciales.    
BusinessEntityId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades.    
PersonId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único, representa el ID de las personas.    
ContactTypeId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único, representa el ID de el tipo de contactos.    
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.    
ModifiedDate: Es de tipo datetime, no acepta valores null y permite que se mantenga automáticamente la fecha y hora en que se creó y actualizó un registro.     

### ContactType: 
Propósito: Presenta los tipos de contactos.    
ContactTypeId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de los tipos de contactos.    
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de los tipos de contactos.     
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.    

### CountryRegion: 
Propósito: Presenta información sobre la región del país.    
CountryRegionCode: Es de tipo varchar(3), acepta cadenas de texto hasta 3 caracteres, es la llave primaria por lo que no puede ser null y es de valor único, representa el código de la región el país.    
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de los países.     
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.    

### CountryRegionCurrency: 
Propósito: Presenta información sobre la moneda dependiendo de la región del país.    
CountryRegionCode: Es de tipo varchar(3), acepta cadenas de texto hasta 3 caracteres, es la llave primaria por lo que no puede ser null y es de valor único, representa el código de la región el país.    
CurrencyCode: Es de tipo char(3), donde se acepta cadenas de textos solo de 3 caracteres, es llave primaria y es de valor no null y representa el código de la moneda.     
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.    

### CreditCard: 
Propósito: Presenta información sobre las tarjetas de créditos.    
CreditCardId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las tarjetas de créditos.     
CardType: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el tipo de tarjeta.     
CardNumber: Es de tipo varchar(25), donde se acepta cadenas de textos hasta 25 caracteres, es de valor no null y representa el número de la tarjeta.   
ExpMonth: Es de tipo tinyint, donde se acepta enteros de hasta 8 bits, es de valor no null y representa el mes de vencimiento.    
ExpYear: Es de tipo smallint, donde se acepta enteros de hasta 16 bits, es de valor no null y representa el año de vencimiento.     
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.    

### Culture: 
Propósito: Presenta información sobre las diferentes culturas.    
CultureId: Es de tipo char(6), acepta cadenas de texto de solo 6 caracteres, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las culturas.    
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de las culturas.     
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.    

### Currency: 
Propósito: Presenta información sobre las divisas.    
CurrencyCode: Es de tipo char(3), acepta cadenas de texto de solo 3 caracteres, es la llave primaria por lo que no puede ser null y es de valor único, representa el código de las diferentes divisas.    
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de las divisas.     
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.    

### CurrencyRate: 
Propósito: Presenta información sobre los tipos de cambios de las divisas.    
CurrencyRateId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de los tipos de cambios.     
CurrencyRateDate: Es de tipo datatime, es de valor no null y representa la fecha del cambio.     
FromCurrencyCode: Es de tipo char(3), donde se acepta cadenas de textos hasta 3 caracteres, es de valor no null y puede tener duplicados, representa el código de moneda.     
AverageRate: Es de tipo , donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y si no se proporciona un valor al insertar un nuevo registro en la base de datos el campo tomará automáticamente el valor 0.  0000.     
EndOfDayRate: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y si no se proporciona un valor al insertar un nuevo registro en la base de datos el campo tomará automáticamente el valor 0.  0000 y representa la tarifa de fin de día.    
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.    

### Customer: 
Propósito: Presenta información sobre los clientes.    
CustomerId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de los clientes.     
PersonId: Es de tipo entero, acepta valor null, puede tener duplicados y representa el ID de las personas.     
StoreId: Es de tipo entero, acepta valor null y puede tener duplicados, representa el ID de la tienda.     
TerritoryId: Es de tipo entero, acepta valor null y puede tener duplicados.    
AccountNumber: Es de tipo varchar(20), donde se acepta cadenas de texto hasta 20 caracteres, no acepta valores null.     
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.    
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.    

### EmailAddress: 
Propósito: Presenta información sobre los correos electrónicos.  
BusinessEntityId: Es de tipo entero, no puede ser null, representa el ID de la entidad de negocio y puede tener valores duplicados.   
EmailAddressId: Es de tipo entero, no acepta valor null y representa el ID de los correos.   
EmailAddress: Es de tipo varchar(50), acepta cadenas de texto de hasta 50 caracteres, puede tener valores null y representa los correos electrónicos.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### Employee: 
Propósito: Presenta información sobre los empleados.  
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades del negocio.   
NationalIdNumber: Es de tipo varchar(15), acepta cadenas de texto de hasta 15 caracteres, no acepta valor null, es único y representa el número de identificación nacional.   
LoginId: Es de tipo varchar(256), acepta cadenas de texto de hasta 256 carateres, no acepta valor null y es único, representa el ID de inicio de sesión.   
OrganizationNode: Es de tipo varchar(255), acepta cadenas de texto de hasta 255 caracteres, acepta valor null y respresenta el nodo de organización.  
OrganizationLevel: Es de tipo entero, acepta valores null y representa el nivel de organización.  
JobTitle: Es de tipo varchar(50), acepta cadenas de texto de hasta 50 caracteres, no acepta valores null y representa el nombre del titulo profesional
BirthDate: Es de tipo date, no acepta valores null y representa la fecha de nacimiento.  
MaritalStatus: Es de tipo char(1), acepta cadenas de texto de solo 1 caracter, no acepta valores null y representa el estado civil.  
Gender: Es de tipo char(1), acepta cadenas de texto de solo 1 caracter, no acepta valores null y representa el género.  
HireDate: Es de tipo date, no acepta valores null y representa la fecha de contratación.   
SalariedFlag: Es de tipo tinyint(1), acepta números enteros de un dígito (1 o 0), no acepta valores null y representa si el empleado es asalariado.  
VacationHours: Es de tipo smallint, acepta números de hasta 16 bits, no acepta valores null y por defecto pone 0, representa las horas de vacaciones.  
SickLeaveHours: Es de tipo smallint, acepta números de hasta 16 bits, no acepta valores null y representa las horas de baja por enfermedad.  
CurrentFlag: Es de tipo tinyint(1), acepta números de un digíto, no acepta valores nully representa la bandera actual.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### Illustration: 
Propósito: Presenta información sobre las ilustraciones.  
IllustrationId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las ilustraciones.  
Diagram: Es de tipo text, donde se acepta cadenas de textos, puede ser de valor null y representa quien diseñó las ilustraciones.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### JobCandidate: 
Propósito: Presenta información sobre los candidatos al puesto de trabajo.  
JobCandidateId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de los candidatos para el trabajo.  
BusinessEntityId: Es de tipo entero, puede ser de valor null y tener valores duplicados y representa el ID de las entidades del negocio.   
Resume: Es de tipo text, acepta cadenas de textos, acepta valores null.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### Location: 
Propósito: Presenta información sobre las localizaciones.  
LocationId: Es de tipo smallint, acepta números de hasta 16 bits, es la llave primaria, no puede ser null, es único y secuencial, representa el ID de las localizaciones.   
Name: Es de tipo varchar(50), acepta cadenas de texto de hasta 50 caracteres, no acepta valor null y representa el nombre de las localizaciones.   
CostRate: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no puede tener valores null, por defecto pone 0.  0000 y representa las tarifas de costo.   
Availability: Es de tipo decimal(8,2), donde se acepta números que tengan hasta 8 dígitos en total de los cuales 2 pueden estar después del punto decimal, no puede tener valores null, por defecto pone 0.  00 y representa la disponibilidad.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### Password: 
Propósito: Presenta información sobre las contraseñas.  
BusinessEntityId: Es de tipo entero, es la llave primaria, no puede ser null, es único, representa el ID de las entidades del negocio.   
PasswordHash: Es de tipo varchar(128), acepta cadenas de texto de hasta 128 caracteres, no acepta valor null y representa el hash de contraseñas.   
PasswordSalt: Es de tipo varchar(10), acepta cadenas de texto de hasta 10 caracteres, no puede tener valores null.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### Person: 
Propósito: Presenta información sobre las personas.  
BusinessEntityId: Es de tipo entero, es la llave primaria, no puede ser null, es único, representa el ID de las entidades del negocio.   
PersonType: Es de tipo char(2), acepta cadenas de texto de solo 2 caracteres, no acepta valor null y representa el tipo de persona.   
NameStyle: Es de tipo tinyint(1), donde acepta números de 1 dígito, no puede tener valores null, por defecto pone 0 y representa el estilo de nombre.   
Title: Es de tipo varchar(8), acepta cadenas de texto hasta 8 caracteres, puede tener valores null y representa el título.  
FirstName: Es de tipo varchar(50), acepta cadenas de texto hasta 50 caracteres, no acepta valores null y representa el primer nombre.  
MiddleName: Es de tipo varchar(50), acepta cadenas de texto de hasta 50 caracteres, puede tener valores null y representa el segundo nombre.  
LastName: Es de tipo varchar(50), acepta cadenas de texto de hasta 50 caracteres, no acepta valores null y representa el apellido.   
Suffix: Es de tipo varchar(10), acepta cadenas de texto de hasta 10 caracteres, puede ser null y representa los apodos.  
EmailPromotion: Es de tipo entero, no acepta valores null y por defecto pone 0 y representa la promoción por correo electrónico.  
AdditionalContactInfo: Es de tipo text, acepta cadenas de texto y valores null y representa la informacion adicional del contacto.  
Demographics: Es de tipo text, acepta cadenas de texto y valores null y representa la demografía.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### PersonCreditCard: 
Propósito: Presenta información sobre las tarjetas de créditos personales.  
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades del negocio.  
CreditCardId: Es de tipo entero, es llave primaria, no puede ser de valor null y es único y representa el ID de la tarjetas de créditos.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### PersonPhone: 
Propósito: Presenta información sobre los números de teléfonos personales.  
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades del negocio.  
PhoneNumber: Es de tipo varchar(25), acepta cadenas de texto hasta 25 caracteres, es llave primaria, no acepta valores null y es único, representa el número de teléfono.  
PhoneNumberTypeId: Es de tipo entero, es llave primaria, no puede ser de valor null y es único y representa el ID de el tipo de número de teléfono.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### PhoneNumberType: 
Propósito: Presenta información sobre tipos de números de teléfonos.  
PhoneNumberTypeId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de los tipos de números de teléfonos.  
Name: Es de tipo varchar, acepta cadenas de texto hasta 50 caracteres, no puede ser de valor null y representa el nombre de los tipos.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### Produt: 
Propósito: Presenta información sobre los productos.  
ProductId: Es de tipo entero, es la llave primaria, no puede ser null, es único y secuencial, representa el ID de los productos.   
Name: Es de tipo char(50), acepta cadenas de texto de solo 50 caracteres, no acepta valor null y representa el nombre del producto.   
ProductNumber: Es de tipo varchar(25), donde acepta cadenas de texto hasta 25 caracteres, no puede tener valores null y representa el número del producto.   
MakeFlag: Es de tipo tinyint(1), acepta números de 1 dígito, no puede tener valores null.  
FinishedGoodsFlag: Es de tipo tinyint(1), acepta números de 1 dígito, no puede tener valores null y representa si el producto terminó.  
Color: Es de tipo varchar(15), acepta cadenas de texto de hasta 15 caracteres, puede tener valores null y representa el color del producto.  
SafetyStockLevel: Es de tipo smallint, donde acepta números hasta 16 bits, no acepta valores null y representa el nivel de stock de seguridad.   
ReorderPoint: Es de tipo smallint, donde acepta números hasta 16 bits, no puede ser null y representa el punto de reorden.  
StandardCost: Es de tipo decimal(19,4),  donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y representa el costo estándar.  
ListPrice: Es de tipo decimal(19,4),  donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y representa la lista de los precios.  
Size: Es de tipo varchar(5), acepta cadenas de texto hasta 5 caracteres y valores null y representa el tamaño.  
SizeUnitMeasureCode: Es de tipo char(3), acepta cadenas de texto de solo 3 caracteres y valores null, puede tener valores duplicados y representa el código de medida de tamaño.  
WeightUnitMeasureCode: Es de tipo char(3), acepta cadenas de texto de solo 3 caracteres y valores null, puede tener valores duplicados y representa el código de unidad de medida de peso.  
Weight: Es de tipo decimal(8,2), donde se acepta números que tengan hasta 8 dígitos en total de los cuales 2 pueden estar después del punto decimal, acepta valores null y representa el peso.  
DaysToManufacture: Es de tipo entero, no acepta valores null y representa los días para fabricar.  
ProductLine: Es de tipo varchar(2), acepta cadenas de texto de hasta 2 caracteres y representa la linea de productos.  
Class: Es de tipo varchar(2), acepta cadenas de texto hasta 2 caracteres y valores null y representa la clase del producto.  
Style: Es de tipo varchar(2), acepta cadenas de texto hasta 2 caracteres y valores null y representa el estilo.  
ProductSubcategoryId: Es de tipo entero, acepta valores null y puede tern valores duplicados y representa el ID de subcategoría del producto.   
ProductModelId: Es de tipo entero, acepta valores null y puede tenr valores duplicados y representa el ID del modelo del producto.  
SellStartDate: Es de tipo datatime, no acepta valores null y representa la fecha de inicio de venta.  
SellEndDate: Es de tipo datatime, acepta valores null y representa la fecha del final de la venta.  
DiscontinuedDate: Es de tipo datatime, acepta valores null y representa la fecha de descontinuación.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductCategory: 
Propósito: Presenta información sobre la categoría de los productos.  
ProductCategoryId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las categorías de los productos.  
Name: Es de tipo varchar(50), acepta cadenas de texto hasta 50 caracteres, no acepta valores null, representa el número de las categorías.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductCostHistory: 
Propósito: Presenta información sobre el historial de los precios de los productos.  
ProductId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de los productos.  
StartDate: Es de tipo datatime, es la llave perimaria, no acepta valores null y es único, representa fecha de inicio.  
EndDate: Es de tipo datatime, acepta valores null y representa la fecha de final.   
StandardCost: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y representa el costo estándar.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductDescription: 
Propósito: Presenta información sobre la descripción de los productos.  
ProductDescriptionId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de la descripción de los productos.  
Description: Es de tipo varchar(400), acepta cadenas de texto hasta 400 caracteres, no acepta valores null, representa la descripción del producto.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductInventory: 
Propósito: Presenta información sobre inventario de los productos.  
ProductId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de los productos.  
LocationId: Es de tipo smallint, donde acepta números hasta 16 bits, es llave primaria, no acepta valores null y es único, representa el ID de la localización.  
Shelf: Es de tipo varchar(10), acepta cadenas de texto hasta 10 caracteres, no acepta valores null y representa los estantes.   
Bin: Es de tipo tinyint, donde se acepta enteros de hasta 8 bits, no acepta valores null y representa información sobre la papelera.  
Quantity: Es de tipo smallint, donde acepta números hasta 16 bits, no acepta valores null y por defecto pone 0 y representa la cantidad.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductListPriceHistory: 
Propósito: Presenta información sobre el historial de precios de la lista de productos.  
ProductId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de los productos.  
StartDate: Es de tipo datatime, es la llave perimaria, no acepta valores null y es único, representa fecha de inicio.  
EndDate: Es de tipo datatime, acepta valores null y representa la fecha de final.   
ListPrice: Es de tipo decimal(19,4),  donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null, representa la lista de precios.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductModel: 
Propósito: Presenta información sobre el modelo del producto.  
ProductModelId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de los modelos de los productos.  
Name: Es de tipo varchar(50), acepta cadenas de texto hasta 50 caracteres, no acepta valores nulll y representa el nombre del modelo.  
CatalogDescription: Es de tipo text, acepta cadenas d textos, acepta valores null, representa la descripción del catálogo.  
Instructions: Es de tipo text, acepta cadenas d etextos, acepta valores null y representa las intrucciones.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductModelIllustration: 
Propósito: Presenta información sobre las intrucciones de el modelo del producto.  
ProductModelId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de los modelos de los productos.  
IllustrationId: Es de tipo entero, es llave primaria, no acepta valores null y es único y representa el ID de las intrucciones.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductModelProductDescriptionCulture: 
Propósito: Presenta una descripción sobre el modelo de producto dependiendo de la cultura.  
ProductModelId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de los modelos de los productos.  
ProductDescriptionId: Es de tipo entero, es llave primaria, no acepta valores null y es único y representa el ID de las descripciones de los productos.   
CultureId: Es de tipo char(6), acepta cadenas de texto de solol 6 caracteres, es llave primaria, no acepta valores null y es único y representa el ID de la diferentes culturas.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductPhoto: 
Propósito: Presenta una descripción sobre las fotos de los productos.  
ProductPhotoId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las fotos de los productos.  
ThumbNailPhoto: Es de tipo text, acepta cadenas de texto, acepta valores null.   
ThumbNailPhotoFileName: Es de tipo varchar(50), acepta cadenas de texto de hasta 50 caracteres, acepta valores null y representa el archivo de las fotos minuaturas.  
LargePhoto: Es de tipo text, acepta cadenas de texto y valores null y representa el tamaño de las fotos.  
LargePhotoFileName: Es de tipo varchar(50), acepta cadenas de texto hasta 50 caracteres y valores null y representa el archivo del nombre de las fotos grandes
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductProductPhoto: 
Propósito: Presenta información sobre las fotos de los productos.  
ProductId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de los productos.  
ProductPhotoId: Es de tipo entero, es llave primaria, no acepta valores null, es único y representa el ID de las fotos de los productos.   
Primary: Es de tipo tinyint(1), acepta números de solo 1 dígito, no acepta valores null y por defecto toma el valor 0.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductSubcategory: 
Propósito: Presenta información sobre las subcategoría de los productos.  
ProductSubcategoryId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las subcategorías de los productos.  
ProductCategoryId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID de las categorías de los productos.   
Name: Es de tipo varchar(50), acepta cadenas de textos hasta 50 caracteres, no acepta valores null y representa el nombre de las subcategorías de productos.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ProductVendor: 
Propósito: Presenta información sobre los proveedores de los productos.  
ProductId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de los productos.  
BusinessEntityId: Es de tipo entero, es llave primaria, no acepta valores null, es único y representa el ID de las entidades del negocio.   
AverageLeadTime: Es de tipo entero, no acepta valores null y representa el tiempo de entrega promedio.  
StandardPrice: Es de tipo decimal(19, 4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y representa el precio estándar.  
LastReceiptCost: Es de tipo decimal(19, 4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, acepta valores null y representa el costo del último recibo.  
LastReceiptDate: Es de tipo datatime, acepta valores null y representa la fecha del último recibo.  
MinOrderQty: Es de tipo entero, no acepta valores null y representa la cantidad mínima pedida.  
MaxOrderQty: Es de tipo entero, no acepta valores null y representa la cantidad máxima pedida.  
OnOrderQty: Es de tipo entero, acepta valores null y representa la cantidad pedida.  
UnitMeasureCode: Es de tipo char(3), acepta cadenas de texto de solo 3 caracteres, no acepta valores null, puede tener valores repetidos y representa el código de medida de unidad.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### PurchaseOrderDetail: 
Propósito: Presenta detalles sobre la orden de compra.  
PurchaseOrderId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las orden de compra.  
PurchaseOrderDetailId: Es de tipo entero, es llave primaria, no acepta valores null, es único y representa el ID de los detalles de las compras.   
DueDate: Es de tipo datatime, no acepta valores null y representa la fecha de vencimiento.  
OrderQty: Es de tipo smallint, donde acepta números hasta 16 bits, no acepta valores null y representa cantidad de pedido.  
ProductId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID del producto.  
UnitPrice: Es de tipo decimal(19, 4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y representa el precio unitario.  
LineTotal: Es de tipo entero, acepta valores null, almacenará el total calculado de OrderQty * UnitPrice, asegurando que si alguno de esos valores es NULL, se guardará como 0.  00.  
ReceivedQty: Es de tipo decimal(8,2),  donde se acepta números que tengan hasta 8 dígitos en total de los cuales 2 pueden estar después del punto decimal, no acepta valores null y representa la cantidad recibida.  
RejectedQty: Es de tipo decimal(8,2), donde se acepta números que tengan hasta 8 dígitos en total de los cuales 2 pueden estar después del punto decimal, acepta valores null y por defecto toma 0.  00 y representa la cantidad rechazada.  
StockedQty: Es de tipo decimal(8,2), donde se acepta números que tengan hasta 8 dígitos en total de los cuales 2 pueden estar después del punto decimal, no acepta valores null, puede tener valores repetidos y representa la cantidad de existencia.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### PurchaseOrderHeader: 
Propósito: Presenta detalles sobre el encabezado de la orden de compra.  
PurchaseOrderId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las orden de compra.  
RevisionNumber: Es de tipo tinyint, donde se acepta enteros de hasta 8 bits, no acepta valores null, por defecto toma valor 0 y representa el número de la revisión.   
Status: Es de tipo tinyint, donde se acepta enteros de hasta 8 bits, no acepta valores null, por defecto toma valor 1 y representa el estado.   
EmployeeId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID de el empleado.  
VendorId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID de el proveedor.  
ShipMethodId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID del metodo de envío.  
OrderDate: Es de tipo datatime, no acepta valores null, se genera automático y representa la fecha de la orden de pedido.  
ShipDate: Es de tipo datatime, acepta valores null y representa la fecha del envío.  
SubTotal: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y por defecto toma 0.  0000 y representa el subtotal.  
TaxAmt: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto toma 0.  0000, no acepta valores null y representa monto de impuesto.  
Freight: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto toma 0.  0000, no acepta valores null y representa el transporte.   
TotalDue: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, almacenará el total calculado de (SubTotal + TaxAmt) + Freight, asegurando que si alguno de esos valores es NULL, se guardará como 0, no acepta valores null y representa el total adecuado.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesOrderDetail: 
Propósito: Presenta detalles sobre el pedido de venta.  
SalesOrderId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único, representa el ID de el pedido de venta.  
SalesOrderDetailId: Es de tipo entero, es llave primaria,no acepta valores null y es único y representa el ID del detalle de el pedido de venta.   
CarrierTrackingNumber: Es de tipo varchar(25), donde se acepta cadenas de texto hasta 25 caracteres, acepta valores null y representa el número de seguimiento del transportista.   
OrderQty: Es de tipo smallint, donde acepta números hasta 16 bits, no acepta valores null y representa el orden del pedido.  
ProductId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID de el producto.  
SpecialOfferId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID de la oferta especial.  
UnitPrice: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y representa el precio unitario.  
UnitPriceDiscount: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto toma 0.  0000, no acepta valores null y representa el descuento por precio unitario.  
LineTotal: Es de tipo entero, acepta valores null, almacenará el total calculado de UnitPrice * (1.  0-UnitPriceDiscount)* OrderQty, asegurando que si alguno de esos valores es NULL, se guardará como 0.  0.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesOrderHeader: 
Propósito: Presenta detalles sobre el encabezado de pedido de venta.  
SalesOrderId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único y seceuncial, representa el ID de el pedido de venta.  
RevisionNumber: Es de tipo tinyint, donde se acepta enteros de hasta 8 bits, no acepta valores null, por defecto toma valor 0 y representa el número de la revisión.  
OrderDate: Es de tipo datatime, no acepta valores null, se genera automático y representa la fecha de la orden de pedido.   
DueDate: Es de tipo datatime, no acepta valores null y representa la fecha de vencimiento.  
ShipDate: Es de tipo datatime, acepta valores null y representa la fecha del envío.  
Status: Es de tipo tinyint, donde se acepta enteros de hasta 8 bits, no acepta valores null, por defecto toma valor 1 y representa el estado.  
OnlineOrderFlag: Es de tipo tinyint(1), donde acepta enteros de un dígito, por defecto toma el valor 1, no acepta valores null y representa el pedido en línea.   
SalesOrderNumber: Es de tipo varchar(50), donde se acepta cadenas de texto hasta 50 caracteres, no acepta valores null y representa el número de pedido de venta.   
PurchaseOrderNumber: Es de tipo varchar(25), donde acepta cadenas de texto hasta 25 caracteres, acepta valores null y representa el número de orden de compra.  
AccountNumber: Es de tipo varchar(25), donde se acepta cadenas de texto hasta 25 caracteres, acepta valores null.   
CustomerId: Es de tipo entero, no puede ser null y puede tener duplicados, representa el ID de los clientes.   
SalesPersonId: Es de tipo entero, acepta valores null, puede tener valores duplicados y representa el ID de el vendedor.  
TerritoryId: Es de tipo entero, acepta valor null y puede tener duplicados.  
BillToAddressId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID de la dirección de facturación.  
ShipToAddressId: Es de tipo entero, puede tener duplicados, no acepta valores null y representa el ID de la dirección de envío.  
ShipMethodId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID del método de envío.  
CreditCardId: Es de tipo entero, no puede ser null, puede tenr valores duplicados y representa el ID de las tarjetas de créditos.   
CreditCardApprovalCode: Es de tipo vrachar(15), donde se acepta cadenas de texto hasta 15 caracteres, acepta valores null y representa el código de aprobación de la tarjeta.  
CurrencyRateId: Es de tipo entero, acepta valores null, puede tner valores duplicados y representa el ID de la tasa de cambio.   
SubTotal: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y por defecto toma 0.  0000 y representa el subtotal.  
TaxAmt: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto toma 0.  0000, no acepta valores null y representa monto de impuesto.  
Freight: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto toma 0.  0000, no acepta valores null y representa el transporte.   
TotalDue: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, almacenará el total calculado de (SubTotal + TaxAmt) + Freight, asegurando que si alguno de esos valores es NULL, se guardará como 0, acepta valores null y representa el total adecuado.   
Comment: Es de tipo varchar(128), acepta cadenas de texto hasta 128 caracteres, acepta valores null y representa los comenatrios.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesOrderHeaderSalesReason: 
Propósito: Presenta detalles sobre el encabezado de orden de venta.  
SalesOrderId: Es de tipo entero, es llave primaria por lo que no puede ser null y es de valor único, representa el ID de el pedido de venta.  
SalesReasonId: Es de tipo entero, es llave primaria, no acepta valores null y es único y representa el ID de motivo de venta.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesPerson: 
Propósito: Presenta detalles sobre las personas de la venta.  
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades.  
TerritoryId: Es de tipo entero, acepta valor null y puede tener duplicados.  
SalesQuota: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, puede ser null, representa las cuotas de ventas.  
Bonus: Es de tipo  decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, no puede ser null, representa los bonus.  
CommissionPct: Es de tipo decimal(10,4), donde se acepta números que tengan hasta 10 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, no puede ser null, representa la comisión
SalesYTD: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, no puede ser null, representa las ventas hasta la fecha.  
SalesLastYear: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, no puede ser null, representa las ventas del año pasado.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesPersonQuotaHistory: 
Propósito: Presenta detalles sobre el historial de las personas de la venta.  
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades.  
QuotaDate: Es de tipo datatime, es llave primaria, no acepta valor null y es único y representa la fecha de cotización.  
SalesQuota: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no puede ser null, representa las cuotas de ventas.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesReason: 
Propósito: Presenta detalles sobre la razón de las ventas.  
SalesReasonId: Es de tipo entero, es llave primaria, no acepta valores null, es único y secuencial y representa el ID de motivo de venta.  
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de las razones.   
ReasonType: Es de tipo varchar(50), acepta cadenas de texto hasta 50 caracteres, no puede ser null, representa el ID de las entidades.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesTaxRate: 
Propósito: Presenta detalles sobre la tasa de impuesto sobre las ventas.  
SalesTaxRateId: Es de tipo entero, es llave primaria, no acepta valores null, es único y secuencial y representa el ID de la tasa de impuesto de venta.  
StateProvinceId: Es de tipo entero, no acepta valores null, representa el código correspondiente al estado provincial y puede contener valores duplicados.  
TaxType: Es de tipo tinyint, donde se acepta enteros de hasta 8 bits, es de valor no null y representa el tipo de impuestos.  
TaxRate: Es de tipo decimal(10,4), donde se acepta números que tengan hasta 10 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y por defecto toma 0,0000 y representa la tasa de impuesto.  
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesTerritory: 
Propósito: Presenta detalles sobre los territorios de ventas.  
TerritoryId: Es de tipo entero, es llave primaria, no acepta valor null, es única y secuencial
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre.   
CountryRegionCode: Es de tipo varchar(3), acepta cadenas de texto hasta 3 caracteres, es la llave primaria por lo que no puede ser null y es de valor único, representa el código de la región el país.  
Group: Es de tipo varchar(50), acepta cadenas de texto hasta 50 caracteres, no acepta valores null y representa los grupos.  
SalesYTD: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, no puede ser null, representa las ventas hasta la fecha.  
SalesLastYear: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, no puede ser null, representa las ventas del año pasado.  
CostYTD: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, no puede ser null, representa el costo hasta la fecha.  
CostLastYear: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, es de valor no null y representa el costo del año pasado.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SalesTerritoryHistory: 
Propósito: Presenta detalles sobre el historial de los territorios de ventas.  
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades.  
TerritoryId: Es de tipo entero, es llave primaria, no acepta valor null, es única.  
StartDate: Es de tipo datetime, es llave primaria, no acepta valores null, es único y representa la fecha de inicio (año-mes-día).  
EndDate: Es de tipo datetime, acepta valores null y representa la fecha de finalización.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ScrapReason: 
Propósito: Presenta detalles sobre las razones de desecho.  
ScrapReasonId: Es de tipo smallint, donde acepta números hasta 16 bits, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las razones.  
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de las razones.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ShipMethod: 
Propósito: Presenta detalles sobre los métodos de envío.  
ShipMethodId: Es de tipo entero, es la llave primaria, no acepta valores null, es único y secuencial y representa el ID del metodo de envío.  
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de las razones.   
ShipBase: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, es de valor no null.   
ShipRate: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, es de valor no null.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### ShoppingCartItem: 
Propósito: Presenta detalles sobre los artículos del carrito de compras.  
ShoppingCartItemId: Es de tipo entero, es la llave primaria, no acepta valores null, es único y secuencial y representa el ID de los artículos del carrito.  
ShoppingCartId: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el ID del carrito.  
Quantity: Es de tipo entero, no acepta valores null y por defecto pone 1 y representa la cantidad.  
ProductId: Es de tipo entero, no acepta valores null, puede tener valores duplicados y representa el ID del producto.  
DateCreated: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual y representa la fecha de creación.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SpecialOffer: 
Propósito: Presenta detalles sobre las ofertas especiales.  
SpecialOfferId: Es de tipo entero, es la llave primaria, no acepta valores null, es único y secuencial y representa el ID de las ofertas especiales.  
Description: Es de tipo varchar(255), acepta cadenas de texto hasta 255 caracteres, no acepta valores null, representa la descripción.  
DiscountPct: Es de tipo decimal(10,4), donde se acepta números que tengan hasta 10 dígitos en total de los cuales 4 pueden estar después del punto decimal, por defecto puede tomar el valor 0,0000, es de valor no null y representa el porciento de descuento.  
Type: Es de tipo varchar(50), acepta cadenas de texto hasta 50 caracteres, no acepta valores null y representa el tipo.  
Category: Es de tipo varchar(50), acepta cadenas de texto hasta 50 caracteres, no acepta valores null y representa la categoría.  
StartDate: Es de tipo datetime, no acepta valores null y representa la fecha de inicio (año-mes-día).  
EndDate: Es de tipo datetime, no acepta valores null y representa la fecha de finalización.  
MinQty: Es de tipo entero, no acepta valores null, por defecto toma el valor 0 y representa la cantidad mínima.  
MaxQty: Es de tipo entero, acepta valore null y representa la cantidad máxima.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### SpecialOfferProduct: 
Propósito: Presenta detalles sobre las ofertas especiales de productos.  
SpecialOfferId: Es de tipo entero, es la llave primaria, no acepta valores null, es único y representa el ID de las ofertas especiales.  
ProductId: Es de tipo entero, es la llave primaria, no puede ser null, es único, representa el ID de los productos.   
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### StateProvince: 
Propósito: Presenta detalles sobre los estados.  
StateProvinceId: Es de tipo entero, es llave priamria, no acepta valores null, es único y secuencial, representa el ID correspondiente al estado provincial.  
StateProvinceCode: Es de tipo char(3), acepta cadenas de texto de solo 3 caracteres, no puede ser null, representa el código de los estados provinciales.   
CountryRegionCode: Es de tipo varchar(3), acepta cadenas de texto hasta 3 caracteres, no puede ser null, representa el código de la región el país y puede tenr valores duplicados.  
IsOnlyStateProvinceFlag: Es de tipo tinyint(1), acepta enteros de un dígito, no acepta valores null y representa si es estado provincial.  
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de las razones.   
TerritoryId: Es de tipo entero, acepta valor null y puede tener duplicados.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### Store: 
Propósito: Presenta detalles sobre las tiendas.  
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades.  
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de las razones.  
SalesPersonId: Es de tipo entero, acepta valores null, puede tener valores duplicados y representa el ID de el vendedor.  
Demographics: Es de tipo text, acepta cadenas de texto y valores null y representa la demografía.  
rowguid: Es de tipo char(36), acepta cadenas de texto de solo 36 caracteres, no acepta valores null y se genera autómaticamente y secuencial.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### TransactionHistory: 
Propósito: Presenta detalles sobre el historial de transacciones.  
TransactionId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de las transacciones.   
ProductId: Es de tipo entero, no puede ser null, representa el ID de los productos y puede tener valores duplicados.   
ReferenceOrderId: Es de tipo entero, es de valor no null y representa el ID de pedidos de referencia.  
ReferenceOrderLineId: Es de tipo entero, no acepta valores null, toma como valor por defecto 0 y representa el ID de línea de pedido de referencia.  
TransactionDate:  Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual y representa la fecha de las transacciones.  
TransactionType: Es de tipo char(1), acepta cadenas de texto de solo 1 caracter, no acepta valores null y representa el tipo de las transacciones.  
Quantity: Es de tipo entero, no acepta valores null y representa la cantidad.  
ActualCost: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, es de valor no null y representa el costo actual.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### UnitMeasure: 
Propósito: Presenta detalles sobre las unidades de medidas.    
UnitMeasureCode: Es de tipo char(3), donde acepta cadenas de textos de solo 3 caracteres, es llave primaria, no acepta valores null, es único y representa el código de medida de unidad.  
Name: Es de tipo varchar(50), donde se acepta cadenas de textos hasta 50 caracteres, es de valor no null y representa el nombre de las medidas.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### Vendor: 
Propósito: Presenta detalles sobre los proveedores.  
BusinessEntityId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de las entidades.  
AccountNumber: Es de tipo varchar(20), donde se acepta cadenas de texto hasta 20 caracteres, no acepta valores null.   
Name: Es de tipo varchar(100), donde se acepta cadenas de textos hasta 100 caracteres, es de valor no null y representa el nombre de los proveedores.  
CreditRating: Es de tipo tinyint, donde se acepta enteros de hasta 8 bits, no acepta valores null y representa el calificación creditaria.  
PreferredVendorStatus: Es de tipo tinyint(1) , acepta enteros de un dígito, no acepta valores null y representa el estado del proveedor preferido, toma por defecto el valor 1.  
ActiveFlag: Es de tipo tinyint(1), acepta enteros de un dígito, no acepta valores null y por defecto toma el valor 1.  
PurchasingWebServiceURL: Es de tipo varchar(1024), acepta cadenas de texto hasta 1024 caracteres, acepta valores null y representa la URL del servicio web de compras.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### WorkOrder: 
Propósito: Presenta detalles sobre el orden de trabajo.  
WorkOrderId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único y secuencial, representa el ID de el orden de trabajo.  
ProductId: Es de tipo entero, no puede ser null, representa el ID de los productos y puede tener valores duplicados.   
OrderQty: Es de tipo entero, no acepta valores null y representa cantidad de pedido.  
ScrappedQty: Es de tipo entero, no acepta valores null y representa la cantidad desechada.   
StockedQty: Es de tipo entero, almacena el total calculado de OrderQty-ScrappedQty y sino toma valor 0, acepta valores null y representa la cantidad de existencia.  
StartDate: Es de tipo datetime, no acepta valores null y representa la fecha de inicio (año-mes-día).  
EndDate: Es de tipo datetime, acepta valores null y representa la fecha de finalización.  
DueDate: Es de tipo datatime, no acepta valores null y representa la fecha de vencimiento.  
ScrapReasonId: Es de tipo smallint, donde acepta números hasta 16 bits, acepta valores null, representa el ID de las razones y puede tener valores duplicados.  
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  

### WorkOrderRouting: 
Propósito: Presenta detalles sobre las rutas del orden de trabajo.  
WorkOrderId: Es de tipo entero, es la llave primaria por lo que no puede ser null y es de valor único, representa el ID de el orden de trabajo.  
ProductId: Es de tipo entero, es llave primaria, no puede ser null y es de valor único, representa el ID de los productos.   
OperationSequence: Es de tipo smallint, donde acepta números hasta 16 bits, es llave orimaria, no acepta valores null, es único y representa la secuencia de operación.   
LocationId: Es de tipo smallint, acepta números de hasta 16 bits, es la llave primaria, no puede ser null, representa el ID de las localizaciones y los valores puede estar duplicados.   
ScheduledStartDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual y representa la fecha de inicio programada.  
ScheduledEndDate: Es de tipo datetime, no acepta valores null y representa la fecha de inicio (año-mes-día).  
ActualStartDate: Es de tipo datetime, acepta valores null y representa la fecha de inicio final.  
ActualEndDate: Es de tipo datetime, acepta valores null y representa la fecha de vencimiento.  
ActualResourceHrs: Es de tipo decimal(9,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y representa las horas de recursos reales.  
PlannedCost: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, no acepta valores null y representa el costo planificado.  
ActualCost: Es de tipo decimal(19,4), donde se acepta números que tengan hasta 19 dígitos en total de los cuales 4 pueden estar después del punto decimal, acepta valores null y representa el costo actual.   
ModifiedDate: Es de tipo datetime, no acepta valores null, y maneja automáticamente la fecha y hora en registros sin necesidad de intervención manual.  