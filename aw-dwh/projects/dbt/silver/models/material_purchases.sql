select
    productid,
    transactiondate,
    quantity,
    actualcost 
from {{ source('bronze', 'transactionhistory') }}
where transactiontype = 'P' 