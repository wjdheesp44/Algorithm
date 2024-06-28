SELECT  SUBSTRING(PRODUCT_CODE,1,2) AS CATEGORY
        ,COUNT(PRODUCT_ID) AS PRODUCTS
FROM  PRODUCT
GROUP BY  SUBSTRING(PRODUCT_CODE,1,2)
ORDER BY  CATEGORY;