DROP TABLE IF EXISTS `hospital_users`;
DROP TABLE IF EXISTS `hospital_user_types`;
DROP TABLE IF EXISTS `hospital_regions`;

CREATE TABLE `hospital_user_types`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `type` VARCHAR(255) NOT NULL
);

CREATE TABLE `hospital_regions`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `region` VARCHAR(255) NOT NULL
);

CREATE TABLE `hospital_users`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `fname` VARCHAR(255) NOT NULL,
    `lname` VARCHAR(255) NOT NULL,
    `login` VARCHAR(32) NOT NULL,
    `password` VARCHAR(1024) NOT NULL,
    `pwd_modified_at` DATETIME,
    `type` INT UNSIGNED NOT NULL,
    `region` INT UNSIGNED NOT NULL,
    `ban_date` DATETIME,
    FOREIGN KEY (`type`) REFERENCES `hospital_user_types`(`id`),
    FOREIGN KEY (`region`) REFERENCES `hospital_regions`(`id`)
);

INSERT INTO `hospital_user_types`(`type`) VALUES('Super_Admin');
INSERT INTO `hospital_user_types`(`type`) VALUES('Admin');
INSERT INTO `hospital_user_types`(`type`) VALUES('Doctor');
INSERT INTO `hospital_user_types`(`type`) VALUES('Nurse');
INSERT INTO `hospital_user_types`(`type`) VALUES('Patient');

INSERT INTO `hospital_regions`(`region`) VALUES('Paris');
INSERT INTO `hospital_regions`(`region`) VALUES('Rennes');
INSERT INTO `hospital_regions`(`region`) VALUES('Strasbourg');
INSERT INTO `hospital_regions`(`region`) VALUES('Grenoble');
INSERT INTO `hospital_regions`(`region`) VALUES('Nantes');