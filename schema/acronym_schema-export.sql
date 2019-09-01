SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP DATABASE IF EXISTS `acronym`;
CREATE DATABASE `acronym` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `acronym`;

DROP TABLE IF EXISTS `tbl_AcroTag`;
CREATE TABLE `tbl_AcroTag` (
  `acroID` int(11) NOT NULL,
  `tagID` int(11) NOT NULL,
  PRIMARY KEY (`acroID`,`tagID`),
  KEY `acroID` (`acroID`) USING BTREE,
  KEY `tagID` (`tagID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `tbl_Acronym`;
CREATE TABLE `tbl_Acronym` (
  `acroID` int(11) NOT NULL AUTO_INCREMENT,
  `acronym` varchar(80) NOT NULL,
  `definition` varchar(80) NOT NULL,
  `authID` int(11) DEFAULT NULL,
  `dateCreate` datetime DEFAULT NULL,
  PRIMARY KEY (`acroID`),
  KEY `acroID` (`acroID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `tbl_user`;
CREATE TABLE `tbl_user` (
  `userID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `userFN` varchar(80) DEFAULT NULL,
  `userLN` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`userID`),
  KEY `userID` (`userID`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
