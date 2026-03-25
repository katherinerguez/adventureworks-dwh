with

material_criticality as (
    select
        bom.componentid as productid,
        count(distinct bom.productassemblyid) as number_of_products_used_in,
        sum(bom.perassemblyqty) as total_quantity_in_boms
    from {{ ref('bill_of_materials') }} bom 
    group by 1
),

price_volatility as (
    select
        productid,
        avg(actualcost) as average_cost,
        stddev(actualcost) as price_volatility_score
    from {{ ref('material_purchases') }}
    group by 1
),

supply_risk as (
    select
        productid,
        count(distinct vendorid) as number_of_suppliers
    from {{ ref('product_vendor') }}
    group by 1
),

risk_analysis as (
    select
        p.name as material_name,
        coalesce(crit.number_of_products_used_in, 0) as products_used_in,
        coalesce(crit.total_quantity_in_boms, 0) as total_quantity_needed,
        coalesce(vol.average_cost, 0) as current_average_cost,
        coalesce(vol.price_volatility_score, 0) as price_volatility,
        coalesce(sup.number_of_suppliers, 0) as supplier_count,

        
        rank() over (order by coalesce(crit.number_of_products_used_in, 0) desc) as criticality_rank,
        rank() over (order by coalesce(vol.price_volatility_score, 0) desc) as volatility_rank,
        rank() over (order by coalesce(sup.number_of_suppliers, 999) asc) as supply_risk_rank

    from {{ ref('dim_product') }} p
    left join material_criticality crit on p.productid = crit.productid
    left join price_volatility vol on p.productid = vol.productid
    left join supply_risk sup on p.productid = sup.productid
)

select
    material_name,
    products_used_in,
    supplier_count,
    current_average_cost,
    price_volatility,
    
    (criticality_rank + volatility_rank + supply_risk_rank) as final_priority_score,

    rank() over (order by (criticality_rank + volatility_rank + supply_risk_rank) asc) as overall_priority_rank

from risk_analysis
where products_used_in > 0 
order by overall_priority_rank