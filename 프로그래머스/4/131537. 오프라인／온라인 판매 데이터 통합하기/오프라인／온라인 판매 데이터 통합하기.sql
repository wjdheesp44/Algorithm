-- 코드를 입력하세요
SELECT 
DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
PRODUCT_ID,
case when os.USER_ID is null then null else os.USER_ID end as USER_ID, 
SALES_AMOUNT
from ONLINE_SALE os 
where os.SALES_DATE between '2022-03-01' and '2022-03-31'

union

SELECT 
DATE_FORMAT(SALES_DATE, '%Y-%m-%d') as SALES_DATE,
PRODUCT_ID,
NULL as USER_ID, 
SALES_AMOUNT
from OFFLINE_SALE os 
where os.SALES_DATE between '2022-03-01' and '2022-03-31'

order by SALES_DATE asc, PRODUCT_ID asc, USER_ID asc
