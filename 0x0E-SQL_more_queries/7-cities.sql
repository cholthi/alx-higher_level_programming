-- Create a database hbtn_0d_usa and table states in it
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities`(
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY UNIQUE,
	`name` VARCHAR(256) NOT NULL,
	`state_id` INT NOT NULL,
	CONSTRAINT `fk_state` FOREIGN KEY (`state_id`)
	                      REFRENCES `states`(`id`)
);
