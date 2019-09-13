SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `tbl_AcroTag`;
CREATE TABLE `tbl_AcroTag` (
  `acroID` bigint(20) NOT NULL,
  `tagID` bigint(20) NOT NULL,
  PRIMARY KEY (`acroID`,`tagID`),
  KEY `acroID` (`acroID`) USING BTREE,
  KEY `tagID` (`tagID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `tbl_Acronym`;
CREATE TABLE `tbl_Acronym` (
  `acroID` bigint(20) NOT NULL AUTO_INCREMENT,
  `acronym` varchar(80) NOT NULL,
  `definition` varchar(80) NOT NULL,
  `authID` bigint(20) DEFAULT NULL,
  `dateCreate` datetime DEFAULT NULL,
  PRIMARY KEY (`acroID`),
  KEY `acroID` (`acroID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `tbl_Tag`;
CREATE TABLE `tbl_Tag` (
  `tagID` bigint(20) NOT NULL AUTO_INCREMENT,
  `Tag` varchar(80) NOT NULL,
  PRIMARY KEY (`tagID`),
  KEY `acroID` (`tagID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `tbl_User`;
CREATE TABLE `tbl_User` (
  `userID` bigint(20) NOT NULL AUTO_INCREMENT,
  `userEmail` varchar(80) NOT NULL,
  `username` varchar(80) NOT NULL,
  `userFN` varchar(80) DEFAULT NULL,
  `userLN` varchar(80) DEFAULT NULL,
  `userPasswordHash` varchar(128) DEFAULT NULL,
  `userIsAdmin` int(11) DEFAULT NULL,
  `userLastLoginDT` datetime DEFAULT NULL,
  PRIMARY KEY (`userID`),
  KEY `userID` (`userID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
