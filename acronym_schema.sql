create database my_acronym;

create table tbl_user (
userID INT NOT NULL AUTO_INCREMENT,
username varchar(80) not null,
userFN varchar(80),
userLN varchar(80),
KEY userID(userID) using BTREE,
primary key(userID)
) ENGINE=InnoDB;

create table `tbl_Acronym` (
`acroID` INT NOT NULL AUTO_INCREMENT,
`acronym` VARCHAR(80) NOT NULL,
`definition` VARCHAR(80) NOT NULL,
`authID` INT,
`dateCreate` DATETIME,
KEY `acroID` (`acroID`) USING BTREE,
PRIMARY KEY (`acroID`)
) ENGINE=InnoDB;

create table `tbl_Tag` (
`tagID` INT NOT NULL AUTO_INCREMENT,
`tag` VARCHAR(80) NOT NULL,
KEY `tagID` (`tagID`) USING BTREE,
PRIMARY KEY (`tagID`)
) ENGINE=InnoDB

create table `tbl_AcroTag` (
`acroID` INT NOT NULL,
`tagID` INT NOT NULL,
KEY `acroID` (`acroID`) USING BTREE,
KEY `tagID` (`tagID`) USING BTREE,
PRIMARY KEY (`acroID`,`tagID`)
) ENGINE=InnoDB;
