
SELECT 
year(o.SALES_DATE) as YEAR, 
month(o.SALES_DATE) as MONTH, 
count(distinct o.USER_ID) as PUCHASED_USERS,
round(count(distinct o.USER_ID) / 
      (select count(DISTINCT USER_ID) from USER_INFO where YEAR(JOINED) = 2021), 1) as PUCHASED_RATIO
from USER_INFO u
join ONLINE_SALE o on u.USER_ID = o.USER_ID
where year(u.JOINED) = 2021
group by year(o.SALES_DATE), month(o.SALES_DATE)
order by 1, 2