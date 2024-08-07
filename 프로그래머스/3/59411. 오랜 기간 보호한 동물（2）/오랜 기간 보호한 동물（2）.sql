SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
INNER JOIN (
   SELECT ANIMAL_ID, DATETIME AS D
    FROM ANIMAL_OUTS
) a 
USING (ANIMAL_ID)
order by datetime-d
limit 2;
