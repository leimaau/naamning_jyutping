set echo off
set trimspool on
set feedback off
set wrap off
set linesize 20000
set pagesize 20000
set newpage none
set heading off
set term off

spool E:\LocalRepository\github\\naamning_jyutping_build\bat\v_nb_zingjam_rime.txt
select trad||'	'||note_jp_expl||'	'||rate from v_nb_zingjam_rime;

spool E:\LocalRepository\github\\naamning_jyutping_build\bat\tab_nbdict_2020_phrase.txt
select replace(trad,'…','')||'	'||replace(jyutping,'…','') from tab_nbdict_2020_phrase where trad not like '%～%' and trad not like '%(%' order by tab_id;

spool E:\LocalRepository\github\\naamning_jyutping_build\bat\v_nb_zingjam_bw_rime.txt
select trad||'	'||note_jp_expl||'	'||rate from v_nb_zingjam_bw_rime;

spool E:\LocalRepository\github\\naamning_jyutping_build\bat\tab_nbdict_2020_bw_phrase.txt
select replace(trad,'…','')||'	'||replace(jyutping,'…','') from tab_nbdict_2020_bw_phrase where trad not like '%～%' and trad not like '%(%' order by tab_id;


delete from temp_xxxx;
delete from temp_xxxx2;
delete from temp_xxxx3;
delete from temp_xxxx4;

insert into temp_xxxx(word,jyutping,freq)
select distinct trad,jyutping,'' from v_nb_zingjam_all;

insert into temp_xxxx2(word,jyutping,freq)
select distinct trad,jyutping,'' from v_nbdict_infer where note like '%《廣韻》%';

insert into temp_xxxx3(word,jyutping,freq)
select distinct trad,jyutping,'' from v_nbdict_infer where note like '%《集韻》%';

commit;

insert into temp_xxxx4(word,jyutping,freq)
select distinct word,jp,rate from (
  select distinct word,'(推)'||jyutping jp,'0%' rate from temp_xxxx3 
  where (word,jyutping) not in(select word,jyutping from temp_xxxx)
  and (word,jyutping) not in(select word,jyutping from temp_xxxx2)
  and word not in(select word from temp_xxxx)
  and word<>'□'
  union
  select distinct word,'(推)'||jyutping jp,'' rate from temp_xxxx2 
  where (word,jyutping) not in(select word,jyutping from temp_xxxx)
  and word not in(select word from temp_xxxx)
  and word<>'□'
);

commit;

spool E:\LocalRepository\github\\naamning_jyutping_build\bat\temp_xxxx4_infer.txt
select distinct word||'	'||jyutping||'	'||freq from temp_xxxx4;


delete from temp_xxxx;
delete from temp_xxxx2;
delete from temp_xxxx3;
delete from temp_xxxx4;

insert into temp_xxxx(word,jyutping,freq)
select distinct trad,jyutping,'' from v_nb_zingjam_bw_all;

insert into temp_xxxx2(word,jyutping,freq)
select distinct trad,jyutping,'' from v_nbdict_infer_bw where note like '%《廣韻》%';

insert into temp_xxxx3(word,jyutping,freq)
select distinct trad,jyutping,'' from v_nbdict_infer_bw where note like '%《集韻》%';

commit;

insert into temp_xxxx4(word,jyutping,freq)
select distinct word,jp,rate from (
  select distinct word,'(推)'||jyutping jp,'0%' rate from temp_xxxx3 
  where (word,jyutping) not in(select word,jyutping from temp_xxxx)
  and (word,jyutping) not in(select word,jyutping from temp_xxxx2)
  and word not in(select word from temp_xxxx)
  and word<>'□'
  union
  select distinct word,'(推)'||jyutping jp,'' rate from temp_xxxx2 
  where (word,jyutping) not in(select word,jyutping from temp_xxxx)
  and word not in(select word from temp_xxxx)
  and word<>'□'
);

commit;

spool E:\LocalRepository\github\\naamning_jyutping_build\bat\temp_xxxx4_bw_infer.txt
select distinct word||'	'||jyutping||'	'||freq from temp_xxxx4;

spool off