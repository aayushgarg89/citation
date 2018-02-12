USE Citation

select * from Cite_Style

--update Cite_Style set Style='APA' where ID in (4,5,6,7)

--ALTER TABLE Cite_Rules 
--ADD Weigh float
select * from Cite_Rules
--update Cite_Rules SET Weigh=11.11 where Description='edition of the work'
---update Cite_Rules SET Rules='Lname<comma><space>FI<dot><space>PublicationYear<dot><space>title(ITALICS)<dot><space>location<colon><space>Publisher
---' where weigh=111.011
--update Cite_Rules set weigh=11.0111 where Description='volume of the journal'

--delete from Cite_Rules where style_id=3