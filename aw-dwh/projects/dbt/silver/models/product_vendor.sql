select
    productid,
    vendorid
from {{ source('bronze', 'productvendor') }}