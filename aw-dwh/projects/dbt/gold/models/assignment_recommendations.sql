with

salesperson_performance as (
    select
        s.businessentityid,
        p.firstname,
        p.lastname,
        sum(soh.subtotal) as total_sales_amount,
        count(soh.salesorderid) as total_orders
    from {{ source('silver', 'salesperson') }} s
    inner join {{ source('silver', 'salesorderheader') }} soh
        on s.businessentityid = soh.salespersonid
    inner join {{ source('silver', 'person') }} p
        on s.businessentityid = p.businessentityid
    group by 1, 2, 3
),

ranked_salespeople as (
    select
        *,
        dense_rank() over (order by total_sales_amount desc) as sales_rank
    from salesperson_performance
),

top_performers as (
    select
        businessentityid,
        firstname,
        lastname,
        total_sales_amount,
        total_orders
    from ranked_salespeople
    where sales_rank <= 5 
),

-- Rendimiento de cada territorio

territory_performance as (
    select
        st.territoryid,
        st.name as territory_name,
        st.countryregioncode,
        st.salesytd,            
        st.saleslastyear,          
     
        (st.salesytd - st.saleslastyear) as sales_growth
    from {{ source('silver', 'salesterritory') }} st
),

ranked_territories as (
    select
        *,
        dense_rank() over (order by salesytd asc) as performance_rank
    from territory_performance
    where salesytd > 0 
),

underperforming_territories as (
    select
        territoryid,
        territory_name,
        countryregioncode,
        salesytd,
        sales_growth
    from ranked_territories
    where performance_rank <= 5 
)

select
    tp.firstname || ' ' || tp.lastname as salesperson_name,
    tp.total_sales_amount as salesperson_current_sales,
    ut.territory_name,
    ut.countryregioncode,
    ut.salesytd as territory_current_sales,
    ut.sales_growth,

    -- Prioridad de la recomendacion

    row_number() over(
        order by
            tp.total_sales_amount desc, 
            ut.salesytd asc             
    ) as recommendation_priority

from top_performers tp
cross join underperforming_territories ut

order by
    recommendation_priority