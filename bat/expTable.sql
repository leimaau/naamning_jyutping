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
select trad||'	'||jyutping from tab_nbdict_2020_phrase order by tab_id;

spool E:\LocalRepository\github\\naamning_jyutping_build\bat\v_nb_zingjam_bw_rime.txt
select trad||'	'||note_jp_expl||'	'||rate from v_nb_zingjam_bw_rime;

spool E:\LocalRepository\github\\naamning_jyutping_build\bat\tab_nbdict_2020_bw_phrase.txt
select trad||'	'||jyutping from tab_nbdict_2020_bw_phrase order by tab_id;

spool off