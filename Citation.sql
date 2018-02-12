USE Citation;

--create table Cite_Style(
--ID INT IDENTITY(1,1) PRIMARY KEY,
--Style VARCHAR(50),
--Publication VARCHAR(50))

--select * from Cite_Style

--INSERT INTO Cite_Style VALUES('MLA','Journal')
--INSERT INTO Cite_Style VALUES('MLA','Video')
--INSERT INTO Cite_Style VALUES('MLA','Book')
--INSERT INTO Cite_Style VALUES('MLA','Journal')
--INSERT INTO Cite_Style VALUES('MLA','Chapter')
--INSERT INTO Cite_Style VALUES('MLA','Video')

--CREATE TABLE Cite_Rules(
--Style_ID INT NOT NULL,
--Rules VARCHAR(MAX),
--Description VARCHAR(MAX),
--FOREIGN KEY(Style_ID) REFERENCES Cite_Style(ID))

--INSERT INTO Cite_Rules VALUES(2,'Lname<comma><space>Fname<dot><space>"Title"<space>Publisher<comma><space>PublicationDate<dot>','title in quotation marks')
--INSERT INTO Cite_Rules VALUES(2,'Lname<comma><space>Fname<dot><space>"Title"<space>3rd ed<dot><comma><space>Publisher<comma><space>PublicationDate<dot>
--','edition of the work')
--INSERT INTO Cite_Rules VALUES(2,'Lname<comma><space>Fname<dot><space>"Title"<space>vol<dot><space>number<comma><space>Publisher<comma><space>PublicationDate<dot>
--','volume of the journal')
--INSERT INTO Cite_Rules VALUES(3,'"title"<space>titleContainer<comma><space>created<space>by<space>Fname<space>Lname<comma><space><performance<space>by<space>Fname<space>Lname<comma><space>season<space>number<comma><space>episode<space>number<comma><space>network<comma><space>dd<space>mmm<dot><space>yyyy<dot>
--','Television episode')
--INSERT INTO Cite_Rules VALUES(4,'Lname<comma><space>FI<dot><space>PublicationYear<dot><space>title(italics)<dot><space>location<colon><space>Publisher
--','1 author')
--INSERT INTO Cite_Rules VALUES(4,'Lname<comma><space>FI<dot><space>PublicationYear<dot><space>title(italics)<dot><space>FI<dot><space>MI<dot><space>Lname<space>(Ed.)<dot><space>location<colon><space>Publisher
--','edited book with an author')
--INSERT INTO Cite_Rules VALUES(5,'Lname<comma><space>FI<dot><space>PulicationYear<dot><space>ArticleTitle<dot><space>JournalTitile<comma><space>VolumeNumber<comma><space>pageRange<dot><space>doi
--','format for a journal with doi')
--INSERT INTO Cite_Rules VALUES(6,'Lname<comma><space>FI<dot><space>PublicationYear<dot><space>ArticleTitle<dot><space>Book/JournalTitle(chapter or section number)<dot><space>Retrieved<space>from<space>URL
--','format for a APA chapter')
--INSERT INTO Cite_Rules VALUES(7,'Lname<comma><space>FI<dot><space>PublicationDate<dot><space>VideoTitle<dot><space>PodcastName<dot><space>Podcast<space>retrieved<space>from<space>URL
--','format for a APA video')


select * from Cite_Style
select * from Cite_Rules
