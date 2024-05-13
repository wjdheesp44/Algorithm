select user_id, nickname, concat(city, ' ',street_address1,' ', street_address2)as '전체주소', 
(concat(SUBSTR(TLNO, 1,3) ,'-',substr(tlno, 4,4),'-',substr(tlno, 8,4))) as '전화번호'

from 
(select writer_id
from used_goods_board
group by writer_id
having count(*)>=3) a join 
used_goods_user b on a.writer_id = b.user_id
order by b.user_id desc