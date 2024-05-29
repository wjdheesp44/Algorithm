select car_id, 
    case when max(availability) = '1' then '대여중' 
    else '대여 가능' end as availability 
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as A 
    left join (select history_id, '1' as availability from CAR_RENTAL_COMPANY_RENTAL_HISTORY where start_date <= '2022-10-16' and end_date >= '2022-10-16') as B 
    on A.history_id = B.history_id 
group by car_id 
order by car_id desc