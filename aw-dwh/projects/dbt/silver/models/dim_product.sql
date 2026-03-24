select
    productid,
    name,
    standardcost,
    listprice,
    productsubcategoryid
from {{ source('bronze', 'product') }}
where finishedgoodsflag = 0 